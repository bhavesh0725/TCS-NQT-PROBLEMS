def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in s:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    string = input("Enter a string: ")
    result = remove_vowels(string)
    print("String after removing vowels:", result)
