import logging
import os

logger = logging.Logger(__name__)

number = os.getenv('NUMB', '')

if not number:
    logger.warning('ERROR!')

else:
    num = list(map(int, number.split(',')))
    logger.warning('SUM', sum(num))