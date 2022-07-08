class sample:
    def count(self):
        name = input('Enter a String:')
        alphabets = digits = special = 0
        for i in range(len(name)):
            if name[i].isalpha():
                alphabets = alphabets + 1
            elif name[i].isdigit():
                digits = digits + 1
            else:
                special = special + 1

        print("In the given string alphabets :", alphabets, 'Digits: ', digits, 'and Special Characters: ', special)

    def palindrome(self):
        name = input('Enter a String:')
        rev = reversed(name)
        if name == rev:
            print("Palindrome")
        else:
            print("Not Palindrome")

    def count_vowels_consonants(self):
        name = input('Enter a String:')
        vowels = consonants = 0
        name.lower()
        for i in name:
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                vowels = vowels + 1
            else:
                consonants = consonants + 1

        print("The number of vowels:", vowels)
        print("The number of consonants:", consonants)

    def no_of_words(self):
        name = input('Enter a String:')
        no_of_words = 0
        for i in name:
            no_of_words = no_of_words + 1
        print('No.of words in a given string is: ', no_of_words)

    def reverse_string(self):
        name = input('Enter a String:')
        reverse = ''
        for i in name:
            reverse = i + reverse
        print(reverse)

    def remove_duplicates(self):
        name_list = list(input('Enter List: '))
        sam_list = list(set(name_list))
        sam_list.sort()
        print("The list after removing duplicates : ", sam_list)


s = sample()
s.count()
s.palindrome()
s.count_vowels_consonants()
s.no_of_words()
s.reverse_string()
