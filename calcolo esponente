from tkinter import *
def calcola():
    base = float(e1.get())
    esponente = e2.get()
    if '/' in esponente:
        def cerca():
            i = 0
            while i < len(esponente):
                if esponente[i] == '/':
                    return i
                i = i+1
        indice = cerca()
        r = esponente[indice+1:]
        esponente = 1/int(r)
        risultato = base ** esponente
        l3.config(text = risultato)
    else:
        esponente = float(e2.get())
        risultato = base ** esponente
        l3.config(text = risultato)
def pulisci():
    e1.delete(0, END)
    e2.delete(0, END)
    l3.config(text = '')
    e1.focus_set()
r = Tk()
r.title('POTENZA')
zona_alta = Frame(r)
zona_alta.pack()
l1 = Label(zona_alta, text = 'base')
l1.grid(column = 0, row = 0, sticky = W, padx = 4)
e1 = Entry(zona_alta, width = 15, justify = RIGHT)
e1.grid(column = 1, row = 0, padx = 4, pady = 4)
e1.focus_set()
l2 = Label(zona_alta, text = 'esponente')
l2.grid(column = 0, row = 1, sticky = W, padx = 4)
e2 = Entry(zona_alta, width = 15, justify = RIGHT)
e2.grid(column = 1, row = 1, padx = 4, pady = 4)
l3 = Label(zona_alta)
l3.grid(row = 2, columnspan = 2, pady = 4)
zona_bassa = Frame(r)
zona_bassa.pack()
b1 = Button(zona_bassa, text = 'CALCOLA', command = calcola)
b1.grid(column = 0, row = 0, padx = 4, pady = 6)
b2 = Button(zona_bassa, text = 'PULISCI', command = pulisci)
b2.grid(column = 1, row = 0, padx = 4)
b3 = Button(zona_bassa, text = 'ESCI', width = 7, command = quit)
b3.grid(column = 2, row = 0, padx = 4)
r.mainloop()
