import csv
import json
import random
from datetime import datetime, timedelta

OUTPUT_DIR = '.'

outlets = [
    {'outlet_id': 'OUT001', 'name': 'Eta-Beta-Pi Baker Street', 'region': 'London'},
    {'outlet_id': 'OUT002', 'name': 'Eta-Beta-Pi Piccadilly', 'region': 'London'},
    {'outlet_id': 'OUT003', 'name': 'Eta-Beta-Pi Manchester', 'region': 'North West'},
    {'outlet_id': 'OUT004', 'name': 'Eta-Beta-Pi Glasgow', 'region': 'Scotland'},
]

products = [
    {'product_id': 'P001', 'name': 'Retro Burger', 'category': 'Burger', 'price': 5.95},
    {'product_id': 'P002', 'name': 'Heritage Fries', 'category': 'Sides', 'price': 2.45},
    {'product_id': 'P003', 'name': 'Tea Room Shake', 'category': 'Beverage', 'price': 3.15},
    {'product_id': 'P004', 'name': 'Vintage Salad', 'category': 'Salad', 'price': 4.85},
]

promotions = [
    {'promo_id': 'PROMO10', 'description': '10% off Retro Burger', 'discount_pct': 0.10},
    {'promo_id': 'PROMO2FOR1', 'description': 'Buy one get one free Fries', 'discount_pct': 0.50},
    {'promo_id': 'PROMO5', 'description': '£5 bundle offer', 'discount_pct': 0.15},
]

start_date = datetime(2026, 5, 1)

def generate_legacy_pos_csv(filename):
    rows = []
    for outlet in outlets:
        for i in range(20):
            order_date = start_date + timedelta(days=random.randint(0, 29))
            product = random.choice(products)
            promo = random.choice(promotions + [None, None])
            quantity = random.randint(1, 4)
            revenue = product['price'] * quantity
            discount = revenue * (promo['discount_pct'] if promo else 0)
            rows.append({
                'outlet_id': outlet['outlet_id'],
                'order_id': f"L{outlet['outlet_id']}-{i+1:04d}",
                'order_date': order_date.strftime('%Y-%m-%d'),
                'product_id': product['product_id'],
                'product_name': product['name'],
                'category': product['category'],
                'quantity': quantity,
                'unit_price': f"{product['price']:.2f}",
                'revenue': f"{revenue:.2f}",
                'discount': f"{discount:.2f}",
                'promotion_code': promo['promo_id'] if promo else '',
            })
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def generate_modern_pos_json(filename):
    records = []
    for outlet in outlets:
        for i in range(20):
            order_date = (start_date + timedelta(days=random.randint(0, 29))).isoformat()
            product = random.choice(products)
            promo = random.choice(promotions + [None])
            quantity = random.randint(1, 5)
            records.append({
                'outlet_id': outlet['outlet_id'],
                'order_id': f"M{outlet['outlet_id']}-{i+1:04d}",
                'timestamp': order_date,
                'items': [
                    {
                        'product_id': product['product_id'],
                        'name': product['name'],
                        'category': product['category'],
                        'quantity': quantity,
                        'unit_price': product['price'],
                        'promotion_code': promo['promo_id'] if promo else None,
                    }
                ],
                'payment_method': random.choice(['card', 'cash', 'voucher']),
                'customer_count': random.randint(1, 4),
            })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({'transactions': records}, f, indent=2)


def generate_monthly_report_csv(filename):
    rows = []
    for outlet in outlets:
        rows.append({
            'outlet_id': outlet['outlet_id'],
            'month': '2026-05',
            'sales_total': f"{random.uniform(15000, 32000):.2f}",
            'labor_cost': f"{random.uniform(4000, 9000):.2f}",
            'food_cost': f"{random.uniform(5000, 12000):.2f}",
            'other_expenses': f"{random.uniform(1200, 3500):.2f}",
            'customer_count': random.randint(2500, 6800),
            'average_ticket': f"{random.uniform(4.50, 7.80):.2f}",
        })
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def generate_franchise_costs_csv(filename):
    rows = []
    categories = ['Rent', 'Utilities', 'Insurance', 'Maintenance', 'Marketing']
    for outlet in outlets:
        for category in categories:
            rows.append({
                'outlet_id': outlet['outlet_id'],
                'month': '2026-05',
                'cost_category': category,
                'amount': f"{random.uniform(500, 4500):.2f}",
                'vendor': random.choice(['Local Supplier', 'Corporate', 'Utility Co', 'Maintenance Ltd']),
            })
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    generate_legacy_pos_csv('data_samples/pos_legacy_may_2026.csv')
    generate_modern_pos_json('data_samples/pos_modern_may_2026.json')
    generate_monthly_report_csv('data_samples/monthly_report_may_2026.csv')
    generate_franchise_costs_csv('data_samples/franchise_costs_may_2026.csv')
    print('Synthetic sample files generated in data_samples/')

if __name__ == '__main__':
    main()
