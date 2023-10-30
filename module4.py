def find_index():
    # Ask the user for input N
    N = int(input("Enter the value of N (positive integer): "))

    # Read N numbers from the user
    numbers = []
    for i in range(N):
        num = int(input("Enter number {i + 1}:\n"))
        numbers.append(num)

    # Ask the user for input X
    X = int(input("Enter the value of X (integer):\n"))

    # Check if X is in the list and print the result
    if X in numbers:
        index = numbers.index(X) + 1
        print("The index of {X} is: {index}")
    else:
        print("-1")

# Call the function to execute the program
find_index()
