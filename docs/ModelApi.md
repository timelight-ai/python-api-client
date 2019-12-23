# timelight_ai_python_api_client.ModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_model_bulk_patch**](ModelApi.md#v1_model_bulk_patch) | **PATCH** /v1/model/bulk | Model bulk update
[**v1_model_bulk_replace_source_id_post**](ModelApi.md#v1_model_bulk_replace_source_id_post) | **POST** /v1/model/bulk-replace/{sourceId} | Custom Model create
[**v1_model_list_get**](ModelApi.md#v1_model_list_get) | **GET** /v1/model/list | List models data of this source
[**v1_model_list_source_id_get**](ModelApi.md#v1_model_list_source_id_get) | **GET** /v1/model/list/{sourceId} | List models data of this source
[**v1_model_reset_source_id_model_count_post**](ModelApi.md#v1_model_reset_source_id_model_count_post) | **POST** /v1/model/reset/{sourceId}/{modelCount} | Reset to default timelight models configuration


# **v1_model_bulk_patch**
> ModelListDto v1_model_bulk_patch(models_patch_dto)

Model bulk update

Update many models at once, mainly used to set color and name of the model

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
api_instance = timelight_ai_python_api_client.ModelApi(timelight_ai_python_api_client.ApiClient(configuration))
models_patch_dto = timelight_ai_python_api_client.ModelsPatchDto() # ModelsPatchDto | 

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

# **v1_model_bulk_replace_source_id_post**
> ModelListDto v1_model_bulk_replace_source_id_post(models_post_dto, source_id)

Custom Model create

Create many custom models at once, this config replaces the original models.        WARNING: This action will remove all previsions and alerts.

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
api_instance = timelight_ai_python_api_client.ModelApi(timelight_ai_python_api_client.ApiClient(configuration))
models_post_dto = timelight_ai_python_api_client.ModelsPostDto() # ModelsPostDto | 
source_id = 8.14 # float | 

try:
    # Custom Model create
    api_response = api_instance.v1_model_bulk_replace_source_id_post(models_post_dto, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->v1_model_bulk_replace_source_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models_post_dto** | [**ModelsPostDto**](ModelsPostDto.md)|  | 
 **source_id** | **float**|  | 

### Return type

[**ModelListDto**](ModelListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_model_list_get**
> ModelListDto v1_model_list_get()

List models data of this source

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
api_instance = timelight_ai_python_api_client.ModelApi(timelight_ai_python_api_client.ApiClient(configuration))

try:
    # List models data of this source
    api_response = api_instance.v1_model_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->v1_model_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
configuration = timelight_ai_python_api_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = timelight_ai_python_api_client.ModelApi(timelight_ai_python_api_client.ApiClient(configuration))
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

# **v1_model_reset_source_id_model_count_post**
> ModelListDto v1_model_reset_source_id_model_count_post(model_count, source_id)

Reset to default timelight models configuration

Drop all models and re-create them from data

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
api_instance = timelight_ai_python_api_client.ModelApi(timelight_ai_python_api_client.ApiClient(configuration))
model_count = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Reset to default timelight models configuration
    api_response = api_instance.v1_model_reset_source_id_model_count_post(model_count, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelApi->v1_model_reset_source_id_model_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_count** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**ModelListDto**](ModelListDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

