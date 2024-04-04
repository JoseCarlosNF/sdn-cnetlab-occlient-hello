#!/usr/bin/env python3
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2020 National Network for Education and Research (RNP)        +
#                                                                              +
#     Licensed under the Apache License, Version 2.0 (the "License");          +
#     you may not use this file except in compliance with the License.         +
#     You may obtain a copy of the License at                                  +
#                                                                              +
#         http://www.apache.org/licenses/LICENSE-2.0                           +
#                                                                              +
#     Unless required by applicable law or agreed to in writing, software      +
#     distributed under the License is distributed on an "AS IS" BASIS,        +
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. +
#     See the License for the specific language governing permissions and      +
#     limitations under the License.                                           +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import cnetlab.log as log
from cnetlab.dataplane import Dataplane
from cnetlab.models.switches.whitebox import Whitebox

ONOS_IP = "172.17.0.1"
ONOS_PORT = 6653
CONNECT_DEVICES_ON_CONTROLLER = False


class OVSOnlyTopology(Dataplane):
    def create_nodes(self):
        self.add_node("ovsw1", Whitebox("ovsw1"))
        self.add_node("ovsw2", Whitebox("ovsw2"))

    def create_links(self):
        self.add_link(src="ovsw1", dst="ovsw2")

    def configure_controller(self):
        sw2 = self.get_node("ovsw2")
        sw2.set_controller(ONOS_IP, ONOS_PORT)
        sw1 = self.get_node("ovsw1")
        sw1.set_controller(ONOS_IP, ONOS_PORT)

    def run(self):
        logger.info("Creating Open vSwitches")
        self.create_nodes()

        logger.info("Creating ehternet links")
        self.create_links()

        if CONNECT_DEVICES_ON_CONTROLLER:
            logger.info("Configuring controller on Open vSwitches")
            self.configure_controller()


if __name__ == "__main__":
    logger = log.get_logger(__name__)

    topo = OVSOnlyTopology()

    try:
        logger.info("Starting Network Emulation")
        logger.info("Allocating Elements Resources")
        topo.run()
        while True:
            pass
    except KeyboardInterrupt:
        logger.info("Stopping Network Emulation")
        topo.delete_all()
