import os
from pathlib import Path

class Config:
    
    API_ID = int(os.environ.get('API_ID', 12538392))
    API_HASH = os.environ.get('API_HASH', "a13f6314d9782b0eb18cd0b096247eca")
    BOT_TOKEN = os.environ.get('BOT_TOKEN', "6934973525:AAF4hFgEI9-9JsyE_jJjZN5Tlr5T50rJJoI")
    SESSION_NAME = os.environ.get('SESSION_NAME', "screshbot")
    USER_SESSION_STRING = os.environ.get('USER_SESSION_STRING')
    MIDDLE_MAN = int(os.environ.get('MIDDLE_MAN'))
    LINK_GEN_BOT = os.environ.get('LINK_GEN_BOT')
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL'))
    DATABASE_URL = os.environ.get('mongodb+srv://pulaskitina:alex@#6565@cluster0.ioqv7po.mongodb.net')
    AUTH_USERS = [int(i) for i in os.environ.get('AUTH_USERS', '1464180060').split(' ')]
    
    SCRST_OP_FLDR = Path('screenshots/')
