import tkinter as tk

class Submit():
    
    def __init__(self,root,sh,tv):

        brand_entry = tk.Entry(root, font=('calibre',10,'normal'))
        body_entry = tk.Entry(root, font=('calibre',10,'normal'))
        fuel_entry = tk.Entry(root, font=('calibre',10,'normal'))
        
        sub_btn=tk.Button(root,text = 'Submit', command = lambda: Submit.submit(self,sh,brand_entry,body_entry, fuel_entry,tv))
        sub_btn.grid(row=3,column=1)
            
        brand_label = tk.Label(root, text = 'Brand:', font=('calibre',10, 'bold'))
        body_label = tk.Label(root, text = 'Body:', font=('calibre',10, 'bold'))
        fuel_label = tk.Label(root, text = 'Fuel type:', font=('calibre',10, 'bold'))
        
        brand_label.grid(row=0,column=0)
        brand_entry.grid(row=0,column=1)
        body_label.grid(row=1,column=0)
        body_entry.grid(row=1,column=1)
        fuel_label.grid(row=2,column=0)
        fuel_entry.grid(row=2,column=1)
        
    def submit(self,sh,brand_entry,body_entry,fuel_entry,tv):
        for auto in tv.get_children():                                   #petla wchodzaca do tabeli tv(bierze kazdy rekord po kolei)
            tv.delete(auto)                                              #usuwanie rekordow z tabeli
            
        brand = brand_entry.get()
        body = body_entry.get()
        fuel = fuel_entry.get()
        
        brand_entry.delete(0, tk.END)
        body_entry.delete(0, tk.END)
        fuel_entry.delete(0, tk.END)
        
        for i in range (2,1638):
            if brand == sh.cell(row=i,column =1).value:
                if body == sh.cell(row=i,column =4).value:
                    if fuel == sh.cell(row=i,column =8).value:
                        tv.insert("",0,values=(sh.cell(row=i,column =1).value,sh.cell(row=i,column =2).value,sh.cell(row=i,column =3).value,sh.cell(row=i,column =4).value,sh.cell(row=i,column =7).value,sh.cell(row=i,column =8).value,sh.cell(row=i,column =9).value,sh.cell(row=i,column =10).value))
                            
        