nums = [num for num in range(1, 10)]
for num in nums:
    match num:
        case 1:
            print(f"{num}st")
        case 2:
            print(f"{num}nd")
        case 3:
            print(f"{num}rd")
        case _:
            print(f"{num}th")