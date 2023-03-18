from pyprembly.base import PremblyBase


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Sierra Leone
    """

    def voters_card(
        self , 
        search_mode:str='ID', 
        number:str= None , 
        firstname:str=None , 
        lastname:str=None,
        middlename:str=None , 
        dob:str=None
        ):
        """
        Verify user voters card
        
        Params:
            search_mode : mode [ ID or BIO] default ID
            number : ID number [ if search_mode is ID ]
            firstname : user first name[ if search_mode is BIO]
            lastname : user last name[ if search_mode is BIO]
            middlename : user middle name[ if search_mode is BIO]
            dob :  user date of birth[ if search_mode is BIO]
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'search_mode' :search_mode,
            'firstname' :firstname,
            'lastname' :lastname,
            'middlename' :middlename,
            'number' :number,
            'dob': dob ,
        }
        url = self.create_request_url(suburl='/sl/voters') 
        return self._handle_request('POST', url , data=data)


    def drivers_license(
        self , 
        search_mode:str='ID', 
        number:str= None , 
        firstname:str=None , 
        lastname:str=None, 
        dob:str=None
        ):
        """
        Verify user voters card
        
        Params:
            search_mode : mode [ ID or BIO] default ID
            number : ID number [ if search_mode is ID ]
            firstname : user first name[ if search_mode is BIO]
            lastname : user last name[ if search_mode is BIO]
            middlename : user middle name[ if search_mode is BIO]
            dob :  user date of birth[ if search_mode is BIO]
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'search_mode' :search_mode,
            'firstname' :firstname,
            'lastname' :lastname,
            'number' :number,
            'dob': dob ,
        }
        url = self.create_request_url(suburl='/sl/drivers_license') 
        return self._handle_request('POST', url , data=data)

