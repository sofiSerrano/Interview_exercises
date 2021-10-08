def comparar_palabras(pal,pal2):
    #me devuelve a partir de donde son distintas o donde esta su ultima letra 
    pos=0
    band=False
    i=0
    while i<len(pal) and i<len(pal2) and band==False:
        if pal[i]!=pal2[i]:
            band=True
        i=1+i
    pos=i-1
    return pos

def encontrarmen(lst,stri):
    men=lst[0]
    for i in range(0,len(lst)):
        comp=comparar_palabras(lst[i],men)
        if stri.index(lst[i][comp])<stri.index(men[comp]):
            men=lst[i]
        if stri.index(lst[i][comp])<=stri.index(men[comp]) and len(lst[i])<len(men):
            men=lst[i]
    return men

def ordenar_extraterrestre(desordenadas,orden_alfabeto):
    ordenada=[]
    while len(desordenadas)>0:
        agregar=encontrarmayor(desordenadas,orden_alfabeto)
        ordenada.append(agregar)
        desordenadas.remove(agregar)
    return ordenada

def main():
    lista=ordenar_extraterrestre(['miel', 'extraterrestre', 'al', 'automovil', 'auto', 'revestir'],'zyxwvutsrqponmlkjihgfedcba')
    print(lista)
main()