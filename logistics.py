number_loads = int(input())
microbus = 0
truck = 0
train = 0
total_amount = 0
average_price = 0

for x in range(number_loads):
    weight_per_load = int(input())

    if weight_per_load <= 3:
        microbus += weight_per_load
    elif weight_per_load <= 11:
        truck += weight_per_load
    else:
        train += weight_per_load

total_amount = (microbus + train + truck)

average_price = (microbus * 200 + truck * 175 + train * 120) / total_amount

print(f"{average_price:.2f}")
print(f"{microbus / total_amount * 100:.2f}%")
print(f"{truck / total_amount * 100:.2f}%")
print(f"{train / total_amount * 100:.2f}%")
