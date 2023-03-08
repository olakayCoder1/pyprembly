from urllib.parse import *
import base64
import requests
from PIL import Image
import io
import json
from cryptography.hazmat.primitives.asymmetric import padding , rsa
from cryptography.hazmat.primitives import serialization , hashes
import binascii






def image_to_base64(image_path):
    """
    Convert an image to base64, regardless of whether 
    the image is passed as a URL or file path and regardless of its format

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






def is_base64_image(image):
    """
    Check if image is in base64 format if not convert it to base64
    """
    try:
        # check if image is already in base64 format
        base64.b64decode(image)
        return image
    except binascii.Error:
        # if image is not in base64 format, try to encode it
        return None
    except :
        return image_to_base64(image)




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
        



def encrypt_info(data):
    #  Generate a new RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    #  Get the public key in PEM format
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Define the message to encrypt
    if isinstance(data, dict):
        message = data
    else:
        return None
    # message = {
    #     'username': '',
    #     'password' : '',
    #     'auth_method':'internet_banking',
    #     'institution': ''
    # }
    # Convert the message to byte and serialize as JSON
    message_bytes = json.dumps(message).encode()

    # Encrypt the message to bytes and serialize as JSON
    ciphertext = public_key.encrypt(
        message_bytes,
        padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
        )
    )

    return ciphertext

