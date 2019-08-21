# To check whether a number is pallindrome or not.

num = int(input("Enter a number: "))
reverse = 0
while num != 0:
    reverse = reverse * 10 + num % 10
    num = num // 10
print(reverse)

if num == reverse:
    print("Number is pallindrome")
else:
    print("Not a pallindrome")
