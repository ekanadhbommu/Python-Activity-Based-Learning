distance = 350; travel_class = 'AC'; age = 65; cancelled = True
rate = 1.2 if travel_class == 'Sleeper' else 2.0; fare = distance * rate
fare = fare * (0.8 if age >= 60 else 1); total = fare + 40; refund = total - 0.25*fare if cancelled else 0
print(f'Fare: {total:.2f} | Refund on cancellation: {refund:.2f}')
