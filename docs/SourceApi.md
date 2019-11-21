# timelight_ai_python_api_client.SourceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_source_list_get**](SourceApi.md#v1_source_list_get) | **GET** /v1/source/list | All user sources
[**v1_source_source_id_delete**](SourceApi.md#v1_source_source_id_delete) | **DELETE** /v1/source/{sourceId} | Delete a source and all linked data
[**v1_source_source_id_group_patch**](SourceApi.md#v1_source_source_id_group_patch) | **PATCH** /v1/source/{sourceId}/group | Update a source group
[**v1_source_source_id_patch**](SourceApi.md#v1_source_source_id_patch) | **PATCH** /v1/source/{sourceId} | Update a source


# **v1_source_list_get**
> SourceListDto v1_source_list_get()

All user sources

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
api_instance = timelight_ai_python_api_client.SourceApi(timelight_ai_python_api_client.ApiClient(configuration))

try:
    # All user sources
    api_response = api_instance.v1_source_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->v1_source_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SourceListDto**](SourceListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_source_source_id_delete**
> v1_source_source_id_delete(source_id)

Delete a source and all linked data

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
api_instance = timelight_ai_python_api_client.SourceApi(timelight_ai_python_api_client.ApiClient(configuration))
source_id = 8.14 # float | 

try:
    # Delete a source and all linked data
    api_instance.v1_source_source_id_delete(source_id)
except ApiException as e:
    print("Exception when calling SourceApi->v1_source_source_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_source_source_id_group_patch**
> SourceDto v1_source_source_id_group_patch(source_patch_group_dto, source_id)

Update a source group

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
api_instance = timelight_ai_python_api_client.SourceApi(timelight_ai_python_api_client.ApiClient(configuration))
source_patch_group_dto = timelight_ai_python_api_client.SourcePatchGroupDto() # SourcePatchGroupDto | 
source_id = 8.14 # float | 

try:
    # Update a source group
    api_response = api_instance.v1_source_source_id_group_patch(source_patch_group_dto, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->v1_source_source_id_group_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_patch_group_dto** | [**SourcePatchGroupDto**](SourcePatchGroupDto.md)|  | 
 **source_id** | **float**|  | 

### Return type

[**SourceDto**](SourceDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_source_source_id_patch**
> SourceDto v1_source_source_id_patch(source_patch_dto, source_id)

Update a source

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
api_instance = timelight_ai_python_api_client.SourceApi(timelight_ai_python_api_client.ApiClient(configuration))
source_patch_dto = timelight_ai_python_api_client.SourcePatchDto() # SourcePatchDto | 
source_id = 8.14 # float | 

try:
    # Update a source
    api_response = api_instance.v1_source_source_id_patch(source_patch_dto, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceApi->v1_source_source_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_patch_dto** | [**SourcePatchDto**](SourcePatchDto.md)|  | 
 **source_id** | **float**|  | 

### Return type

[**SourceDto**](SourceDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

