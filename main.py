from typing import Dict, Any, List

# Level 0
def load_customers() -> Dict[str, Any]:
    pass

def load_products() -> Dict[str, Any]:
    pass

def load_transactions() -> Dict[str, Any]:
    pass

# Level 1
def does_customer_exist(id: str) -> bool:
    pass


def does_product_exist(id: str) -> bool:
    pass


def does_transaction_exist(id: str) -> bool:
    pass

# Level 2
def get_customer(id: str) -> Dict[str, Any]:
    pass


def get_product(id: str) -> Dict[str, Any]:
    pass


def get_transaction(id: str) -> Dict[str, Any]:
    pass

# Level 3

# get_detailed_transaction returns a dict with all the transaction fields
# but also with three new fiels: 
# - `customer`: With all the customer data
# - `product`: With all the product data
# - `total`: With how much the transaction is worth
def get_detailed_transaction(id: str) -> Dict[str, Any]:
    pass

# Level 4:
# get_customer_history returns a dict with all the customer data
# but also with a new fields:
# `transactions` is a list of DetailedTransaction
# `total_spent` is a dict list {currency_code: amount} where amount is the total spent by the customer in that currency
def get_customer_history(id: str) -> Dict[str, Any]:
    pass


#

