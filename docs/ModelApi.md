# timelight-ai-python-api-client.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_model_bulk_patch**](ModelApi.md#v1_model_bulk_patch) | **PATCH** /v1/model/bulk | Model bulk update
[**v1_model_list_source_id_get**](ModelApi.md#v1_model_list_source_id_get) | **GET** /v1/model/list/{sourceId} | List models data of this source


# **v1_model_bulk_patch**
> ModelListDto v1_model_bulk_patch(models_patch_dto)

Model bulk update

Update many models at once, mainly used to set color and name of the model

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
api_instance = timelight-ai-python-api-client.ModelApi(timelight-ai-python-api-client.ApiClient(configuration))
models_patch_dto = timelight-ai-python-api-client.ModelsPatchDto() # ModelsPatchDto | 

try:
    # Model bulk update
    api_response = api_instance.v1_model_bulk_patch(models_patch_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->v1_model_bulk_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_patch_dto** | [**ModelsPatchDto**](ModelsPatchDto.md)|  | 

### Return type

[**ModelListDto**](ModelListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_model_list_source_id_get**
> ModelListDto v1_model_list_source_id_get(source_id)

List models data of this source

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
api_instance = timelight-ai-python-api-client.ModelApi(timelight-ai-python-api-client.ApiClient(configuration))
source_id = 8.14 # float | 

try:
    # List models data of this source
    api_response = api_instance.v1_model_list_source_id_get(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->v1_model_list_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | 

### Return type

[**ModelListDto**](ModelListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

