def list_turn(lista):
    aux = [[]]
    z = 0
    i = 0
    while i < (len(lista)-len(lista) % 3):
            aux[z].append(lista[i])
            aux[z].append(lista[i + 1])
            aux[z].append(lista[i + 2])
            aux.append([])
            i+=3
            z+=1
    aux.pop()
    if len(lista) % 3 == 1:
        aux.append([lista[len(lista)-1]])
    elif len(lista) % 3 == 2:
        aux.append([lista[len(lista)-2], lista[len(lista)-1]])
    return aux

def edit_distance(string1, string2):
    aux1 = " " + string1
    aux2 = " " + string2
    ant = [x for x in range(len(aux2)) ]
    prezent = []
    for i in range(1, len(aux1)):
        prezent = [i + 1]
        for j in range(1, len(aux2)):
            if aux2[j] == aux1[i]:
                repl = ant[j - 1]
            else:
                repl = ant[j - 1] + 1
            nr = min(prezent[j - 1] + 1, ant[j] + 1, repl)
            prezent.append(nr)
        ant = prezent
    if prezent == []: return -1
    return prezent[-1]

def edit_distance_text(string, text):
    mini = 99999
    for j in range(len(text)):
            for jp in range(j):
                cv = edit_distance(string, text[jp:j])
                if cv < mini:
                    mini = cv
    return mini

def get_approximate_product(string, lista):
    rez = []
    a = {}
    for el in lista:
        cv = edit_distance_text(string, el.get_title())
        if cv <= 2:
            rez.append(el)
            a[el] = cv
    rez.sort(key = lambda x: a[x], reversed = True)
    return rez