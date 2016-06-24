# coding: utf-
class Transaction(object):
    def __init__(self, number, name, category, date, value):
        """
        An object to hold each individual transaction added.
        Constructor
        :param number: int
        :param name: string
        :param category: string
        :param date: datetime
        :param value: float
        """
        self.number = number  # ID Number for the transaction.
        self.name = name  # Description identifier for the transaction.
        self.category = category  # Category for the transaction.
        self.date = date  # datetime entry for the time at which the transaction was added.
        self.value = value  # Amount of the transaction.
