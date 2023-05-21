class BuildingError(Exception):
    def __init__(self, amount, limit):
        self.Amount = amount
        self.Limit = limit
    def __str__(self):
        return f"Amount: {self.Amount} is greater then limit: {self.Limit}"

