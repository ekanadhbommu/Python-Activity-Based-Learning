items = [('Headphones', 2, 900), ('Cable', 1, 300)];
category = 'Electronics'

subtotal = sum(q * p for name, q, p in items);
discount = min(subtotal * 0.10, 300) if subtotal >= 2000 else 0
rate = 0.18 if category == 'Electronics' else 0.05;
total = (subtotal - discount) * (1 + rate)
print(
    f'Subtotal: {subtotal:.2f} | Discount: {discount:.2f} | Tax: {(subtotal - discount) * rate:.2f} | Total: {total:.2f}')

