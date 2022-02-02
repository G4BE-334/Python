rounds = int(input())
numeros = []
listaGuia = [1, 5, 10, 50, 100, 500, 1000]
listaGuiaS = ["I", "V", "X", "L", "C", "D", "M"]

for i in range(rounds):
    numeros.append(int(input()))


for x in range(rounds):
    especial = False
    for y in range(1, len(listaGuia)):
        if (numeros[x] < listaGuia[y]):
            if (numeros[x] % 10 == 4):
                temp = numeros[x]
                count = 1
                done = False
                while (done == False):
                    if (temp == 4):
                        print("IV")
                        break
                    else:
                        qtd = int(temp/listaGuia[y-count])
                        for i in range(qtd):
                            print(listaGuiaS[y-count], end="")
                        temp = temp - listaGuia[y-count]*qtd
                        count += 1
            elif (numeros[x] % 10 == 9):
                especial = True
            else:
                count = 1
                temp = numeros[x]
                done = False
                while (done == False):
                    if (temp % listaGuia[y-count] == 0):
                        qtd = int(temp/listaGuia[y-count])
                        for i in range(qtd):
                            print(listaGuiaS[y-count], end="")
                            done = True
                    else:
                        qtd = int(temp/listaGuia[y-count])
                        for i in range(qtd):
                            print(listaGuiaS[y-count], end="")
                        temp = temp - listaGuia[y-count]*qtd
                        count += 1
            break
    print()
