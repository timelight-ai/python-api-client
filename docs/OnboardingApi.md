# timelight_ai_python_api_client.OnboardingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_onboarding_analyze_csv_post**](OnboardingApi.md#v1_onboarding_analyze_csv_post) | **POST** /v1/onboarding/analyze-csv | Analyze a csv input
[**v1_onboarding_validate_csv_post**](OnboardingApi.md#v1_onboarding_validate_csv_post) | **POST** /v1/onboarding/validate-csv | Checks that our onboarding csv file is valid


# **v1_onboarding_analyze_csv_post**
> v1_onboarding_analyze_csv_post()

Analyze a csv input

### Example
```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timelight_ai_python_api_client.OnboardingApi()

try:
    # Analyze a csv input
    api_instance.v1_onboarding_analyze_csv_post()
except ApiException as e:
    print("Exception when calling OnboardingApi->v1_onboarding_analyze_csv_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_onboarding_validate_csv_post**
> v1_onboarding_validate_csv_post()

Checks that our onboarding csv file is valid

### Example
```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timelight_ai_python_api_client.OnboardingApi()

try:
    # Checks that our onboarding csv file is valid
    api_instance.v1_onboarding_validate_csv_post()
except ApiException as e:
    print("Exception when calling OnboardingApi->v1_onboarding_validate_csv_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

