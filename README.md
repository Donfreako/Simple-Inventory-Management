
# Simple Inventory Management System

 Develop a backend API for an Inventory Management System that supports CRUD
 operations on inventory items, integrated with JWT-based authentication for secure
 access. The system should use Django Rest Framework (DRF) for the API framework,
 PostgreSQL for the database, Redis for caching, and include unit tests to ensure
 functionality. Implement proper error handling with appropriate error codes and integrate a
 logger for debugging and monitoring.


## API Reference
#### Get all items

```http
  POST /register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username, password` | `string` | **Required**. to register |

#### To login

```http
  POST login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username,password` | `string` | **Required**. to login |

#### To refresh token

```http
  POST refresh/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `refresh token` | `string` | **Required**. to get JWT token |

#### To create items

```http
  POST /item/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key to create items |

#### Get all items

```http
  POST /items/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**.API key to get all items |

#### Get item

```http
  GET /item/<int:item_id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id`      | `int` | **Required**. Id of item to fetch |


## Deployment

To deploy this project run

```bash
  py manage.py runserver
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`rest_framework`

`rest_framework_simplejwt`

`redis`

`logging`

`psycopg2`
