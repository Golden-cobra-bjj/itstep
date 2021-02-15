a = int(input())
if a % 2 == 0 and a > 0:
    print(a, "Even positive number")
elif a % 2 != 0 and a > 0:
    print(a, "Odd positive number")
elif a % 2 == 0 and a < 0:
    print(a, "Even negative number")
elif a % 2 != 0 and a < 0:
    print(a, "Odd negative number")
else:
    print(a, "is zero")