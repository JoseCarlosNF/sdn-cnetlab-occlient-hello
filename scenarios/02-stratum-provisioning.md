# 02 Provisioning stratum switch

Na primeira parte do guia provisionamos dois switches com o Open vSwitch, que é
uma abordagem virtualizada para switches multicamadas.

Agora vamos dar mais um passo nas redes definidas por software, emulando
dispositivos que utilizem o stratum como sistema operacional.

> *Enabling the era of next generation SDN*

## Habilitando as aplicações necessárias para o Stratum

Como abordamos no início do guia, cada funcionalidade do ONOS é uma aplicação e
precisa ser instalada ou habilitada.

Para o nosso caso, precisaremos apenas habilitar a aplicação. A seguir temos o
comando para ativação das aplicações necessárias para usar switches que rodem
stratum.

### Buscando apps stratum

Para visualizar o status atual das apps, podemos buscar pelas apps que precisam
ser ativadas, com o comando a seguir:

```bash Buscando apps p/ stratum
onos:apps -s | grep '(org.onosproject.drivers.bmv2|org.onosproject.drivers.gnmi|org.onosproject.drivers.gnoi|org.onosproject.drivers.odtn-driver|org.onosproject.drivers.p4runtime|org.onosproject.drivers.stratum|org.onosproject.fwd|org.onosproject.generaldeviceprovider|org.onosproject.hostprovider|org.onosproject.lldpprovider|org.onosproject.pipelines.basic|org.onosproject.pipelines.fabric|org.onosproject.protocols.grpc)'
```

Todas as apps que têm `*` estão ativadas. Entretanto, não há problemas ao
solicitar que sejam ativadas novamente, apenas será identificado que não há ação
para ser tomada.

### Ativando apps stratum

Para ativar as apps, basta executar o comando a seguir:

```bash Ativando apps p/ stratum
onos:app activate \
  org.onosproject.drivers.bmv2 \
  org.onosproject.drivers.gnmi \
  org.onosproject.drivers.gnoi \
  org.onosproject.drivers.odtn-driver \
  org.onosproject.drivers.p4runtime \
  org.onosproject.drivers.stratum \
  org.onosproject.fwd \
  org.onosproject.generaldeviceprovider \
  org.onosproject.hostprovider \
  org.onosproject.lldpprovider \
  org.onosproject.pipelines.basic \
  org.onosproject.pipelines.fabric \
  org.onosproject.protocols.grpc
```

Durante os testes, algumas vezes na primeira tentativa de ativação houve falha.
Porém, ao tentar novamente é possível ativar todas as apps.

## Referências

- [Página do Stratum no site de ONF][onf-stratum]
- [Repositório do Stratum no GitHub][gh-stratum]

<!-- Links -->
[onf-stratum]: https://opennetworking.org/stratum/
[gh-stratum]: https://github.com/stratum/stratum
