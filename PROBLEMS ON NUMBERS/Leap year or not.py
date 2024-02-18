def leapYear(Y):
  if ((Y%4 ==0) and (Y %100 !=0)) or (Y % 400 ==0):
    return "Leap Year"
  else:
    return "Not leap year"
  
if __name__=="__main__":
  Y=int(input("Enter the Year: "))
  print(Y ," : ", leapYear(Y))
  
 
  
  
# In summary:

# Time Complexity: O(1)
# Space Complexity: O(1)


