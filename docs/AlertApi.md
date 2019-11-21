# timelight-ai-python-api-client.AlertApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_alert_alert_id_comment_patch**](AlertApi.md#v1_alert_alert_id_comment_patch) | **PATCH** /v1/alert/{alertId}/comment | Add a comment to an alert
[**v1_alert_alert_id_favorite_patch**](AlertApi.md#v1_alert_alert_id_favorite_patch) | **PATCH** /v1/alert/{alertId}/favorite | Set alert favorite for the current user
[**v1_alert_list_get**](AlertApi.md#v1_alert_list_get) | **GET** /v1/alert/list | List alerts data of the selected year, all alerts if no year is provided
[**v1_alert_ref_list_get**](AlertApi.md#v1_alert_ref_list_get) | **GET** /v1/alert/ref/list | List alerts data of the selected year, all alerts if no year is provided


# **v1_alert_alert_id_comment_patch**
> AlertRefDto v1_alert_alert_id_comment_patch(alert_comment_dto, alert_id)

Add a comment to an alert

A commented alert is closed and is moved to the alert referential

### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight-ai-python-api-client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight-ai-python-api-client.AlertApi(timelight-ai-python-api-client.ApiClient(configuration))
alert_comment_dto = timelight-ai-python-api-client.AlertCommentDto() # AlertCommentDto | 
alert_id = 8.14 # float | 

try:
    # Add a comment to an alert
    api_response = api_instance.v1_alert_alert_id_comment_patch(alert_comment_dto, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->v1_alert_alert_id_comment_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_comment_dto** | [**AlertCommentDto**](AlertCommentDto.md)|  | 
 **alert_id** | **float**|  | 

### Return type

[**AlertRefDto**](AlertRefDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alert_alert_id_favorite_patch**
> AlertDto v1_alert_alert_id_favorite_patch(alert_favorite_dto, alert_id)

Set alert favorite for the current user

### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight-ai-python-api-client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight-ai-python-api-client.AlertApi(timelight-ai-python-api-client.ApiClient(configuration))
alert_favorite_dto = timelight-ai-python-api-client.AlertFavoriteDto() # AlertFavoriteDto | 
alert_id = 8.14 # float | 

try:
    # Set alert favorite for the current user
    api_response = api_instance.v1_alert_alert_id_favorite_patch(alert_favorite_dto, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->v1_alert_alert_id_favorite_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_favorite_dto** | [**AlertFavoriteDto**](AlertFavoriteDto.md)|  | 
 **alert_id** | **float**|  | 

### Return type

[**AlertDto**](AlertDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alert_list_get**
> AlertListDto v1_alert_list_get(source_id=source_id, year=year)

List alerts data of the selected year, all alerts if no year is provided

### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight-ai-python-api-client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight-ai-python-api-client.AlertApi(timelight-ai-python-api-client.ApiClient(configuration))
source_id = 8.14 # float |  (optional)
year = 8.14 # float |  (optional)

try:
    # List alerts data of the selected year, all alerts if no year is provided
    api_response = api_instance.v1_alert_list_get(source_id=source_id, year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->v1_alert_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | [optional] 
 **year** | **float**|  | [optional] 

### Return type

[**AlertListDto**](AlertListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alert_ref_list_get**
> AlertRefListDto v1_alert_ref_list_get(source_id=source_id, year=year)

List alerts data of the selected year, all alerts if no year is provided

### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight-ai-python-api-client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight-ai-python-api-client.AlertApi(timelight-ai-python-api-client.ApiClient(configuration))
source_id = 8.14 # float |  (optional)
year = 8.14 # float |  (optional)

try:
    # List alerts data of the selected year, all alerts if no year is provided
    api_response = api_instance.v1_alert_ref_list_get(source_id=source_id, year=year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertApi->v1_alert_ref_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | [optional] 
 **year** | **float**|  | [optional] 

### Return type

[**AlertRefListDto**](AlertRefListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

