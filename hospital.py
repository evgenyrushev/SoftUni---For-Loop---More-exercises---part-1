period = int(input())

treated = 0
untreated = 0
doctors = 7

for x in range(1, period + 1):
    patients = int(input())

    if x % 3 == 0:
        if untreated > treated:
            doctors += 1
    if patients > doctors:
        untreated += patients - doctors
        treated += doctors
    else:
        treated += patients


print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
