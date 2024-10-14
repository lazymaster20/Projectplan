import tkinter as tk

class hospital():
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital management")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, bg=self.clr(220,180,190), text="Project management System", bd=3, relief="groove",font=("Arial",50,"bold"))
        title.pack(side="top", fill="x")

    def clr(self, r,g,b):
            return f"#{r:02x}{g:02x}{b:02x}"

root=tk.Tk()
obj = hospital(root)
root.mainloop()