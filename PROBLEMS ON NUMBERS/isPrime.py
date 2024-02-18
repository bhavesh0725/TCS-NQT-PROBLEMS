import math

def isPrime(N):
  if N <= 1:
    print(N, "is not prime number")
    return
    
  for i in range(2,int(math.sqrt(N))+1):
    if N %i ==0:
      print(N, "is not prime number")
      break

  else:
    print(N, " is prime no")

if __name__=="__main__":
  N=int(input("enter the number: "))
  isPrime(N)
  


  # Time Complexity: O(√n)

  # Space Complexity: O(1)