# coding: utf-8
class Register(object):
    @staticmethod
    def get_total(transaction_list):
        """
        Static method to return the total of a list of transactions.
        :param transaction_list: list<Transaction>
        :return: float
        """
        total = 0
        # Recover Transaction.value for all x and sum.
        for x in transaction_list:
            total += float(x.value)
        return total
