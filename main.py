import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_acumulate = True
    n1 = float(input("Enter the first number: "))

    while should_acumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Select the operation: ")
        n2 = float(input("Enter the second number: "))
        final_value = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {final_value}")
        choice = input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start a vew calculation: ")

        if choice == "y":
            n1 = final_value
        else:
            should_acumulate = False
            print("\n" * 20)
            calculator()

calculator()