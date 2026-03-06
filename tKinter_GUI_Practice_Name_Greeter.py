import tkinter as tk

# create and configure the main window
def createRoot():
    root = tk.Tk()
    root.title("Name Greeter")
    root.configure(bg="black")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.resizable(False, False)
    return root

# create and layout widgets, return references
def createWidgets(root):
    # prompt label for name entry
    promptLabel = tk.Label(root, text="Enter your name:", bg="black", fg="orange")
    promptLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # entry for the user's name
    nameEntry = tk.Entry(root, width=30, bg="black", fg="orange", insertbackground="orange")
    nameEntry.grid(row=0, column=1, padx=5, pady=5)

    # label to show the greeting result
    resultLabel = tk.Label(root, text="", bg="black", fg="orange")
    resultLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # greet button 
    greetButton = tk.Button(root, text="Greet Me", bg="orange", fg="black", activebackground="#ffb347")
    greetButton.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    # clear button
    clearButton = tk.Button(root, text="Clear", bg="orange", fg="black", activebackground="#ffb347")
    clearButton.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

    return nameEntry, resultLabel, greetButton, clearButton

# build greeting text based on entry content (no formatter)
def greetName(nameEntry, resultLabel):
    raw = nameEntry.get().strip()
    if raw:
        # keep raw (trimmed) value in entry, no formatting applied
        nameEntry.delete(0, tk.END)
        nameEntry.insert(0, raw)
        resultLabel.config(text=f"Hello, {raw}! Welcome to DS3850.")
    else:
        resultLabel.config(text="")  # no greeting for empty name

# clear entry and result label
def clearName(nameEntry, resultLabel):
    nameEntry.delete(0, tk.END)
    resultLabel.config(text="")

# main application setup and loop
def main():
    root = createRoot()
    nameEntry, resultLabel, greetButton, clearButton = createWidgets(root)

    # assign button commands using functions
    greetButton.config(command=lambda: greetName(nameEntry, resultLabel))
    clearButton.config(command=lambda: clearName(nameEntry, resultLabel))

    root.mainloop()

if __name__ == "__main__":
    main()