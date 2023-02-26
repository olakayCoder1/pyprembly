from prembly.base import PremblyBase

class DocumentVerification(PremblyBase):


    def verify(self , doct_country:str=None, doc_type:str=None , doc_image:str=None):
        """
        Verify document image
        
        Params:
            doct_country : Document country code 
            doc_type : Document type - Passport(PP)|Driver's License(DL)|Government Issue Identity Card(ID)|Resident Permit (RP)|Utility Bill(UB) 
            doc_type : Base 64 encoding of document image
        Returns : 
            Json data from Prembly API.
        """

        data = {
            'doct_country': doct_country,
            'doc_image' : doc_image,
            'doc_type':doc_type
        }
        url = self.create_request_url(suburl='/document')
        self._handle_request('Post', url , data)
