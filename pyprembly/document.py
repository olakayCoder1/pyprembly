from pyprembly.base import PremblyBase
from pyprembly.utils import image_to_base64



class DataVerification(PremblyBase):


    def verify(
            self ,
            doc_image, 
            doct_country:str=None, 
            doc_type:str=None ,
            ):
        """
        Verify document image
        
        Params:
            doct_country : Document country code 
            doc_type : Document type - Passport(PP)|Driver's License(DL)|Government Issue Identity Card(ID)|Resident Permit (RP)|Utility Bill(UB) 
            doc_image : document image
        Returns : 
            Json data from Prembly API.
        """
        if doc_image:
            doc_image = image_to_base64(doc_image) 
        data = {
            'doct_country': doct_country,
            'doc_image' : doc_image,
            'doc_type':doc_type
        }
        url = self.create_request_url(suburl='/document')
        self._handle_request('Post', url , data)
