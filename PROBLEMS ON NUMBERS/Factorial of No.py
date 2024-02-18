def factorial(n):
  result = 1
  for i in range(1, n + 1):
      result *= i
  return result

if __name__ == "__main__":
  num = int(input("Enter a number to compute its factorial: "))
  result = factorial(num)
  print("Factorial of", num, "is", result)
