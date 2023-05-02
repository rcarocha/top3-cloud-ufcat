#!/bin/sh

## Copia do script para a sua VM, considerando que a VM tem nome cloud-test
# multipass transfer gcloud-install.sh cloud-test:.
## Execucao do script
# multipass exec cloud-test source gcloud-install.sh

sudo apt update
sudo apt-get -y install apt-transport-https ca-certificates gnupg
sudo apt-get -y install apt-transport-https ca-certificates gnupg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
sudo apt-get update && sudo apt-get -y install google-cloud-cli
