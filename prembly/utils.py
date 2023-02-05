from urllib.parse import *
import json


def create_params(**kwargs):
    """
    Add query params to the url, the kwargs should include url, params eg
    url  =   'https://www.google.com/search'\n
    params =  {
        'q' : 'how to add rich text editor in django',
        'ie':'UTF-8',
    }\n
    create_params(url=url , params=json.dumps(params))\n
    result : https://www.google.com/search?q=how+to+add+rich+text+editor+in+django&ie=UTF-8
    """
    url = kwargs.get('url')
    params = kwargs.get('params')
    if params:
        query_string = urlencode(eval(params))
    return "{}?{}".format(url,query_string)
