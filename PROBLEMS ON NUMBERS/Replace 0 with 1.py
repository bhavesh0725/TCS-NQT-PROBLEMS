def replaceZeroWithOne(N):
  numStr=str(N)
  numStr= numStr.replace('0', '1')
  return int(numStr)

if __name__=="__main__":
  N= int(input("Enter the Number: "))
  print("After replacing O with 1, the Number became: ", replaceZeroWithOne(N))
  