# 🛒 E-Commerce Microservices Platform

Микросервисная платформа на Django + Docker.  
Аутентификация, товары, заказы, оплата, уведомления.  
Готова к деплою.

---

## ⚠️ Важно: Безопасность
Никогда не используй реальные email и пароли в примерах.  
Все тестовые данные — условные.

Примеры используют:
- `user@example.com` — вместо реального email
- `password` — как placeholder
- `<your_access_token>` — заменяется на настоящий JWT

---

## 🧩 Архитектура

| Сервис | Описание | Порт |
|-------|--------|------|
| `user-service` | Аутентификация, JWT | 8001 |
| `product-service` | Каталог товаров | 8002 |
| `order-service` | Управление заказами | 8003 |
| `payment-service` | Обработка платежей | 8004 |
| `notification-service` | Уведомления | 8005 |
| `postgres-db` | PostgreSQL (многобазовый) | 5432 |

Каждый сервис использует свою БД через общего пользователя `postgres1`.

---

## 🚀 Запуск

```bash
docker compose up -d --build


---

```markdown
# 🛒 E-Commerce Microservices Platform

Microservices platform on Django + Docker.  
Authentication, products, orders, payments, notifications.  
Ready for deployment.

---

## ⚠️ Security Notice
Never use real credentials in examples.  
All test data is placeholder.

Examples use:
- `user@example.com` — instead of real email
- `password` — as placeholder
- `<your_access_token>` — replace with actual JWT

---

## 🧩 Architecture

| Service | Description | Port |
|--------|------------|------|
| `user-service` | Auth, JWT | 8001 |
| `product-service` | Product catalog | 8002 |
| `order-service` | Order management | 8003 |
| `payment-service` | Payment processing | 8004 |
| `notification-service` | Notifications | 8005 |
| `postgres-db` | PostgreSQL (multi-database) | 5432 |

Each service uses its own DB via shared user `postgres1`.

---

## 🚀 Run

```bash
docker compose up -d --build