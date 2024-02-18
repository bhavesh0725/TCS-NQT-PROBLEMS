def isPalindrome(X):
    Y=0
    while X>0:
        digit=X % 10
        Y= Y*10 + digit
        X = X//10

    return Y



if __name__ == "__main__":
  X = int(input("Enter the number: "))
  dummy = X
  Y = isPalindrome(X)
  if dummy == Y:
      print("Palindrome Number")
  else:
      print("Not Palindrome Number")