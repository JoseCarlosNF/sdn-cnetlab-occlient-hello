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

Para ter um ambiente minimamente viável, você precisa de um controlador `onos` e
alguns dispositivos sendo emulados pelo `cnetlab`.

Existem pelo menos duas formas de provisionar esses componentes. Você pode subir
uma instância do ONOS controller manualmente, ativando as aplicações necessárias
para o seu laboratório (exige mais conhecimento sobre os componentes). Ou
utilizando os cenários já descritos no CNETLAB. Nesse caso, o controlador será
provisionado pelo próprio CNETLAB, junto com os demais dispositivos (exige menos
conhecimento sobre os componentes).

> [!TIP]
> **Recomendo que utilize a VM**, inclusive para provisionar o ONOS manualmente.
> Por ser um ambiente isolado da máquina local, tende a ter um comportamento
> de mais fácil replicação, uma vez que o estado base pode ser retomado a
> qualquer momento, destruindo e provisionando o ambiente novamente.

#### Provisionamento da Máquina Virtual

O processo de provisionamento da máquina virtual consiste na obtenção da imagem
base (`Ubuntu 20.4 LTS`) e instalação das dependências e clone dos repositórios.
Todos esses passos são abstraídos pela utilização do vagrant.

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

#### Executando o ONOS

Utilizado quando estamos subindo o controlador manualmente.

```bash Executar container do ONOS
docker run --name oran-onos --rm --network host -d muriloavlis/oran-onos:v2.0.0
```

Através do comando a seguir você pode obter os logs gerados pelo controlador.
Não deve ser uma preocupação no início, mas vou deixar na página inicial pra
facilitar uma consulta posterior.

```bash Obtendo os logs do controlador
docker logs -f oran-onos
```

##### Acessando o ONOS via SSH (Opcional)

Essa é uma dica para os amantes de terminal e CLIs, como eu. Devemos lembrar que
a abordagem de software pressupõe uma arquitetura *API First*. Logo, a maioria
das ações que podem ser tomadas através de uma interface mais programática, como
uma CLI, ou mesmo o `occlient`.

Como estamos em um ambiente mais controlado, podemos acessar o controlador
diretamente, via ssh. Para instalar e acessar o ssh no container do controlador,
basta executar os comandos a seguir:

```bash Habilitando o SSH
docker exec -it oran-onos apt update
docker exec -it oran-onos apt install -y ssh
```

```bash Acessando via SSH
docker exec -it oran-onos ssh -p 8101 onos@localhost
# A senha é `rocks`
```

#### CNETLAB

Será o componente responsável por emular os dispositivos de rede.

*[Repositório do CNETLAB][cnetlab]*

<!-- Links -->
[virtualbox]: https://www.virtualbox.org/
[docker]: https://www.docker.com/get-started/
[vagrant]: https://www.vagrantup.com/
[cnetlab]: https://git.rnp.br/cnar/sdn-multicamada/emulacao/emulador-optico.git
