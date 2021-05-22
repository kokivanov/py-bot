-- Create base table of servers
CREATE  DATABASE  test;

USE test;

CREATE TABLE global_config(
    server_id VARCHAR(32) PRIMARY KEY NOT NULL,
    prefix VARCHAR(32) DEFAULT NULL
);

INSERT INTO global_config(server_id, server_owner_id) VALUES ("0", "0");
-- Create table of configs for features
CREATE TABLE feature_config(
    server_id VARCHAR(32) NOT NULL,
    global_mutes BOOLEAN DEFAULT 0,
    global_bans BOOLEAN DEFAULT 0,
    global_leveling BOOLEAN DEFAULT 0,
    rpg_use_global_mobs BOOLEAN DEFAULT 0,
    rpg_use_global_items BOOLEAN DEFAULT 0,
    fishing_use_global_items BOOLEAN DEFAULT 0,
    FOREIGN KEY (server_id) REFERENCES global_config(server_id) ON DELETE CASCADE,
    PRIMARY KEY (server_id)
);

INSERT  INTO  feature_config(server_id) VALUES ("0");

-- Create view of all basic configs
CREATE VIEW config_vw AS
SELECT global_config.prefix, feature_config.*
FROM global_config
JOIN feature_config ON global_config.server_id = feature_config.server_id;

-- Create table of commands configurations
CREATE TABLE command_list(  
    server_id VARCHAR(32) NOT NULL,
    command_name VARCHAR(32) NOT NULL,
    aliases VARCHAR(255),
    is_callable BOOLEAN,
    required_permission VARCHAR(1024),
    channel_black VARCHAR(1024),
    roles_blacklist VARCHAR(1024),
    custom_parameters VARCHAR(1024),
    FOREIGN KEY (server_id) REFERENCES global_config(server_id) ON DELETE CASCADE,
    PRIMARY KEY (server_id, command_name)
);

CREATE VIEW config_all_vw AS
SELECT global_config.*,
command_list.command_name, command_list.aliases, command_list.is_callable, command_list.required_permission, command_list.channel_black, command_list.roles_blacklist,  command_list.custom_parameters
FROM global_config
LEFT JOIN command_list ON global_config.server_id = command_list.server_id;

CREATE VIEW  get_aliases_vw AS
SELECT global_config.server_id,
command_list.command_name, command_list.aliases
FROM global_config
LEFT JOIN command_list ON command_list.server_id = global_config.server_id;

CREATE VIEW get_prefix_vw AS
SELECT global_config.server_id, global_config.prefix
FROM global_config;

CREATE VIEW get_commands AS
SELECT global_config.server_id, command_list.command_name, command_list.aliases, command_list.is_callable, command_list.required_permission, command_list.channel_black, command_list.roles_blacklist, command_list.custom_parameters
FROM global_config
LEFT JOIN command_list ON global_config.server_id = command_list.server_id;