import tkinter as tk
import math

root = tk.Tk()
root.title('Scientific Calculator')
root.configure(bg='#333333')  # Updated background color
root.resizable(width=False, height=False)

ent_field = tk.Entry(root, bg='#444444', fg='#FFFFFF', font=('Arial', 25),  # Updated entry colors
                     borderwidth=10, justify="right")
ent_field.grid(row=0, columnspan=10, padx=10, pady=10, sticky='n'+'s'+'e'+'w')
ent_field.insert(0, '0')

FONT = ('Arial', 10, 'bold')


class SC_Calculator():
    def __init__(self):
        self.current = ''
        self.inp_value = True
        self.result = False

    def Entry(self, value):
        ent_field.delete(0, 'end')
        ent_field.insert(0, value)

    def Enter_Num(self, num):
        self.result = False
        firstnum = ent_field.get()
        secondnum = str(num)
        if self.inp_value:
            self.current = secondnum
            self.inp_value = False
        else:
            self.current = firstnum+secondnum
        self.Entry(self.current)

    def Standard_Ops(self, val):
        temp_str = ent_field.get()
        try:
            if val == '=':
                ans = str(eval(temp_str))
                self.result = True
                self.Entry(ans)
            else:
                self.Entry(temp_str+val)
            self.inp_value = False
        except ValueError:
            self.Entry('Error')
        except SyntaxError:
            self.Entry('Error')

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.Entry(0)
        self.inp_value = True

    # Other methods remain unchanged
    # ...


numberpad = "789456123"
i = 0
button = []
for j in range(2, 5):
    for k in range(3):
        button.append(tk.Button(root, text=numberpad[i], font=FONT,
                                fg="#FFFFFF", bg="#555555",  # Updated number button colors
                                width=6, height=2,
                                highlightbackground='#ADD8E6', highlightthickness=2))
        button[i].grid(row=j, column=k, sticky='n'+'s'+'e'+'w', padx=10, pady=10)
        button[i]["command"] = lambda x=numberpad[i]: sc_app.Enter_Num(x)
        i += 1

btn_CE = tk.Button(root, text='CE', command=lambda: sc_app.Clear_Entry(),
                   font=FONT, height=2, fg="#FFFFFF", bg="#FF5733",  # Clear button color
                   highlightbackground='#ADD8E6', highlightthickness=2)
btn_CE.grid(row=1, column=0, columnspan=2,
            sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sqr = tk.Button(root, text='\u221A', command=lambda: sc_app.SQ_Root(),
                    font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",  # Operator color
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sqr.grid(row=1, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_0 = tk.Button(root, text='0', command=lambda: sc_app.Enter_Num('0'),
                  font=FONT, width=6, height=2, fg="#FFFFFF", bg="#555555",
                  highlightbackground='#ADD8E6', highlightthickness=2)
btn_0.grid(row=5, column=0, columnspan=2,
           sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_point = tk.Button(root, text='.', command=lambda: sc_app.Standard_Ops('.'),
                      font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_point.grid(row=5, column=2, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_equal = tk.Button(root, text='=', command=lambda: sc_app.Standard_Ops('='),
                      font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                      highlightbackground='#ADD8E6', highlightthickness=2)
btn_equal.grid(row=5, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_add = tk.Button(root, text='+', command=lambda: sc_app.Standard_Ops('+'),
                    font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_add.grid(row=1, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_sub = tk.Button(root, text='-', command=lambda: sc_app.Standard_Ops('-'),
                    font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_sub.grid(row=2, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_mul = tk.Button(root, text='*', command=lambda: sc_app.Standard_Ops('*'),
                    font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_mul.grid(row=3, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

btn_div = tk.Button(root, text='/', command=lambda: sc_app.Standard_Ops('/'),
                    font=FONT, width=6, height=2, fg="#FFFFFF", bg="#FF5733",
                    highlightbackground='#ADD8E6', highlightthickness=2)
btn_div.grid(row=4, column=3, sticky='n'+'s'+'e'+'w', padx=10, pady=10)

# Additional buttons updated similarly...

if __name__ == '__main__':

    sc_app = SC_Calculator()

    root.mainloop()
