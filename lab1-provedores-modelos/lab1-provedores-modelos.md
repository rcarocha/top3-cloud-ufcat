# Laboratório 1: Provedores e Modelos para Computação em Nuvem

## Objetivos

O objetivo deste laboratório é ilustrar os modelos de computação de nuvem discutidos, particularmente IaaS e PaaS, por meio da demonstração de uso e instalação de aplicações em máquinas virtuais e plataformas na Google Cloud Platform. Este laboratório tem os seguintes objetivos adicionais:

- oferecer uma visão geral do encadeamento de conceitos fundamentais de computação em nuvem, como virtualização, máquinas virtuais, redes virtualizadas, entre outros.
- permitir ao aluno compreender alguns cenário elementares de uso de computação em nuvem.
- oferecer uma visão geral das ferramentas de gerenciamento oferecidas por um provedor de computação em nuvem.
- demonstrar o uso de uma ferramenta de desenvolvedor e administrador de projetos na nuvem oferecido por um provedor.


## Recursos

* [multipass](https://multipass.run/docs/tutorials) - gerenciador de máquinas virtuais
  * [Folha de referência](https://assets.ubuntu.com/v1/f401c3f4-Ubuntu_Server_CLI_pro_tips_2020-04.pdf) para multipass e servidor Ubuntu
* [Google Cloud CLI](https://cloud.google.com/sdk/gcloud/reference) - ferramenta em linha de comando do Google Cloud
  * [Folha de referência](https://cloud.google.com/sdk/docs/cheatsheet?hl=pt-br)

### Comandos Linux Úteis para o Laboratório

Além dos comandos exemplificados na folha de referência, os seguintes comandos podem ser úteis:

* Obter o endereço IP público de uma estação

  ```sh
  curl ifconfig.co
  ```

  Alternativamente, podem ser utilizados os seguintes endereços: `ifconfig.me`, `icanhazip.com`.

* Executar um servidor web usando Python

  ```sh
  python3 -m http.server 9090
  ```

  Inclua a opção `--bind ADDRESS` com o endereço IP da estação em `ADDRESS`, caso o servidor precise aceitar requisições por um endereço específico.


## Pré-requisitos

Espera-se que o aluno tenha o **multipass** ou outro ambiente de gerenciamento de máquinas virtuais (exemplo: VirtualBox) instalado na sua estação e com uma máquina com imagem do servidor Ubuntu ou Debian.

## Atividades

As atividades aqui descritas não serão um passo-a-passo ou servirão como documentação das ferramentas utilizadas. Elas são unicamente guia das atividades feitas em sala de aula. Sugiro que tome nota das ações atividades que quiser reproduzir mais à frente entretanto não é o objetivo da aula capacitar o aluno a reproduzi-las.

Exceto quando estivermos utilizando o console do Google Cloud, as atividades serão realizadas no terminal de comandos no Linux.

Este documento, scripts e códigos mencionados neste documento estão disponíveis no projeto GitHub em <https://github.com/rcarocha/top3-cloud-ufcat>. Quando for necessário utilizar algum dos códigos mencionados, copie esse projeto para o seu ambiene, utilizando o comando git:

    git clone https://github.com/rcarocha/top3-cloud-ufcat

### Parte 1: Uso do `multipass` e máquina virtualizada

A tabela abaixo mostra um guia de comandos que serão utilizadas durante a aula. Documentação detalhada pode ser encontrada na [página do multipass](https://multipass.run/docs/how-to-guides).

| Tarefas                                       | Comando Exemplo          |
|-----------------------------------------------|--------------------------|
| Criar uma instância                           | `multipass launch`       |
| Listar imagens de instâncias                  | `multipass find`         |
| Criar uma instância com uma imagem específica | `multipass launch 20.04` |
| Criar uma instância com um nome específico    | `multipass launch 20.04 --name lab1` |
| Criar uma instância com atributos específicos | `multipass launch --cpus 4 --disk 20G --memory 8G` |
| Listar instâncias de VM criadas               | `multipass list`         |
| Obter atributos de uma instância              | `multipass info lab1`    |
| Abrir um terminal em uma instância            | `multipass shell lab1`   |
| Executar um comando em uma instância          | `multipass exec lab1 ls` |
| Iniciar uma instância                         | `multipass start lab1`   |
| Suspender uma instância                       | `multipass suspend lab1` |
| Parar uma instância                           | `multipass stop lab1`    |
| Apagar uma instância                          | `multipass delete lab1`  |
| Remover uma instância do disco                | `multipass purge`        |

Execute um servidor web em uma máquina virtualizada e acesse pelo seu browser.

Instale o módulo Flask no Python com o comando:

        sudo apt install python3-pip
        pip3 install flask

Coloque a aplicação Python Flask no servidor (diretório [`python-app`](python-app)) e acesse-a do seu browser.

        python3 appteste.py

### Parte 2: Google Cloud Platform

#### Google Cloud Platform

1. Entre no console do Google Cloud em <https://console.cloud.google.com/>
2. Crie um projeto com o nome `lab1-SEU.NOME.EM.MAIUSCULAS`
3. Compartilhe o projeto com o professor (email `@ufcat` do professor)

#### Google Cloud - Compute Engine - IaaS

1. Crie uma máquina virtual no Compute Engine (inicie a máquina logo depois)
2. Verifique a precificação da VM que você pretende criar (escolha um com preço o menor possível)
3. Verifique as imagens (appliances) disponíveis para criação de VMs
4. Verifique as configurações de rede (IP interno e externo, firewall) da sua máquina
5. Abra um terminal SSH para a sua máquina.
   1. Execute um servidor web na estação e tente acessar do seu browser.
   2. Coloque a aplicação web Python em Flask e acesse do seu browser. Utilize a opção "Upload de arquivo" no canto superior direito ou utilize o git.
6. Entre na interface de monitoramento na sua VM
7. Entre na interface de monitoramento e controle de preços e defina limites para o gasto do seu projeto.

#### Google Cloud CLI - gcloud

1. Instale o Google Cloud CLI na sua VM local (criada com o multipass ou VirtualBox), utilizando o script [`gcloud-install.sh`](scripts/gcloud-install.sh) deste laboratório.
2. Inicialize e se autentique na ferramenta.

        gcloud init

   * Uma vez autenticado, o `gcloud` não solicitará mais a autenticação para acessar o seu projeto no Google Cloud. Se você estiver usando uma máquina que não seja pessoal, outro aluno que acessar a sua VM terá acesso ao Google Cloud pela sua conta. Portanto, ao final do laboratório limpe as suas credenciais no `gcloud` usando o comando

     ```
     gcloud auth revoke nome-do-seu-usuario
     ```

   A lista de usuários registrados no `gcloud` pode ser obtida com o comando

        gcloud auth list

3. Usos simplificados no `gcloud` para realizar algumas tarefas com o Compute Engine (ver <https://cloud.google.com/sdk/gcloud/reference/compute>).

   * Lista de imagens existentes: `gcloud compute images list`
   * Criação de VM com nome `minha-vm-1`: `gcloud compute instances create minha-vm-1`
   * Interrupção e início de VM com nome `minha-vm-1`: `gcloud compute instances start minha-vm-1` (utilize `stop` no lugar de `start` para parar a instância)
   * Iniciar terminal SSH com a VM com nome `minha-vm-1`: `gcloud compute ssh minha-vm-1`


#### Google Cloud Run - PaaS

Nós instalaremos a aplicação de exemplo Python na Google Cloud na usando um serviço PaaS chamado **Cloud Run**.

O exemplo de serviço web python aproveita o exemplo de aplicação teste disponível em: <https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?hl=pt-br>.

No Cloud Run, a aplicação é mantida em um **container**, pode ser desenvolvida em qualquer linguagem e a implantação possui as seguintes características:

* Todo o gerenciamento da infraestrutura fica a cargo da Google Cloud.
* Novas instâncias da aplicação são criadas na Google Cloud de acordo com a quantidade de tráfego e sob demanda.
* A cobrança é feita:
  1. Por número de acessos efetivamente recebidos.
  2. Por [região do Google Cloud Run](https://cloud.google.com/run/docs/locations?hl=pt_BR). Procure usar `us-central1` nos testes.

Cloud Run não é a única plataforma de PaaS da Google, mas as outras são específicas de linguagem e podem ser mais vantajosas dependendo do tráfego aplicado e outras características.

O projeto de exemplo do Google Cloud Run está no projeto github de referência, no diretório `top3-cloud-ufcat/lab1-provedores-modelos/paas-cloud-run`. Baixa uma cópia do projeto usando

```
git clone https://github.com/rcarocha/top3-cloud-ufcat.git
```

ou atualize o seu projeto baixado na outra aula (há algumas alterações) com

```
git pull
```

No diretório `top3-cloud-ufcat/lab1-provedores-modelos/paas-cloud-run`, o projeto pode ser implantado na nuvem usando o comando `gcloud`:

```
gcloud run deploy
```



<!--
https://github.com/GoogleCloudPlatform/python-docs-samples/tree/7d13ba8da63d1ff70ac25b77de529c6587f8f141/run
-->




