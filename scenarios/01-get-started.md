# 01 Get Started

Agora que você já tem um controlador minimamente funcional, é importante saber
que antes de criar nossa primeira topologia de rede, precisamos ativar as
aplicações necessárias no controlador, afinal:
> "Se as redes são definias por software. Cadê o software?"

Cada uma das funções de redes convencionais, podem ser descritas através de suas
regras e métodos de funcionamento. Tal como um software é feito.

Dito isso, tenha em mente que cada uma dessas funções pode ser uma aplicação,
que precisa ser ativada. Afinal a graça é justamente usar apenas o que se
precisa, quando se precisa.

## Ativando OpenFlow

Para facilitar o caminho, e nos poupar de um *ClickOps* evitável na UI.
Utilizaremos a CLI para interagir com as apps. As mesmas ações podem ser tomadas
através da CLI, na área da *applications*, caso você prefira o *ClickOps*.

> [!NOTE]
> Caso você tenha optado pelo ClickOps, as apps podem ser localizadas na UI pelo
> mesmo nome que referenciamos aqui.

Presumo que você já saiba como acessar a CLI do ONOS, do contrário as
informações estão [aqui](/README.md#acessando-o-onos-via-ssh-opcional).

```bash Habilita o OpenFlow no ONOS
onos:app activate \
  org.onosproject.openflow-base \
  org.onosproject.openflow-message \
  org.onosproject.openflow \
  org.onosproject.fwd
```

Com a ativação do OpenFlow, já conseguimos provisionar nossos primeiros
recursos, as soluções OVS (Open vSwitch). Altamente flexíveis, podemos
considerá-los a porta de entrada para as redes definidas por software.

A seguir um exemplo de código python, que utiliza o CNETLAB para provisionar
dois dispositivos OVS conectados. Você pode baixar o arquivo e executar em
qualquer lugar da máquina virtual.

> [!TIP]
> Pra quem tem pressa, o comando a seguir executa diretamente o arquivo, sem que
> precise baixá-lo. Mas fique a vontade para acessar o código, acessando a URL
> diretamente.

```bash
curl -fSsl 'https://gist.githubusercontent.com/JoseCarlosNF/702c645103fc9b558664dbaa5c48aec3/raw/ovs_only_topology.py' | python3
```


## Acessando a interface do ONOS

Se tudo correu bem, você deve conseguir acessar a interface do ONOS no endereço
a seguir:

<http://192.168.56.20:8181/onos/ui>

> [!IMPORTANT]
> O IP especificado é da máquina virtual, caso você tenha provisionado o de uma
> forma diferente, infelizmente o guia não cobri esses outros cenários. E se você
> executou o código python sem modificar, possivelmente não funcionou, haja
> vista que para os containers levantados pelo CNETLAB, o endereço do
> controlador não será o `172.17.0.1`.

As **credenciais padrão** para o acesso a interface são as mesmas do acesso via ssh:

```plain Credenciais do onos
User: onos
Password: rocks
```
