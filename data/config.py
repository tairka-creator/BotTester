import os

from dotenv import load_dotenv
from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

load_dotenv()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

QIWI_TOKEN = os.getenv("QIWI_TOKEN")
WALLET_TOKEN = os.getenv("WALLET_QIWI")
QIWI_PUBKEY = os.getenv("QIWI_PUBKEY")
QIWI_SECKEY = os.getenv("QIWI_SECKEY")
