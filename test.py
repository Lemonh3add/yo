import tkinter as tk

root = tk.Tk()
label = tk.Label(root)
listbox = tk.Listbox(root)
label.pack(side="bottom", fill="x")
listbox.pack(side="top", fill="both", expand=True)

listbox.insert("end", "one", "two", "three", "four", "five")

def callback(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print("yo")
    else:
        print("sup")

listbox.bind("<<ListboxSelect>>", callback)

root.mainloop()

sup = ["hi", "bye", "hello"]
sup.pop()

print(sup)