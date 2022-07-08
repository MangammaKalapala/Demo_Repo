class sample:

    # Count Alphabets Digits and Special Characters in a String
    def count(self,str):
        alphabets = digits = special = 0
        for i in range(len(str)):
            if str[i].isalpha():
                alphabets = alphabets + 1
            elif str[i].isdigit():
                digits = digits + 1
            else:
                special = special + 1

        print('In the given string alphabets :', alphabets, '\tDigits:', digits, '\tSpecial Characters:', special)

    # Check a Given String is Palindrome
    def palindrome(self, name):
        rev = reversed(name)
        if name == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

    # Count Vowels and Consonants in a String
    def countVC(self, letters):
        vowels = consonants = 0
        letters.lower()
#        letters.replace(" ",'')
        for i in letters:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                vowels = vowels + 1
            else:
                consonants = consonants + 1

        print("The number of vowels:", vowels)
        print("The number of consonants:", consonants)

    # Count Total Number of Words in a String
    def countTN(self, words):
        no_of_words = 1
        for i in range(len(words)):
            if words[i] == ' ' or words=='\t' or words=='\n':
                no_of_words = no_of_words + 1
        print('No.of words in a given string is: ', no_of_words)

    # Reverse String using For Loop
    def reverse_string(self, rev):
        reverse = ''
        for i in rev:
            reverse = i + reverse
        print('Reverse string is:', reverse)

    # Remove Duplicates from List
    def removeDuplicate(self, dup):
        sam_list = list(set(dup))
        sam_list.sort()
        print("The list after removing duplicates : " + str(sam_list))

    # Remove Even Numbers in a List
    def remove_even_no(self, even_no):
        for i in even_no[:]:
            if (i % 2) == 0:
                even_no.remove(i)
        print('List Items after removing even Items =', even_no)

    # Second Largest Number in a List
    def second_max(self, l):
        second_largest = l[0]
        largest_val = l[0]
        for i in range(len(l)):
            if l[i] > largest_val:
                largest_val = l[i]
        for i in range(len(l)):
            if l[i] > second_largest and l[i] != largest_val:
                second_largest = l[i]
        print('Second largest number is: ', second_largest)

    # Sum of Even and Odd Numbers in a List
    def sum_ofEven_Odd_number(self, num):
        odd_sum = 0
        even_sum = 0
        for sub in num:
            if sub % 2 == 0:
                even_sum += sub
            else:
                odd_sum += sub
        print("Sum of Even Numbers in a List: ", even_sum)
        print("Sum of Odd Numbers in a List : ", odd_sum)

    # Reverse List
    def reverse_list(self, r_list):
        reverse_list = r_list[::-1]
        print('Reverse List is: ', reverse_list)

name = 'Fission Labs #2022'
l = [1, 2, 3, 2, 4, 8, 9, 1, 7, 6, 4, 5]
t = sample()
t.count(name)
t.palindrome(name)
t.countVC(name)
t.countTN(name)
t.reverse_string(name)
t.removeDuplicate(l)
t.second_max(l)
t.sum_ofEven_Odd_number(l)
t.reverse_list(l)
t.remove_even_no(l)
