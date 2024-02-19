def gcd(a, b):
  while b:
      a, b = b, a % b
  return a

def addFraction(a, b, c, d):
  numerator = (a * d) + (b * c)
  denominator = b * d
  common_divisor = gcd(numerator, denominator)
  return numerator // common_divisor, denominator // common_divisor

if __name__ == "__main__":
  a = int(input("Enter the numerator of the first fraction: "))
  b = int(input("Enter the denominator of the first fraction: "))
  c = int(input("Enter the numerator of the second fraction: "))
  d = int(input("Enter the denominator of the second fraction: "))

  result_num, result_denom = addFraction(a, b, c, d)
  print("Sum of the fractions:", result_num, "/", result_denom)
