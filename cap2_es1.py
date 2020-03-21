from collections import Counter
import urllib.request, re

# comunica con l'utente e con internet
url = input("Inserisci un url: ")
try:
    html = urllib.request.urlopen(url)
except:
    print("Impossibile aprire %s" % url)
    quit()

# legge e normalizza parzialmente la pagina
doc = html.read().decode().lower()

# suddivide il testo in parole
words = re.findall(r"\w+", doc)

# crea un contatore e mostra la risposta
print(Counter(words).most_common(10))
