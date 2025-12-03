'''
Obiettivo: Praticare l'accesso agli elementi e lo slicing.
'''

# Creare una lista temperature
Lista_iniziale = ["15", "18", "22", "25", "28", "30", "27", "24", "20"] 

# Ordinare i numeri automaticamente
Lista_ordinata = sorted(Lista_iniziale) 


# ------------ #

# Stampare la prima temperatura
print(Lista_ordinata[0]) 

# Stampare l'ultima temperatura
print(Lista_ordinata[-1]) 

# Stampare le temperature dalla posizione 2 alla 5 (esclusa)
print(Lista_ordinata[1:4])

# Stampare tutte le temperature con step 2 (saltando una ogni due)
print(Lista_ordinata[::2])

# Stampare la lista ordinata
print(Lista_ordinata)