arquivo = open("exemplo.txt", "w")
arquivo.write("Escrevendo no meu primeiro arquivinho....")
arquivo.close()

arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()