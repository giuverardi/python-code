from random import *
def inizializza():
    areaTentativi.delete('pallina')
    areaRisposte.delete('quadratino')
    combinazione.delete('pallina')
    messaggio.configure(text = '')
    global listaGioco
    global listaTentativo
    global tentativi
    tentativi= 0
    global x1
    x1 = 28
    global x2
    x2 = 28
    global y1
    y1 = 10
    global y2
    y2 = 12
    listaBase = ['R', 'V', 'G', 'B']
    listaGioco = [1,2,3,4]
    for i in range(4):
        p = int(random() * 4)
        listaGioco[i] = listaBase[p]
def tentativo(event):
    nomiColori = {'R':'RED', 'V':'GREEN', 'G':'YELLOW', 'B':'BLUE'}
    stringaColori = 'RVGB'
    stringaTentativo = stringaInput.get()
    verifica = ''
    if len(stringaTentativo) != 4:
        messaggio.config(text = 'DEVI INSERIRE ALMENO 4 CARATTERI')
        verifica = 'NO'
    for i in range(4):
        if stringaTentativo[i] not in stringaColori:
            verifica = 'NO'
            break
    if verifica == 'NO':
        messaggio.config(text = 'HAI INSERITO MALE QUALCOSA')
    else:
        messaggio.config(text = '')
    global listaTentativo
    listaTentativo = [1,2,3,4]
    global x1
    global y1
    global tentativi
    for i in range(4):
        listaTentativo[i] = stringaTentativo[i]
    for i in range(4):
        areaTentativi.create_oval(x1, y1, x1+15, y1+15, fill = nomiColori[listaTentativo[i]])
        x1 += 20
        areaTentativi.addtag_all('pallina')
    stringaInput.delete(0,4)
    x1 = 28
    y1 += 20
    tentativi += 1
    xx = 28
    yy = 5
if listaTentativo == listaGioco:
    messaggio.config(text = 'MOLTO BENE!\nHAI VINTO CON %d TENTATIVI\nLA COMBINAZIONE ERA:' % (tentativi))
    for i in range(4):
        combinazione.create_oval(xx, yy, xx+15, yy+15, fill = nomiColori[listaGioco[i]])
        xx += 20
        combinazione.addtag_all('pallina')
elif tentativi == 9:
    messaggio.config(text = 'HAI PERSO!\nLA COMBINAZIONE ERA:')
    for i in range(4):
        combinazione.create_oval(xx, yy, xx+15, yy+15, fill = nomiColori[listaGioco[i]])
        xx += 20
        combinazione.addtag_all('pallina')
elif verifica != 'NO':
    risposta()
def risposta():
    risposta = []
    for i in range(4):
        if listaTentativo[i] == listaGioco[i]:
            risposta.append('BLACK')
        elif listaTentativo[i] != listaGioco[i] and listaTentativo[i] in listaGioco:
            risposta.append('WHITE')
    risposta.sort()
    global x2
    global y2
    for i in range(len(risposta)):
        areaRisposte.create_rectangle(x2, y2, x2+11, y2+11, fill = risposta[i])
        x2 += 20
        areaRisposte.addtag_all('quadratino')
    x2 = 28
    y2 += 20
from tkinter import *
pianoDiGioco = Tk()
zonaApertura = Frame(pianoDiGioco)
zonaApertura.grid()
descrizione = Label(zonaApertura)
descrizione.configure(text = 'Colori in gioco: ', foreground = 'blue')
descrizione.pack()
strisciaColori = Canvas(zonaApertura, width = 150, height = 20)
strisciaColori.pack()
strisciaColori.create_text(30, 10, text = 'R', font = ('Helvetica', '18', 'bold'), fill = 'red')
strisciaColori.create_text(60, 10, text = 'V', font = ('Helvetica', '18', 'bold'), fill = 'green')
strisciaColori.create_text(90, 10, text = 'G', font = ('Helvetica', '18', 'bold'), fill = 'yellow')
strisciaColori.create_text(120, 10, text = 'B', font = ('Helvetica', '18', 'bold'), fill = 'blue')
regole = Label(zonaApertura, text = '9 tentativi a disposizione\n quadratino nero: colore giusto posto giusto\n quadratino bianco: colore giusto posto sbagliato', fg = 'blue')
regole.pack(pady = 5)
zonaGioco = Frame(pianoDiGioco)
zonaGioco.grid()
areaTentativi = Canvas(zonaGioco)
areaTentativi.configure(width = 130, height = 200)
areaTentativi.grid(row = 0, column = 0, sticky = N)
areaRisposte = Canvas(zonaGioco)
areaRisposte.configure(width = 130, height = 200)
areaRisposte.grid(row = 0, column = 1, sticky = N)
zonaInput = Frame(pianoDiGioco)
zonaInput.grid()
descrizione_1 = Label(zonaInput)
descrizione_1.configure(text = 'Scegli quattro colori indicando', foreground = 'BLUE')
descrizione_1.grid(sticky = N)
descrizione_2 = Label(zonaInput)
descrizione_2.configure(text = 'la loro iniziale maiuscola.', foreground = 'BLUE')
descrizione_2.grid(sticky = N)
descrizione_3 = Label(zonaInput)
descrizione_3.configure(text = 'Poi premi il tasto INVIO.', foreground = 'BLUE')
descrizione_3.grid(sticky = N)
stringaInput = Entry(zonaInput)
stringaInput.configure(justify = CENTER, font = ('Helvetica', '16', 'bold'))
stringaInput.focus_set()
stringaInput.bind('<Return>', tentativo)
stringaInput.grid(sticky = N)
zonaMessaggi = Frame(pianoDiGioco)
zonaMessaggi.grid()
messaggio = Label(zonaMessaggi)
messaggio.configure(justify = CENTER, foreground = 'RED')
messaggio.grid(sticky = N)
combinazione = Canvas(zonaMessaggi)
combinazione.configure(width = 130, height = 25)
combinazione.grid(sticky = N)
zonaSceltaFinale = Frame(pianoDiGioco)
zonaSceltaFinale.grid()
pulsanteAltroGioco = Button(zonaSceltaFinale)
pulsanteAltroGioco.configure(text = 'ALTRO GIOCO', padx=1, pady=1, background = 'GREEN', width = 13, command
= inizializza)
pulsanteAltroGioco.grid(row = 0, column = 0, sticky = N, padx = 4, pady = 4)
pulsanteChiudi = Button(zonaSceltaFinale)
pulsanteChiudi.configure(text = 'CHIUDI', padx = 1, pady = 1, background = 'GREEN', width = 8, command = quit)
pulsanteChiudi.grid(row = 0, column = 1, sticky = N, padx = 4, pady = 4)
pianoDiGioco.title('MASTER MIND')
inizializza()
pianoDiGioco.mainloop()
