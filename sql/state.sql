CREATE TABLE State(
    state VARCHAR(8) PRIMARY KEY NOT NULL,
    url VARCHAR(128) NOT NULL,
    lastupdate timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8;
