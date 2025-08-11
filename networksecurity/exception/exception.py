import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    """Base class for all exceptions in the Network Security module."""
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return f"Error occurred in script: [{self.filename}] at line number: [{self.lineno}] with message: [{self.error_message}]"
if __name__ == "__main__":
    try:
        logger.logging.info("enter the try block")
        a = 1 / 0  # Example to raise an exception
        print(a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)