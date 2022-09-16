traco = str('-')
espaco = str(' ')
controle = str(0)

print(' \n ▀█▀ ▒█▀▀█ ▒█▀▄▀█ 　 ░░ 　 ▒█▀▀▀█ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▄▀█ \n ▒█░ ▒█▀▀▄ ▒█▒█▒█ 　 ▀▀ 　 ░▀▀▀▄▄ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▒█▒█ \n ▄█▄ ▒█▄▄█ ▒█░░▒█ 　 ░░ 　 ▒█▄▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░░▒█ \n')

print(' BEM VINDO!! \n\n run - help (para saber todos os comandos.)')

while(True):
	

	comm=str(input('\n=>> '))
	
	if ( comm == 'help'): #ajuda
		print(f'\n{traco*48}\n| file - cria um arquivo.{espaco*22}|\n{traco*48}\n| creatept - cria uma pasta.{espaco*19}|\n{traco*48}\n| calc - para chamar a calculadora.{espaco*12}|\n{traco*48}\n| config - acessa as configurações do sistema.{espaco}|\n{traco*48}\n| off - para desligar{espaco*26}|\n{traco*48}')

	
	elif (comm == 'calc'): #calculadora!!!!!!
		
		pri=float(input('\nPrimeiro valor: '))
		seg=float(input('Segundo valor: '))
		
		print('\n(+ para soma.)\n(- para subtração.)\n(* para multiplicação.)\n(/ para divisão.)')
		ope=str(input('\nInsira o operador: '))
		
		if (ope == '+'):
			soma=pri+seg
			print(f'\nResultado: {soma:.2f}')
		elif (ope == '-'):
			sub=pri-seg
			print(f'\nResultado: {sub:.2f}')
		elif (ope == '*'):
			mult=pri*seg
			print(f'\nResultado: {mult:.2f}')
		elif (ope == '/'):
			div=pri/seg
			print(f'\nResultado: {div:.2f}')
		elif(ope != '+' or '-' or '*' or '/'):
			print('\n--------|X|---------\n\nERROR!!\nTENTE NOVAMENTE:')
			controle=1

		while (controle == 1):
			print('\n(+ para soma.)\n(- para subtração.)\n(* para multiplicação.)\n(/ para divisão.)')
			ope=str(input('\nInsira o operador: '))
			
			if (ope == '+'):
				soma=pri+seg
				print(f'\nResultado: {soma:.2f}')
				break
			elif (ope == '-'):
				sub=pri-seg
				print(f'\nResultado: {sub:.2f}')
				break
			elif (ope == '*'):
				mult=pri*seg
				print(f'\nResultado: {mult:.2f}')
				break
			elif (ope == '/'):
				div=pri/seg
				print(f'\nResultado: {div:.2f}')
				break
			elif(ope != '+' or '-' or '*' or '/'):
				print('\n--------|X|---------\n\nERROR!!\nTENTE NOVAMENTE:')

	elif(comm == 'config'):
		while(True):
			conf_1='Sim'
			print(f'\n{traco*52}\n| Confirme para salvar as configurações.{espaco*11}|\n{traco*52}\n| Selecione um número para entrar na configuração.{espaco}|\n{traco*52}\n| exit - para sair.{espaco*32}|\n{traco*52}\n\n   [1] - Configurações de senha. \n   [2] - Configurações de interface.'.format(conf_1))
			conf=str(input('\n(config)=>> '))

			if(conf == '1'):
				while(True):
					print('\nSeção [Senhas]:\n\n [1] - Iniciar com senha: {}\n [2] - senha: ****'.format(conf_1))
					conf=str(input('\n(config-[senhas])=>> '))
					if(conf == '1'):
						conf_1=str(input('- Iniciar com senha? [Sim|Não]\n\n> '))
					if(conf == 'exit'):
						break
			
			if(conf == 'exit'):
				print('\nSalve antes de sair. [S|N]')
				conf=str(input('\nSalvar?\n\n(config)==> ').upper())
				
				if(conf == 'S'):
					print('\nSALVO')
					break
				elif(conf == 'N'):
					print('\nOk')
					break
	elif(comm == 'file'): #mexer com arquivos
		print('\n[1] - Para criar um arquivo. \n[2] - Para ler um arquivo.')
		arq = int(input('\n(file)=> '))
		if(arq == 1):
			nome_arq = str(input('\nNome do arquivo com formato: '))
			info = str(input('\n'))
			criar = open(f'{nome_arq}','w')
			dados = (criar.write(f'{info}'))
			criar.close()
		elif(arq == 2):
			nome_arq = str(input('\nInsira o nome do arquivo: '))
			ler = open(f'{nome_arq}','r')
			print(f'\n{traco*77}\n{ler.read(1000)}\n{traco*77}')


	elif(comm == 'off'): #sair
		break
print('\nBye')
