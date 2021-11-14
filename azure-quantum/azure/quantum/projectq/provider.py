##
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
##
try:
    import projectq
except ImportError:
    raise ImportError(
    "Missing optional 'projectq' dependencies. \
To install run: pip install azure-quantum[projectq]"
    )

from typing import Union, List, Optional
from azure.quantum import Workspace

from azure.quantum.projectq.job import AzureQuantumJob
from azure.quantum.projectq.backends import *

PROJECTQ_USER_AGENT = "azure-quantum-projectq"


class AzureQuantumProvider:
    def __init__(self, workspace=None, **kwargs):
        self._backends = None
        if workspace is None:
            workspace = Workspace(**kwargs)

        workspace.append_user_agent(PROJECTQ_USER_AGENT)

        self._workspace = workspace

    def get_workspace(self) -> Workspace:
        return self._workspace

    def backends(self, name=None, provider_id=None, **kwargs):
        """Return a list of backends matching the specified filtering.
        Args:
            name (str): name of the backend.
            **kwargs: dict used for filtering.
        Returns:
            list[Backend]: a list of Backends that match the filtering
                criteria.
        """
        pass

    def get_job(self, job_id) -> AzureQuantumJob:
        pass
