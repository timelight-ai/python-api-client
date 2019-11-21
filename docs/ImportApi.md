# timelight_ai_python_api_client.ImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_import_create_source_post**](ImportApi.md#v1_import_create_source_post) | **POST** /v1/import/create-source | First source creation
[**v1_import_days_post**](ImportApi.md#v1_import_days_post) | **POST** /v1/import/days | Add new data to a source
[**v1_import_reprocess_days_source_id_year_post**](ImportApi.md#v1_import_reprocess_days_source_id_year_post) | **POST** /v1/import/reprocess-days/{sourceId}/{year} | Reprocess days from database
[**v1_import_source_id_days_post**](ImportApi.md#v1_import_source_id_days_post) | **POST** /v1/import/{sourceId}/days | Add new data to a source


# **v1_import_create_source_post**
> v1_import_create_source_post(create_source_dto)

First source creation

Creates a source, add a first batch of day data, then computes the models for the first time.

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
api_instance = timelight_ai_python_api_client.ImportApi(timelight_ai_python_api_client.ApiClient(configuration))
create_source_dto = timelight_ai_python_api_client.CreateSourceDto() # CreateSourceDto | 

try:
    # First source creation
    api_instance.v1_import_create_source_post(create_source_dto)
except ApiException as e:
    print("Exception when calling ImportApi->v1_import_create_source_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_source_dto** | [**CreateSourceDto**](CreateSourceDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_import_days_post**
> v1_import_days_post(import_days_dto)

Add new data to a source

When new data is added, we compute alerts for this data

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
api_instance = timelight_ai_python_api_client.ImportApi(timelight_ai_python_api_client.ApiClient(configuration))
import_days_dto = timelight_ai_python_api_client.ImportDaysDto() # ImportDaysDto | 

try:
    # Add new data to a source
    api_instance.v1_import_days_post(import_days_dto)
except ApiException as e:
    print("Exception when calling ImportApi->v1_import_days_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_days_dto** | [**ImportDaysDto**](ImportDaysDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_import_reprocess_days_source_id_year_post**
> v1_import_reprocess_days_source_id_year_post(year, source_id)

Reprocess days from database

Compute maps, alerts and closest models

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
api_instance = timelight_ai_python_api_client.ImportApi(timelight_ai_python_api_client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Reprocess days from database
    api_instance.v1_import_reprocess_days_source_id_year_post(year, source_id)
except ApiException as e:
    print("Exception when calling ImportApi->v1_import_reprocess_days_source_id_year_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_import_source_id_days_post**
> v1_import_source_id_days_post(source_id, import_days_dto)

Add new data to a source

When new data is added, we compute alerts for this data

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
api_instance = timelight_ai_python_api_client.ImportApi(timelight_ai_python_api_client.ApiClient(configuration))
source_id = 8.14 # float | 
import_days_dto = timelight_ai_python_api_client.ImportDaysDto() # ImportDaysDto | 

try:
    # Add new data to a source
    api_instance.v1_import_source_id_days_post(source_id, import_days_dto)
except ApiException as e:
    print("Exception when calling ImportApi->v1_import_source_id_days_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | 
 **import_days_dto** | [**ImportDaysDto**](ImportDaysDto.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

