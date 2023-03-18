# Prembly Identitypass PyPI version 

The Python library for the Prembly Identitypass API.The Python library provides easy access to Prembly Identitypass API's from Django, Flask, and other Python apps. It abstracts the complexity involved in direct integration and allows you to make quick calls to the APIs.


## Table of Contents

- [Prembly Identitypass PyPI version](#prembly-identitypass-pypi-version)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Documentation](#documentation)
  - [Getting Started](#getting-started)
    - [Configuration](#configuration)
    - [Country and Available method](#country-and-available-method)
      - [Nigeria](#nigeria)
      - [Ghana](#ghana)
      - [Kenya](#kenya)
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
from prembly.data.nigeria import DataVerification
``` 
Available methods are :

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
| 9 | bank_account_comparison | _Verify bank account number and compare name with customer name_| 
| 10 | all_bank_with_statement | _Get all available banking institution that bank statement can be retrieve_| 
| 11 | advance_bank_account | _Verify bank account number : return advance result_| 
| 12 | bank_account_with_name | _Verify bank account number_| 
| 13 | voters_card_image | _Verify voters card ID image_| 
| 14 | voters_card_lookup | _Verify voters card number_| 
| 15 | basic_drivers_license | _VVerify drivers license_| 
| 16 | advance_drivers_license | _Verify drivers license : return advance result_| 
| 17 | image_drivers_license | _Verify drivers license ID image_| 
| 18 | drivers_license_image | _Verify drivers license ID image_| 
| 19 | international_passport | _Verify international passport_| 
| 20 | international_passport_image | _Verify international passport image_| 
| 21 | international_passport_with_face | _Verify international passport image_| 
| 22 | international_passport_async | _Verify international passport in an asynchronous manner_| 
| 23 | credit_bureau | _Get Credit bureau statement_| 
| 24 | credit_bureau_customer | _Verify advance credit details of a user| 
| 25 | credit_bureau_commercial | _Verify advance credit details of a business_| 
| 26 | credit_bureau_commercial_basic | _Verify basic credit details of a business_| 
| 27 | credit_bureau_statement | _Verify basic credit details of a business_| 
| 28 | nin_slip | _Verify a National Identification Number(NIN) Slip_| 
| 29 | nin_lookup | _Verify a National Identification Number(NIN) with phone number and (NIN) number_| 
| 30 | nin_virtual | _Verify a National Identification Number(NIN) with NIN and virtual number_| 
| 31 | nin_face | _Verify a National Identification Number(NIN) with user's image_| 
| 32 | stamp_duty | _Verify a stamp  duty reference number_| 
| 33 | vehicle_verification | _Verify a vehicle number plate_| 
| 34 | tax_identification_number | _Verify tax identification number_| 


#### Ghana 
```python
from prembly.data.ghana import DataVerification
``` 
Available methods are:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | drivers_license | _Verify user drivers license_|
| 2 | ssnit | _Verify SSNIT_| 
| 3 | voters_card | _Verify voters card_| 
| 4 | international_passport | _Verify user passport_| 

#### Kenya 
```python
from prembly.data.kenya import DataVerification

``` 
Available methods are:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | drivers_license | _Verify user drivers license_|
| 2 | international_passport | _Verify user passport_| 
| 3 | serial_number | _Verify user serial number_| 
| 4 | national_identity_number_new | _Verify user national identity number_| 
| 5 | alien_id | _Verify and authenticate foreign resident_| 

#### Sierra Leone 
```python
from prembly.data.sierra_leone import DataVerification
``` 
Available methods are:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | drivers_license | _Verify user drivers license_|
| 2 | voters_card | _Verify voters card_| 


#### South Africa 
```python
from prembly.data.south_africa import DataVerification
``` 
Available methods are:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | national_id | _Verify user national id card_|
| 2 | company | _Verify a business_|


#### Uganda 
```python
from prembly.data.uganda import DataVerification
``` 
Available methods are:

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | company | _Verify a business_|

### Global 
```python
from prembly.business import DataVerification
``` 

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | search_with_email | _Verify a company using email_|
| 2 | search_with_name | _Verify a company using  name_| 
| 3 | search_with_string | _Verify a company_| 
| 4 | search_interpol_ban_list | _Search an interpol ban list_|
| 5 | search_company | _Search for a company using email_|
| 6 | verify_company | _Verify a company information_|
| 7 | vin_verification | _Verify a VIN/CAR Identification Number_|
| 8 | card_bin_verification | _Verify a card BIN (Bank Identification Number)_|
| 9 | email_verification | _Verify an email address_|



### FACE VALIDATION 
```python
from prembly.face import DataVerification
``` 

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | age_and_gender | _Get the age range and gender of a person in an image_|
| 2 | comparison | _Compare two face images_| 
| 3 | enrollment | _Enroll user_| 
| 4 | authentication | _Authenticate user using face_| 
| 5 | face_id | _Verify user identity user  against their registered image using their id card(Voters card, National ID, Card etc)_| 
| 6 | liveliness_check | _Authenticate user with liveliness check on face_| 

### RADAR
```python
from prembly.radar import DataVerification
``` 

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | phone_intelligence | _Get deep insight about a phone number_|
| 2 | email_intelligence | _Get deep insight about an email_| 
| 3 | ip_intelligence | _Get deep insight about an IP_|



### DOCUMENT
```python
from prembly.radar import DataVerification
``` 

| SN | METHOD NAME | DESCRIPTION|
| ------- | ----- | ------------- |
| 1 | verify | _Verify document image_|


### Calling Endpoints
To make a simple API call:

```python
from pyprembly.data.nigeria import DataVerification


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



