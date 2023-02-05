from prembly.base import BaseConfig




class EmailVerification(BaseConfig):
    
    def email_verification(self, email : None ):

        if not email : 
            raise TypeError
        return 