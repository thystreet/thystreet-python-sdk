# thystreet.OrderApi

All URIs are relative to *https://cheffy-api.thystreet.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_by_id**](OrderApi.md#get_order_by_id) | **GET** /order/params/{orderToken} | 
[**set_status**](OrderApi.md#set_status) | **PUT** /order/status | 


# **get_order_by_id**
> get_order_by_id(order_token)



### Example

* Basic Authentication (thystreetAuth):

```python
import time
import thystreet
from thystreet.api import order_api
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
    api_instance = order_api.OrderApi(api_client)
    order_token = "orderToken_example" # str | This is the id recieved from the qrcode

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_order_by_id(order_token)
    except thystreet.ApiException as e:
        print("Exception when calling OrderApi->get_order_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_token** | **str**| This is the id recieved from the qrcode |

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
**200** | Returns order information for the given id |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_status**
> set_status(order_status_dto)



### Example

* Basic Authentication (thystreetAuth):

```python
import time
import thystreet
from thystreet.api import order_api
from thystreet.model.order_status_dto import OrderStatusDto
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
    api_instance = order_api.OrderApi(api_client)
    order_status_dto = OrderStatusDto(
        order_id="order_id_example",
        status="CONFIRMED",
    ) # OrderStatusDto | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_status(order_status_dto)
    except thystreet.ApiException as e:
        print("Exception when calling OrderApi->set_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_status_dto** | [**OrderStatusDto**](OrderStatusDto.md)|  |

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
**200** | Updates order status. |  -  |
**401** | Unauthorized. |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

