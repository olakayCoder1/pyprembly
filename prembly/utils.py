from urllib.parse import *
import base64
import requests
from PIL import Image
import io

def image_to_base64(image_path):
    """
    Convert an image to base64, regardless of whether the image is passed as a URL or file path and regardless of its format

    Params:
         image_path: image location
    """
    if image_path.startswith('http'):
        response = requests.get(image_path)
        image_data = response.content
    else:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    image = Image.open(io.BytesIO(image_data))
    encoded_string = base64.b64encode(image.tobytes())

    return encoded_string



def create_request_url(**kwargs):
    """
    Add query params to the url, the kwargs should include url, params eg
    suburl  =   'https://www.google.com/search'\n
    params =  {
        'q' : 'how to add rich text editor in django',
        'ie':'UTF-8',
    }\n
    create_params(suburl=url , params=json.dumps(params))\n
    result : https://www.google.com/search?q=how+to+add+rich+text+editor+in+django&ie=UTF-8
    """
    url = kwargs.get('url')
    params = kwargs.get('params')
    if params:
        query_string = urlencode(eval(params))
        return "{}?{}".format(url,query_string)
    return "{}".format(url)
        


