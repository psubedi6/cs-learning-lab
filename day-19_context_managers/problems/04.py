class Calculator:
    def __enter__(self):
        print("Calculator started...")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Calculator closed...")
        print(exc_type)
        return True

with Calculator() as f:
    print(f"The calculation is: {10/0}")
