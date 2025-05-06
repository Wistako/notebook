import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

price = 120000
price_increase = 0.05 # 5% rocznie

freq = 12
years = 5
rate = 0.12 # 12% rocznie 

rate /= freq
nper = years * freq

# Cen mieszkania za 5 lat
future_price = price * (1 + price_increase) ** years
print(f"Cena mieszkania za {years} lat: {future_price:.2f} zł")

# Miesięczna wpłata
npf.pmt
monthly_payment = npf.pmt(rate, nper, 0, -future_price)
print(f"Wymagana miesięczna wpłata: {monthly_payment:.2f} zł")

# Wykres
months = np.arange(0, nper + 1)
price_growth = price * (1 + price_increase) ** (months / freq)
savings = npf.fv(rate, months, -monthly_payment, 0)

plt.figure(figsize=(10, 6))
plt.plot(months, price_growth, label='Cena mieszkania')
plt.plot(months, savings, label='Wartość lokaty')
plt.xlabel('Miesiące')
plt.ylabel('Wartość [zł]')
plt.title('Wzrost ceny mieszkania vs wartość lokaty')
plt.legend()
plt.grid(True)
plt.show()






