expenses = [('Hotel', 300), ('Food', 100), ('Transport', 80)]; rate = 83;
budget = 50000

converted = [(name, amount * rate) for name, amount in expenses]
total = sum(amount for name, amount in converted) * 1.02; largest = max(converted, key=lambda x: x[1])
print(f'Total with fee: {total:.2f} | Largest: {largest[0]} | Within budget: {total <= budget}')
