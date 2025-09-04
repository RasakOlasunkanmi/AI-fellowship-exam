# Question 1 Answer


# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Display operation options to the user
def calculator():
    print("======CALCULATOR======")

while True:
    print("=====Welcome To Calculator=====")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Take input from the user for operation choice
    print("=" * 40)
    choice = input("Enter choice (1/2/3/4/5): ").strip()
    if choice == '5':
        print("\n" + "=" * 40)
        print("\n" + "=" * 40)
        break

    # Perform calculation based on user's choice :
    try:
        if choice in ['1', '2', '3', '4']:  # Two-number operations
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
            if choice == '1':
                print("\n" + "=" * 40)
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("\n" + "=" * 40)
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("\n" + "=" * 40)
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("\n" + "=" * 40)
                print("Result:", divide(num1, num2))
        else:
            print("Invalid choice")
        
    except ValueError:
        print("\n" + "=" * 40)
        print("Error: Please enter valid numbers.")
    except OverflowError:
        print("\n" + "=" * 40)
        print("Error: Result is too large.")

    print("\n" + "=" * 40)
    continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
    if continue_choice not in ["yes", "y"]:
        print("\n" + "=" * 40)
        print("Exiting calculator... Goodbye!") 
        break
if __name__ == "__main__":
    calculator() 









#     # Question 2 Answer


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break            # break out of loop

    num = int(user_input)     # convert to integer

    if num % 2 == 0:
        print("The number is even")

    else:
        print("The number is odd")








# Question 3 Answer

while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == "exit":
        print("Goodbye!")
        break

    try:
        var = int(age)
        if var >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except:
        print("Invalid input. Please enter a number.")