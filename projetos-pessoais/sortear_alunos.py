import random

#ler documento (aluno.txt)
r = open('alunos.txt','r')
ler = r.readlines()
r.close()

#sortear questão
questao = random.randint(1,20)

#sortear aluno
aluno = random.randint(0,2)
print(f'Aluno: {ler[aluno]}\nQuestão: {questao}')
ler.pop(aluno)
ler = ''.join(ler)

#reenviaar dados
w = open('alunos.txt','w')
criar = w.write(ler)


#https://github.com/Weest0
