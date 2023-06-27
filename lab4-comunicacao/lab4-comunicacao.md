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



###  OpenStack

* Arquitetura: <https://ubuntu.com/openstack/what-is-openstack>
* Documento de instalação: <https://ubuntu.com/openstack/install>
* Requisitos mínimos: 8Gb de RAM e 100Gb de disco. Utilizaremos 16 Gb de RAM e 200 Gb de disco.
200 G

### Instalação

    sudo snap install microstack --beta


### Inicialização do OpenStack

    sudo microstack init --auto --control

A iniciação demora aproximadamente 10min.

### Listar Imagens Disponíveis

    microstack.openstack image list

### Atributos ("Sabores") Disponíveis para VMs

    microstack.openstack flavor list

### Obter a senha do administrator do OpenStack

Acesse a interface web do adminstrador OpenStack pelo IP público da sua VM. Usuário administrador do OpenStack é `admin` e a senah deve ser obtida na estação executando o comando abaixo a partir de um terminal:

    sudo snap get microstack config.credentials.keystone-password

