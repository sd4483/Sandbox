"""
lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower,upper))
for i in range(10, 120, 11):
          print("{} {}".format(i, chr(i)))
"""
def get_number(prompt):
        print(prompt)
        flag = False
        while flag == False:
            try:
                num = int(input("Enter the number:"))
                while num < 10 or num > 50:
                    print("Error")
                    num = int(input("Enter the number:"))
                flag = True
            except ValueError:
                print("Invalid number")
        return num

lower = get_number("Enter the first number(10-50):")
upper = get_number("Enter the second number(10-50):")

for i in range(lower,upper):
    print("{:>3} -> {}".format(i,chr(i)))



