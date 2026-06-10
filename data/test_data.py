from config import settings

VALID_USERS = [
    {"username": settings.STANDARD_USER, "password": settings.STANDARD_PASSWORD},
    {"username": "problem_user", "password": settings.STANDARD_PASSWORD},
    {"username": "performance_glitch_user", "password": settings.STANDARD_PASSWORD},
]

INVALID_LOGIN_CASES = [
    {"username": "", "password": settings.STANDARD_PASSWORD, "error": "Username is required"},
    {"username": settings.STANDARD_USER, "password": "", "error": "Password is required"},
    {"username": settings.LOCKED_USER, "password": settings.STANDARD_PASSWORD, "error": "locked out"},
]

CHECKOUT_DATA = {
    "first_name": "Ivan",
    "last_name": "Petrov",
    "postal_code": "123456",
}
