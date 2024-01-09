import tkinter as tk
from tkinter import scrolledtext

def show_error_message(error_message):
    error_box.delete(1.0, tk.END)  # پاک کردن محتوای قبلی
    error_box.insert(tk.END, error_message)  # نمایش خطاها در باکس

def show_user_input(user_input):
    user_input_box.delete(1.0, tk.END)  # پاک کردن محتوای قبلی
    user_input_box.insert(tk.END, f"ورودی کاربر: {user_input}")  # نمایش ورودی کاربر در باکس

def get_name():
    name = nameInput.get()
    if not name:
        show_error_message("لطفاً نام خود را وارد کنید.")
    else:
        show_user_input(name)
        show_error_message("")  # پاک کردن خطاها

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ترکیب دو کد Tkinter")
root.geometry('400x500')
root.resizable(width=False, height=False)

# ایجاد باکس متن برای نمایش خطاها
error_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
error_box.place(x=10, y=10, padx=10, pady=10)

# ایجاد دکمه برای شبیه‌سازی یک خطا
simulate_error_button = tk.Button(root, text="شبیه‌سازی خطا", command=lambda: show_error_message("خطای شبیه‌سازی شده"))
simulate_error_button.place(x=10, y=300)

# ایجاد Label و Entry برای وارد کردن نام
nameLabel = tk.Label(root, text="لطفاً نام خود را وارد کنید:")
nameLabel.place(x=8, y=340)

nameInput = tk.Entry(root)
nameInput.place(x=10, y=360)

# ایجاد دکمه برای دریافت نام و نمایش خطا
btn = tk.Button(root, text="دریافت نام", command=get_name)
btn.place(x=10, y=390)

# ایجاد باکس متن برای نمایش ورودی کاربر
user_input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=5, font=("Arial", 12))
user_input_box.place(x=10, y=430, padx=10, pady=10)

# اجرای پنجره اصلی
root.mainloop()
