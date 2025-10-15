class BaseException(Exception):
    def __init__(self, message: str = "Ошибка при выполнении"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"