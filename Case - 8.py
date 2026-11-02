qty = 100; material_rate = 500; labour = 12000; machine = 5000; selling_price = 750
material = qty * material_rate; wastage = material * 0.08; cost = material + wastage + labour + machine
revenue = qty * selling_price; profit = revenue - cost; target = 15000
print(f'Cost: {cost:.2f} | Revenue: {revenue:.2f} | Profit: {profit:.2f} | Target met: {profit >= target}')