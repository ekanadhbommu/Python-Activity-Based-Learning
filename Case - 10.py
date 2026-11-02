venue = 20000; equipment = 8000; transport = 5000; people = 120; catering = 250; certificate = 50
fixed = venue + equipment + transport; per_person = catering + certificate; total = fixed
+ people * per_person
sponsor = 15000; fee = 400; shortfall = total - sponsor - people * fee; minimum = (fixed
- sponsor) // (fee - per_person) + 1
print(f'Total cost: {total} | Funding shortfall: {max(shortfall, 0)} | Break-even registrations: {minimum}')
