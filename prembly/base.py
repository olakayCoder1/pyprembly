from prembly.configuration import  BASE_END_POINT_DICTIONARY
from prembly.exceptions import (
    MissingAuthKeyError , InvalidMethodError
)
import os
import requests
import json
from urllib.parse import *
from prembly.utils import create_request_url




        
class BaseConfig(object):
    """
    Base class that will be subclass by all other classes 
    """

    _CONTENT_TYPE = "application/json"
    


        
    _BASE_END_POINT = BASE_END_POINT_DICTIONARY.get( 'test'  )

    _API_VERSION = 'v1'

    _API_URL_BASE =_BASE_END_POINT +_API_VERSION + '/biometrics/merchant/data/verification'


    _PREMBLY_APP_ID = os.getenv('PREMBLY_APP_ID', None)


    if _PREMBLY_APP_ID is None:
        raise MissingAuthKeyError(
            """
            We can't find application id in your environment key variable.
            to set :
                PREMBLY_APP_ID="your application id"
            """
        )


    _PREMBLY_X_API_KEY = os.getenv('PREMBLY_X_API_KEY', None)


    if _PREMBLY_X_API_KEY is None:
        raise MissingAuthKeyError(
            """
            We can't find prembly_x_api_key id in your environment key variable.
            to set :
                PREMBLY_X_API_KEY="your x_app_key id"
            """
        )


    @classmethod
    def _headers(cls):
        return {
            "Content-Type": "application/json", 
            'x-api-key': cls._PREMBLY_X_API_KEY, 
            'app-id' : cls._PREMBLY_APP_ID  
        }


    @classmethod
    def create_request_url(cls , **kwargs):
        """
        Add query params to the url, the kwargs should include suburl, params eg

        Kwargs:
            suburl  =   '/credit_bureau/commercial/basic'\n
            params =  {
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
            return "{}{}?{}".format(cls._API_URL_BASE , suburl ,query_string)
        return "{}{}".format(cls._API_URL_BASE , suburl  )


    @classmethod
    def _handle_request(cls, method, url, data=None):
        """
        Generic function to handle all API url calls
        Returns a python tuple of status code, status(bool), message, data
        """
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognized or implemented")

        response = request(url, headers=cls._headers(), data=payload)

        return response
        



