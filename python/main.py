import tkinter as tk
import calendar
from tkinter import filedialog
from PIL import Image, ImageTk

# Create a new Tkinter window
window = tk.Tk()

window.title("Today")

# Set the window size to 800x800 and center it on the screen
window_width = 800
window_height = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Set the initial year and month
year = 2024
month = 2

def clear_window():
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

def display_day(year, month, day):
    clear_window()

    # Display the selected day
    label = tk.Label(window, text=f"Date: {year}-{month}-{day}")
    label.grid(row=0, column=0, columnspan=3, pady=10)

    # Add a "Go Back" button
    go_back_button = tk.Button(window, text="Go Back", command=lambda: display_calendar(year, month))
    go_back_button.grid(row=1, column=0, columnspan=3, pady=10)

    # Section for Facebook
    fb_label = tk.Label(window, text="Facebook Section")
    fb_label.grid(row=2, column=0, pady=10)

    fb_input = tk.Text(window, height=4, width=30)
    fb_input.grid(row=3, column=0, pady=10)

    fb_photo_label = tk.Label(window)
    fb_photo_label.grid(row=3, column=1)

    fb_upload_button = tk.Button(window, text="Upload Photos", command=lambda: upload_photos(fb_photo_label))
    fb_upload_button.grid(row=4, column=0, pady=10)

    # Add a "Save" button
    save_button = tk.Button(window, text="Save", command=save_data)
    save_button.grid(row=5, column=0, columnspan=3, pady=10)

def upload_photos(photo_label):
    # Open a file dialog to select the photo
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])

    # Open the photo and resize it
    image = Image.open(file_path)
    image.thumbnail((100, 100), Image.LANCZOS)  # Use thumbnail instead of resize to keep the aspect ratio

    # Convert the photo to a Tkinter-compatible photo image
    photo_image = ImageTk.PhotoImage(image)

    # Set the image of the photo label
    photo_label.config(image=photo_image)
    photo_label.image = photo_image  # Keep a reference to the image to prevent it from being garbage collected

def save_data():
    # Save the data
    pass

def display_calendar(year, month):
    clear_window()

    # Display the current month and year
    month_year_label = tk.Label(window, text=f"{calendar.month_name[month]} {year}")
    month_year_label.pack()

    # Add navigation buttons
    prev_button = tk.Button(window, text="Previous Month", command=lambda: change_month(-1))
    prev_button.pack(side=tk.LEFT)

    next_button = tk.Button(window, text="Next Month", command=lambda: change_month(1))
    next_button.pack(side=tk.RIGHT)

    # Add a "Go Back" button
    go_back_button = tk.Button(window, text="Go Back", command=initial_window)
    go_back_button.pack()

    # Create a new frame for the calendar
    calendar_frame = tk.Frame(window)
    calendar_frame.pack()

    # Display the names of each day above the calendar
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(days):
        label = tk.Label(calendar_frame, text=day, width=5, height=2, relief="flat")
        label.grid(row=0, column=i)

    # Get the calendar for the specified year and month
    cal = calendar.monthcalendar(year, month)

    # Create a grid of buttons for each day in the calendar
    for i, week in enumerate(cal, start=1):  # start enumeration from 1 to account for day names
        for j, day in enumerate(week):
            # Create a button for each day
            if day == 0:
                label = tk.Label(calendar_frame, text=" ", width=5, height=2, relief="flat")
                label.grid(row=i, column=j)
            else:
                button = tk.Button(calendar_frame, text=str(day), width=5, height=2, relief="raised", bd=2, command=lambda day=day: display_day(year, month, day))
                button.grid(row=i, column=j)

def initial_window():
    clear_window()
    calendar_button = tk.Button(window, text="Calendar", command=lambda: display_calendar(year, month))
    calendar_button.pack()

def change_month(delta):
    global month, year
    month += delta
    if month > 12:
        month = 1
        year += 1
    elif month < 1:
        month = 12
        year -= 1
    display_calendar(year, month)

# Create a "Calendar" button
calendar_button = tk.Button(window, text="Calendar", command=lambda: display_calendar(year, month))
calendar_button.pack()

# Run the Tkinter event loop
window.mainloop()