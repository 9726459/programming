import tkinter as tk
import pygame

class CarRentalSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Car Rental System")
        self.master.geometry("400x300")

        # Initialize pygame for sound
        pygame.init()

        # Create a label for the start screen
        self.start_label = tk.Label(self.master, text="Welcome to Car Rental System", font=("Helvetica", 18))
        self.start_label.pack(pady=20)

        # Create a button to transition to the main application screen
        self.start_button = tk.Button(self.master, text="Start", command=self.open_app_screen)
        self.start_button.pack(pady=10)

        # Bind mouse click event to the start button
        self.start_button.bind("<Button-1>", lambda event: self.open_app_screen())

        # Bind keypress event to the start screen
        self.master.bind("<Return>", lambda event: self.open_app_screen())

    def open_app_screen(self):
        # Destroy start screen elements
        self.start_label.destroy()
        self.start_button.destroy()

        # Create and display elements for the main application screen
        self.app_label = tk.Label(self.master, text="Car Rental Application", font=("Helvetica", 18))
        self.app_label.pack(pady=20)

        # Create a canvas for graphics
        self.canvas = tk.Canvas(self.master, width=400, height=200)
        self.canvas.pack()

        # Draw a rectangle on the canvas
        self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")

        # Load and play a sound effect
        sound = pygame.mixer.Sound("sound.wav")
        sound.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalSystemApp(root)
    root.mainloop()