import random
saldo = float(100)
dinh = str('moedas')
t = str('-')
b = str('|')
sm = str('+') 
esp = str(' ')

print(f'\n{esp*13}█▀▀▀ █▀▀█ █▀▄▀█ █▀▀ \n{esp*13}█░▀█ █▄▄█ █░▀░█ █▀▀ \n{esp*13}▀▀▀▀ ▀░░▀ ▀░░░▀ ▀▀▀ ')

while (True):
	print(f'+{t*45}+\n| Modo A: Apostas entre 10.00 e 30.00 moedas. |\n+{t*45}+\n| Modo B: Apostas entre 30.00 e 60.00 moedas. |\n+{t*45}+\n| Modo C: Apostas acima de 60.00 moedas.      |\n+{t*45}+ \n\nSeu saldo: {saldo}')
	modo=str(input('\nEm qual modo de jogo jogará? [A, B ou C]: ').upper())
	
	if(modo == 'A'):
		aposta=float(input('Qual será o valor da aposta? '))
		print('\nEscolha um numero de 1 a 10.')
		num_apst=int(input('Numero: '))
		aleat = random.randint(1, 10)
		if(num_apst == aleat):
			lucro = (aposta * 5)
			saldo = saldo + lucro
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
		else:
			saldo = (saldo - aposta)
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

		while(aposta < 10 or aposta > 30):
			print('Valor é diferente do suportado, no modo A somente apostas entre 10.00 e 30.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))
			print('Escolha um numero de 1 a 10.')
			num_apst=int(input('Numero: '))
			aleat = random.randint(1, 10)
			if(num_apst == aleat):
				lucro = (aposta * 5)
				saldo = saldo + lucro
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
			else:
				saldo = (saldo - aposta)
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

	if(modo == 'B'):
		aposta=float(input('Qual será o valor da aposta? '))
		print('\nEscolha um numero de 1 a 30.')
		num_apst=int(input('Numero: '))
		aleat = random.randint(1, 30)
		if(num_apst == aleat):
			lucro = (aposta * 10)
			saldo = saldo + lucro
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
		else:
			saldo = (saldo - aposta)
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

		while(aposta < 30 or aposta > 60):
			print('Valor é diferente do suportado, no modo B somente apostas entre 30.00 e 60.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))
			print('Escolha um numero de 1 a 30.')
			num_apst=int(input('Numero: '))
			aleat = random.randint(1, 30)
			if(num_apst == aleat):
				lucro = (aposta * 10)
				saldo = saldo + lucro
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
			else:
				saldo = (saldo - aposta)
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')


	if(modo == 'C'):
		aposta=float(input('Qual será o valor da aposta? '))
		print('\nEscolha um numero de 1 a 100.')
		num_apst=int(input('Numero: '))
		aleat = random.randint(1, 100)
		if(num_apst == aleat):
			lucro = (aposta * 15)
			saldo = saldo + lucro
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
		else:
			saldo = (saldo - aposta)
			print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
			print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

		while(aposta < 60):
			print('Valor é diferente do suportado, no modo C somente apostas acima de 100.00 moedas.')
			aposta=float(input('Qual será o valor da aposta? '))
			print('Escolha um numero de 1 a 100.')
			num_apst=int(input('Numero: '))
			aleat = random.randint(1, 100)
			if(num_apst == aleat):
				lucro = (aposta * 15)
				saldo = saldo + lucro
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█──░█ ▀█▀ ░█▄─░█ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█░█░█ ░█─ ░█░█░█ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▀▄█ ▄█▄ ░█──▀█ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nLucrou: {lucro} {dinh} \n\nSaldo Atual: {saldo} {dinh}')
			else:
				saldo = (saldo - aposta)
				print('\n ░█──░█ ░█▀▀▀█ ░█─░█ ── ░█─── ░█▀▀▀█ ░█▀▀▀█ ░█▀▀▀ \n ░█▄▄▄█ ░█──░█ ░█─░█ ▀▀ ░█─── ░█──░█ ─▀▀▀▄▄ ░█▀▀▀ \n ──░█── ░█▄▄▄█ ─▀▄▄▀ ── ░█▄▄█ ░█▄▄▄█ ░█▄▄▄█ ░█▄▄▄ ')
				print(f'\n\nO numero sorteado foi: {aleat}\n\nPerdeu: {aposta} {dinh}\n\nSaldo Atual: {saldo} {dinh}')

	if(modo == 'E'):
		break
