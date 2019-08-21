def calci():
    print("""Enter your choice from the following...
    + for addition
    - for substraction
    * for multiplication
    / for divide
    % for modulus or remainder
    ** for power""")


calci()
choice = input("> ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '+':
    if num1 == 56 and num2 == 9:
        print("56+9=77")
    else:
        print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '*':
    if num1 == 45 and num2 == 3:
        print("45 x 3 = 555")
    else:
        print(f"{num1} x {num2} = {num1 * num2}")
elif choice == '/':
    if num1 == 56 and num2 == 6:
        print("56 / 6 = 4")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
elif choice == '**':
    print(f"{num1} ** {num2} = {num1 ** num2}")
elif choice == '%':
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Invalid choice")


def again():
    print("""Do you want to calculate again
    Please type y for Yes and n for No""")
again()

repeat_again = input("> ")
if repeat_again == "y":
    calci()
elif repeat_again == "n":
    print("Quitting the calculator...")
    quit()
else:
    print("Invalid choice")
