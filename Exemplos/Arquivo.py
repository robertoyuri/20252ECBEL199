arquivo = open("exemplo.csv", "w")
arquivo.write("Escrevendo no meu primeiro arquivinho....")
arquivo.close()

arquivo = open("exemplo.csv", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()