def pattern():
    num = int(input("Enter Number: "))
    for p in range(1, num + 1):
        for c in range(1, p + 1):
            print(c, end=' ')
        print(" ")


pattern()


def sum():
    myList = [23, 45, 12, 10, 25]
    ele = total = 0
    while ele < len(myList):
        total = total + myList[ele]
        ele = ele + 1
    print("Sum of all elements in given list: ", total)


sum()


def multiplication():
    n = int(input('Enter Multiplication Number: '))
    i = 1
    while i <= 10:
        print(n * i)
        i = i + 1


multiplication()


def reverseNumbers():
    num = int(input("Enter Number(print reverse): "))
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10
    print('The reverse number is =', reverse)


reverseNumbers()
