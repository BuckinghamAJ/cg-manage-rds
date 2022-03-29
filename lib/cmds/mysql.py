from typing import List
from lib.cmds.utils import run_sync
from lib.cmds.engine import Engine
import click

class MySql(Engine):

    def prerequisites(self) -> None:
        pass

    def backup(self, db_name: str, creds: dict, backup_file: str, options: list=list()) -> None:
        pass

    def restore(self, db_name: str, creds: dict, backup_file: str, options: list=list()) -> None:
        pass

    def credentials(self, service_name: str, key_name: str='key') -> dict:
        pass