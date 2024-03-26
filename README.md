# sdn-cnetlab-occlient-hello

Com o objetivo de introduzir os estudos sobre gerenciamento de um ambiente de
redes definidas por software (SDN) multidomínio, utilizando o projeto ONOS como
controlador, esse repositório é um apanhado geral de passos e conceitos básicos
necessários para a construção de um ambiente de testes simples.

## :pushpin: Tópicos abordados

Se você chegou até o ponto de querer fazer um laboratório existem duas
possibilidades, você já sabe o que é uma SDN e como ela funciona, ou você é um
dos meus e gosta de aprender na prática. Mas ressalto, existem muito conceitos e
fundamentos que facilitam o entendimento sobre o assunto, então não espere
entender tudo de primeira, a constância é melhor do que os grandes saltos.

- [ONOS](#onos)
- [OpenRAN](#openran)
- [OCCLIENT](#occlient)

### ONOS

Controlador SDN, atualmente o mais aceito quando a abordagem é open-source.

### OpenRAN

Abordagem aberta para redes via rádio. Alguns exemplos são as redes de telefonia
celular.

### OCCLIENT

CLI proposta para manutençã e configuração de ambientes multidomínio,
controlados pelo ONOS.

## :rocket: Rodando

O ambiente foi pensado para depender o mínimo possível da plataforma onde está
rodando e prover a heterogeneidade de um sistema distribuído, característica
bastante explorada pelas SDNs.

Em todo projeto, a documentação dos passos e abstração foi levada em
consideração. Então não devem ser esperados problemas ao tentar executar esses
mesmo laboratório em alguns ~anos ou~ meses.

Utilizaremos as seguintes ferramentas:

- **[VirtualBox][virtualbox]**: para subir o emulador. Optei por usar em uma VM,
pois como é necessário instalar alguns componentes diretamente no sistema
operacional, e a própria manipulação das funções de rede acontecem em nível de
kernel, para evitar problemas com o ambiente local, preferi usar um ambiente
mais controlado e que pudesse ser replicado com facilidade.

- **[Docker][docker]**: será instalado tanto na VM quanto na máquina local.
Localmente, deverá rodar o controlador, e na máquina virtual deverá rodar os
dispositivos de rede, emulados pelo `cnetlab`.

- **[Vagrant][vagrant]**: será a ferramenta que subirá a VM no VirtualBox,
através dela toda a configuração necessária para a VM será abstraída, e apenas
acessaremos a máquina para executar os scripts de emulação dos dispositivos.

### :test_tube: Executando o ambiente

Para ter um ambiente minimamente viável, com um controlador `onos` e alguns
dispositivos sendo emulados pelo `cnetlab`. Você pode executar os seguintes
passos:

#### Executando o ONOS

Existem pelo menos duas formas de executar os testes propostos. Você pode subir
uma instância do ONOS controller manualmente, ativando as aplicações necessárias
para o seu teste (exige mais conhecimento sobre os componentes). Ou utilizando
a máquina virtual declarada com o vagrant (mais fácil, um ambiente built-in com
tudo que você precisa).

```bash Executar container do ONOS
docker run --name oran-onos --rm --network host -d muriloavlis/oran-onos:v2.0.0
```

##### Acessando o ONOS via SSH (Opcional)

Essa é uma dica para os amantes de terminal e CLIs, como eu. Devemos lembrar que
a abordagem de software pressupõe uma arquitetura *API First*. Logo, a maioria
das ações que podem ser tomadas via interface, também poderão ser feitas via
CLI, algo mais prático para algumas pessoas.

Para isso, será necessário executar os passos a seguir, para instalar e acessar
o ssh.

```bash Habilitando o SSH
docker exec -it oran-onos apt update
docker exec -it oran-onos apt install -y ssh
```

```bash Acessando via SSH
docker exec -it oran-onos ssh -p 8101 onos@localhost
# A senha é `rocks`
```

#### CNETLAB

Operando **sob uma máquina virtual**, será o componente responsável por emular
os dispositivos de rede.

O processo de provisionamento da máquina virtual consiste na obtenção da imagem
base (`Ubuntu 20.4 LTS`) e instalação das dependências e clone dos repositórios.

##### Comandos básicos do vagrant

Os comandos a seguir ligam, acessam, desligam e destroem a máquina virtual.

```bash Ligar VM
vagrant up
```

```bash Acessar máquina vis SSH
vagrant ssh
```

```bash Desligar VM
vagrant down
```

```bash Destruir VM
vagrant destroy --force
```

*[Repositório do CNETLAB][cnetlab]*

<!-- Links -->
[virtualbox]: https://www.virtualbox.org/
[docker]: https://www.docker.com/get-started/
[vagrant]: https://www.vagrantup.com/
[cnetlab]: https://git.rnp.br/cnar/sdn-multicamada/emulacao/emulador-optico.git
