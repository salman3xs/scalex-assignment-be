from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt, JWTError

from app.config.constant import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_EXPIRY_MINUTES


class JWTHandler:
    """
    Handles JWT token creation and verification.
    Encapsulates all JWT-related logic in a single class.
    """

    def __init__(self):
        self.secret_key = JWT_SECRET_KEY
        self.algorithm = JWT_ALGORITHM
        self.expiry_minutes = JWT_EXPIRY_MINUTES

    def create_token(self, data: dict) -> str:
        """
        Creates a JWT token with the given payload data.
        Adds an expiration claim automatically.

        Args:
            data: Dictionary containing the claims to encode.

        Returns:
            Encoded JWT token string.
        """
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.expiry_minutes)
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_token(self, token: str) -> Optional[dict]:
        """
        Verifies and decodes a JWT token.

        Args:
            token: The JWT token string to verify.

        Returns:
            Decoded payload dictionary if valid, None otherwise.
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None


# Singleton instance for use across the application
jwt_handler = JWTHandler()
