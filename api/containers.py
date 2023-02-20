"""Dependency Injection containers to manage configuration."""

from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])


#    github_client = providers.Factory(
#        Github,
#        login_or_token=config.github.auth_token,
#        timeout=config.github.request_timeout,
#    )
