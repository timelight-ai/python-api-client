# timelight-ai-python-api-client.DayApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_day_bulk_patch**](DayApi.md#v1_day_bulk_patch) | **PATCH** /v1/day/bulk | Update day entities
[**v1_day_list_source_id_year_get**](DayApi.md#v1_day_list_source_id_year_get) | **GET** /v1/day/list/{sourceId}/{year} | List day data of the reference year


# **v1_day_bulk_patch**
> DayListDto v1_day_bulk_patch(days_patch_dto)

Update day entities

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
api_instance = timelight-ai-python-api-client.DayApi(timelight-ai-python-api-client.ApiClient(configuration))
days_patch_dto = timelight-ai-python-api-client.DaysPatchDto() # DaysPatchDto | 

try:
    # Update day entities
    api_response = api_instance.v1_day_bulk_patch(days_patch_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DayApi->v1_day_bulk_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days_patch_dto** | [**DaysPatchDto**](DaysPatchDto.md)|  | 

### Return type

[**DayListDto**](DayListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_day_list_source_id_year_get**
> DayListDto v1_day_list_source_id_year_get(year, source_id)

List day data of the reference year

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
api_instance = timelight-ai-python-api-client.DayApi(timelight-ai-python-api-client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # List day data of the reference year
    api_response = api_instance.v1_day_list_source_id_year_get(year, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DayApi->v1_day_list_source_id_year_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**DayListDto**](DayListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

