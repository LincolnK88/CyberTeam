import math
def solve():
    print("Program to solve quadratic formula.")
    print("Equation format: ax^2 + bx + c = 0")


    #pull input as a float for each variable 
    try:
        a  = float(input("Enter the coeffectient a (must not be 0):"))
        if a == 0:
            print("cannot be 0")
            return
        
        b = float(input("enter the coeffectient b:"))
        c = float(input("enter the costant c:"))
    except ValueError:
      #catches value errors
        print("Please enter a numeric value.")
        return
    
    # 
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"This equation has two real roots: {root1:2f} and {root2:2f}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"This equation has one real root: {root:2f}")
    else:
        print(f"This equation has no real soulutions")

if __name__ == "__main__":
    solve()
