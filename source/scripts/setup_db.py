import os
import sys
cwd = os.getcwd()
sys.path.append(cwd)

from source.local_development.db.db_model import *

def setup_db():
    tables = [RentFlat, Metro, Districts, Cities]
    with db:
        db.create_tables(tables)

if __name__ == "__main__":
    setup_db()