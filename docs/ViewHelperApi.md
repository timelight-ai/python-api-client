# timelight_ai_python_api_client.ViewHelperApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_view_helper_alerts_get**](ViewHelperApi.md#v1_view_helper_alerts_get) | **GET** /v1/view-helper/alerts | Get the alert view data
[**v1_view_helper_alerts_ref_get**](ViewHelperApi.md#v1_view_helper_alerts_ref_get) | **GET** /v1/view-helper/alerts-ref | Get the alert referential view data
[**v1_view_helper_days_near_date_source_id_day_date_get**](ViewHelperApi.md#v1_view_helper_days_near_date_source_id_day_date_get) | **GET** /v1/view-helper/days-near-date/{sourceId}/{dayDate} | Get the alert modal view data


# **v1_view_helper_alerts_get**
> v1_view_helper_alerts_get()

Get the alert view data

### Example
```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight_ai_python_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight_ai_python_api_client.ViewHelperApi(timelight_ai_python_api_client.ApiClient(configuration))

try:
    # Get the alert view data
    api_instance.v1_view_helper_alerts_get()
except ApiException as e:
    print("Exception when calling ViewHelperApi->v1_view_helper_alerts_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_view_helper_alerts_ref_get**
> AlertRefResultDto v1_view_helper_alerts_ref_get()

Get the alert referential view data

### Example
```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight_ai_python_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight_ai_python_api_client.ViewHelperApi(timelight_ai_python_api_client.ApiClient(configuration))

try:
    # Get the alert referential view data
    api_response = api_instance.v1_view_helper_alerts_ref_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewHelperApi->v1_view_helper_alerts_ref_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AlertRefResultDto**](AlertRefResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_view_helper_days_near_date_source_id_day_date_get**
> DaysNearDateResultDto v1_view_helper_days_near_date_source_id_day_date_get(day_date, source_id)

Get the alert modal view data

### Example
```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight_ai_python_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight_ai_python_api_client.ViewHelperApi(timelight_ai_python_api_client.ApiClient(configuration))
day_date = 'day_date_example' # str | 
source_id = 8.14 # float | 

try:
    # Get the alert modal view data
    api_response = api_instance.v1_view_helper_days_near_date_source_id_day_date_get(day_date, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewHelperApi->v1_view_helper_days_near_date_source_id_day_date_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **day_date** | **str**|  | 
 **source_id** | **float**|  | 

### Return type

[**DaysNearDateResultDto**](DaysNearDateResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

