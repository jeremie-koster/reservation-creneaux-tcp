"""
    This class implements the interface and concrete classes to get user credentials to connect to TCP website (Strategy Pattern).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import os

import yaml



class CredentialsFetcher(ABC):
    def __init__(self) -> None:
        self.login, self.password = self._get_credentials()

    @abstractmethod
    def _get_credentials(self, input_data=None):
        pass

    @property
    def user_login(self):
        return self.login
    
    @property
    def user_password(self):
        return self.password


class LocalCredentialsFetcher(CredentialsFetcher):
    directory_path = os.path.dirname(os.path.realpath(__file__))
    credentials_file_path = os.path.join(directory_path,"../configuration/credentials.yml")
    
    def __init__(self, file_path: str = credentials_file_path) -> None:
        self.file_path = file_path
        super().__init__()

    def _get_credentials(self, file_path: str = None):
        if file_path is None:
            file_path = self.file_path
        return self._get_local_credentials(file_path)

    def _get_local_credentials(self, file_path: str) -> (str, str):
        with open(file_path, "r") as stream:
            try:
                credentials = yaml.safe_load(stream)
                return credentials["user"], credentials["password"]
            except yaml.YAMLError as exc:
                print(exc)


class GcpCredentialsFetcher(CredentialsFetcher):
    def _get_credentials(self):
        pass
