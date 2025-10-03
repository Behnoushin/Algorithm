# To Lower Case
# - Given a string `s`, return the string after converting every uppercase letter to its lowercase equivalent.  
# - All other characters remain unchanged.  


def toLowerCase(s: str) -> str:
    return s.lower()



#----------------------------------------------
# Without using the ready method

def toLowerCase(s: str) -> str:
    result = []
    for ch in s:
        if 'A' <= ch <= 'Z':     
            result.append(chr(ord(ch) + 32))
        else:
            result.append(ch)     
    return "".join(result)
