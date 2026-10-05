import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        quantity = int(quantity_entry.get())

        if price < 0:
            raise ValueError("Original price cannot be negative.")
        if not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        subtotal = price * quantity
        discount_amount = subtotal * (discount / 100)
        final_price = subtotal - discount_amount

        result_label.config(
            text=f"Final Price: Rp {final_price:,.2f}",
            fg="#2196F3"
        )

    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("500x520")
root.resizable(False, False)
root.configure(bg="#F5F7FA")

tk.Label(
    root, text="Discount Calculator",
    font=("Arial", 24, "bold"),
    bg="#F5F7FA", fg="#222222"
).pack(pady=(35, 30))

tk.Label(
    root, text="Original Price (Rp):",
    font=("Arial", 14), bg="#F5F7FA", fg="#333333"
).pack(pady=(0, 8))

price_entry = tk.Entry(
    root, font=("Arial", 14), justify="center", width=28
)
price_entry.pack(pady=(0, 20))

tk.Label(
    root, text="Discount (%):",
    font=("Arial", 14), bg="#F5F7FA", fg="#333333"
).pack(pady=(0, 8))

discount_entry = tk.Entry(
    root, font=("Arial", 14), justify="center", width=28
)
discount_entry.pack(pady=(0, 20))

tk.Label(
    root, text="Quantity:",
    font=("Arial", 14), bg="#F5F7FA", fg="#333333"
).pack(pady=(0, 8))

quantity_entry = tk.Entry(
    root, font=("Arial", 14), justify="center", width=28
)
quantity_entry.pack(pady=(0, 25))

tk.Button(
    root, text="Calculate",
    command=calculate_discount,
    font=("Arial", 14, "bold"),
    bg="#4CAF50", fg="white",
    activebackground="#45A049",
    activeforeground="white",
    width=15, cursor="hand2"
).pack(pady=5)

result_label = tk.Label(
    root, text="Final Price: Rp 0.00",
    font=("Arial", 17, "bold"),
    bg="#F5F7FA", fg="#2196F3"
)
result_label.pack(pady=(30, 10))

tk.Label(
    root,
    text="Example: Rp 20,000 x 2 items with 25% discount = Rp 30,000",
    font=("Arial", 9), bg="#F5F7FA", fg="#777777"
).pack(pady=10)

root.bind("<Return>", lambda event: calculate_discount())
price_entry.focus()

root.mainloop()
