import servidor
import grpc

import registro_pb2
import registro_pb2_grpc


SERVIDOR = 'localhost:50051'

with grpc.insecure_channel(SERVIDOR) as channel:
        
        print(f'Conectando com servidor em {SERVIDOR}')
        
        stub = registro_pb2_grpc.RegistroStub(channel)
        resposta = stub.RegistreAtividade(registro_pb2.AtividadeAluno(aluno='you', mesg='?? teste ??'))
        print("Resposta para Cliente: " + resposta.hashBase64)

#resposta = servidor.registre_atividade("RICARDO (prof)", "acesso local ao servidor")

#print("Resposta: " + resposta.decode())
