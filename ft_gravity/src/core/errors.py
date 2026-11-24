class minimumNumberError(BaseException):
    def __init__(self):
        super().__init__("The value you entered must be greater than 0.")

class invailedNumberError(BaseException):
    def __init__(self):
        super().__init__("You can only enter a value between 0 and 1.")