#Problem 1
def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    k = float(input("Enter k: "))
    x = float(input("Enter the starting value of x: "))
    n = int(input("Enter the number of iterations: "))

    if x < 0 or x > 1:
        print("Error: x must be between 0 and 1.")
        return

    chaos(k, x, n)


if __name__ == "__main__":
    main()

#Problem 2
def main():
    side1 = float(input("Enter the first side length: "))
    side2 = float(input("Enter the second side length: "))
    side3 = float(input("Enter the third side length: "))

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("The sides you entered cannot form a triangle.")
    elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("The sides you entered cannot form a triangle.")
    elif side1 == side2 and side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")


if __name__ == "__main__":
    main()
#problem 3

def classifyAge(age):
    if age < 0:
        return "Impossible"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age < 65:
        return "Adult"
    elif age <= 100:
        return "Senior"
    else:
        return "Senior. Congratulations on appearing on the Smucker's jar!"


def main():
    age = int(input("Enter your age: "))
    print(classifyAge(age))


if __name__ == "__main__":
    main()


#Problem 4

from graphics import *

def buttonClicked(point, button):
    x = point.getX()
    y = point.getY()

    return (button.getP1().getX() <= x <= button.getP2().getX()
            and button.getP1().getY() <= y <= button.getP2().getY())


def main():
    win = GraphWin("Button Click Test", 400, 300)

    button = Rectangle(Point(125, 100), Point(275, 160))
    button.draw(win)

    label = Text(Point(200, 130), "Click Here 10 times")
    label.draw(win)

    result = Text(Point(200, 220), "")
    result.draw(win)

    for i in range(10):
        point = win.getMouse()

        if buttonClicked(point, button):
            result.setText("Button was clicked!")
        else:
            result.setText("Button was not clicked.")

    win.close()


if __name__ == "__main__":
    main()

#Problem 5

def isPrime(n):
    found = False

    for i in range(2, n):
        if n % i == 0:
            found = True

    return not found and n > 1


def main():
    n = int(input("Enter an integer: "))

    if isPrime(n):
        print(n, "is prime.")
    else:
        print(n, "is not prime.")


if __name__ == "__main__":
    main()
