from typing import Any, Dict, List
import faker
import random
import string
import csv


ID_LENGHT = 25
AMOUNT_OF_TRANSACTIONS = 10_000
AMOUNT_OF_CUSTOMERS = int(AMOUNT_OF_TRANSACTIONS / 10)
AMOUNT_OF_PRODUCTS = int(AMOUNT_OF_TRANSACTIONS / (10 * 5))

fake = faker.Faker()

def get_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
    
def generate_id(prefix: str) -> str:
    assert(len(prefix)< ID_LENGHT - 5)
    return f'{prefix}_{get_random_string(ID_LENGHT - len(prefix))}'

generate_customer_id = lambda : generate_id('cus')
generate_product_id = lambda : generate_id('pro')
generate_transaction_id = lambda : generate_id('txn')

def generate_customer() -> Dict[str, Any]:
    return {
        'id': generate_customer_id(),
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'active': random.choice([True] * 9 + [False]),
    }

def generate_product() -> Dict[str, Any]:
    return {
        'id': generate_product_id(),
        'name': f'{fake.word()} {fake.word()}',
        'description': fake.text(),
        'price': int(random.uniform(10, 1000)),
        'currency': random.choice(['USD'] * 8 + ['GBP'] * 2),
        'active': random.choice([True] * 9 + [False]),
    }

def generate_transactions(customers: List[Dict[str, Any]], products: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    customers = customers.copy()
    products = products.copy()

    # Remove customers so they don't have transactions
    for _ in range(int(AMOUNT_OF_CUSTOMERS * 0.05)):
        customers.pop(random.choice(range(len(customers))))

    # Remove products so they don't have transactions
    for _ in range(int(AMOUNT_OF_PRODUCTS * 0.05)):
        customers.pop(random.choice(range(len(customers))))

    transactions = []
    for _ in range(AMOUNT_OF_TRANSACTIONS):
        customer_id = customers[random.choice(range(len(customers)))]['id']
        product_id = customers[random.choice(range(len(products)))]['id']
        transactions.append({
            'id': generate_transaction_id(),
            'customer_id': customer_id,
            'product_id': product_id,
            'status': random.choice(['paid'] * 10 + ['pending'] * 5 + ['failed'] * 3),
            'quantity': int(random.uniform(1,10))
        })
    return transactions


customers = [generate_customer() for _ in range(AMOUNT_OF_CUSTOMERS)]
products = [generate_product() for _ in range(AMOUNT_OF_PRODUCTS)]
transactions = generate_transactions(customers, products)

with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list(customers[0].keys()))
    for customer in customers:
        writer.writerow(list(customer.values()))

with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list(products[0].keys()))
    for product in products:
        writer.writerow(list(product.values()))

with open('transactions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list(transactions[0].keys()))
    for transaction in transactions:
        writer.writerow(list(transaction.values()))

def a():
    pass