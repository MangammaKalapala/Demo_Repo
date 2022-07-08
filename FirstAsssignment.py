class sample:

    def factorial(self):
        fact = 1
        for i in range(1, self+1):
            fact = fact*i
        print("The factorial of", self, "is", fact)

    def palindrome(self):
        rev = reversed(self)
        if self == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

    def count(str):
        alphabets = digits = special = 0
        for i in range(len(str)):
            if str[i].isalpha():
                alphabets = alphabets + 1
            elif str[i].isdigit():
                digits = digits + 1
            else:
                special = special + 1

        print("Total Number of Alphabets in this String :", alphabets)
        print("Total Number of Digits in this String :  ", digits)
        print("Total Number of Special Characters in this String :  ", special)

    def getMissingNumber(self):
        missing_elements = []
        for ele in range(self[0], self[-1] + 1):
            if ele not in self:
                missing_elements.append(ele)
        print(missing_elements)

    def max_min(self):
        maximum = max(self)
        minimum = min(self)
        print("Maximum number in the given list ", maximum)
        print("Minimum number in the given list ", minimum)

    def removeDuplicate(self):
        sam_fruits = list(set(self))
        sam_fruits.sort()
        print("The list after removing duplicates : " + str(sam_fruits))


Alist = [11, 12, 14, 15, 16, 17, 18, 19, 20]
l = [1, 176, 209, 456, 789, 2, 44, 56, 56, 7, 9, 12]
fruits = ['apple', 'cherry', 'orange', 'mango', 'mango', 'apple', 'orange']

t = sample
t.factorial(5)
t.palindrome('FissionLabs')
t.count('#FissionLabs')
t.getMissingNumber(Alist)
t.max_min(l)
t.removeDuplicate(fruits)
