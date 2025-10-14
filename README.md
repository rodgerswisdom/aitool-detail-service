# aitool-detail-service

## Authentication Gate

This service now protects all API endpoints with a shared bearer token. Configure the following environment variables before running locally or deploying:

| Variable | Description |
| --- | --- |
| `GATEKEEPER_EMAIL` | Email required on the login form. |
| `GATEKEEPER_PASSWORD` | Password required on the login form. |
| `GATEKEEPER_TOKEN` | Random string returned on login and required in the `Authorization: Bearer` header. |

Expose the login endpoint at `/api/auth/login/` so the frontend can exchange an email/password for the bearer token.

When this service retrieves categories from the category microservice it forwards the configured bearer token automatically. Make sure both services share the same credentials.
