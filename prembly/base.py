from prembly.configuration import (
    
    PREMBLY_API_VERSION , 
    PREMBLY_APP_ID ,
    PREMBLY_ENVIRONMENT , 
    PREMBLY_X_API_KEY
)
from prembly.exceptions import (
    MissingAuthKeyError , InvalidMethodError
)

import requests
import json


class BaseConfig(object):
    """
    Base class that will be subclass by all other classes 
    """
    _BASE_END_POINT_DICTIONARY =  {
        'live': 'https://api.myidentitypass.com/',
        'test': 'https://sandbox.myidentitypass.com/',
        'sandbox' : "https://sandbox.myidentitypass.com/",
    }

    _API_VERSION = PREMBLY_API_VERSION

    _BASE_END_POINT = _BASE_END_POINT_DICTIONARY.get(
        PREMBLY_ENVIRONMENT , 'test'
    )

    _BASE_END_POINT_VERSION = _BASE_END_POINT + _API_VERSION

    _CONTENT_TYPE = "application/json"
    
    

    if PREMBLY_APP_ID is None:
        raise MissingAuthKeyError(
            """
            We can't find application id in your environment key variable.
            to set :
                PREMBLY_APP_ID="your application id"
            """)

    if PREMBLY_X_API_KEY is None:
        raise MissingAuthKeyError(
            """
            We can't find prembly_x_api_key id in your environment key variable.
            to set :
                PREMBLY_X_API_KEY="your x_app_key id"
            """)


    def _headers(self):
        return {
            "Content-Type": self._CONTENT_TYPE,
            'x-api-key':  PREMBLY_X_API_KEY,
            'app-id' : PREMBLY_APP_ID 
        }

    
    def _handle_request(self, method, url, data=None):

        """
        Generic function to handle all API url calls
        Returns a python tuple of status code, status(bool), message, data
        """
        method_map = {
            'GET': requests.get,
            'POST': requests.post,
            'PUT': requests.put,
            'DELETE': requests.delete
        }

        payload = json.dumps(data) if data else data
        request = method_map.get(method)

        if not request:
            raise InvalidMethodError("Request method not recognized or implemented")

        response = request(url, headers=self._headers(), data=payload)

        if response.status_code == 404:
            return response.status_code, False, "The object request cannot be found", None

        if response.status_code in [200, 201 , 401 ]:
            return response
        else:
            return response
            # body = response.json()
            # return response.status_code, body.get('status'), body.get('message'), body.get('errors')



