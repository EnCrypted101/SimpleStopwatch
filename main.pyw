import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("SimpleStopwatch")
        self.root.geometry("325x175")
        self.root.resizable(False, False)  # Set window to non-resizable

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:000", font=("Helvetica", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch, height=2, width=6)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_stopwatch, height=2, width=6)
        self.stop_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stopwatch, height=2, width=6)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

        self.update_time()

    def update_time(self):
        if self.is_running:
            self.elapsed_time = int((time.time() - self.start_time) * 1000)
        minutes, seconds = divmod(self.elapsed_time // 1000, 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = self.elapsed_time % 1000
        time_string = "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, milliseconds)
        self.label.config(text=time_string)
        self.root.after(1, self.update_time)

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - (self.elapsed_time / 1000)

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = time.time()
        self.elapsed_time = 0
        self.label.config(text="00:00:000")
        self.start_button.config(state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
