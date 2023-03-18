from dotenv import load_dotenv
load_dotenv()
import os



class PremblyConfiguration:
    """
    Global variables configuration
    """
    # Application id gotten from prembly website
    PREMBLY_APP_ID = os.getenv('PREMBLY_APP_ID', None)
    # Application secret key from prembly website
    PREMBLY_X_API_KEY = os.getenv('PREMBLY_X_API_KEY', None)
    # Api version to be used
    PREMBLY_API_VERSION = os.getenv('PREMBLY_API_VERSION', 'v1')
    # Environment type this can be either live or test  or sandbox
    PREMBLY_ENVIRONMENT = os.getenv('PREMBLY_ENVIRONMENT' , 'test')


    BASE_END_POINT_DICTIONARY =  {
            'live': 'https://api.myidentitypass.com',
            'test': 'https://sandbox.myidentitypass.com',
            'sandbox' : "https://sandbox.myidentitypass.com",
        }


