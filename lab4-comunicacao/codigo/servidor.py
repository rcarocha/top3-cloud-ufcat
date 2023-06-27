# https://wiki.python.org/moin/WebServices
# HTTP
# RPC:XMLRPC, JSONRPC, gRPC (https://grpc.io/)
# CORBA
# SOAP
# WSDL
# REST: https://realpython.com/api-integration-in-python/

import datetime
import hashlib
import base64
import salto

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


#registre_atividade("TESTE 1", "mensagem de aluno TESTE 1")
#registre_atividade("TESTE 2", "mensagem de aluno TESTE 2")


