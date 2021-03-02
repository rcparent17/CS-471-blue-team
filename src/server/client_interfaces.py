from transactions import *


def try_transaction(transaction: UnprocessedTransaction) -> str:
    result = transaction.process()
    if type(result) is not ProcessedTransaction:
        return result
