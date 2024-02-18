def isPalindrome(X):
    Y=0
    while X>0:
        digit=X % 10
        Y= Y*10 + digit
        X = X//10

    return Y

def PalidromeNo(start, end):
    for i in range(start, end):
        ans=isPalindrome(i)
        if i== ans:
            print(i, end=" ")
        else:
            pass

if __name__ == "__main__":
    
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    PalidromeNo(start, end)



# Summary:
# Time Complexity: O(N * log(X))
# Space Complexity: O(1)