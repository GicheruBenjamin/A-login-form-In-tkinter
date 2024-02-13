import tkinter as tk

# Main application window
app = tk.Tk()

# The app title
app.title("Login Form")

# It is a login form
heading = tk.Label(app, text='LOGIN', font=('Helvetica', 16, 'bold'))

# Labels for name and password
name_label = tk.Label(app, text="Username:")
password_label = tk.Label(app, text="Password:")

# Entry widgets for name and password
name_entry = tk.Entry(app)
password_entry = tk.Entry(app, show='*')  # Show '*' for password input

# Login button
login_btn = tk.Button(app, text="Login", command=lambda: login_action())

# Login action to show name and password in the terminal
def login_action():
    username = name_entry.get()
    password = password_entry.get()

    # Add your login logic here (for demonstration, printing the values)
    print(f"Username: {username}, Password: {password}")

# Place widgets in the window using grid
heading.grid(row=0, column=1, pady=10)
name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
name_entry.grid(row=1, column=1, padx=10, pady=5)
password_entry.grid(row=2, column=1, padx=10, pady=5)
login_btn.grid(row=3, column=1, pady=10)

# Main event loop
app.mainloop()
