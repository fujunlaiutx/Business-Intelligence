import matplotlib.pyplot as plt

years = [2021, 2022, 2023, 2024, 2025]
sales = [100, 200, 300, 400, 600]

plt.bar(years, sales, color="steelblue")
plt.title("Annual Sales (2021-2025)")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.xticks(years)
plt.ylim(0, 700)
plt.tight_layout()
plt.show()
