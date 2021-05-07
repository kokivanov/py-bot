-- Create base table of servers
CREATE TABLE global_config(
    server_id VARCHAR(32) PRIMARY KEY NOT NULL,
    prefix VARCHAR(32) DEFAULT NULL,
    server_owner_id VARCHAR(32) NOT NULL
);

-- Create table of configs for features
CREATE TABLE feature_config(
    server_id VARCHAR(32) NOT NULL,
    global_mutes BOOLEAN DEFAULT 0,
    gloabl_bans BOOLEAN DEFAULT 0,
    global_leveling BOOLEAN DEFAULT 0,
    rpg_use_global_mobs BOOLEAN DEFAULT 0,
    rpg_use_global_items BOOLEAN DEFAULT 0,
    fishing_use_global_items BOOLEAN DEFAULT 0,
    FOREIGN KEY (server_id) REFERENCES global_config(server_id),
    PRIMARY KEY (server_id)
);

-- Create view of all basic configs
CREATE VIEW config_vw AS
SELECT global_config.server_owner_id, global_config.prefix, feature_config.*
FROM global_config
JOIN feature_config ON feature_config.server_id = feature_config.server_id;

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
    FOREIGN KEY (server_id) REFERENCES global_config(server_id),
    PRIMARY KEY (server_id, command_name)
);

-- Create table of modules configurations and configuration for each command
CREATE TABLE module_list(
    server_id VARCHAR(32) NOT NULL,
    module_name VARCHAR(32) NOT NULL,
    command_name VARCHAR(32) NOT NULL DEFAULT '&common',
    aliases VARCHAR(255),
    is_callable BOOLEAN,
    required_permission VARCHAR(1024),
    channel_black VARCHAR(1024),
    roles_blacklist VARCHAR(1024),
    custom_parameters VARCHAR(1024),
    FOREIGN KEY (server_id) REFERENCES global_config(server_id),
    PRIMARY KEY (server_id, command_name, module_name)
);

