import tkinter as tk

# Tip Calculator
def createRootTip():
    root = tk.Tk()
    root.title("Tip Calculator")
    root.configure(bg="black")
    return root

# create and layout widgets for tip calculator (labels in upper case, orange/black theme)
def createWidgetsTip(root):
    billLabel = tk.Label(root, text="BILL AMOUNT:", bg="black", fg="orange")
    billLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    billEntry = tk.Entry(root, width=20, bg="orange", fg="black", insertbackground="black")
    billEntry.grid(row=0, column=1, padx=5, pady=5)

    tipLabel = tk.Label(root, text="TIP PERCENTAGE:", bg="black", fg="orange")
    tipLabel.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    tipEntry = tk.Entry(root, width=20, bg="orange", fg="black", insertbackground="black")
    tipEntry.grid(row=1, column=1, padx=5, pady=5)

    resultLabel = tk.Label(root, text="", justify="left", bg="black", fg="orange")
    resultLabel.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    calcButton = tk.Button(root, text="CALCULATE", bg="orange", fg="black", activebackground="darkorange")
    calcButton.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    clearButton = tk.Button(root, text="CLEAR", bg="orange", fg="black", activebackground="darkorange")
    clearButton.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

    return billEntry, tipEntry, resultLabel, calcButton, clearButton

# calculate tip and total, show error in red for invalid input
def calculateTip(billEntry, tipEntry, resultLabel):
    billText = billEntry.get().strip()
    tipText = tipEntry.get().strip()
    try:
        if not billText or not tipText:
            raise ValueError
        bill = float(billText)
        tipPercent = float(tipText)
    except ValueError:
        resultLabel.config(text="ERROR: ENTER NUMERIC VALUES FOR BILL AND TIP PERCENT", fg="red")
        return

    tipAmount = bill * (tipPercent / 100)
    total = bill + tipAmount

    # display tip percent without unnecessary .0
    if float(tipPercent).is_integer():
        tip_display = f"{int(tipPercent)}"
    else:
        tip_display = f"{tipPercent}"

    message = (
        f"BILL AMOUNT: ${bill:.2f}\n"
        f"TIP PERCENT: {tip_display}%\n"
        f"TIP AMOUNT: ${tipAmount:.2f}\n"
        f"TOTAL WITH TIP: ${total:.2f}"
    )
    resultLabel.config(text=message, fg="orange")

# clear entries and result
def clearTip(billEntry, tipEntry, resultLabel):
    billEntry.delete(0, tk.END)
    tipEntry.delete(0, tk.END)
    resultLabel.config(text="", fg="orange")

# tip calculator main builder (call tipMain() to run)
def tipMain():
    root = createRootTip()
    billEntry, tipEntry, resultLabel, calcButton, clearButton = createWidgetsTip(root)
    calcButton.config(command=lambda: calculateTip(billEntry, tipEntry, resultLabel))
    clearButton.config(command=lambda: clearTip(billEntry, tipEntry, resultLabel))
    root.mainloop()

if __name__ == "__main__":
    tipMain()