pi=3.14159

def calculate_area_circle(radius):
    return pi * radius * 2

r=int(input("Enter radius: "))
area=calculate_area_circle(r)
print(area)