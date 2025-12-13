# - Check if email ends with '@gmail.com'

class Solution:
    def isGmail(self, email: str) -> bool:
        return email.endswith("@gmail.com")
