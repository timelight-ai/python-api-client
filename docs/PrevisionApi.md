# timelight_ai_python_api_client.PrevisionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_prevision_group_apply_prevision_post**](PrevisionApi.md#v1_prevision_group_apply_prevision_post) | **POST** /v1/prevision/group-apply-prevision | Apply a source prevision to the whole group
[**v1_prevision_list_source_id_year_get**](PrevisionApi.md#v1_prevision_list_source_id_year_get) | **GET** /v1/prevision/list/{sourceId}/{year} | Fetch data previsions for a given year
[**v1_prevision_save_default_previsions_source_id_year_post**](PrevisionApi.md#v1_prevision_save_default_previsions_source_id_year_post) | **POST** /v1/prevision/save-default-previsions/{sourceId}/{year} | Generate default previsions for the source and save them
[**v1_prevision_save_post**](PrevisionApi.md#v1_prevision_save_post) | **POST** /v1/prevision/save | Save many previsions at once
[**v1_prevision_update_patch**](PrevisionApi.md#v1_prevision_update_patch) | **PATCH** /v1/prevision/update | Update a specific prevision


# **v1_prevision_group_apply_prevision_post**
> PrevisionApplyGroupResponseDto v1_prevision_group_apply_prevision_post(prevision_apply_group_dto)

Apply a source prevision to the whole group

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
api_instance = timelight_ai_python_api_client.PrevisionApi(timelight_ai_python_api_client.ApiClient(configuration))
prevision_apply_group_dto = timelight_ai_python_api_client.PrevisionApplyGroupDto() # PrevisionApplyGroupDto | 

try:
    # Apply a source prevision to the whole group
    api_response = api_instance.v1_prevision_group_apply_prevision_post(prevision_apply_group_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrevisionApi->v1_prevision_group_apply_prevision_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prevision_apply_group_dto** | [**PrevisionApplyGroupDto**](PrevisionApplyGroupDto.md)|  | 

### Return type

[**PrevisionApplyGroupResponseDto**](PrevisionApplyGroupResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_prevision_list_source_id_year_get**
> PrevisionListDto v1_prevision_list_source_id_year_get(year, source_id)

Fetch data previsions for a given year

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
api_instance = timelight_ai_python_api_client.PrevisionApi(timelight_ai_python_api_client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Fetch data previsions for a given year
    api_response = api_instance.v1_prevision_list_source_id_year_get(year, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrevisionApi->v1_prevision_list_source_id_year_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**PrevisionListDto**](PrevisionListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_prevision_save_default_previsions_source_id_year_post**
> PrevisionBulkSaveResultDto v1_prevision_save_default_previsions_source_id_year_post(year, source_id)

Generate default previsions for the source and save them

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
api_instance = timelight_ai_python_api_client.PrevisionApi(timelight_ai_python_api_client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Generate default previsions for the source and save them
    api_response = api_instance.v1_prevision_save_default_previsions_source_id_year_post(year, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrevisionApi->v1_prevision_save_default_previsions_source_id_year_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**PrevisionBulkSaveResultDto**](PrevisionBulkSaveResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_prevision_save_post**
> PrevisionBulkSaveResultDto v1_prevision_save_post(prevision_bulk_save_dto)

Save many previsions at once

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
api_instance = timelight_ai_python_api_client.PrevisionApi(timelight_ai_python_api_client.ApiClient(configuration))
prevision_bulk_save_dto = timelight_ai_python_api_client.PrevisionBulkSaveDto() # PrevisionBulkSaveDto | 

try:
    # Save many previsions at once
    api_response = api_instance.v1_prevision_save_post(prevision_bulk_save_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrevisionApi->v1_prevision_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prevision_bulk_save_dto** | [**PrevisionBulkSaveDto**](PrevisionBulkSaveDto.md)|  | 

### Return type

[**PrevisionBulkSaveResultDto**](PrevisionBulkSaveResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_prevision_update_patch**
> PrevisionUpdateResultDto v1_prevision_update_patch(prevision_patch_dto)

Update a specific prevision

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
api_instance = timelight_ai_python_api_client.PrevisionApi(timelight_ai_python_api_client.ApiClient(configuration))
prevision_patch_dto = timelight_ai_python_api_client.PrevisionPatchDto() # PrevisionPatchDto | 

try:
    # Update a specific prevision
    api_response = api_instance.v1_prevision_update_patch(prevision_patch_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrevisionApi->v1_prevision_update_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prevision_patch_dto** | [**PrevisionPatchDto**](PrevisionPatchDto.md)|  | 

### Return type

[**PrevisionUpdateResultDto**](PrevisionUpdateResultDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

