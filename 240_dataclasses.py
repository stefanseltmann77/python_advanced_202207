from dataclasses import dataclass
from datetime import date
from typing import List, Tuple


@dataclass
class Customer:
    customer_id: int
    name: str
    year_of_birth: int
    account_balance: float = 0.0

    @property
    def age(self) -> int:
        return date.today().year - self.year_of_birth

    @property
    def has_debt(self) -> bool:
        return True if self.account_balance < 0 else False

    def __str__(self) -> str:
        return f"Customer #{self.customer_id}: " \
               f"{self.name}, born in {self.year_of_birth}"


# Example for query result
database_result: List[Tuple] = \
    [(1, "John Doe", 1980, 120.0),
     (2, "Joe Nobody", 1977, -20.0),
     (3, "Jane Sombody", 1930, 56.3)]

# Parsing as Customer objects
customers: List[Customer] = [Customer(*record)
                             for record in database_result]

# Filtern on subset
suitable_for_loans: List[Customer] = \
    [customer for customer in customers
     if not customer.has_debt
     and customer.age < 70]

customer_sample: Customer = suitable_for_loans.pop()
print(customer_sample)
# Customer #1: John Doe, born in 1980
