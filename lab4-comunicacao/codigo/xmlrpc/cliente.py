import xmlrpc.client

IP_SERVIDOR    = 'localhost'
PORTA_SERVIDOR = 8000

servidor = xmlrpc.client.ServerProxy('http://' + IP_SERVIDOR + ':' + str(PORTA_SERVIDOR))

resposta = servidor.registre_atividade("RICARDO (prof)", "acesso local ao servidor")

# Mostra a lista dos metodos registrados no servidor
# print(servidor.system.listMethods())

print("Resposta: " + str(resposta))
