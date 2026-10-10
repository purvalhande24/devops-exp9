def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def get_greeting(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the CI/CD application."


if __name__ == "__main__":
    print("Application started successfully!")
    print(add_numbers(10, 20))
    print(get_greeting("DevOps"))