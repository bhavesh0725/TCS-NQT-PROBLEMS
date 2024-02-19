def count_vowels_consonants_spaces(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    num_vowels = sum(1 for char in s if char.lower() in vowels)
    num_consonants = sum(1 for char in s if char.lower() in consonants)
    num_spaces = sum(1 for char in s if char.isspace())

    return num_vowels, num_consonants, num_spaces

if __name__ == "__main__":
    string = input("Enter a string: ")
    vowels, consonants, spaces = count_vowels_consonants_spaces(string)
    
    print("Number of vowels:", vowels)
    print("Number of consonants:", consonants)
    print("Number of spaces:", spaces)
