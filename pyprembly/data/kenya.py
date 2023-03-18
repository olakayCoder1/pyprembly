from pyprembly.base import PremblyBase


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Kenya
    """

    def passport(
            self, 
            number=None , 
            customer_name=None , 
            customer_reference=None
            ):
        """
        Verify user passport
        
        Params:
            number : passport number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """

        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/passport') 
        return self._handle_request('POST', url , data=data)


    def serial_number(
            self ,  
            number=None ,
            customer_name=None , 
            customer_reference=None
            ):
        """
        Verify user serial number
        
        Params:
            number : serial number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/serial_number') 
        return self._handle_request('POST', url , data=data)
    


    def national_identity_number_new(
            self ,  
            number=None ,
            customer_name=None , 
            customer_reference=None
            ):
        """
        Verify national identity number
        
        Params:
            number : NATIONAL ID
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/national_id/new') 
        return self._handle_request('POST', url , data=data)



    def drivers_license(
            self ,  
            number=None ,
            customer_name=None , 
            customer_reference=None
            ):
        """
        Verify user drivers license
        
        Params:
            number : license number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/drivers_license') 
        return self._handle_request('POST', url , data=data)


    def alien_id(
            self ,  
            number=None ,
            customer_name=None , 
            customer_reference=None
            ):
        """
        Verify and authenticate foreign resident 
        
        Params:
            number : customer number
            customer_name : Customer name
            customer_reference : Customer reference
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
            'customer_name': customer_name ,
            'customer_reference': customer_reference
        }
        url = self.create_request_url(suburl='/ke/alien_id') 
        return self._handle_request('POST', url , data=data)