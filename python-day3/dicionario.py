aluno={'nome':'Paulo', 'idade':'35', 'matricula':'01928'}
#print(aluno) #impressão de todo o dicionário
#print(aluno['nome']) # refinar a impressão
#print(aluno['celular'])# retorna um erro, pois não existe dentro do dicionário.
#print(aluno.get('celular'))# retorna none
aluno['celular']='9999999'#adicionamos o número
aluno['nome']='Alice' #trocamos o nome
#print(aluno.get('celular',' nao exite'))
aluno.update({'nome':' Maria', 'idade':'20'})
#del aluno['idade']# excluir o registro de idade
#print(aluno)
#print(len(aluno))
#print(aluno.keys())
#print(aluno.values())
#print(aluno.items())
#for key in aluno:
for key, values in aluno.items():
    print(key, values)
