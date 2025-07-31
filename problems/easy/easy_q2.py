def largest_of_two(a, b):
    if a > b:
        return a   
    else:
        return b

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))
        res = largest_of_two(num1, num2)
        print("The largest number is:", res)
    except ValueError:
        print("ENTER ONLY INTEGER VALUES")
