import random
saldo = float(100)
dinh = str('moedas')
t = str('-')
b = str('|')
sm = str('+') 


while (True):
	print(f'\n+{t*45}+\n| Modo A: Apostas entre 10.00 e 30.00 moedas. |\n+{t*45}+\n| Modo B: Apostas entre 30.00 e 60.00 moedas. |\n+{t*45}+\n| Modo C: Apostas acima de 60.00 moedas.      |\n+{t*45}+ \n\nSeu saldo: {saldo}')
	modo=str(input('\nEm qual modo de jogo jogará? [A, B ou C]: ').upper())
	
	if(modo == 'A'):
		aposta=float(input('Qual será o valor da aposta? '))
		print('\nEscolha um numero de 1 a 10.')
		num_apst=int(input('Numero: '))
		aleat = random.randint(1, 10)
		if(num_apst == aleat):
			lucro = (aposta * 5)
			saldo = saldo + lucro
			print(f'\n\n-#-#-Você ganhou!!-#-#- \nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
		else:
			saldo = (saldo - aposta)
			print(f'\n\n-#-#-Você perdeu-#-#- \nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

		while(aposta < 10 or aposta > 30):
			print('Valor é diferente do suportado, no modo A somente apostas entre 10.00 e 30.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))
			print('Escolha um numero de 1 a 10.')
			num_apst=int(input('Numero: '))
			aleat = random.randint(1, 10)
			if(num_apst == aleat):
				lucro = (aposta * 5)
				saldo = saldo + lucro
				print(f'\n\n-#-#-Você ganhou!!-#-#- \nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
			else:
				saldo = (saldo - aposta)
				print(f'\n\n-#-#-Você perdeu-#-#- \nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

	if(modo == 'B'):
		aposta=float(input('Qual será o valor da aposta? '))
		print('B')
		while(aposta < 30 or aposta > 60):
			print('Valor é diferente do suportado, no modo B somente apostas entre 30.00 e 60.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))

	if(modo == 'C'):
		aposta=float(input('Qual será o valor da aposta? '))
		while(aposta < 100):
			print('C')
			print('Valor é diferente do suportado, no modo C somente apostas acima de 100.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))


	#print(random.randint(1, 10))


	if(modo == 'E'):
		break
