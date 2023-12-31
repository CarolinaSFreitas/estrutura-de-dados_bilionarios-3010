import matplotlib.pyplot as plt
import csv

ricos = []

def carrega_dados():
    with open('forbes_2640_billionaires.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            ricos.append(linha)    # lista de dicionários


def titulo(texto, traco="-"):
    print()
    print(texto)
    print(traco*40)


def top_20():
    titulo("Top 20: Bilionários")
    
    print("\nNº Nome.......................... Pais................ Atividade........... Bills")
    
    contador = 0 

    for rico in ricos:
        contador += 1
        print(f"{contador:2d} {rico['name'][0:30]:30} {rico['country']:20} {rico['industry']:20} {rico['net_worth']:>5}")
        if contador == 20:
            break


def compara_paises():
    titulo("Comparativo entre Países")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()

    #primeiro país
    conta1 = 0

    print(f"\nBilionários: {pais1}")
 
    print("\nRank Nome.......................... Atividade........... Bills")

    for rico in ricos:
        if (rico['country'].upper() == pais1):
            conta1 += 1
            print(f"{rico['rank']:>4} {rico['name'][0:30]:30} {rico['industry']:20} {rico['net_worth']:>5}")
    print("-"*75)
    print(f"Total de Bilionários - {pais1}: {conta1}")

    input()

    #segundo país
    conta2 = 0

    print(f"\nBilionários: {pais2}")
 
    print("\nRank Nome.......................... Atividade........... Bills")

    for rico in ricos:
        if (rico['country'].upper() == pais2):
            conta2 += 1
            print(f"{rico['rank']:>4} {rico['name'][0:30]:30} {rico['industry']:20} {rico['net_worth']:>5}")

    print("-"*75)
    print(f"Total de Bilionários - {pais2}: {conta2}")


def agrupa_atividade():
    titulo("Agrupar por Atividade")
    
    atividades = []
    numeros = []

    for rico in ricos:
        if rico['industry'] in atividades:
            indice = atividades.index(rico['industry'])
            numeros[indice] += 1
        else:
            atividades.append(rico['industry'])
            numeros.append(1)
        
    # ordena por ordem decrescente de numeros    
    numeros2, atividades2 = zip(*sorted(zip(numeros, atividades), reverse=True))    #esse reverse=True ordena de forma decrescente

    print("Atividade.....................: Numero")

    for ativ, num in zip(atividades2, numeros2):
        print(f"{ativ:30} {num:5d}")


def grafico_atividades():
    titulo("Gráfico por Atividades")
    fig, ax = plt.subplots()                   #do matplotlib

    atividades = []
    numeros = []

    for rico in ricos:
        if rico['industry'] in atividades:
            indice = atividades.index(rico['industry'])
            numeros[indice] += 1
        else:
            atividades.append(rico['industry'])
            numeros.append(1)

    numeros2, atividades2 = zip(*sorted(zip(numeros, atividades), reverse=True))    #esse reverse=True ordena de forma decrescente

    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:red', 'tab:green']

    ax.bar(atividades2[0:6], numeros2[0:6], color = bar_colors)

    ax.set_ylabel('Nº de Bilionários')
    ax.set_title('Gráfico Comparando Atividades dos Bilionários')
    plt.tight_layout()      #ajusta os nomes das atividades
    plt.show()           #mostra o gráfico


def grafico_idades():
    titulo("Gráfico Comparando Idade do Bilionários")
    fig, ax = plt.subplots()                   #do matplotlib

    faixas = ["Até 30 anos", "Entre 31 e 40", "Entre 41 e 50", "Entre 51 e 60", "Acima de 60"]
    numeros = [0, 0, 0, 0, 0]
    explode = (0, 0, 0, 0, 0.1)     #esse 0.1 afasta o valor em fatia da quinta posição em faixas

    for rico in ricos:
        #se o campo tem conteudo (alguns estão vazios no csv)
        if rico['age']:
            idade = float(rico['age'])
            if idade <= 30:
                numeros[0] += 1
            elif idade <= 40:
                numeros[1] += 1
            elif idade <= 40:
                numeros[2] += 1
            elif idade <= 60:
                numeros[3] += 1
            else:
                numeros[4] += 1

    ax.pie(numeros, labels=faixas, autopct='%.1f%%', explode=explode, shadow=True)  #esse "autopct='%1.1f%%'" mostra com porcentagem no gráfico

    ax.set_title('Gráfico Comparando Idades dos Bilionários')
    plt.show()           


def boxplot_idades():
    titulo("Gráfico Boxplot de Idades dos Bilionários")

    idades = []
    nomes = []
    for rico in ricos:
        if rico['age']:
            idades.append(float(rico['age']))
            if float(rico["age"]) >= 100:
                nomes.append(rico['name'])
    print(nomes)

    fig, ax = plt.subplots()
    ax.boxplot(idades)
    plt.show()
 

# ---------------------------------------------------------------------  Programa Principal
carrega_dados()

while True:
    titulo("Forbes: Bilionários 2023", "=")
    print("1. Top 20 Bilionários")
    print("2. Comparativo entre 2 Países")
    print("3. Agrupar por Atividade")
    print("4. Gráfico Relacionando Atividades")
    print("5. Gráfico Comparando Idades")
    print("6. Gráfico Boxplot de Idades")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top_20()
    elif opcao == 2:
        compara_paises()
    elif opcao == 3:
        agrupa_atividade()
    elif opcao == 4:
        grafico_atividades()
    elif opcao == 5:
        grafico_idades()
    elif opcao == 6:
        boxplot_idades()
    else:
        break

