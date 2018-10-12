def remove_caracter(texto) :
    remove = "()\n\r"
    for i in range(0, len(remove)) :
        texto = texto.replace(remove[i],"")
    return texto

def remove_espacos_vazios(vetor_generico,*args):
    deletar = list(args)
    for item in deletar:
        while item in vetor_generico:
            vetor_generico.remove(item)
    return vetor_generico

def quebra_lista(lista, n):
	return [lista[i:i+n] for i in range(0, len(lista), n)]

def lista_para_caracter(lista):
	texto = ''
	for index in lista:
		texto += ' ' + index
	return texto

def escreve_arquivo(texto):
	arquivo = open('saida.txt', 'w')
	arquivo.writelines(texto)
	arquivo.close()

def le_arquivo(nomeArq):
	
	arq = open(nomeArq,'r')
	texto = arq.readline()
	matriz_generica = []
	vetor_generico = []

	while texto != '':
		texto = remove_caracter(texto)
		vetor_generico= texto.split(" ")
		vetor_generico = remove_espacos_vazios(vetor_generico,'')
		matriz_generica.append(vetor_generico)
		texto = arq.readline()

	arq.close()
	separa_informacoes(matriz_generica)

	return texto

def separa_informacoes(matriz_generica):
	dicionario = {}
	trans = []
	out_fn = []
	enum = 0

	for pos_matriz in matriz_generica:

		if 'mealy' in pos_matriz or 'moore' in pos_matriz:
			dicionario['nome'] = pos_matriz[0]

		elif 'symbols-in' in pos_matriz:
			dicionario['symbols-in'] = pos_matriz[1:]

		elif 'symbols-out' in pos_matriz:
			dicionario['symbols-out'] = pos_matriz[1:]

		elif 'states' in pos_matriz:
			dicionario['states'] = pos_matriz[1:]

		elif 'finals' in pos_matriz:
			dicionario['finals'] = pos_matriz[1:]

		elif 'start' in pos_matriz:
			dicionario['start'] = pos_matriz[1:]

		elif 'trans' in pos_matriz:
			enum = 1

		elif 'out-fn' in pos_matriz:
			enum = 2
			
		elif enum == 1:
			trans.extend(pos_matriz)
			dicionario['trans'] = trans

		elif enum == 2:
			out_fn.extend(pos_matriz)
			dicionario['out-fn'] = out_fn

	if dicionario['nome'] == 'mealy':
		dicionario['trans'] = quebra_lista(dicionario['trans'], 4)
		mealy_to_moore(dicionario)
	else :
		dicionario['trans'] = quebra_lista(dicionario['trans'], 3)
		dicionario['out-fn'] = remove_espacos_vazios(dicionario['out-fn'], dicionario['start'][0])
		dicionario['out-fn'] = quebra_lista(dicionario['out-fn'], 2)
		moore_to_mealy(dicionario)

def cria_texto(dicionario):
	texto_pronto = ''
	trocar = ''

	for key in dicionario:
		if key == 'nome':
			texto_pronto += '(' + dicionario[key] + '\n'
		if key == 'symbols-in':
			trocar = lista_para_caracter(dicionario[key])
			texto_pronto += '(' + key + ' ' + trocar + ')' + '\n'
		if key == 'symbols-out':
			trocar = lista_para_caracter(dicionario[key])
			texto_pronto += '(' + key + ' ' + trocar + ')' + '\n'
		if key == 'states':
			trocar = lista_para_caracter(dicionario[key])
			texto_pronto += '(' + key + ' ' + trocar + ')' + '\n'
		if key == 'finals':
			trocar = lista_para_caracter(dicionario[key])
			texto_pronto += '(' + key + ' ' + trocar + ')' + '\n'
		if key == 'start':
			trocar = lista_para_caracter(dicionario[key])
			texto_pronto += '(' + key + ' ' + trocar + ')' + '\n'
			
		if key == 'trans':
			texto_pronto +=  '(' + key + '\n'
			count = 0
			for i in dicionario[key]:
				trocar = lista_para_caracter(i)
				texto_pronto +=  '(' + trocar + ')'
				count +=1
				if (count == (len(dicionario[key])//2)):
					texto_pronto += '\n'
			texto_pronto += ')' + '\n'

		if key == 'out-fn':
			texto_pronto +=  '(' + key + '\n'
			count = 0
			for i in dicionario[key]:
				trocar = lista_para_caracter(i)
				texto_pronto +=  '(' + trocar + ')'
				count +=1
				if (count == (len(dicionario[key])//2)):
					texto_pronto += '\n'
			texto_pronto += ')'

	texto_pronto += ')'
	escreve_arquivo(texto_pronto)

def moore_to_mealy(dicionario):
	pos_trans = 0

	while dicionario['out-fn'] != []:
		pos_trans = 0
		for index_trans in dicionario['trans']:	
			if (dicionario['out-fn'][0][0] == index_trans[1]):
				dicionario['trans'][pos_trans].append(dicionario['out-fn'][0][1])
			pos_trans += 1
		dicionario['out-fn'].remove(dicionario['out-fn'][0])
	dicionario.pop('out-fn')
	cria_texto(dicionario)

def mealy_to_moore(dicionario):
	# print(dicionario)
	states_dicionario = {}
	pesquisa = 1
	dicionario.update({'out-fn': []})
	
	
	#carregando o out-fn 
	for index in dicionario['trans']:
		dicionario['out-fn'].append(index[1])
		dicionario['out-fn'].append(index[3])
	dicionario['out-fn'] = quebra_lista(dicionario['out-fn'], 2)
	
	# retirando valores repetidos do out-fn
	for index in range(0, len(dicionario['out-fn'])): 
		pesquisa = (index + 1)
		while pesquisa < (len(dicionario['out-fn'])):
			if (dicionario['out-fn'][index] == dicionario['out-fn'][pesquisa]):
				dicionario['out-fn'].remove(dicionario['out-fn'][pesquisa])
			pesquisa += 1
	
	#criando um dicionario auxilixar para fazer o update no dicionario original
	for index in range(0, len(dicionario['out-fn'])): 
		pesquisa = (index + 1)
		while pesquisa < (len(dicionario['out-fn'])):
			if (dicionario['out-fn'][index][0] == dicionario['out-fn'][pesquisa][0]):
				states_dicionario[(str(dicionario['out-fn'][pesquisa][0] + dicionario['out-fn'][pesquisa][1]))] = dicionario['out-fn'][pesquisa]
				states_dicionario[(str(dicionario['out-fn'][index][0] + dicionario['out-fn'][index][1]))] = dicionario['out-fn'][index]
			pesquisa += 1

	print(dicionario)

	#update no dicionario original nas transicoes
	for index in range(0, len(dicionario['trans'])): 
		pesquisa = (index + 1)
		for key in states_dicionario:
			if (dicionario['trans'][index][1] == states_dicionario[key][0] and dicionario['trans'][index][3] == states_dicionario[key][1]):
				dicionario['trans'][index][1] = key

	#update no dicionario original nas transicoes
	for index in range(0, len(dicionario['out-fn'])): 
		pesquisa = (index + 1)
		for key in states_dicionario:
			if (dicionario['out-fn'][index][0] == states_dicionario[key][0] and dicionario['out-fn'][index][1] == states_dicionario[key][1]):
				dicionario['out-fn'][index][0] = key

	#update no dicionario original nos estados
	for index in states_dicionario:
		dicionario['states'].append(index)
	
	# apagando pesos das transicoes
	for index in dicionario['trans']:
		del(index[3])


	print(dicionario)
	print(states_dicionario)
	cria_texto(dicionario)