# timelight-ai-python-api-client.AIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ai_anomalies_source_id_get**](AIApi.md#v1_ai_anomalies_source_id_get) | **GET** /v1/ai/anomalies/{sourceId} | Auto detect-anomalies
[**v1_ai_recompute_day_models_source_id_year_post**](AIApi.md#v1_ai_recompute_day_models_source_id_year_post) | **POST** /v1/ai/recompute-day-models/{sourceId}/{year} | Recomputes all day modesl
[**v1_ai_recompute_days_projection_source_id_year_post**](AIApi.md#v1_ai_recompute_days_projection_source_id_year_post) | **POST** /v1/ai/recompute-days-projection/{sourceId}/{year} | Computes all days projection for a source and save them
[**v1_ai_recompute_models_source_id_year_post**](AIApi.md#v1_ai_recompute_models_source_id_year_post) | **POST** /v1/ai/recompute-models/{sourceId}/{year} | Triggers a model recompute
[**v1_ai_recompute_source_models_model_count_post**](AIApi.md#v1_ai_recompute_source_models_model_count_post) | **POST** /v1/ai/recompute-source-models/{modelCount} | Triggers a model recompute for source groups


# **v1_ai_anomalies_source_id_get**
> AnomaliesResponseDto v1_ai_anomalies_source_id_get(source_id)

Auto detect-anomalies

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
api_instance = timelight-ai-python-api-client.AIApi(timelight-ai-python-api-client.ApiClient(configuration))
source_id = 8.14 # float | 

try:
    # Auto detect-anomalies
    api_response = api_instance.v1_ai_anomalies_source_id_get(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_anomalies_source_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **float**|  | 

### Return type

[**AnomaliesResponseDto**](AnomaliesResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ai_recompute_day_models_source_id_year_post**
> RecomputeDayModelsResponseDto v1_ai_recompute_day_models_source_id_year_post(year, source_id)

Recomputes all day modesl

Erases and re-computes all day models for a source and year

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
api_instance = timelight-ai-python-api-client.AIApi(timelight-ai-python-api-client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Recomputes all day modesl
    api_response = api_instance.v1_ai_recompute_day_models_source_id_year_post(year, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_recompute_day_models_source_id_year_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**RecomputeDayModelsResponseDto**](RecomputeDayModelsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ai_recompute_days_projection_source_id_year_post**
> RecomputeDaysProjectionResponseDto v1_ai_recompute_days_projection_source_id_year_post(year, source_id)

Computes all days projection for a source and save them

This computes the X/Y projection of all days in the source for the given year

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
api_instance = timelight-ai-python-api-client.AIApi(timelight-ai-python-api-client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 

try:
    # Computes all days projection for a source and save them
    api_response = api_instance.v1_ai_recompute_days_projection_source_id_year_post(year, source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_recompute_days_projection_source_id_year_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 

### Return type

[**RecomputeDaysProjectionResponseDto**](RecomputeDaysProjectionResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ai_recompute_models_source_id_year_post**
> RecomputeModelsResponseDto v1_ai_recompute_models_source_id_year_post(year, source_id, model_count=model_count)

Triggers a model recompute

This operations erases both non-handled alerts and user previsions

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
api_instance = timelight-ai-python-api-client.AIApi(timelight-ai-python-api-client.ApiClient(configuration))
year = 8.14 # float | 
source_id = 8.14 # float | 
model_count = 8.14 # float |  (optional)

try:
    # Triggers a model recompute
    api_response = api_instance.v1_ai_recompute_models_source_id_year_post(year, source_id, model_count=model_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_recompute_models_source_id_year_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **float**|  | 
 **source_id** | **float**|  | 
 **model_count** | **float**|  | [optional] 

### Return type

[**RecomputeModelsResponseDto**](RecomputeModelsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ai_recompute_source_models_model_count_post**
> RecomputeSourceModelsResponseDto v1_ai_recompute_source_models_model_count_post(model_count)

Triggers a model recompute for source groups

This operations erases the group configuration

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
api_instance = timelight-ai-python-api-client.AIApi(timelight-ai-python-api-client.ApiClient(configuration))
model_count = 8.14 # float | 

try:
    # Triggers a model recompute for source groups
    api_response = api_instance.v1_ai_recompute_source_models_model_count_post(model_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_recompute_source_models_model_count_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_count** | **float**|  | 

### Return type

[**RecomputeSourceModelsResponseDto**](RecomputeSourceModelsResponseDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

