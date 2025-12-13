# - Check if password contains uppercase letters

class Solution:
    def hasUpper(self, password: str) -> bool:
        return any(c.isupper() for c in password)
