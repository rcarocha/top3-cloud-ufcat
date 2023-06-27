# Laboratório 4: Modelos de Comunicação em Ambientes Distribuídos

## Objetivos

O objetivo deste laboratório é exemplificar alguns modelos de comunicação em computação distribuída, identificando sua flexibilidade e abertura.




## Atividades

Neste laboratório implementaremos simples programas para acessar um serviço remoto utilizando RPC baseado no modelo gRPC e SOAP/WSDL utilizando python.

## Requisitos de Software

### netcat - nc

Manipulador flexível de sockets para envio e recebimentos de mensagens pela rede. Utilizaremos para os seguintes fins:

Verificação de disponibilidade de porta `<porta>` no IP `<ip>`

        nc <ip> <porta>

Servidor TCP na porta `<porta>` que apenas exige o conteúdo recebido na tela.

        nc -l <porta>


### TShark

Analisador de protocolos na versão textual (sem interface gráfica). Instale na VM utilizando o seguinte comando:

        sudo apt update
        sudo apt install tshark

Teclar **Enter** quando aparecer uma janela perguntando uma opção de instalação.

Nos experimentos, executaremos o tshark com os seguintes parâmetros:

        sudo tshark -Y "tcp.dstport==2222" -x
        sudo tshark -i lo -Y "tcp.dstport==2222" -x

Nesses exemplos, estamos inspecionando mensagens que chegam destinadas à porta 2222 (TCP) e, no segundo exemplo, inspecionando apenas os pacotes da interface de rede loopback (`lo`). Acompanhe com o professor a correta interface a ser utilizada no experimento.

### Instalação dos pacotes Python usados nos exemplos

        pip install grpcio grpcio-tools


### Código de Referência

* [`codigo/`](codigo/) - Versão Local
* [`codigo/grpc/`](codigo/grpc/) - Comunicação via gRPC/python
* [`codigo/xmlrpc/`](codigo/xmlrpc/) - Comunicação via xmlrpc/python

