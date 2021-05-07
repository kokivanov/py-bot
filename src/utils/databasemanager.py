import mysql.connector
import json

class dbmanager():
    def __init__(self, config_file):
        self.cfg = json.load(config_file)
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

    def save(self, *args, **kwargs): ...

    def get_Server_Config(self, server_ID) -> dict:
        self.cursor.execute("SELECT * FROM config_vw WHERE server_id={}".format(server_ID))
        res = self.cursor.fetchall()[0]
        self.cursor.execute("DESCRIBE config_vw")
        headers = self.cursor.fetchall()
        print(headers)

        res_dict = {}

        res_dict["server_owner_id"], res_dict["prefix"], res_dict["server_id"], res_dict["globam_mutes"], res_dict["global_bans"], res_dict["global_leveling"], res_dict["rpg_use_global_mobs"], res_dict["rpg_use_global_items"], res_dict["fishing_use_global_items"] = res
        return res_dict    
        
    def get_command(self, *args, **kwargs): ...
    def get_module(self, *args, **kwargs): ...

    def update_server_config(self, *args, **kwargs): ...
    def update_command(self, *args, **kwargs): ...
    def update_module(self, *args, **kwargs): ...

    def get_leaderboard(self, *args, **kwargs): ...
    def get_user_stats(self, *args, **kwargs): ...

    def update_user_stats(self, *args, **kwargs): ...

    def get_column(self, *args, **kwargs): ...
    def get_row(self, *args, **kwargs): ...

    def update_row(self, *args, **kwargs): ...