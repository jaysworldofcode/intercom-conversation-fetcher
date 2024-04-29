from enum import Enum
from colorama import Fore, init

class MESSAGE_TYPE(Enum):
    ERROR = 1
    MESSAGE = 2
    SUCCESS = 3

def message_logger(message, log_type:MESSAGE_TYPE):
    
    font_color = None
    
    if(log_type == MESSAGE_TYPE.ERROR):
        font_color = Fore.RED

    if(log_type == MESSAGE_TYPE.SUCCESS):
        font_color = Fore.GREEN

    if(log_type == MESSAGE_TYPE.MESSAGE):
        font_color = Fore.YELLOW

    print(font_color+'['+log_type.name+'] '+message+Fore.RESET)