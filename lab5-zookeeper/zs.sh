#!/bin.sh 

# Executa Servidor de Zookeeper em cluster com 3 nos informados nos parametros

cd ~ 

SERVER_1=$1
SERVER_2=$2
SERVER_3=$3

sudo apt update
sudo apt install openjdk-11-jre-headless
wget https://dlcdn.apache.org/zookeeper/zookeeper-3.9.0/apache-zookeeper-3.9.0-bin.tar.gz
tar -xzvf apache-zookeeper-3.9.0-bin.tar.gz

VARLIB=~/apache-zookeeper-3.9.0-bin/var/lib/zookeeper/
mkdir -p $VARLIB

printf "\
tickTime=2000\n\
dataDir=$VARLIB\n\
clientPort=2181\n\
initLimit=5\n\
syncLimit=2\n\
server.1=$SERVER_1:2888:3888\n\
server.2=$SERVER_1:2888:3888\n\
server.3=$SERVER_1:2888:3888\n" > ~/apache-zookeeper-3.9.0-bin/conf/zoo.cfg

# standalno para testes locais
# VARLIB=~/apache-zookeeper-3.9.0-bin/var/lib/zookeeper/
# mkdir -p $VARLIB

printf "\
tickTime=2000\n\
dataDir=$VARLIB\n\
clientPort=2181" > ~/apache-zookeeper-3.9.0-bin/conf/zoo.cfg

echo Para executar o servidor zookeeper, execute o seguinte comando
echo
echo ~/apache-zookeeper-3.9.0-bin/zkServer.sh start


# # cliente
# echo Para executar o cliente zookeeper, execute o seguinte comando,
# echo onde IP-SERVIDOR deve ser trocado pelo IP do servidor zookeeper
# echo
# echo ./zkCli.sh -server IP-SERVIDOR:2181




