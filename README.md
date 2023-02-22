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

The package supports all Prembly Identitypass API endpoints for Nigeria.

The available method of the `Verification` class are as follow:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | cac | _Verify a business using rc_number_|
| 2 | cac_with_name | _Verify a business using rc_number_| 
| 3 | cac_advance | _Verify a business using rc_number : return advance result_| 
| 4 | bvn_number | _Verify a Bank Verification Number (BVN)_| 
| 5 | bvn_with_face | _Verify a Bank Verification Number (BVN) using image and number_| 
| 6 | phone_number | _Verify a Phone Number_| 
| 7 | banks_code | _Get all banks code_| 
| 8 | bank_account | _Verify bank account number_| 
| 9 | advance_bank_account | _Verify bank account number : return advance result_| 
| 10 | bank_account_with_name | _Verify bank account number_| 
| 11 | voters_card_image | _Verify voters card ID image_| 
| 12 | voters_card_lookup | _Verify voters card number_| 
| 13 | basic_drivers_license | _VVerify drivers license_| 
| 14 | advance_drivers_license | _Verify drivers license : return advance result_| 
| 15 | image_drivers_license | _Verify drivers license ID image_| 

| 17 | international_passport | _Verify international passport_| 
| 18 | international_passport_image | _Verify international passport image_| 
| 19 | international_passport_with_face | _Verify international passport image_| 
| 20 | international_passport_async | _Verify international passport in an asynchronous manner_| 
| 21 | credit_bureau | _Verify advance credit details of a user_| 
| 22 | credit_bureau_commercial | _Verify advance credit details of a business_| 
| 23 | credit_bureau_commercial_basic | _Verify basic credit details of a business_| 
| 24 | credit_bureau_statement | _Verify basic credit details of a business_| 

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