from pyprembly.base import PremblyBase


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Rwanda Leone
    """

    def national_id( self,number= None ):
        """
        Verify national identity card issued to Rwandan
        
        Params:
            number : national ID number
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
        }
        url = self.create_request_url(suburl='/rwanda/nin') 
        return self._handle_request('POST', url , data=data)


    def passport(self ,number= None ):
        """
        Verify Rwandan passport
        
        Params:
            number : passport number
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
        }
        url = self.create_request_url(suburl='/rwanda/passport') 
        return self._handle_request('POST', url , data=data)

