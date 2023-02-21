import openpyxl
from tkinter import ttk
import tkinter as tk
import Class

excelFile = openpyxl.load_workbook('123.xlsx') #Loading a excel file to python
sh = excelFile.active 

root = tk.Tk()

frm = tk.Frame(root)
frm.pack(fill="both")
frm.place(x = 809, y = 300, anchor = 'center')

tv = ttk.Treeview(frm, columns =(1,2,3,4,5,6,7,8), show = "headings", height = "15")
tv.pack(side = "left")


tv.heading(1, text = "Marka")
tv.heading(2, text = "Model")
tv.heading(3, text = "Generacja")
tv.heading(4, text = "Typ nadwozia")
tv.heading(5, text = "Rodzaj Silnika")
tv.heading(6, text = "Paliwo")
tv.heading(7, text = "Pojemnosc [cm^3]")
tv.heading(8, text = "Moc [KM]")

#yscrollbar
verscrlbar = ttk.Scrollbar(frm,orient ="vertical",command = tv.yview)
tv.configure(yscrollcommand = verscrlbar.set)
verscrlbar.pack(side = "right",fill="y")

Class.Submit(root,sh,tv)

root.title("Table_excel_project")
root.geometry("1600x650")
root.resizable(False,False)
root.mainloop()