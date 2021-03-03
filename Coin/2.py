n = int(input())

is_happy_number = False

num_dict = {}

num = n

while True:
    num_dict[num] = True

    sum_val = 0
    for val in list(str(num)):
        sum_val += int(val) ** 2

    if sum_val in num_dict:
        break

    if sum_val == 1:
        is_happy_number = True
        break

    num = sum_val

if is_happy_number:
    print(f"{n} is Happy Number.")
else:
    print(f"{n} is Unhappy Number.")

