class Logger:
    def __enter__(self):
        print("Entering Logger...")
    
    def __exit__(self, exc_type,exc_value,traceback):
        print("Exiting Logger...")

with Logger() as f:
    print("Logging application started.")