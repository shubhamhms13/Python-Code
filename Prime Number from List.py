def prime_num(num):
    if num < 2:
        print(num, "Not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(num, "Not a prime number.")
                break
        else:
            print(num, "Prime number")


numbers = [-3, 5, 7, 8, 29, 27, 29, 35, 37]
for number in numbers:
    prime_num(number)
