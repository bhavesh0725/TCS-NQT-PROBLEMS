def is_automorphic(num):
    square = num * num
    num_str = str(num)
    square_str = str(square)
    return square_str.endswith(num_str)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_automorphic(num):
        print(num, "is an Automorphic Number.")
    else:
        print(num, "is not an Automorphic Number.")
