def maxAndMin(N):
  max=0
  min=9
  # Special case when N is a single digit
  if N < 10:
      return N, N
    
  while N > 0:
    digit= N% 10
    if digit >= max :
      max= digit
    if digit <= min:
      min=digit
    N //= 10
  return max, min

if __name__=="__main__":
  N=int(input("Enter the no: "))
  max,min= maxAndMin(N)
  print("Maximum: ", max, " Minimum: ", min)



