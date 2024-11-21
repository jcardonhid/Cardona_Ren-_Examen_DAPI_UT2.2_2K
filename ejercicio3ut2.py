
palabra = input("Ingresa una palabra:")
cons = input("Ingresa una consonante:")
voc = input("Ingresa una vocal:")

palabra1 = palabra.replace(cons,cons.upper())
palabra2 = palabra1.replace(voc,"")

print(palabra2)

