print(' \n ▀█▀ ▒█▀▀█ ▒█▀▄▀█ 　 ░░ 　 ▒█▀▀▀█ ▀█▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀ ▒█▀▄▀█ \n ▒█░ ▒█▀▀▄ ▒█▒█▒█ 　 ▀▀ 　 ░▀▀▀▄▄ ▒█░ ░▀▀▀▄▄ ░▒█░░ ▒█▀▀▀ ▒█▒█▒█ \n ▄█▄ ▒█▄▄█ ▒█░░▒█ 　 ░░ 　 ▒█▄▄▄█ ▄█▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄ ▒█░░▒█ \n')

print(' BEM VINDO!! \n\n run - help (para saber todos os comandos.)')

while(True):
	controle = 0

	comm=str(input('\n=>> '))
	
	if ( comm == 'help'): #ajuda
		print('\ncreate - cria um arquivo.\ncreatept - cria uma pasta.\ncalc - para chamar a calculadora. \nconfig - acessa as configurações do sistema.\noff - para desligar')
	
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

		while (True):
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
			print('\n------------------------------------------------\nConfirme para salvar as configurações.\n------------------------------------------------\nSelecione um número para entrar na configuração. \n------------------------------------------------\nexit - para sair. \n------------------------------------------------\n\n   [1] - Configurações de senha. \n'.format(conf_1))
			conf=str(input('\n(config)=>> '))

			if(conf == '1'):
				while(True):
					print('\nSeção [Senhas]:\n\n [1] - Iniciar com senha: {}'.format(conf_1))
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

	elif(comm == 'off'): #sair
		break
print('\nBye')
