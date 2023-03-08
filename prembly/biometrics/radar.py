# https://radarapi.myidentitypass.com
from prembly.base import PremblyBase


class RadarVerification(PremblyBase):
    """
    
    """
    def _radar_base_endpoint(self):
        return 'https://radarapi.myidentitypass.com/intelligence'
    

    
    def phone_intelligence(self, phone_number):
        """
        Get deep insight about a phone number
        Params:
            phone_number:
        """
        data = {'phone_number':phone_number}
        url = self._radar_base_endpoint() +  '/complete-profile-check'
        return self._handle_request('POST', url , data )
    

    def email_intelligence(self, email):
        """
        Get deep insight about an email
        Params:
            email:
        """

        data = {'email':email}
        url = self._radar_base_endpoint() +  '/complete-profile-check'
        return self._handle_request('POST', url , data )


    def ip_intelligence(self, ip):
        """
        Get deep insight about an IP
        Params:
            ip: This shoul be an IP ex 102.10.21.1
        """

        data = {'ip':ip}
        url = self._radar_base_endpoint() +  '/complete-profile-check'
        return self._handle_request('POST', url , data )

