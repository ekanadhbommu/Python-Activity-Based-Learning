basic = 25000;
allowances = 5000;
overtime = 2000;
incentives = 1500
gross = basic + allowances + overtime + incentives
deduction = 0.05 * min(gross, 20000) + 0.10 * max(gross - 20000, 0)
print(f'Gross: {gross:.2f} | Deduction: {deduction:.2f} | Net: {gross - deduction:.2f}')
