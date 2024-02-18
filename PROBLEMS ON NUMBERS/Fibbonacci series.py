def fibonacci(n):
  fib_series = []
  a, b = 0, 1
  for _ in range(n):
      fib_series.append(a)
      a, b = b, a + b
  return fib_series

if __name__ == "__main__":
  num_terms = int(input("Enter the number of terms: "))
  fib_series = fibonacci(num_terms)
  print("Fibonacci series:")
  print(fib_series)
