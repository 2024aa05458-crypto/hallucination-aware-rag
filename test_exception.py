import sys

from src.exception import CustomException
from src.utils.logger import logger


try:

    a = 10
    b = 0

    c = a / b

except Exception as e:

    logger.error(e)

    raise CustomException(e, sys)