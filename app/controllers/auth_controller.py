from app.config.users import USERS
from app.utils.jwt_handler import jwt_handler


class AuthController:
    """
    Controller handling authentication logic.
    """

    def login(self, username: str, password: str) -> dict:
        """
        Authenticates a user with username and password.

        Args:
            username: The username to authenticate.
            password: The password to verify.

        Returns:
            Dictionary with success status, message, token, and user info.

        Raises:
            ValueError: If credentials are invalid.
        """
        # Find user by credentials
        user = next(
            (
                u
                for u in USERS
                if u["username"] == username and u["password"] == password
            ),
            None,
        )

        if not user:
            raise ValueError("Invalid username or password.")

        # Generate JWT token
        token = jwt_handler.create_token(
            {
                "id": user["id"],
                "username": user["username"],
                "user_type": user["user_type"],
            }
        )

        return {
            "success": True,
            "message": "Login successful.",
            "token": token,
            "user": {
                "id": user["id"],
                "username": user["username"],
                "user_type": user["user_type"],
            },
        }


auth_controller = AuthController()
