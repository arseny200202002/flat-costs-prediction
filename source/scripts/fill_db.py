import os
import sys
cwd = os.getcwd()
sys.path.append(cwd)

from source.local_development.db.db_model import *

if __name__ == "__main__":
    with db:
        pass