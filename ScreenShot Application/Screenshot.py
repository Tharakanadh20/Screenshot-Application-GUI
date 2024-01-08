# For this project we need to install PyAutoGUI Library on Terminal.
# import the PyAutoGUI Package
from unicodedata import name
import pyautogui
import time
import tkinter as tk
import tkinter as ttk


def screenshot():
    time.sleep(3)
    name = time.time()
    name = 'F:\Projects\ScreenShot Application\Images\{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()


# root = tk.Tk()
# frame = tk.Frame(root)
# frame.pack()

# button = tk.Button(frame, text='Take a Screenshot', command=screenshot)
# button.pack(side=tk.LEFT)

# close = tk.Button(frame, text='Quit', command=quit)
# close.pack(side=tk.LEFT)

# root.mainloop()

root = tk.Tk()
root.title("Screenshot Application")

frame = tk.Frame(root, padx=20, pady=20)
frame.grid(row=0, column=0, padx=10, pady=10)

label = tk.Label(frame, text="Screenshot Application", font=('Helvetica', 12))
label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

button = tk.Button(frame, text='Take a Screenshot',
                   command=screenshot, bg="#007BFF", fg="white", padx=10, pady=5)
button.grid(row=1, column=0, pady=(0, 10))

close = tk.Button(frame, text='Quit', command=root.quit,
                  bg="#007BFF", fg="white", padx=10, pady=5)
close.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))

root.mainloop()
