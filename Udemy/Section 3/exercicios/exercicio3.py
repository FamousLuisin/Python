frase = "noc é lindo!         "

mais_apareceu = ""
qnt_apareceu = 0

i = 0

while i < len(frase):

    if frase[i] == " ":
        i += 1
        continue
    
    if frase.count(frase[i]) > qnt_apareceu:
        mais_apareceu = frase[i]
        qnt_apareceu = frase.count(frase[i])
    
    i += 1

print("A letra que apareceu mais vezes foi o: '{0}' que apareceu {1} vezes".format(mais_apareceu, qnt_apareceu))