from io import TextIOWrapper
import mysql.connector
import json
import asyncio
from .abc import commandParameters as cmd_p


def _join_headers_and_values_single(headers, values) -> dict:
    res = {}
    for i in range(len(headers)):
        res[headers[i][0]] = values[i]

    return res


class dbmanager():
    def __init__(self, config_file: TextIOWrapper or dict):
        self.cfg = json.load(config_file) if isinstance(
            config_file, TextIOWrapper) else config_file
        if self.cfg["type"] == "mysql":
            self.client = mysql.connector.connect(
                host=self.cfg["host"],
                user=self.cfg["user"],
                password=self.cfg["password"],
                database=self.cfg["database"]
            )

        if (self.client.is_connected()):
            print("Successfully connected to {}".format(self.cfg["database"]))
            self.cursor = self.client.cursor()
        else:
            self.client.ping(reconnect=True)
            print("Connection error trying to reconnect...")
            print("Is connected: ", self.client.is_connected())

    def is_still_connected(self) -> bool:
        return self.client.is_connected()

    def pingAndReconnect(self) -> bool:
        return self.client.ping(reconnect=True)

    async def get_Server_Config(self, server_ID, owner_ID) -> dict:

        self.cursor.execute(
            "SELECT * FROM config_vw WHERE server_id=\"{}\"".format(server_ID))
        res = self.cursor.fetchone()
        self.client.commit()

        if res is None or len(res) < 1:
            try:
                self.cursor.execute(
                    "INSERT INTO global_config(server_id) VALUES (\"{}\")".format(server_ID))
                self.client.commit()
                self.cursor.execute(
                    "INSERT INTO feature_config(server_id) VALUES (\"{}\")".format(server_ID))
                self.client.commit()
            except mysql.connector.errors.IntegrityError:
                pass
            self.cursor.execute(
                "SELECT * FROM config_vw WHERE server_id=\"{}\"".format(server_ID))
            res = self.cursor.fetchone()
            self.client.commit()

        self.cursor.execute("DESC config_vw")
        headers = self.cursor.fetchall()
        self.client.commit()

        return _join_headers_and_values_single(headers=headers, values=res)

    async def get_command(self, server_id: str, command_full_name: str): ...
    async def update_command(self, server_id: str, parameters: cmd_p): ...

    async def get_prefix(self, server_id: str) -> dict:
        self.cursor.execute(
            "SELECT * FROM get_prefix_vw WHERE server_id=\"{}\"".format(server_id))
        res = self.cursor.fetchone()
        self.client.commit()

        if res is None or len(res) < 1:
            self.cursor.execute(
                "SELECT * FROM get_prefix_vw WHERE server_id=\"{}\"".format("0"))
            res = self.cursor.fetchone()
            self.client.commit()

        self.cursor.execute("DESC get_prefix_vw")
        headers = self.cursor.fetchall()
        self.client.commit()

        return _join_headers_and_values_single(headers=headers, values=res)

    async def update_server_config(self, *args, **kwargs): ...
    async def update_module(self, *args, **kwargs): ...

    async def get_leaderboard(self, *args, **kwargs): ...
    async def get_user_stats(self, *args, **kwargs): ...

    async def update_user_stats(self, *args, **kwargs): ...

    async def get_column(self, *args, **kwargs): ...
    async def get_row(self, *args, **kwargs): ...

    async def update_row(self, *args, **kwargs): ...

    async def delete_row(self, table, server_ID):
        self.cursor.execute(
            "DELETE FROM {} WHERE server_id={}".format(table, server_ID))
        self.client.commit()
