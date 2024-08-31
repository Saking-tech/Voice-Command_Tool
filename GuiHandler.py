import tkinter as tk
from tkinter import messagebox

class GUIHandler:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Assistant GUI")
        self.root.geometry("400x300")

        # Example label
        self.label = tk.Label(self.root, text="Welcome to the AI Assistant!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Example buttons
        self.greet_button = tk.Button(self.root, text="Greet", command=self.greet)
        self.greet_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def greet(self):
        """
        Displays a greeting message in a messagebox.
        """
        messagebox.showinfo("Greeting", "Hello! How can I assist you today?")
        print("Displayed greeting message.")

    def quit_app(self):
        """
        Quits the application.
        """
        self.root.quit()
        print("Quitting the application.")

    def run(self):
        """
        Runs the main loop for the GUI.
        """
        self.root.mainloop()

# Example usage:
if __name__ == "__main__":
    gui_handler = GUIHandler()
    gui_handler.run()
