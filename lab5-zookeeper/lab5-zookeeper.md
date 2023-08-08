# Laboratório 5: Zookeeper

## Objetivos

O objetivo deste laboratório é demonstrar a utilização do [Zookeeper](https://zookeeper.apache.org/) como serviço de coordenação para aplicações na nuvem.

## Software

Para auxiliar o laboratório, dois scripts para terminal foram disponibilizados:

* [zc.sh](zc.sh): faz o download do Zookeeper cliente e indica como executá-lo.
* [zs.sh](zs.sh): faz o download do Zookeeper **servidor** e indica como executá-lo. Este script será executado pelo professor.

## Atividades

Nós criaremos três servidores Zookeeper e cada aluno irá acessar um dos servidores conforme indicado pelo professor. O laboratório consiste em realizar atualizações e consultas no Zookeeper e verificar a sincronização entre as réplicas do servidor.

Os alunos devem utilizar os seguintes servidores, cujo IP será informado durante a aula.

| Servidor 1 | Servidor 2 | Servidor 3 |
|------------|------------|------------|
| BRUNO      | GUSTAVO    | MARCIO     |
| DANILO     | HUGO       | MARCOS     |
| EDUARDA    | IAN        | MATEUS     |
| EDUARDO    | JEAN       | MIGUEL     |
| EMILY      | JESSYCA    | NILSON     |
| ENZO       | JOÃO       | PHELIPE    |
| ERNESTO    | JULIA      | RAFAEL     |
| EZEQUIEL   | LUAN       | RENAM      |
| GABRIEL    | LUIZ       | SAMUEL     |
| GIOVANNI   |            | WELESON    |

### Comandos Zookeeper

Utilizaremos os seguintes comandos no laboratório, aqui indicados como utilizando o caminho `/teste` e armazenando conteúdo `conteudo-de-teste`

* `create /teste conteudo-de-teste`: cria um novo znode
* `get /teste`: retorna o dado armazenado no znode
* `getAllChildrenNumber /teste`: retorna o número de filhos do znode
* `ls /teste`: mostra os filhos do znode
* `set /teste novo-conteudo-de-teste`: modifica o conteúdo no znode
* `sync /teste`: força e indica status de sincronização do znode

### Tarefas

1. Baixe o código do script para instalar o Zookeeper cliente em [zc.sh](zc.sh) - necessariamente em terminal Linux.
1. Execute o script `zc.sh`.
1. Execute o Zookeeper cliente informando o IP do servidor para você aluno (indicado na tabela acima).
1. Crie um znode em `/alunos` com o seu nome completo (coloque entre aspas) e coloque no conteúdo o endereço IP da sua estação.
2. Verifique a criação no seu znode utilizando `ls`
3. Navegue nos znodes criados, indicando os alunos que já acrescentaram seus znodes. Veja o conteúdo de cada znode filho de `/alunos`.
4. Siga a instrução do professor para o teste de coordenação e tolerância a falhas.

Essa atividade será cobrada e posteriormente verificada pelo professor, valendo pontuação.

