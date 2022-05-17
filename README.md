# Adminer-Autologin Docker Image

Please only use this image in a local development environment.

This image will auto-update every 30 days (if a new offical Docker image was released).

## Usage

Load the Adminer plugin `login-env-vars` and set the following env vars to login automatically.

- `ADMINER_DRIVER`
- `ADMINER_SERVER`
- `ADMINER_USERNAME`
- `ADMINER_PASSWORD`
- `ADMINER_DB`

### Example

docker-compose.yaml:

```YAML
services:
  adminer:
    image: ghcr.io/jeliebig/adminer-autologin
    environment:
      ADMINER_PLUGINS: login-env-vars
      # Without loading other plugins you can choose one of these:
      # Format: driver_name -> db_name
      # - server -> MySQL
      # - sqlite -> SQLite3
      # - sqlite2 -> SQLite2
      # - pgsql -> PostgreSQL
      # - oracle -> Oracle (beta)
      # - mssql -> MS SQL (beta)
      # - mongo -> MongoDB (alpha)
      # - elastic -> Elasticsearch (beta)
      ADMINER_DRIVER: driver_name
      ADMINER_SERVER: server_host
      ADMINER_USERNAME: username
      ADMINER_PASSWORD: password
      ADMINER_DB: db
```
