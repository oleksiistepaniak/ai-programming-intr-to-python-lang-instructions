print("Hello. Please, enter specific coordinates to determine whether they belong to the shaded area")

valid_x_coords = [-1, -2, 1, 2]
valid_y_coords = [-1, -2]

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

firstCoordinate = input("Enter x coordinate: ")
secondCoordinate = input("Enter y coordinate: ")

if is_number(firstCoordinate) and is_number(secondCoordinate):
    x = int(firstCoordinate)
    y = int(secondCoordinate)

    if x in valid_x_coords and y in valid_y_coords:
        print(f"The coordinates ({x}, {y}) are valid and belong to the shaded area.")
    else:
        print(f"The coordinates ({x}, {y}) do NOT belong to the shaded area.")
else:
    print("Error: You must enter valid numeric coordinates.")
