import sys
from src.logger import logging


def error_msg_detail(error, error_detail:sys) -> str:
    """Custom Error Message"""
    
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    detail_message = f"Error occured in python script name [{filename}], line number [{exc_tb.tb_lineno}], error  message [{str(error)}]"
    
    return detail_message


class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_message = error_msg_detail(error=error_msg, error_detail=error_detail)
        
    
    def __str__(self) -> str:
        return self.error_message



    