# sdn-cnetlab-occlient-hello

Com o objetivo de introduzir os estudos sobre gerenciamento de um ambiente de redes
definidas por software (SDN) multidomínio, utilizando o projeto ONOS como
controlador, esse repositório é um apanhado geral de passos e conceitos
básicos necessários para a construção de um ambiente de testes simples. 

## :pushpin: Tópicos abordados

Se você chegou até o ponto de querer fazer um laboratório existem duas
possibilidades, você já sabe o que é uma SDN e como ela funciona, ou você é um
dos meus e gosta de aprender na prática. Mas ressalto, existem muito conceitos
e fundamentos que facilitam o entendimento sobre o assunto, então não espere
entender tudo de primeira, a constância é melhor do que os grandes saltos. 

- [ONOS](#onos)
- [OpenRAN](#openran)
- [OCCLIENT](#occlient)

### ONOS

### OpenRAN

### OCCLIENT

## :rocket: Rodando

O ambiente foi pensado para depender o mínimo possível da plataforma onde está
rodando e prover a heterogeneidade de um sistema distribuído, característica
bastante explorada pelas SDNs.

Em todo projeto, a documentação dos passos e abstração foi levada em
consideração. Então não devem ser esperados problemas ao tentar executar esses
mesmo laboratório em alguns ~anos ou~ meses.

Utilizaremos as seguintes ferramentas:

- **[VirtualBox][virtualbox]**: para subir o emulador. Optei por usar em uma VM, pois como é
  necessário instalar alguns componentes diretamente no sistema operacional, e
  a própria manipulação das funções de rede acontecem em nível de kernel, para
  evitar problemas com o ambiente local, preferi usar um ambiente mais
  controlado e que pudesse ser replicado com facilidade.
- **[Docker][docker]**: será instalado tanto na VM quanto na máquina local. Localmente,
  deverá rodar o controlador, e na máquina virtual deverá rodar os dispositivos
  de rede, emulados pelo `cnetlab`.
- **[Vagrant][vagrant]**: será a ferramenta que subirá a VM no VirtualBox, através dela
  toda a configuração necessária para a VM será abstraída, e apenas acessaremos
  a máquina para executar os scripts de emulação dos dispositivos.

### :test_tube: Executando o ambiente

#### ONOS

```
docker run --name oran-onos --rm --network host -d muriloavlis/oran-onos:v2.0.0
```

##### Habilitando ssh no container do onos

```
docker exec -it oran-onos apt update
docker exec -it oran-onos apt install -y ssh
```

##### Acessando o onos via ssh

```
docker exec -it oran-onos ssh -p 8101 onos@localhost

# Senha é `rocks`
```

#### CNETLAB

Operando sob uma máquina virtual, será o componente responsável por emular os
dispositivos de rede.

##### Ligar VM

Durante esse processo, todas as dependências serão instaladas e os projetos
clonados dos repositórios.

```
vagrant up
```

##### Desligar VM

Apenas desligará, sem destruir as configurações e modificações que vieram a ser
feitas.

```
vagrant down
```

##### Destruir VM

**Destruirá completamente a VM**, e todos os seus dados serão perdidos.

```
vagrant destroy --force
```

<!-- Links -->
[virtualbox]: https://www.virtualbox.org/
[docker]: https://www.docker.com/get-started/
[vagrant]: https://www.vagrantup.com/
