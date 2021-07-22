# thystreet
Thy Street APIs are completely RESTful and all our responses are returned in JSON.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://thystreet.com/support](https://thystreet.com/support)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import thystreet
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import thystreet
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import thystreet
from pprint import pprint
from thystreet.api import device_api
from thystreet.model.device_status_dto import DeviceStatusDto
from thystreet.model.device_token_dto import DeviceTokenDto
# Defining the host is optional and defaults to https://cheffy-api.thystreet.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = thystreet.Configuration(
    host = "https://cheffy-api.thystreet.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: thystreetAuth
configuration = thystreet.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with thystreet.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = device_api.DeviceApi(api_client)
    device_id = "deviceId_example" # str | 

    try:
        api_instance.generate_token(device_id)
    except thystreet.ApiException as e:
        print("Exception when calling DeviceApi->generate_token: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://cheffy-api.thystreet.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceApi* | [**generate_token**](docs/DeviceApi.md#generate_token) | **GET** /device/generate/{deviceId} | 
*DeviceApi* | [**set_device_token**](docs/DeviceApi.md#set_device_token) | **PUT** /device/token | 
*DeviceApi* | [**set_status**](docs/DeviceApi.md#set_status) | **PUT** /device/status | 
*OrderApi* | [**set_status**](docs/OrderApi.md#set_status) | **PUT** /order/status | 


## Documentation For Models

 - [DeviceStatusDto](docs/DeviceStatusDto.md)
 - [DeviceTokenDto](docs/DeviceTokenDto.md)
 - [OrderStatusDto](docs/OrderStatusDto.md)


## Documentation For Authorization


## thystreetAuth

- **Type**: HTTP basic authentication


## Author

support@thystreet.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in thystreet.apis and thystreet.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from thystreet.api.default_api import DefaultApi`
- `from thystreet.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import thystreet
from thystreet.apis import *
from thystreet.models import *
```

