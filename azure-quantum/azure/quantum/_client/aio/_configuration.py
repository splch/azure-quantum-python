# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6365, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION


class QuantumClientConfiguration(Configuration):
    """Configuration for QuantumClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param workspace_name: Name of the workspace.
    :type workspace_name: str
    """

    def __init__(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        **kwargs: Any
    ) -> None:
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if resource_group_name is None:
            raise ValueError("Parameter 'resource_group_name' must not be None.")
        if workspace_name is None:
            raise ValueError("Parameter 'workspace_name' must not be None.")
        super(QuantumClientConfiguration, self).__init__(**kwargs)

        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.workspace_name = workspace_name
        kwargs.setdefault('sdk_moniker', 'quantum-client/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
