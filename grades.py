number_students = int(input())
top = 0
dobur = 0
sreden = 0
fail = 0
ocenka = 0
average_g = 0

for x in range(number_students):
    grades = float(input())

    if grades >= 5:
        top += 1
        ocenka += grades
    elif grades >= 4:
        dobur += 1
        ocenka += grades
    elif grades >= 3:
        sreden += 1
        ocenka += grades
    else:
        fail += 1
        ocenka += grades

average_g = ocenka / number_students

print(f"Top students: {top / number_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {dobur / number_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {sreden / number_students * 100:.2f}%")
print(f"Fail: {fail / number_students * 100:.2f}%")
print(f"Average: {average_g:.2f}")


