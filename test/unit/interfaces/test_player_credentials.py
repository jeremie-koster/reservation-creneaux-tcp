import os
from src.interfaces.player_credentials import LocalCredentialsFetcher



def test_local_credentials_fetcher():
    directory_path = os.path.abspath(os.curdir)
    credentials_file_path = os.path.join(directory_path,"test/unit/data/interfaces/fake_credentials.yml")

    fetcher = LocalCredentialsFetcher(credentials_file_path)

    assert fetcher.user_login == "titi"
    assert fetcher.user_password == "grominet"