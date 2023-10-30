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


# ---------------------------------------------------------------------  Programa Principal
carrega_dados()

while True:
    titulo("Forbes: Bilionários 2023", "=")
    print("1. Top 20 Bilionários")
    print("2. Comparativo entre 2 Países")
    print("3. Agrupar por Atividade")
    print("4. Gráfico Relacionando Atividades")
    print("5. Finalizar")
    opcao = int(input("Opção: "))

