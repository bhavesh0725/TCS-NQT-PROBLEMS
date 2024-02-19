def ascii_value(char):
    return ord(char)

if __name__ == "__main__":
    char = input("Enter a character: ")
    ascii_val = ascii_value(char)
    print("ASCII value of", char, "is:", ascii_val)
