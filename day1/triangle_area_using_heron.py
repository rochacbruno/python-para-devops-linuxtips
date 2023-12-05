# triangle_area_using_heron.py
import sys

def heron(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def triangle_area_using_heron():
    sides = [float(x) for x in sys.stdin.readline().split()]

    if len(sides) != 3:
        print("Error: Please provide exactly three sides of the triangle.")
        return

    area = heron(*sides)
    print(f"Area of the triangle: {area:.2f}")

if __name__ == "__main__":
    triangle_area_using_heron()
