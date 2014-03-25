CREATE TABLE Message(
    ToUserName VARCHAR(32),
    FromUserName VARCHAR(32),
    CreateTime DATETIME,
    MsgType VARCHAR(16),
    Content TEXT,
    MsgId BIGINT,
    raw_data TEXT,
    created_time timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) DEFAULT CHARSET=utf8;
