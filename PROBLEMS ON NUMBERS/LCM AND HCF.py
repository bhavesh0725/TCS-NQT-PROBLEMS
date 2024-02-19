def gcd(a, b):
    """Function to compute the Greatest Common Divisor (GCD) using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Function to compute the Least Common Multiple (LCM) of two numbers."""
    return (a * b) // gcd(a, b)

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    hcf = gcd(num1, num2)
    lcm_val = lcm(num1, num2)

    print("HCF (GCD) of", num1, "and", num2, "is:", hcf)
    print("LCM of", num1, "and", num2, "is:", lcm_val)
