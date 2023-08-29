<!--exemplo de scale: https://ubuntu.com/tutorials/install-a-local-kubernetes-with-microk8s#5-host-your-first-service-in-kubernetes

https://microk8s.io/docs/command-reference
https://microk8s.io/docs/working-with-kubectl
https://microk8s.io/docs/addons
-->


<!--- origem

- cenário
- sem kubernetes
- com kubernetes

- o que é possível fazer com kubernetes

- ferramentas
  opensource
  google
  ubuntu
    . vertentes
    
    
- qual usar no experimento

https://kubernetes.io/docs/tutorials/kubernetes-basics/
cenarios


usar o google 
  
  e kubernetes no ubuntu. -->

# Demonstração de Uso de Kubernetes




## Criação de Cluster kubernetes

Como primeiro passo nós criaremos um cluster de 4 VMs que serão nossos nós kubernetes.

## Instalação do microk8s

1. Instalação do microkubernetes - [referência](https://microk8s.io/docs/getting-started):

        sudo snap install microk8s --classic

2. Verifique o status do kubernetes

        sudo microk8s status --wait-ready

   Exemplo de saída:

        microk8s is running
        high-availability: no
        datastore master nodes: 127.0.0.1:19001
        datastore standby nodes: none
        addons:
        enabled:
            dns                  # (core) CoreDNS
            ha-cluster           # (core) Configure high availability on the current node
            helm                 # (core) Helm - the package manager for Kubernetes
            helm3                # (core) Helm 3 - the package manager for Kubernetes
        disabled:
            cert-manager         # (core) Cloud native certificate management
            community            # (core) The community addons repository
            dashboard            # (core) The Kubernetes dashboard
            gpu                  # (core) Automatic enablement of Nvidia CUDA
            host-access          # (core) Allow Pods connecting to Host services smoothly
            hostpath-storage     # (core) Storage class; allocates storage from host directory
            ingress              # (core) Ingress controller for external access
            kube-ovn             # (core) An advanced network fabric for Kubernetes
            mayastor             # (core) OpenEBS MayaStor
            metallb              # (core) Loadbalancer for your Kubernetes cluster
            metrics-server       # (core) K8s Metrics Server for API access to service metrics
            minio                # (core) MinIO object storage
            observability        # (core) A lightweight observability stack for logs, traces and metrics
            prometheus           # (core) Prometheus operator for monitoring and logging
            rbac                 # (core) Role-Based Access Control for authorisation
            registry             # (core) Private image registry exposed on localhost:32000
            storage              # (core) Alias to hostpath-storage add-on, deprecated

3. Acessar e verificar nós e serviços

   * Nós

                sudo microk8s kubectl get nodes
   * Servicos

                sudo microk8s kubectl get services

   Exemplo de saída:

        rcarocha@rcarocha-desk-xps:~$ sudo microk8s kubectl get nodes
        NAME                STATUS   ROLES    AGE     VERSION
        rcarocha-desk-xps   Ready    <none>   2m20s   v1.27.4
        rcarocha@rcarocha-desk-xps:~$ sudo microk8s kubectl get services
        NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
        kubernetes   ClusterIP   10.152.183.1   <none>        443/TCP   2m31s
        
4. Implantar uma aplicação

                sudo microk8s kubectl create deployment nginx --image=nginx

5. Verificar o status após a implantação

                sudo microk8s kubectl get pods

6. Acrescentar extensões pré-existentes (componentes) ao sistema kubernetes

                microk8s enable dns
                microk8s enable hostpath-storage

   Exemplo de saída:

        rcarocha@rcarocha-desk-xps:~$ sudo microk8s enable hostpath-storage
        Infer repository core for addon hostpath-storage
        Enabling default storage class.
        WARNING: Hostpath storage is not suitable for production environments.
                A hostpath volume can grow beyond the size limit set in the volume claim manifest.

        deployment.apps/hostpath-provisioner created
        storageclass.storage.k8s.io/microk8s-hostpath created
        serviceaccount/microk8s-hostpath created
        clusterrole.rbac.authorization.k8s.io/microk8s-hostpath created
        clusterrolebinding.rbac.authorization.k8s.io/microk8s-hostpath created
        Storage will be available soon.
        rcarocha@rcarocha-desk-xps:~$ 


### Criação do Cluster kubernetes

1. Acréscimo dos nós no kubernetes ([referência](https://microk8s.io/docs/clustering))

                sudo microk8s add-node

   Exemplo de saída:

        rcarocha@rcarocha-desk-xps:~$ sudo microk8s add-node
        From the node you wish to join to this cluster, run the following:
        microk8s join 192.168.100.38:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8

        Use the '--worker' flag to join a node as a worker not running the control plane, eg:
        microk8s join 192.168.100.38:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8 --worker

        If the node you are adding is not reachable through the default interface you can use one of the following:
        microk8s join 192.168.100.38:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8
        microk8s join 10.98.9.1:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8
        microk8s join 172.17.0.1:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8
        microk8s join 2804:1e68:c21b:67f3:a937:49c4:e57c:636e:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8
        microk8s join 2804:1e68:c21b:67f3:e2a2:f5ce:7b4c:11cb:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8

   A segunda linha na saída mostra o comando que deve ser executado em um nós para incluí-lo no cluster kubernetes. Em cada nós é necessário, obviamente, instalar o sistema kubernetes.

                sudo snap install microk8s --classic
                sudo microk8s status --wait-ready

   Pode ser necessário permitir o acesso pelo firewall no nó controlador (`sudo ufw allow from 10.0.0.0/8`). Execução do código para participação no cluster. Na saída anterior é (segunda linha da saída)

                sudo microk8s join 192.168.100.38:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8

#### Problema no DNS

Os nós só são reconhecidos se no nó gerente o nome dos nós é resolvido (por DNS) para a estação em questão. Exemplo de problema:

        ubuntu@node-1:~$ sudo microk8s join 192.168.100.38:25000/0629c4a341669bf14b28a474cd120d7f/18d498fbf7b8
        Contacting cluster at 192.168.100.38
        Connection failed. The hostname (node-1) of the joining node does not resolve to the IP "10.98.9.4". Refusing join (400).

O problema é resolvido com a inclusão de uma entrada no arquivo `/etc/hosts`, que deve ser editado com permissões de superusuário (usando `sudo`). Adicione o IP e o nome do nó e use o ping para testar.

O comando `add-nodes` deve ser executado novamente para cada novo nó a ser adicionado. O token utilizado vale apenas para um nó (não pode ser reutilizado). Ao final, deverá aparecer uma saída como

        rcarocha@rcarocha-desk-xps:~$ sudo microk8s kubectl get nodes
        NAME                STATUS   ROLES    AGE    VERSION
        rcarocha-desk-xps   Ready    <none>   56m    v1.27.4
        node-2              Ready    <none>   69s    v1.27.4
        node-1              Ready    <none>   6m6s   v1.27.4
        node-3              Ready    <none>   4s     v1.27.4
        
## Habilitando dashboard

**Atenção**: não utilizaremos esta etapa porque o nó gerente estará no ambiente Google.

Habilite o dashboard no nó gerente ([referência](https://microk8s.io/docs/addon-dashboard))

                sudo microk8s enable dashboard
                sudo microk8s kubectl create deployment dashboard --image=dashboard
                sudo microk8s kubectl get pods

        rcarocha@rcarocha-desk-xps:~$ sudo microk8s kubectl get pods
        NAME                        READY   STATUS             RESTARTS   AGE
        nginx-77b4fdf86c-jbw6v      1/1     Running            0          65m
        dashboard-8546cc4c9-dgmc4   0/1     ImagePullBackOff   0          21s

Habilitando acesso ao dashboard

                sudo microk8s kubectl proxy


## Estrutura de uma Aplicação Containerizada Docker

### Codigo da aplicação

```go
// demo baseado em: https://medium.com/manikkothu/build-and-deploy-apps-on-microk8s-1df26d1ddd3c

package main

import (
  "fmt"
  "net/http"
)

func main() {
  http.HandleFunc("/", func (w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, "Olá, esta é uma mensagem da sua aplicação containerizada")
  })
  http.ListenAndServe(":8080", nil)
}
```

### Dockerfile

```
# DockerfileFROM golang:latest

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go build -o hello-web .
CMD ["/app/hello-web"]
```

### Geração de imagem

                sudo docker build . -t hello-web

                sudo docker images

*As etapas de geração de uma aplicação containerizada estão incompletas para efeito de uso com kubernetes.*

## Implantação (Deployment) de Aplicação Kubernetes

* Imagem: indica onde obter o código da aplicação, que deve ser containerizada

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/


## Escalar (Scaling) uma aplicação

* Referência: <https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/>

* Visualizando os deployments

        kubectl get deployments

  Exemplo de saída:

                NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
                kubernetes-bootcamp   1/1     1            1           11m

* Escalar uma aplicação para utilizar quatro réplicas

                kubectl scale deployments/kubernetes-bootcamp --replicas=4

                <!--

Componentes

components-of-kubernetes.svg

Objects


Arquitetura
Containers
Pods
Deployments

Definir a Escala da Aplicação no Cluster

module_05_scaling1.svg-->
