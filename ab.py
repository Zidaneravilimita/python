import tkinter as tk
dev = tk.Tk()

dev.geometry("700x400")

dev.title("Salut")

dev.config(background='yellow')

soratra=tk.Label(dev, 
                  text="Bienvenue",
                fg='yellow',
                bg="blue"

                 )
soratra.pack()






dev.mainloop()