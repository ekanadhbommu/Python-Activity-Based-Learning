usage = 3; days = 28; budget = 350; plans = [('A', 199, 2, 28), ('B', 299, 5, 56)]
costs = [(n, p + max(usage - d, 0)*20, v) for n, p, d, v in plans if v >= days and p + max(usage - d, 0)*20 <= budget]
best = min(costs, key=lambda x: x[1]) if costs else None
print('Best plan:', best if best else 'No eligible plan')
