def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_strong_number(num):
    num_str = str(num)
    digit_factorial_sum = sum(factorial(int(digit)) for digit in num_str)
    return digit_factorial_sum == num

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_strong_number(num):
        print(num, "is a Strong Number.")
    else:
        print(num, "is not a Strong Number.")
