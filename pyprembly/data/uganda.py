from pyprembly.base import PremblyBase


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



