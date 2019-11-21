# timelight-ai-python-api-client.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_user_login_post**](UserApi.md#v1_user_login_post) | **POST** /v1/user/login | Log the user in
[**v1_user_me_get**](UserApi.md#v1_user_me_get) | **GET** /v1/user/me | Retrieve current user information
[**v1_user_register_demo_post**](UserApi.md#v1_user_register_demo_post) | **POST** /v1/user/register-demo | 


# **v1_user_login_post**
> LoginResponseDto v1_user_login_post(login_dto)

Log the user in

This endpoints returns the jwt and sets a cookie with the same jwt.      This way you can use it from both an api and a browser

### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timelight-ai-python-api-client.UserApi()
login_dto = timelight-ai-python-api-client.LoginDto() # LoginDto | 

try:
    # Log the user in
    api_response = api_instance.v1_user_login_post(login_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_dto** | [**LoginDto**](LoginDto.md)|  | 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_me_get**
> UserDto v1_user_me_get()

Retrieve current user information

Must be authenticated to call this endpoint

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
api_instance = timelight-ai-python-api-client.UserApi(timelight-ai-python-api-client.ApiClient(configuration))

try:
    # Retrieve current user information
    api_response = api_instance.v1_user_me_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_user_me_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDto**](UserDto.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_register_demo_post**
> LoginResponseDto v1_user_register_demo_post(request_demo_dto)



### Example
```python
from __future__ import print_function
import time
import timelight-ai-python-api-client
from timelight-ai-python-api-client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = timelight-ai-python-api-client.UserApi()
request_demo_dto = timelight-ai-python-api-client.RequestDemoDto() # RequestDemoDto | 

try:
    api_response = api_instance.v1_user_register_demo_post(request_demo_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->v1_user_register_demo_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_demo_dto** | [**RequestDemoDto**](RequestDemoDto.md)|  | 

### Return type

[**LoginResponseDto**](LoginResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

