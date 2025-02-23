#!/usr/bin/env python


# Copyright (c) 2021 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

###############################################################################
""" BFD class """
from bf_pktpy.library.specs.container import Container
from bf_pktpy.library.specs.templates import BFDTemplate


# =============================================================================


class BFD(Container):
    """BFD class"""

    fields = (
        "version diag sta flags detect_mult len my_discriminator "
        "your_discriminator min_tx_interval min_rx_interval "
        "echo_rx_interval"
    ).split()

    def __init__(self, **kwargs):
        super(BFD, self).__init__(BFDTemplate, **kwargs)


# =============================================================================
