def isPerfectNo(N):
  sum=0
  for i in range(1, N):
    if N % i==0:
      sum +=i

  return sum == N

if __name__=="__main__":
  n=int(input("Enter the No: "))
  ans=isPerfectNo(n)
  if ans == True:
    print(n," is perfect no.")
  else:
    print(n, " is not perfect no.")



# In summary:

# Time Complexity: O(N)
# Space Complexity: O(1)