def apSeries(a,n,d):
  list1=[]
  
  for i in range(n):
    list1.append(a+(i*d))

  return list1

def sumAP(a,n,d):
  sum= (n/2) * ((2*a) + (n-1)*d)
  return sum
  
  
if __name__=="__main__":
  a=int(input("Enter the value of a: "))
  n=int(input("Enter the value of n: "))
  d=int(input("Enter the value of d: "))
  print("AP series: ", apSeries(a,n,d))
  print("Sum of AP series: ", sumAP(a,n,d))
  
  
 # In summary:

 # Time Complexity: O(n)
 # Space Complexity: O(n)


