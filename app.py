import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("BMI checker")      
root.geometry("500x250")    
root.resizable(0, 0)        
root.attributes('-alpha', 1 ) 
length_text = tk.StringVar()
weight_text = tk.StringVar()

lbl = tk.Label(root, text = "BMI checker", borderwidth=1, fg='white', relief="solid")
lbl.place(x = 0, y = 0, width = 500, height = 50)
lbl.configure(bg='#808000')
lbl1 = tk.Label(root, text = "Your BMI is:", borderwidth=1,  fg='white', relief="solid")
lbl1.place(x = 0, y = 200, width = 500, height = 50)
lbl1.configure(bg='#808000')
lbl2 = tk.Label(root, text = "Enter weight(KG):", borderwidth=1,  fg='white', relief="solid")
lbl2.place(x = 0, y = 125, width = 100, height = 75)
lbl2.configure(bg='#8D8B55')
lbl3 = tk.Label(root, text = "Enter length(CM):", borderwidth=1,  fg='white', relief="solid")
lbl3.place(x = 0, y = 50, width = 100, height = 75)
lbl3.configure(bg='#8D8B55')
btn = tk.Button(root, text = "Enter", bg='#8D8B55',fg='white', command = lambda : press("Knop1"))
btn.place(x = 400, y = 50, width = 100, height = 150)
Length = tk.Entry(root, textvariable = length_text, bg='#B9BE8A')
Length.place(x = 100, y = 50, width = 300, height = 75)
Weight = tk.Entry(root, textvariable = weight_text, bg='#B9BE8A')
Weight.place(x = 100, y = 125, width = 300, height = 75)

def press(Knop1):
 WeightText = Weight.get()  
 WeightText = int(WeightText)
 LengthText = Length.get() 
 LengthText = int(LengthText)

 W = WeightText
 L = LengthText / 100
 BMIvalue = int(W / (L * L))
 if BMIvalue > 25:
    Status = "Overweight"
    lbl1.configure(bg='red')
 elif BMIvalue < 18.5:
    Status = "Underweight"
    lbl1.configure(bg='blue')
 else:
    Status = "Healthy"
    lbl1.configure(bg='#808000')
 lbl1.configure(text="Your BMI is: " + str(BMIvalue) + " Which is is: " + str(Status))

root.mainloop()