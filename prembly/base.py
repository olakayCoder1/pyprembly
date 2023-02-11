from prembly.configuration import  BASE_END_POINT_DICTIONARY
from prembly.exceptions import (
    MissingAuthKeyError , InvalidMethodError
)
import os
import requests
import json


class BaseConfig(object):
    """
    Base class that will be subclass by all other classes 
    """


    _CONTENT_TYPE = "application/json"
    

    def __init__( 
        self, prembly_app_id=None ,  prembly_x_api_key=None , 
        api_version='v1' , environment='sandbox' ):

        
        self._BASE_END_POINT = BASE_END_POINT_DICTIONARY.get( environment  )

        self._API_VERSION = api_version

        self._BASE_END_POINT_VERSION = self._BASE_END_POINT + self._API_VERSION

        print(self._BASE_END_POINT_VERSION)
        if prembly_app_id:
            self._PREMBLY_APP_ID = prembly_app_id
        else:
            self._PREMBLY_APP_ID = os.getenv('PREMBLY_APP_ID', None)

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
            self._PREMBLY_X_API_KEY = os.getenv('PREMBLY_X_API_KEY', None)

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
            "Content-Type": self._CONTENT_TYPE, 
            'x-api-key':  self._PREMBLY_X_API_KEY, 
            'app-id' : self._PREMBLY_APP_ID  
        }


    
    def _handle_request(self, method, url, data=None):
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

        response = request(url, headers=self._headers(), data=payload)
        print(response)
        print(response.status_code)

        return response
        
        # if response.status_code == 404:
        #     return response

        # if response.status_code in [200, 201 , 401 ]:
        #     return response
        # else:
        #     return response
            # body = response.json()
            # return response.status_code, body.get('status'), body.get('message'), body.get('errors')



