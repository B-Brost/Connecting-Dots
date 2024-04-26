"""
Connecting_Dots.py
Brianna Brost
9/21/2022
This script allows the user to create a pattern of dots on a canvas by clicking the mouse. 
The dots are then connected to each other to form a polygon. The user can also load previously saved patterns from a file.
"""

import dudraw
from random import random
from random import randint

# This function saves the coordinates of the points to a file.
def save_to_file(file_name: str, a_list : list[tuple])->None:
    with open(file_name, "w") as a_file:
        for point in a_list:
            a_file.write(f"{point[0]},{point[1]}\n")

# This function reads the coordinates of the points from a file and adds them to the points list.
def read_from_file(file_name: str, points):
    try:
        with open(file_name, "r") as a_file:
            for line in a_file:
                coordinates = line.strip().split(",")
                point = (float(coordinates[0]), float(coordinates[1]))
                points.append(point)
    except FileNotFoundError:
        print("File doesn't exist")

# Set the size of the drawing canvas
dudraw.set_canvas_size(500, 500)

points = []

quit = False
while not quit:
    # Draw a black circle in the middle of the canvas
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.circle(0.5, 0.5, 0.3)
    
    # Draw all points in red
    for i in range(len(points)):
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_circle(points[i][0], points[i][1], 0.01)

    # Connect every point to every other point with a black line
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dudraw.set_pen_color(dudraw.BLACK)
            dudraw.line(points[i][0], points[i][1], points[j][0], points[j][1])    

    # If the mouse is pressed, add the current mouse position to the points list
    if dudraw.mouse_is_pressed():
        points.append((dudraw.mouse_x(), dudraw.mouse_y()))
    
    # If a key is typed, check if it's 'q' or 'l'
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
        if key == 'q':
            quit = True

        # If 'l' is pressed, load the points from the file
        if key == 'l':
            read_from_file("data_files/picture.txt", points)

    # Update the canvas
    dudraw.show(60)

# Save the points to the file
save_to_file("data_files/picture.txt", points)
