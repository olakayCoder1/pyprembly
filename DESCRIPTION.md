# Prembly Identitypass 

The Python library for the Prembly Identitypass API.The Python library provides easy access to Prembly Identitypass API's from Django, Flask, and other Python apps. It abstracts the complexity involved in direct integration and allows you to make quick calls to the APIs.


## Table of Contents

- [Prembly Identitypass](#prembly-identitypass)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Documentation](#documentation)
  - [Getting Started](#getting-started)
    - [Configuration](#configuration)
    - [Country and Available method](#country-and-available-method)
      - [Nigeria](#nigeria)
      - [Ghana](#ghana)
      - [Kenya](#kenya)
      - [Rwanda](#rwanda)
      - [Sierra Leone](#sierra-leone)
      - [South Africa](#south-africa)
      - [Uganda](#uganda)
    - [Global](#global)
    - [FACE VALIDATION](#face-validation)
    - [RADAR](#radar)
    - [DOCUMENT](#document)
    - [Calling Endpoints](#calling-endpoints)
    - [Exceptions](#exceptions)
      - [MissingAuthKeyError](#missingauthkeyerror)
      - [MissingRequiredDataError](#missingrequireddataerror)
      - [APIConnectionError](#apiconnectionerror)
      - [InvalidMethodError](#invalidmethoderror)

## Install

```console
pip install pyprembly
```
Note: This is currently under active development

## Documentation
## Getting Started

The package supports all Prembly Identitypass API endpoints for the following countries:
- Nigeria
- Kenya
- Ghana
- Sierra Leone
- South Africa
- Uganda
- Rwanda


### Configuration

To use pyprembly you will need to set the following in your environment variable

```console
PREMBLY_APP_ID="your application id"
PREMBLY_X_API_KEY="your x_app_key id"
PREMBLY_ENVIRONMENT="environment default to test"
```

Visit [Prembly](https://prembly.com/) to get both app id and x-api-key

### Country and Available method 
The available method of the `DataVerification` class are as follow:
#### Nigeria 


```python
from pyprembly.data.nigeria import DataVerification
``` 
#### Ghana 
```python
from pyprembly.data.ghana import DataVerification
``` 
#### Kenya 
```python
from pyprembly.data.kenya import DataVerification

``` 

#### Rwanda 
```python
from pyprembly.data.rwanda import DataVerification

``` 

#### Sierra Leone 
```python
from pyprembly.data.sierra_leone import DataVerification
``` 

#### South Africa 
```python
from pyprembly.data.south_africa import DataVerification
``` 
#### Uganda 
```python
from pyprembly.data.uganda import DataVerification
``` 
### Global 
```python
from pyprembly.business import DataVerification
``` 

### FACE VALIDATION 
```python
from pyprembly.face import DataVerification
```
### RADAR
```python
from pyprembly.radar import DataVerification
``` 


### DOCUMENT
```python
from pyprembly.radar import DataVerification
``` 

### Calling Endpoints
To make a simple API call:

```python
from pypyprembly.data.nigeria import DataVerification

try:
    DataVerification().bank_account_verification()
except MissingAuthKeyError as e :
    do something
except MissingRequiredDataError as e:
    do something
except APIConnectionError as e:
    do something
``` 
In this case you must have store your API keys in an environment variable.Alternatively you can also do

```python
from pyprembly.data.nigeria import DataVerification

DataVerification(
    prembly_app_id='your app id',
    prembly_x_api_key='your x api key',
    api_version='v2',
    environment='live'
).bank_account_verification()
``` 
We recommend that you store your app id and x api key in an environment variable as PREMBLY_APP_ID and PREMBLY_X_API_KEY respectively. 
### Exceptions
There are only three exceptions that you can encounter while making API call. 

#### MissingAuthKeyError
`MissingAuthKeyError` tells that pyprembly could not find either your APP_ID or X_API_KEY in your environment variable or in class initialization. Class initialization approach:

#### MissingRequiredDataError
`MissingRequiredDataError` tells that you do not provide a required data for the current method call.
#### APIConnectionError
`APIConnectionError` tells that there is an issue communicating with Prembly API, it can happen due to poor internet connection or system permission

#### InvalidMethodError
`InvalidMethodError` tells that the method used for  calling the endpoint is not valid



