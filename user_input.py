def get_text(message: str) -> str:
    """
    str:param message: Message to send the user
    str:return: Input from the user
    """
    clear_terminal()
    return input(message+"\n")


def get_int(message: str) -> int:
    """
    str:param message: Message to send the user
    str:return: Input from the user as an int
    """
    is_int = False

    while not is_int:
        try:
            clear_terminal()
            i = int(input(message+"\n"))
            return i
        except:
            pass

def get_int_positiv(message: str) -> int:
    """
    str:param message: Message to send the user
    str:return: Input from the user as an int
    """
    is_int = False

    while not is_int:
        try:
            clear_terminal()
            i = int(input(message+"\n"))
            if i >= 0:
                return i
        except:
            pass

def get_int_in_range(message: str, min:int, max:int) -> int:
    """
    str:param message: Message to send the user
    int:param min: Min input from user
    int:param max: Max input from user
    str:return: Input from the user as an int in between range
    """
    is_int = False

    while not is_int:
        try:
            clear_terminal()
            print("Min: " + str(min) + " | Max: " + str(max))
            i = int(input(message+"\n"))
            if min <= i <= max:
                return i
        except:
            pass

def get_float(message: str) -> float:
    """
    str:param message: Message to send the user
    str:return: Input from the user as a float
    """
    is_int = False

    while not is_int:
        try:
            clear_terminal()
            i = float(input(message+"\n"))
            return i
        except:
            pass

def get_boolean(message: str) -> bool:
    """
    str:param message: Message to send the user
    str:return: Input from the user as a float
    """
    is_int = False

    while not is_int:
        try:
            clear_terminal()
            print("Input should be TRUE or FALSE")
            i = input(message+"\n")
            if i.lower() == "true" or i.lower() == "yes":
                return True
            elif i.lower() == "false" or i.lower() == "no":
                return False
        except:
            pass

def clear_terminal():
    print("\n"*100)