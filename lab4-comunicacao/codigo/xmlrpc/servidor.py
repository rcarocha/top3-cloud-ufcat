# RPC:XMLRPC
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

import datetime
import hashlib
import base64
import salto

# Tratador de Requisicoes do Servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

alunos = []

def codigo_confirmacao(aluno, mesg):
    codigo = hashlib.sha256()
    codigo.update(bytes(salto.salto, 'utf-8'))
    codigo.update (bytes(aluno, 'utf-8'))
    codigo.update (bytes(mesg, 'utf-8'))
    return base64.b64encode(codigo.digest())


def registre_atividade(aluno, mesg):
    alunos.append((aluno, datetime.datetime.now(), mesg))
    print(f'{aluno[:30]:30} ==> {mesg}')
    c = codigo_confirmacao(aluno, mesg)
    # print(base64.b64encode(c))
    return c

def id_servidor():
    return ('servidor XMLRPC', 'registre_atividade')


IP_SERVIDOR    = 'localhost'
PORTA_SERVIDOR = 8000

with SimpleXMLRPCServer((IP_SERVIDOR, PORTA_SERVIDOR),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    
    print(' ==> Registrando funcao [registre_atividade]')
    server.register_function(registre_atividade)
    print(' ==> Registrando funcao [id_servidor]')
    server.register_function(id_servidor)
    print()
    print(f' ==> Iniciando servidor em {IP_SERVIDOR}:{PORTA_SERVIDOR} ...')
    server.serve_forever()

# Exemplo de invocacao local
#registre_atividade("TESTE 1", "mensagem de aluno TESTE 1")
#registre_atividade("TESTE 2", "mensagem de aluno TESTE 2")


