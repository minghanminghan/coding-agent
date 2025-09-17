import logging
from dotenv import dotenv_values
env = dotenv_values()

ENVIRONMENT = env.get("ENVIRONMENT")
if ENVIRONMENT is None:
    raise ValueError("ENVIRONMENT variable not set in .env file")

if ENVIRONMENT == "dev":
    logLevel = logging.DEBUG
else:
    logLevel = logging.INFO
logger = logging.Logger("coding-agent", level=logLevel)