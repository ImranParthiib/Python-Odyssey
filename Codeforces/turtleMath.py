def is_divisible_by_3(arr):
    total_sum = sum(arr)
    if total_sum % 3 == 0:
        return True

    for i in range(len(arr)):
        temp_arr = arr[:i] + arr[i+1:]
        if sum(temp_arr) % 3 == 0:
            return True

    return False


def turtle_math(new_f_x):
    sum_x = sum(new_f_x)

    if len(new_f_x) == 0:
        return 0

    elif sum_x % 3 == 0:
        return 0

    elif (sum_x + 1) % 3 == 0:
        return 1

    count = 0

    while len(new_f_x):
        if is_divisible_by_3(new_f_x):
            count += 1
            return count
        new_f_x.pop()
        count += 1
        sum_x = sum(new_f_x)
        if sum_x % 3 == 0:
            return count
        elif (sum_x + 1) % 3 == 0:
            count += 1
            return count

    return count


for _ in range(int(input())):
    n = int(input())
    if n == 0:
        x = []
    else:
        x = [int(i) for i in input().split()]

    new_x = [num for num in x if num % 3 != 0]

    new_x.sort()

    print(turtle_math(new_x))