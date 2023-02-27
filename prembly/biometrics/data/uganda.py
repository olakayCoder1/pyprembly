from prembly.base import PremblyBase
from prembly.utils import create_request_url


class DataVerification(PremblyBase):
    """
    Base class for all IdentityPass API available in Uganda
    """

    def company(
            self, 
            reservation_number:int=None 
            ):

        data = {
            'number' :reservation_number,
        }
        url = self.create_request_url(suburl='/ug/company') 
        return self._handle_request('POST', url , data=data)



