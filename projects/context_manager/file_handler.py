class FileContext:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type: Exception, exc_value: str, traceback: str):
        if self.file:
            self.file.close()

        if exc_type:
            print(f"Error occurred: {exc_value}")
        return False
