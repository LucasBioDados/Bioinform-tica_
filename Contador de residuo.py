sequencia = input("Digite aqui sua sequência de aminoácidos: ").upper().replace(" ", "")
total_aminoacidos = len(sequencia)
contagem = {}
for aa in sequencia: 
    if aa in contagem: 
        contagem[aa] +=1
    else:
        contagem[aa] =1 
print("Aqui está o quantitativo de resíduos da sua sequência: ")
for aa, valor in contagem.items():
    porcentagem = (valor/ total_aminoacidos)*100
    porcentagem_arredondada = round(porcentagem, 2)
    print(f"Resíduo {aa}:{valor} percentual ({porcentagem_arredondada}%)")
