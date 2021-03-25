USE planck_db;
ALTER table plk_order ADD INDEX `idx_create_time`(create_time);
ALTER table plk_order_group_map ADD INDEX `idx_create_time`(create_time);
ALTER table dj_pool_order ADD INDEX `idx_create_time`(create_time);