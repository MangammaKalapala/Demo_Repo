class sample:

    def pattern(self):
        for r in range(2, 7):
            line = ""
            for c in range(1, r):
                line = line + str(c) + " "
            print(line)

    def sum(self):
        ele = total = 0
        while ele < len(self):
            total = total + self[ele]
            ele = ele + 1
        print("Sum of all elements in given list: ", total)

    def multiples(self):
        print(self)
        while self < 20:
            self = self + 1
            if self % 2 == 1:
                continue
            print(self)

    def reverseNumbers(self):
        reverse = 0
        while self > 0:
            last_digit = self % 10
            reverse = reverse * 10 + last_digit
            self = self // 10
        print('The reverse number is =', reverse)


myList = [23, 45, 12, 10, 25]
s = sample
s.pattern(1)
s.sum(myList)
s.multiples(2)
s.reverseNumbers(123)
