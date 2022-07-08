# x=int(input("Enter value"))
# y=int(input("enter value"))
# print(x+y)

# dict={}
# dict["First program"]="MyClass"
# print(dict)
#
# string="hello Hi"
# if string=="hello Hi":
#     print("string is matched")
# else:
#     print("string is not matched")

rating = "Good"


def sum_of_numbers():
    global rating
    rating = "Excellent"
    print(rating)


sum_of_numbers()
print(" r is ", rating)
