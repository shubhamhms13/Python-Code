def prime_num(num):
    if num < 2:
        print("Not a prime number")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("Prime number")


n = int(input("Enter a number: "))
prime_num(n)
