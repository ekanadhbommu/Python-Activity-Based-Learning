age = 65
consultation = 500
diagnostics = 900
treatment = 1200
valid = min(consultation, diagnostics, treatment) >= 0
total = (consultation + diagnostics + treatment) * (0.9 if age >= 60 else 1)
print('Invalid charges' if not valid else f'Total: {total:.2f} | Category: {"Basic" if total < 2000 else "Standard"}')