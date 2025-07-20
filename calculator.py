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
    negative = False
    if y < 0:
        negative = not negative
        y = -y
    if x < 0:
        negative = not negative
        x = -x
    m = 0
    for i in range(y):
        m += x
    return -m if negative else m

def division(x,y):
    if y == 0:
        return "Error. Cannot divide by zero."
    if x == 0:
        return 0
    negative = False
    if x < 0:
        negative = not negative
        x = -x
    if y < 0:
        negative = not negative
        y = -y
    count = 0
    while x >= y:
        x -= y
        count += 1
    return -count if negative else count

main()
