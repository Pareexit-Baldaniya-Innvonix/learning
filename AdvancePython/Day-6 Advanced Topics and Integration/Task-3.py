# Task 3: Event
import tkinter as tk


class App:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Event Handler App")

        self.label = tk.Label(
            root, text="Press any key or click me!", font=("Arial", 16)
        )
        self.label.pack(pady=100, padx=100)

        self.label.bind("<Button-1>", self.on_click)

        self.root.bind("<Key>", self.on_key)

    def on_click(self, event: tk.Event) -> None:
        print(f"Mouse clicked at: x = {event.x}, y = {event.y}")
        self.label.config(text="Mouse Clicked!", fg="blue")

    def on_key(self, event: tk.Event) -> None:
        print(f"Key pressed: {event.char}")
        self.label.config(text=f"You pressed: {event.char}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
