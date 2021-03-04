from datetime import datetime
import random
from typing import DefaultDict, List, Optional, Union

from databaseClasses import Inventory, Transaction
from databaseHelper import getInventoryByName, updateInventory


class Money:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __add__(self, other):
        new_cents = self.cents + other.cents
        new_dollars = self.dollars + other.dollars + (new_cents // 100)
        return Money(new_cents % 100, new_dollars)

    def __str__(self):
        return f"${self.dollars}.{self.cents}"


class Payment:
    def __init__(self, value: Money, information: str):
        self.value = value
        self.information = information
        pass

    def __add__(self, other):
        return self.value + other.value

    def __str__(self) -> str:
        return f"{type(self)}, {self.value}"

    def process(self) -> bool:
        raise TypeError()

    def withdraw(self):
        # Not implemented, we aren't connecting to anything to withdraw money
        # from any accounts
        pass


class Cash(Payment):
    def __init__(self, value: Money):
        super().__init__(value, "")

    def process(self) -> bool:
        # It's always assumed that the cash is present
        return True

    def __str__(self):
        return self.value


class CreditCard(Payment):
    def __init__(self, value: Money, card_number: str, zip_code: str):
        information = f"{card_number, zip_code}"
        super().__init__(value, information)

    def process(self) -> bool:
        # For now just have it fail 10% of the time
        return self.information is not None and random.random() > 0.1

    def __str__(self):
        return f"credit card at {self.value} with info {self.information}"


class MemberCard(Payment):
    def __init__(self, value: Money, card_number: str, member_pin: str):
        information = f"{card_number, member_pin}"
        super().__init__(value, information)

    def process(self) -> bool:
        # THis should eventually do a lookup to see how much money
        # the associated member has.
        # For now just have it fail 10% of the time
        return self.information is not None and random.random() > 0.1

    def __str__(self):
        return f"Member card at {self.value} with info {self.information}"


class ProcessedTransaction:
    def __init__(self, payments, items, createdTime, customer_name: str):
        self.payments = payments
        self.items = items
        self.customer_name = customer_name
        self.createdTime = createdTime

    @staticmethod
    def from_unprocessed(unprocessed):
        return ProcessedTransaction(
            unprocessed.payments,
            unprocessed.items,
            unprocessed.createdTime,
            unprocessed.customer_name,
        )

    def database_repr(self) -> Transaction:
        """
        Creates a `Transaction` for putting in the database
        """
        return Transaction(
            None, sum(self.payments), self.createdTime, self.items, self.customer_name
        )


class UnprocessedTransaction:
    def __init__(
        self, payments: List[Payment], items: List[Inventory], customer_name: str
    ):
        self.payments = payments
        self.items = items
        self.createdTime = datetime.now()
        self.customer_name = customer_name

    def items_are_valid(self) -> bool:
        same_items: DefaultDict = DefaultDict(int)
        for item in self.items:
            same_items[item.name] += 1
        for name in same_items.keys():
            inventory = getInventoryByName(name)
            stock = inventory.stock if inventory else None
            print(stock)
            if stock is None or stock < same_items[name]:
                return False
        return True

    def process(self) -> Union[ProcessedTransaction, str]:
        if not self.items_are_valid():
            return "Invalid items, may not be enough stock"

        # Check that all the payments will process correctly
        for payment in self.payments:
            if not payment.process():
                return f"Payment failure for {str(payment)}"

        # Take out all the money from accounts
        for payment in self.payments:
            payment.withdraw()

        total_value = sum([pay.value for pay in self.payments], Money(0, 0))

        # Take out the stock for the items
        inventory_expended: DefaultDict = DefaultDict(int)
        for item in self.items:
            inventory_expended[item.name] += 1

        current_inventory = {
            name: getInventoryByName(name) for name in inventory_expended.keys()
        }

        for (name, inv) in current_inventory.items():
            updateInventory(
                inv.id, inv.name, inv.cost, inv.stock - inventory_expended[name]
            )

        # The transaction is processed!
        return ProcessedTransaction.from_unprocessed(self)
