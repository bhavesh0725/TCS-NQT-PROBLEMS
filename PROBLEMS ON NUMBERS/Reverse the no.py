def reverseNo(N):
  ans=0
  while N >0:
    digit=N%10
    ans = ans *10 + digit
    N //= 10

  return ans


if __name__=="__main__":
  N=int(input("Enter the No: "))
  print("The reverse of the no.", N, " is : ", reverseNo(N))
    