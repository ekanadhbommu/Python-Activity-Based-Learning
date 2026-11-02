u = 180;
prev_bill = 350
energy = min(u, 100) * 2 + min(max(u - 100, 0), 100) * 3 + max(u - 200, 0) * 5
bill = (energy + 50) * 1.05 - (20 if u < 100 else 0)
print(f'Bill: {bill:.2f}', 'Unusual increase:', bill > prev_bill * 1.30)

