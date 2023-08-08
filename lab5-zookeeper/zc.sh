#!/bin.sh 

# Executa Servidor de Zookeeper em cluster com 3 nos informados nos parametros

cd ~ 

wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.0/apache-zookeeper-3.9.0-bin.tar.gz
tar -xzvf apache-zookeeper-3.9.0-bin.tar.gz
cd apache-zookeeper-3.9.0-bin/bin

# cliente
echo Para executar o cliente zookeeper, execute o seguinte comando,
echo onde IP-SERVIDOR deve ser trocado pelo IP do servidor zookeeper.
echo Utilize um dos IPs informados pelo professor.
echo
echo ./zkCli.sh -server IP-SERVIDOR:2181
echo
echo Este comando esta no diretorio
echo ./apache-zookeeper-3.9.0-bin/bin




