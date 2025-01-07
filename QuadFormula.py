import math
def solve():
    print("Program to solve quadratic formula.")
    print("Equation format: ax^2 + bx + c = 0")


    #pull input
    try:
        a  = float(input("Enter the coeffectient a (must not be 0):"))
        if a == 0:
            # Coeffectient cannont be 0 because that would make the equation linear
            print("cannot be 0")
            return
        
        b = float(input("enter the coeffectient b:"))
        c = float(input("enter the costant c:"))
    except ValueError:
        print("Please enter a numeric value.")
        return
    
    #Calcualtes the discriminant (b^2 -4ac)
    discriminant = b**2 - 4*a*c
# check the discriminant to the types of roots
    if discriminant > 0:
        # two distinct real roots 
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"This equation has two real roots: {root1:2f} and {root2:2f}")
    elif discriminant == 0:
        # one repeated real root
        root = -b / (2*a)
        print(f"This equation has one real root: {root:2f}")
    else:
        # not a real root, i haven't learned imagenary numbers yet so this won't include them
        print(f"This equation has no real soulutions")

if __name__ == "__main__":
    solve()
