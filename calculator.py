def main():
    while True:
        calc = int(input(f"\n1. Addition,\n2. Subtraction,\n3. Multiplication,\n4. Division,\n5. Exit.\n\nEnter your choice: "))
        if calc == 5:
            print("Exiting.")
            break
        x = int(input("Enter the first value: "))
        y = int(input("Enter the second value: "))
        if calc == 1:
            print(f"{x} + {y} = {addition(x,y)}")
        elif calc == 2:
            print(f"{x} - {y} = {addition(x,-y)}")
        elif calc == 3:
            print(f"{x} * {y} = {multiply(x,y)}")
        elif calc == 4:
            print(f"{x} / {y} = {division(x,y)}")

def addition(x,y):
    if y == 0:
        x = x
    elif y > 0:
        for i in range(y):
            x += 1
    elif y < 0:
        y = abs(y)
        for i in range(y):
            x -= 1
    return x

def multiply(x,y):
    m = 0
    if y == 0:
        x = 0
    elif y > 0:
        for i in range(y):
            m += x
    elif y < 0:
        y = abs(y)
        for i in range(y):
            m -= x
    return m

def division(x,y):
    count = 0
    if y == 0:
        count = "Error. Cannot divide by zero."
    elif y > 0:
        while x > y:
            x -= y
            count += 1
    elif y < 0:
        y = abs(y)
        while x > y:
            x -= y
            count += 1
    return count

main()
