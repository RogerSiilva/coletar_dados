qnt_pessoas = int(input('Quantas pessoas terão no quarto? '))
# lista vazia 'quarto = []', funciona como vetores.
quarto = []

# input em nome e cpf para coletar os dados, hospede recebe os valores de nome e cpf
# quarto.append() recebe os dados coletados em hospede e adiciona a lista que estava vazia.
for i in range(qnt_pessoas):
    nome = input('Digite o nome: ')
    cpf = input('Digite o CPF: ')
    hospede = [nome, cpf]
    quarto.append(hospede)

print(quarto)