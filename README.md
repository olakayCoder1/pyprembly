# Prembly Identitypass PyPI version 

The Python library for the Prembly Identitypass API.The Python library provides easy access to Prembly Identitypass API (Nigeria) from Django, Flask, and other Python apps. It abstracts the complexity involved in direct integration and allows you to make quick calls to the APIs.


## Table of Contents

- [Prembly Identitypass PyPI version](#prembly-identitypass-pypi-version)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Configuration](#configuration)
  - [Documentation](#documentation)


## Install

```console
pip install pyprembly
```
Note: This is currently under active development

## Configuration

To use pyprembly you will need to set the following in your environment variable

PREMBLY_APP_ID="your application id"
PREMBLY_X_API_KEY="your x_app_key id"
PREMBLY_ENVIRONMENT="environment default to test"

Visit [Prembly](https://prembly.com/) to get both app id and x-api-key


## Documentation

The package supports all Prembly Identitypass API endpoints for Nigeria.  For complete information about

To make a simple API call:

```
from pyprembly.verifications import Verification


try:
    Verification().bank_account_verification()
except MissingAuthKeyError as e :
    do something
except MissingRequiredDataError as e:
    do something

``` 

There are only two exceptions that you can encounter while making API.  `MissingAuthKeyError` tells that pyprembly could not find either your APP_ID or X_API_KEY in your environment variable or in class initialization. Class initialization approach:
```
Verification(
    prembly_app_id='your app id',
    prembly_x_api_key='your x api key',
    api_version='v2',
    environment='live'
).bank_account_verification()
``` 
We recommend that you store your app id and x api key in an environment variable as PREMBLY_APP_ID and PREMBLY_X_API_KEY respectively.