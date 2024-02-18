def isArmstrong(N):
  
  armstrongSum=0
  N_string= str(N)
  digitlen=len(N_string)
  
  for i in N_string:
    product= int(i)**digitlen
    armstrongSum +=product

  return armstrongSum==N
    
  

if __name__=="__main__":
  N=int(input("Enter the no.: "))
  ans=isArmstrong(N)
  if ans==True:
    print("Armstrong No")
  else:
    print("Not Armstrong No")
    
  


    # In summary:

    # Time Complexity: O(d) d is no of digit

    # Space Complexity: O(1)
    