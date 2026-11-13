import logging
from pathlib import Path

path = Path('.')


def get_log(__name__) -> logging.Logger:
    log = logging.getLogger(str(path))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    sh = logging.FileHandler(path / f'{__name__}.log')
    sh.setFormatter(formatter)
    log.addHandler(sh)
    log.setLevel(logging.INFO)
    return log
