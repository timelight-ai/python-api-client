# timelight_ai_python_api_client.SourceGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_source_group_create_post**](SourceGroupApi.md#v1_source_group_create_post) | **POST** /v1/source-group/create | Create a new source groups
[**v1_source_group_group_id_patch**](SourceGroupApi.md#v1_source_group_group_id_patch) | **PATCH** /v1/source-group/{groupId} | Updates a group configuration
[**v1_source_group_list_get**](SourceGroupApi.md#v1_source_group_list_get) | **GET** /v1/source-group/list | All source groups


# **v1_source_group_create_post**
> SourceGroupDto v1_source_group_create_post(source_group_create_dto)

Create a new source groups

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
api_instance = timelight_ai_python_api_client.SourceGroupApi(timelight_ai_python_api_client.ApiClient(configuration))
source_group_create_dto = timelight_ai_python_api_client.SourceGroupCreateDto() # SourceGroupCreateDto | 

try:
    # Create a new source groups
    api_response = api_instance.v1_source_group_create_post(source_group_create_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceGroupApi->v1_source_group_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_group_create_dto** | [**SourceGroupCreateDto**](SourceGroupCreateDto.md)|  | 

### Return type

[**SourceGroupDto**](SourceGroupDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_source_group_group_id_patch**
> SourceGroupDto v1_source_group_group_id_patch(source_group_patch_dto, group_id)

Updates a group configuration

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
api_instance = timelight_ai_python_api_client.SourceGroupApi(timelight_ai_python_api_client.ApiClient(configuration))
source_group_patch_dto = timelight_ai_python_api_client.SourceGroupPatchDto() # SourceGroupPatchDto | 
group_id = 8.14 # float | 

try:
    # Updates a group configuration
    api_response = api_instance.v1_source_group_group_id_patch(source_group_patch_dto, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceGroupApi->v1_source_group_group_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_group_patch_dto** | [**SourceGroupPatchDto**](SourceGroupPatchDto.md)|  | 
 **group_id** | **float**|  | 

### Return type

[**SourceGroupDto**](SourceGroupDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_source_group_list_get**
> SourceGroupListDto v1_source_group_list_get()

All source groups

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
api_instance = timelight_ai_python_api_client.SourceGroupApi(timelight_ai_python_api_client.ApiClient(configuration))

try:
    # All source groups
    api_response = api_instance.v1_source_group_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceGroupApi->v1_source_group_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SourceGroupListDto**](SourceGroupListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

