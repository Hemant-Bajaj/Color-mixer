import tkinter as tk
from tkinter import font
import json
import webcolors

# Load the JSON file with color data
with open("D:\code\music\Color mixer\Colordata.json", "r", encoding="utf-8") as file:
    qa_pairs = json.load(file)

# Function to update button color based on RGB values
def update_color(event=None):
    color_name = ""
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    color = f'#{r:02x}{g:02x}{b:02x}'
    comp_color = get_complementary_color(r, g, b)
    for pair in qa_pairs:
        question = pair['name']
        answer = pair['hex']
        if color == answer:
            color_name = question
    if color_name == "":
        color_name = "color"
    
    color_button.config(bg=color, fg=comp_color, text=color_name)

# Function to calculate the complementary color
def get_complementary_color(r, g, b):
    comp_r = 255 - r
    comp_g = 255 - g
    comp_b = 255 - b
    return f'#{comp_r:02x}{comp_g:02x}{comp_b:02x}'

# Create the main window
root = tk.Tk()
root.title("RGB Color Slider")

# Red slider
red_slider = tk.Scale(root, from_=0, to=255, width=40, length=450, orient=tk.HORIZONTAL, label="Red")
red_slider.pack(padx=10, pady=5)

# Green slider
green_slider = tk.Scale(root, from_=0, to=255, width=40, length=450, orient=tk.HORIZONTAL, label="Green")
green_slider.pack(padx=10, pady=5)

# Blue slider
blue_slider = tk.Scale(root, from_=0, to=255, width=40, length=450, orient=tk.HORIZONTAL, label="Blue")
blue_slider.pack(padx=10, pady=5)

# Create a button that will have its background color updated
color_button = tk.Button(root, text="Update Color", width=30, height=5)
color_button.pack(pady=20)
color_button.bind('<Button-1>', update_color)  # Bind the button click event to update_color

# Increase the font size of the button text
font_style = font.Font(family='Helvetica', size=14, weight='bold')
color_button.config(font=font_style)

# Basic color palette
basic_colors = {
    'Red': '#FF0000',
    'Green': '#00FF00',
    'Blue': '#0000FF',
    'Yellow': '#FFFF00',
    'Cyan': '#00FFFF',
    'Magenta': '#FF00FF',
    'Black': '#000000',
    'White': '#FFFFFF',
    'Gray': '#808080',
    'Orange': '#FFA500'
}

# Frame for basic color palette
palette_frame = tk.Frame(root)
palette_frame.pack(pady=10)
row_num = 0
for color_name, hex_code in basic_colors.items():
    # Convert hexadecimal code to RGB tuple
    rgb_values = webcolors.hex_to_rgb(hex_code)
    # Create label with color name and RGB values in separate labels row-wise
    color_name_label = tk.Label(palette_frame, text=f'Color Name: {color_name}', width=20, anchor='w')
    color_name_label.grid(row=row_num, column=0, padx=5, pady=5)
    
    rgb_label = tk.Label(palette_frame, text=f'RGB: {rgb_values}', width=40, anchor='w')
    rgb_label.grid(row=row_num, column=1, padx=5, pady=5)
    
    color_label = tk.Label(palette_frame, bg=hex_code, width=40, height=2)
    color_label.grid(row=row_num, column=2, padx=5, pady=5)
    
    # Increment row number for the next color
    row_num += 1

    

# Start the Tkinter event loop
root.mainloop()
