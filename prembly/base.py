import requests
import json
from urllib.parse import *
from dotenv import load_dotenv
from prembly.configuration import  PremblyConfiguration
from prembly.exceptions import (
    MissingAuthKeyError , InvalidMethodError , APIConnectionError
)



load_dotenv()


class PremblyBase(object):
    """
    Base class that will be subclass by all other classes 
    """

    _CONTENT_TYPE = "application/json"
    

    def __init__( 
        self, prembly_app_id: str = None , 
        prembly_x_api_key : str = None , 
        api_version: str ='v1' , 
        environment : str ='sandbox', 
        country_code : str = 'NGN' 
        ):

        self._BASE_END_POINT = PremblyConfiguration.BASE_END_POINT_DICTIONARY.get( environment )
        self._API_VERSION = api_version
        self._API_URL_BASE = self._BASE_END_POINT + self._API_VERSION + '/biometrics/merchant/data/verification'


        if prembly_app_id:
            self._PREMBLY_APP_ID = prembly_app_id
        else:
            self._PREMBLY_APP_ID = PremblyConfiguration.PREMBLY_APP_ID  

        if self._PREMBLY_APP_ID is None:
            raise MissingAuthKeyError(
                """
                We can't find application id in your environment key variable.
                to set :
                    PREMBLY_APP_ID="your application id"
                """
            )


        if prembly_app_id:
            self._PREMBLY_X_API_KEY = prembly_x_api_key
        else:
            self._PREMBLY_X_API_KEY = PremblyConfiguration.PREMBLY_X_API_KEY


        if self._PREMBLY_X_API_KEY is None:
            raise MissingAuthKeyError(
                """
                We can't find prembly_x_api_key id in your environment key variable.
                to set :
                    PREMBLY_X_API_KEY="your x_app_key id"
                """
            )



    def _headers(self):

        return {
            "Content-Type": "application/json", 
            'x-api-key':  self._PREMBLY_X_API_KEY, 
            'app-id' : self._PREMBLY_APP_ID  
        }


    
    def create_request_url(self , **kwargs):
        """
        Add query params to the url, the kwargs should include suburl, params eg

        Kwargs:
            suburl  : eg  '/credit_bureau/commercial/basic'\n
            params : eg  {
                'number' : '09082455489',
            }\n
        create_params(url=url , params=json.dumps(params))

        Result : 
            assuming base url is https://sandbox.myidentitypass.com/biometrics/merchant/data/verification
            https://sandbox.myidentitypass.com/biometrics/merchant/data/verification/credit_bureau/commercial/basic?number=09082455489
        """
        suburl = kwargs.get('suburl')
        params = kwargs.get('params')
        if params:
            query_string = urlencode(eval(params))
            return "{}?{}".format(self._API_URL_BASE , suburl,query_string)
        return "{}".format(self._API_URL_BASE , suburl  )


    def _handle_request(self, method, url, data=None):
        """
        Generic function to handle all API url calls
        Args:
            method (TYPE): request method type
            url : request url
            data : request data

        Raises:
            APIConnectionError: When there is issue communicating with Prembly API

        Returns:
            TYPE: Description
        """
        method_dict = {
            'GET': requests.get,
            'POST': requests.post,
        }

        payload = json.dumps(data) if data else data
        request = method_dict.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognized or implemented")

        try:
            response = request(url, headers=self._headers(), data=payload)
        except Exception as e:
            # Would catch just requests.exceptions.RequestException, but can
            # also raise ValueError, RuntimeError, etc.
            self._handle_request_error(e)
        return response
        


    def _handle_request_error(self, e):
        if isinstance(e, requests.exceptions.RequestException):
            msg = ("Unexpected error communicating with Prembly.  "
                   "If this problem persists, let me know at "
                   "programmerolakay@gmail.com.")

        else:  # pragma: no cover
            msg = ("Unexpected error communicating with Prembly. "
                   "It looks like there's probably a configuration "
                   "issue locally.  If this problem persists, let me "
                   "know at programmerolakay@gmail.com.")
        raise APIConnectionError(msg)
        




