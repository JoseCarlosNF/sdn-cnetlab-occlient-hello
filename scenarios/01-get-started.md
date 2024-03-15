# 01 Get Started

Agora que você já tem um ambiente minimamente funcional. Vamos criar nossa
primeira topologia de rede.

Mas primeiro, devemos ter em mente que:
> "Se as redes são definias por software. Cadê o software?"

Cada uma das funções de redes convencionais, podem ser descritas através de suas
regras e métodos de funcionamento. Tal como um software é feito.

Dito isso, tenha em mente que cada uma dessas funções pode ser uma aplicação,
que precisa ser ativada. Afinal a graça é justamente usar apenas o que se
precisa, quando se precisa.

## Ativando OpenFlow via CLI

Para facilitar o caminho, e nos poupar de atualizações na UI. Utilizaremos a CLI
para interagir com as apps. Entretanto, muito provavelmente, as mesmas ações
poderão ser tomadas através da CLI, na área da *applications*.

Presumo que você já saiba como acessar a CLI do ONOS, do contrário as
informações estão [aqui](/README.md#acessando-o-onos-via-ssh-opcional).

```bash Habilita o OpenFlow no ONOS
onos:app activate \
  org.onosproject.openflow-base \
  org.onosproject.openflow-message \
  org.onosproject.openflow \
  org.onosproject.fwd
```

Agora que o OpenFlow está habilitado no controlador, podemos seguir com o
cenário de [provisionamento dos switches e
dispositivos](./02-switches-provisioning.md).
