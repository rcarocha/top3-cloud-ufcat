# Laboratório 2: Plataforma de Virtualização

## Objetivos

O objetivo deste laboratório é ilustrar a necessidade e estrutura de uma plataforma de virtualização completa para computação em nuvem, usando OpenStack como exemplo.




## Atividades

Neste laboratório o professor instalará o OpenStack em uma VM como demonstração de uma plataforma para virtualização.


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

