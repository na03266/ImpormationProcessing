import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def close_file():
    text.delete(1.0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("Text File Viewer")

# Load the background image
bg_image = tk.PhotoImage(file="C:/Users/user/Desktop/wind.gif")

# Create a label to hold the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a "File" menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Add menu items for "Open" and "Close"
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Close", command=close_file)

# Create a text widget to display file content
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))  # Change the font here
text.pack(expand=True, fill='both')

# Run the main event loop
root.mainloop()
