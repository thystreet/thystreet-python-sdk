# thystreet.DeviceApi

All URIs are relative to *https://cheffy-api.thystreet.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token**](DeviceApi.md#generate_token) | **GET** /device/generate/{deviceId} | 
[**set_details**](DeviceApi.md#set_details) | **PUT** /device/details | 
[**set_token**](DeviceApi.md#set_token) | **PUT** /device/token | 


# **generate_token**
> generate_token(device_id)



### Example

* Basic Authentication (thystreetAuth):

```python
import time
import thystreet
from thystreet.api import device_api
from pprint import pprint
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

    # example passing only required values which don't have defaults set
    try:
        api_instance.generate_token(device_id)
    except thystreet.ApiException as e:
        print("Exception when calling DeviceApi->generate_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[thystreetAuth](../README.md#thystreetAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generate and set new 6 digit token. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_details**
> set_details(set_device_details_dto)



### Example

* Basic Authentication (thystreetAuth):

```python
import time
import thystreet
from thystreet.api import device_api
from thystreet.model.set_device_details_dto import SetDeviceDetailsDto
from pprint import pprint
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
    set_device_details_dto = SetDeviceDetailsDto(
        device_id="device_id_example",
        tariff=True,
    ) # SetDeviceDetailsDto | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_details(set_device_details_dto)
    except thystreet.ApiException as e:
        print("Exception when calling DeviceApi->set_details: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_device_details_dto** | [**SetDeviceDetailsDto**](SetDeviceDetailsDto.md)|  |

### Return type

void (empty response body)

### Authorization

[thystreetAuth](../README.md#thystreetAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device status has been successfully enabled. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_token**
> set_token(device_token_dto)



### Example

* Basic Authentication (thystreetAuth):

```python
import time
import thystreet
from thystreet.api import device_api
from thystreet.model.device_token_dto import DeviceTokenDto
from pprint import pprint
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
    device_token_dto = DeviceTokenDto(
        device_id="device_id_example",
        token=True,
    ) # DeviceTokenDto | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_token(device_token_dto)
    except thystreet.ApiException as e:
        print("Exception when calling DeviceApi->set_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_token_dto** | [**DeviceTokenDto**](DeviceTokenDto.md)|  |

### Return type

void (empty response body)

### Authorization

[thystreetAuth](../README.md#thystreetAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device status has been successfully enabled. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

