import math

def isPrime(N):
  if N ==1:
    return 
    
    
  for i in range(2,int(math.sqrt(N))+1):
    if N %i ==0:
      break

  else:
    print(N, end=" ")



def primeInRange(start, end):
  for i in range(start, end):
    isPrime(i)
    
  
  

if __name__=="__main__":
  start=int(input("enter the start number: "))
  end=int(input("enter the end number: "))
  primeInRange(start, end)
  


  # Time Complexity: O(√n)

  # Space Complexity: O(1)