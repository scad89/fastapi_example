import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    DEBUG = os.environ.get("DEBUG")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL')
    RESET_TOKEN = os.environ.get("RESET_TOKEN")
    VERIFICATION_TOKEN = os.environ.get("VERIFICATION_TOKEN")
    # LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    # LOGFILE = "logs/logs.log"
    # LOG_BACKTRACE = True
    # LOG_LEVEL = 'DEBUG'
