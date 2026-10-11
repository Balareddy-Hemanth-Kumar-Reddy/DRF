# API Contract — PepoleHub API

**Version:** v1  
**Base URL:** `http://127.0.0.1:8000`  
**Auth Type:** Token Authentication (DRF `rest_framework.authtoken`)  
**Docs UI:** `http://127.0.0.1:8000/swagger/` (Swagger) and `http://127.0.0.1:8000/redoc/` (ReDoc)

---

## Authentication

All protected endpoints require this header:

```
Authorization: Token <your_token>
```

Get the token by calling `POST /auth/login/` with valid credentials.

> **Warning:** Tokens do **not** expire by default. Delete them via `POST /auth/logout/` or Django Admin.

---

## Endpoints Overview

| Method | URL | Purpose | Auth Required |
| :--- | :--- | :--- | :--- |
| POST | `/auth/register/` | Create a new user account | No |
| POST | `/auth/login/` | Log in and receive an auth token | No |
| POST | `/auth/logout/` | Delete the current user's token | Yes |
| GET | `/api/multipleobj/` | List all people | No (public) |
| POST | `/api/multipleobj/` | Create a new person | No (public) |
| GET | `/api/singleobj/{id}/` | Retrieve one person by ID | Yes |
| PUT | `/api/singleobj/{id}/` | Fully update one person by ID | Yes |
| PATCH | `/api/singleobj/{id}/` | Partially update one person by ID | Yes |
| DELETE | `/api/singleobj/{id}/` | Delete one person by ID | Yes |

---

## 1. Register

**`POST /auth/register/`** — Create a new user.

- **Auth:** Not required
- **Content-Type:** `application/json`

### Request Body
```json
{
  "username": "johndoe",
  "password": "secretpass123"
}
```

### Success Response `201 Created`
```json
{
  "message": "User registered successfully"
}
```

### Error Response `400 Bad Request`
```json
{
  "username": ["A user with that username already exists."]
}
```

---

## 2. Login

**`POST /auth/login/`** — Obtain an auth token.

- **Auth:** Not required
- **Content-Type:** `application/x-www-form-urlencoded` (or JSON depending on client)

### Request Body (form-data)
```
username=johndoe
password=secretpass123
```

### Success Response `200 OK`
```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Error Response `400 Bad Request`
```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

> **Tip:** Save this token. Send it as `Authorization: Token <token>` in all protected requests.

---

## 3. Logout

**`POST /auth/logout/`** — Invalidate the current token.

- **Auth:** Required

### Request Headers
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

### Success Response `200 OK`
```json
{
  "message": "Logged out successfully"
}
```

---

## 4. List People

**`GET /api/multipleobj/`** — Retrieve all people.

- **Auth:** Not required (public)

### Success Response `200 OK`
```json
[
  {
    "id": 1,
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
  },
  {
    "id": 2,
    "name": "Bob",
    "age": 25,
    "email": "bob@example.com"
  }
]
```

---

## 5. Create Person

**`POST /api/multipleobj/`** — Add a new person.

- **Auth:** Not required (public)
- **Content-Type:** `application/json`

### Request Body
```json
{
  "name": "Charlie",
  "age": 28,
  "email": "charlie@example.com"
}
```

### Success Response `201 Created`
```json
{
  "id": 3,
  "name": "Charlie",
  "age": 28,
  "email": "charlie@example.com"
}
```

### Error Response `400 Bad Request`
```json
{
  "age": ["A valid integer is required."]
}
```

---

## 6. Retrieve Person

**`GET /api/singleobj/{id}/`** — Get one person by ID.

- **Auth:** Required

### URL Example
```
GET /api/singleobj/1/
```

### Success Response `200 OK`
```json
{
  "id": 1,
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com"
}
```

### Error Response `404 Not Found`
```json
{
  "detail": "No Person matches the given query."
}
```

---

## 7. Full Update Person

**`PUT /api/singleobj/{id}/`** — Replace all fields of a person.

- **Auth:** Required
- **Content-Type:** `application/json`

### Request Body
```json
{
  "name": "Alice Updated",
  "age": 31,
  "email": "alice.new@example.com"
}
```

### Success Response `200 OK`
```json
{
  "id": 1,
  "name": "Alice Updated",
  "age": 31,
  "email": "alice.new@example.com"
}
```

---

## 8. Partial Update Person

**`PATCH /api/singleobj/{id}/`** — Update only some fields.

- **Auth:** Required
- **Content-Type:** `application/json`

### Request Body (only age changes)
```json
{
  "age": 32
}
```

### Success Response `200 OK`
```json
{
  "id": 1,
  "name": "Alice Updated",
  "age": 32,
  "email": "alice.new@example.com"
}
```

---

## 9. Delete Person

**`DELETE /api/singleobj/{id}/`** — Remove a person.

- **Auth:** Required

### URL Example
```
DELETE /api/singleobj/1/
```

### Success Response `204 No Content`
```
(empty body)
```

---

## Data Models

### Person
| Field | Type | Constraints |
| :--- | :--- | :--- |
| `id` | integer | Auto-generated, read-only |
| `name` | string | Max 100 chars, required |
| `age` | integer | Positive integer, required |
| `email` | string (email) | Valid email, required |

---

## Error Format

All errors follow DRF's standard format. Common status codes:

| Code | Meaning |
| :--- | :--- |
| `200` | OK |
| `201` | Created |
| `204` | No Content |
| `400` | Bad Request (validation error) |
| `401` | Unauthorized (missing/invalid token) |
| `404` | Not Found |
| `405` | Method Not Allowed |

---

## Quick cURL Examples

**Login:**
```bash
curl -X POST http://127.0.0.1:8000/auth/login/ \
  -d "username=johndoe" -d "password=secretpass123"
```

**List people (no auth):**
```bash
curl http://127.0.0.1:8000/api/multipleobj/
```

**Get one person (with auth):**
```bash
curl -H "Authorization: Token YOUR_TOKEN" http://127.0.0.1:8000/api/singleobj/1/
```
