
nome=str(input('Insira o nome do aluno: '))
num1=float(input('Digite a primeira nota: '))
num2=float(input('Digite a segunda nota: '))
num3=float(input('Digite a terceira nota: '))  #pegar os dados

med=float(num1+num2+num3)/3     #calcular

print('A media das notas do aluno {} é {}'.format(nome,med))    #exibir