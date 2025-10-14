from dataclasses import dataclass
from typing import Optional, Tuple

from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


@dataclass
class GateUser:
    """
    Minimal user object so DRF permissions consider the request authenticated.
    """

    email: str

    @property
    def is_authenticated(self) -> bool:  # pragma: no cover - simple property
        return True


class SimpleTokenAuthentication(BaseAuthentication):
    """
    Authentication class that checks for a static bearer token.
    The token is stored in settings.GATEKEEPER_TOKEN.
    """

    keyword = "Bearer"

    def authenticate(self, request: Request) -> Optional[Tuple[GateUser, str]]:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise AuthenticationFailed("Authentication credentials were not provided.")

        parts = auth_header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            raise AuthenticationFailed("Invalid Authorization header.")

        provided_token = parts[1]
        expected_token = getattr(settings, "GATEKEEPER_TOKEN", None)
        if not expected_token:
            raise AuthenticationFailed("Server authentication token is not configured.")

        if provided_token != expected_token:
            raise AuthenticationFailed("Invalid authentication token.")

        email = getattr(settings, "GATEKEEPER_EMAIL", "gatekeeper@example.com")
        return GateUser(email=email), provided_token
