from prembly.configuration import (
    
    PREMBLY_API_VERSION , 
    PREMBLY_APP_ID ,
    PREMBLY_ENVIRONMENT , 
    PREMBLY_X_API_KEY
)
from prembly.exceptions import (
    MissingAuthKeyError
)




class BaseConfig(object):
    """
    Base class that will be subclass by all other classes 
    """
    _BASE_END_POINT_DICTIONARY =  {
        'live': 'https://api.myidentitypass.com',
        'test': 'https://sandbox.myidentitypass.com',
        'sandbox' : "https://sandbox.myidentitypass.com",
    }

    _API_VERSION = 'v1'

    _BASE_END_POINT = _BASE_END_POINT_DICTIONARY.get(
        PREMBLY_ENVIRONMENT , 'test'
    )

    _CONTENT_TYPE = "application/json"
    
    
    def __init__(self , api_version: str =  None ):


        if isinstance(api_version , int ):
            message = 'api_version should be of type string i.e v1 or v2 .....'
            raise TypeError(message)
        else:
            self._API_VERSION = api_version



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

    


m = BaseConfig()



