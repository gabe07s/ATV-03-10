import os 
os.system("cls || clear ")
from dataclasses import dataclass

quantidade_de_familiares = 1
lista_familiares = []
lista_salario = []
contator = 0
media = 0
soma_salario = 0
soma_fihos = 0

while True:
    
        print("""
             === MENU ===
            1 - Adicionar família
            2 - Exibir resultados
            3 - Sair
        
        """)

        resposta = int(input("Deseja adicionar mais uma familia? "))

        match resposta:
            case 1:
                    quantidade_filhos = int(input("Digite a sua quantidade de filhos: "))
                    salario = float(input("Digite seu salario: "))
                    
                    contator += 1
                    lista_familiares.append(quantidade_filhos)
                    lista_salario.append(salario)
                
            case 2:
                print(f"familias que responderam: {contator}")
                maiorsalario =max(lista_salario)
                menorsalario =min(lista_salario)
                soma_salario =sum(lista_salario)
                media_salario = soma_salario / contator
                soma_flihos =sum(lista_familiares)
                media_filhos = soma_flihos / contator
                print(f"Maior salario da população: {maiorsalario}")
                print(f"Menor salario da população: {menorsalario}")
                print(f"Quantidade de filhos da população: {quantidade_filhos}")
                print(f"Media  salarial da população:  {media_salario}")
                print(f"Media de filhos da população:  {media_filhos}")                
                break
            case 3:
                print("===programa finalizado===")
                break    
            case _:
                print("opção invalida")

nome_arquivo = "Pesquisa_prefeitura.txt"

with open(nome_arquivo, "a") as arquivo_familia:
    for i in range(1):
        arquivo_familia.write(f"Familias que responderam {contator}, Media  salarial da população: {media_salario}, Media de filhos da população: {media_filhos}, Maior salario da população: {maiorsalario}, Menor salario da população: {menorsalario}\n  ")
arquivo_familia.close()