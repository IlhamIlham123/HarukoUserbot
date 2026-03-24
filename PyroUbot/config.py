import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7511061771").split()))

API_ID = int(os.getenv("API_ID", "27226978"))

API_HASH = os.getenv("API_HASH", "70ff5e429e0b47471d134344d0185446")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8227163361:AAG8n5-GkydWPPwtX48V5FNSTM5wCfkllOA")

OWNER_ID = int(os.getenv("OWNER_ID", "7511061771"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://dbsatan:dbsatan@cluster0.bbao9oj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1003224777862"))
