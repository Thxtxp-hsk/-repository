import tkinter as tk
from tkinter import messagebox

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Popup Example")

# สร้างฟังก์ชันสำหรับปุ่มกด
def show_me():
    messagebox.showinfo("FOR U", "I LOVE U SO SO SO SO MUCH")
    messagebox.showinfo("FOR U", "Thank u a lot for loveing me")
    
# สร้างปุ่มและตั้งค่าให้เรียกฟังก์ชัน show_popup เมื่อกดปุ่ม
button1 = tk.Button(root, text="Click IT!!", command=show_me)
button1.pack(pady=100)

# รันหน้าต่างหลัก
root.mainloop()
