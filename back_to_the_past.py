inherited_money = float(input())
year_living = int(input())

ivan_age = 18

money_spend = 0

start_year = 1800

for x in range(start_year, year_living + 1):
    if x % 2 == 0:
        money_spend += 12_000
    else:
        money_spend += 12_000 + 50 * (ivan_age + (x - start_year))

if money_spend <= inherited_money:
    print(f"Yes! He will live a carefree life and will have {inherited_money - money_spend:.2f} dollars left.")
else:
    print(f"He will need {money_spend - inherited_money:.2f} dollars to survive.")

