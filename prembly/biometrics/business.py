"""
Premby API wrapper.

@author Olanrewaju Kabiru.

"""
from prembly.base import PremblyBase
from prembly.utils import create_request_url , image_to_base64
from prembly.exceptions import MissingRequiredDataError

class DataVerification(PremblyBase):

    def email_verification(self , email ):
        """
        Verify an email address
         
        Params:
            email :  email address  
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'email' :email,
        }
        url = self.create_request_url(suburl='/emailage') 
        return self._handle_request('POST', url , data=data)



    def card_bin_verification(self , number ):
        """
        Verify a card BIN (Bank Identification Number) 
         
        Params:
            number :  card bin number  
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'number' :number,
        }
        url = self.create_request_url(suburl='/card_bin') 
        return self._handle_request('POST', url , data=data)



    def vin_verification(self , vin ):
        """
        Verify a VIN/CAR Identification Number 
         
        Params:
            vin :  VIN identification number  
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'vin' :vin,
        }
        url = self.create_request_url(suburl='/vehicle/vin') 
        return self._handle_request('POST', url , data=data)
    


    def verify_company(
        self ,customer_name:str=None, customer_reference:str=None ,
        country_code:str=None , company_number:str=None ):
        """
        Verify a company information
        
        Params:
            customer_name : customer name 
            customer_reference: customer reference  
            country_code: company country code ge NG 
            company_number: company registration number ge RC-000000 e    
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'customer_name' :customer_name,
            'customer_reference' :customer_reference,
            'country_code' :country_code,
            'company_number' :company_number,
        }
        url = self.create_request_url(suburl='/global/company') 
        return self._handle_request('POST', url , data=data) 
    


    def search_with_email(self , email ):
        """
        Verify a company using email
         
        Params:
            email : Company email    
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'email' :email,
        }
        url = self.create_request_url(suburl='/global/company/search_with_email') 
        return self._handle_request('POST', url , data=data)
    



    def search_interpol_ban_list(self , search_mode='NAME' , image = None , name:str=None):
        """
        Search an interpol ban list 
         
        Params:
            search_mode :  IMAGE or NAME default -> NAME  
            image :  Image( if search_mode is IMAGE)  
            name : name (if search_mode is NAME)  
        Returns : 
            Json data from Prembly API.
        """
        data = { 'search_mode': search_mode}
        match search_mode.lower():
            case 'name':
                data.update({'name': name})
            case 'image':
                image = image_to_base64(image)
                data.update({'image': image})
            case _ :
                raise MissingRequiredDataError('Invalid search mode specify')
        url = self.create_request_url(suburl='/vehicle/vin') 
        return self._handle_request('POST', url , data=data)
    



    def search_company(self , country_code,  company_name ):
        """
        Search for a company using email
         
        Params:
            country_code : Company country code eg Ng    
            company_name : The company registration name    
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'country_code' :country_code,
            'company_name' :company_name,
        }
        url = self.create_request_url(suburl='/global/company/search') 
        return self._handle_request('POST', url , data=data)


    def search_with_name(self , country_code:str=None , company_name:str=None ):
        """
        Verify a company using  name
          
        Params:
            country_code : country code eg Nigeria ng
            company_name : company registration name  
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'country_code' :country_code.lower(),
            'company_name' :company_name,
        }
        url = self.create_request_url(suburl='/global/company/search_with_name') 
        return self._handle_request('POST', url , data=data)


    def search_with_string(self , query:str=None , customer_name:str=None, customer_reference:str=None ):
        """
        Verify a company
         
        Params:
            query : Search query
            customer_name : customer name 
            customer_reference: customer reference    
        Returns : 
            Json data from Prembly API.
        """
        data = {
            'query' :query,
            'customer_name' :customer_name,
            'customer_reference' :customer_reference,
        }
        url = self.create_request_url(suburl='/global/company/search_with_string') 
        return self._handle_request('POST', url , data=data)


    