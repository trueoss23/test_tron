CREATE DATABASE tron WITH OWNER postgres ENCODING 'UTF8';

-- -----------------------------------------------------------------------------------------
\connect tron;

CREATE USER tron_user WITH ENCRYPTED PASSWORD 'tron_user_pwd';


DROP TABLE IF EXISTS "Tron" CASCADE;
CREATE TABLE "Tron"
(
    id           SERIAL PRIMARY KEY,
    address      VARCHAR(255) NOT NULL,
    bandwidth    VARCHAR(255) NOT NULL,
    energy       VARCHAR(255) NOT NULL,
    trx_balance  FLOAT  NOT NULL,
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at   TIMESTAMP NULL,
    deleted_at   TIMESTAMP NULL
);
--
CREATE INDEX ON "Tron" (created_at);
CREATE INDEX ON "Tron" (address);
--
COMMENT ON TABLE "Tron" is 'информация о Троне по адресу';
COMMENT ON COLUMN "Tron".created_at is 'Создание по UTC';
COMMENT ON COLUMN "Tron".updated_at is 'Обновление по UTC';
COMMENT ON COLUMN "Tron".deleted_at is 'Удален по UTC';
