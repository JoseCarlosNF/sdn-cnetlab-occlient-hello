# 03 Provisioning cassini transponders

Seguindo na nossa jornada nas redes definidas por software, chegamos ao domínio
tecnológico óptico. No nosso caso, os transponders cassini.

Utilizando o stratum como SO, são componentes essenciais para redes de alta
performance.

## Habilitando apps necessárias para transponders cassini

Nesse ponto é esperado que você saiba por que estamos executando os comandos a
seguir.

### Buscando apps para cassini

Como o comando a seguir podemos checar o status dos apps necessários para o
ingresso de transponders cassini.

```bash Buscando apps
onos:apps -s | grep '(org.onosproject.drivers.netconf|org.onosproject.drivers.odtn-driver|org.onosproject.drivers.optical|org.onosproject.fwd|org.onosproject.generaldeviceprovider|org.onosproject.gui2|org.onosproject.hostprovider|org.onosproject.models.ietf|org.onosproject.models.openconfig|org.onosproject.models.openconfig-odtn|org.onosproject.models.tapi|org.onosproject.netcfglinksprovider|org.onosproject.netconf|org.onosproject.odtn-api|org.onosproject.odtn-service|org.onosproject.optical-model|org.onosproject.optical-rest|org.onosproject.protocols.restconfserver|org.onosproject.restconf|org.onosproject.restsb|org.onosproject.roadm|org.onosproject.yang)'
```

### Ativando apps para cassini

```bash Ativação de apps para cassini
onos:app activate \
  org.onosproject.drivers.netconf \
  org.onosproject.drivers.odtn-driver \
  org.onosproject.drivers.optical \
  org.onosproject.fwd \
  org.onosproject.generaldeviceprovider \
  org.onosproject.gui2 \
  org.onosproject.hostprovider \
  org.onosproject.models.ietf \
  org.onosproject.models.openconfig \
  org.onosproject.models.openconfig-odtn \
  org.onosproject.models.tapi \
  org.onosproject.netcfglinksprovider \
  org.onosproject.netconf \
  org.onosproject.odtn-api \
  org.onosproject.odtn-service \
  org.onosproject.optical-model \
  org.onosproject.optical-rest \
  org.onosproject.protocols.restconfserver \
  org.onosproject.restconf \
  org.onosproject.restsb \
  org.onosproject.roadm \
  org.onosproject.yang
```

> [!TIP]
> No caso de falha na ativação das apps, tente novamente. Esse foi o
> procedimento adotado durante os tastes.
