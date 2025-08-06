import pathlib
import sqlite3

HERE = pathlib.Path(__file__).absolute().parent
KEYS = HERE / ".keys"
DATA = HERE / ".data"

for directory in (KEYS, DATA):
    if not directory.exists():
        directory.mkdir()

TOKEN = KEYS / "bot_token.key"
if not TOKEN.exists():
    raise FileNotFoundError("Make a new bot_token.key in the .keys directory.")

SQL = HERE / "sql"
DATABASE = DATA / "database.db"
db = sqlite3.connect(DATABASE)

TICKET_KING_ID = 710034409214181396
