from tkinter import *
import tkinter.filedialog as fd
r = Tk()
r.title('Senza Titolo')
t = Text(r, wrap = WORD)
t.pack(padx = 5, pady = 5)
def apri():
    path = fd.askopenfilename(title = 'Scegli un file')
    if len(path) > 0:
        t.delete('1.0', 'end')
        with open(path, 'U') as f:
            t.insert('1.0', f.read())
        r.title(path)
def salva_come():
    path = fd.asksaveasfilename(title = 'Dove Salvare')
    if len(path) > 0:
        with open(path, 'w') as f:
            f.write(t.get('1.0', 'end'))
        r.title(path)
mb = Menu(r)
r.config(menu=mb)
fm = Menu(mb)
fm.add_command(label = 'Apri...', command = apri)
fm.add_command(label = 'Salva come...', command = salva_come)
fm.add_separator()
fm.add_command(label = 'Esci', command = quit)
mb.add_cascade(label = 'File', menu = fm)
r.mainloop()
