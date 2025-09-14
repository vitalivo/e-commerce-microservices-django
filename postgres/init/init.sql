-- Создаём пользователя с полными правами
CREATE USER postgres1 WITH PASSWORD 'postgres' SUPERUSER CREATEDB CREATEROLE REPLICATION;

-- Создаём базы данных
CREATE DATABASE ecommerce_users OWNER postgres1;
CREATE DATABASE ecommerce_products OWNER postgres1;
CREATE DATABASE ecommerce_orders OWNER postgres1;

-- Даём полные права на базы
GRANT ALL PRIVILEGES ON DATABASE ecommerce_users TO postgres1;
GRANT ALL PRIVILEGES ON DATABASE ecommerce_products TO postgres1;
GRANT ALL PRIVILEGES ON DATABASE ecommerce_orders TO postgres1;

-- Выводим сообщение об успехе
\echo '✅ Пользователь postgres1 и все базы успешно созданы!'