# timelight_ai_python_api_client
This is the timelight api.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import timelight_ai_python_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import timelight_ai_python_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import timelight_ai_python_api_client
from timelight_ai_python_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: bearer
timelight_ai_python_api_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# timelight_ai_python_api_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = timelight_ai_python_api_client.AIApi()
source_id = 8.14 # float | 

try:
    # Auto detect-anomalies
    api_response = api_instance.v1_ai_anomalies_source_id_get(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AIApi->v1_ai_anomalies_source_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AIApi* | [**v1_ai_anomalies_source_id_get**](docs/AIApi.md#v1_ai_anomalies_source_id_get) | **GET** /v1/ai/anomalies/{sourceId} | Auto detect-anomalies
*AIApi* | [**v1_ai_recompute_day_models_source_id_year_post**](docs/AIApi.md#v1_ai_recompute_day_models_source_id_year_post) | **POST** /v1/ai/recompute-day-models/{sourceId}/{year} | Recomputes all day modesl
*AIApi* | [**v1_ai_recompute_days_projection_source_id_year_post**](docs/AIApi.md#v1_ai_recompute_days_projection_source_id_year_post) | **POST** /v1/ai/recompute-days-projection/{sourceId}/{year} | Computes all days projection for a source and save them
*AIApi* | [**v1_ai_recompute_models_source_id_year_post**](docs/AIApi.md#v1_ai_recompute_models_source_id_year_post) | **POST** /v1/ai/recompute-models/{sourceId}/{year} | Triggers a model recompute
*AIApi* | [**v1_ai_recompute_source_models_model_count_post**](docs/AIApi.md#v1_ai_recompute_source_models_model_count_post) | **POST** /v1/ai/recompute-source-models/{modelCount} | Triggers a model recompute for source groups
*AlertApi* | [**v1_alert_alert_id_comment_patch**](docs/AlertApi.md#v1_alert_alert_id_comment_patch) | **PATCH** /v1/alert/{alertId}/comment | Add a comment to an alert
*AlertApi* | [**v1_alert_alert_id_favorite_patch**](docs/AlertApi.md#v1_alert_alert_id_favorite_patch) | **PATCH** /v1/alert/{alertId}/favorite | Set alert favorite for the current user
*AlertApi* | [**v1_alert_list_get**](docs/AlertApi.md#v1_alert_list_get) | **GET** /v1/alert/list | List alerts data of the selected year, all alerts if no year is provided
*AlertApi* | [**v1_alert_ref_list_get**](docs/AlertApi.md#v1_alert_ref_list_get) | **GET** /v1/alert/ref/list | List alerts data of the selected year, all alerts if no year is provided
*DayApi* | [**v1_day_bulk_patch**](docs/DayApi.md#v1_day_bulk_patch) | **PATCH** /v1/day/bulk | Update day entities
*DayApi* | [**v1_day_list_source_id_year_get**](docs/DayApi.md#v1_day_list_source_id_year_get) | **GET** /v1/day/list/{sourceId}/{year} | List day data of the reference year
*DayContextApi* | [**v1_day_context_bulk_post**](docs/DayContextApi.md#v1_day_context_bulk_post) | **POST** /v1/day-context/bulk | Create many DayContext
*DayContextApi* | [**v1_day_context_get**](docs/DayContextApi.md#v1_day_context_get) | **GET** /v1/day-context | Retrieve many DayContext
*DayContextApi* | [**v1_day_context_id_delete**](docs/DayContextApi.md#v1_day_context_id_delete) | **DELETE** /v1/day-context/{id} | Delete one DayContext
*DayContextApi* | [**v1_day_context_id_get**](docs/DayContextApi.md#v1_day_context_id_get) | **GET** /v1/day-context/{id} | Retrieve one DayContext
*DayContextApi* | [**v1_day_context_id_patch**](docs/DayContextApi.md#v1_day_context_id_patch) | **PATCH** /v1/day-context/{id} | Update one DayContext
*DayContextApi* | [**v1_day_context_id_put**](docs/DayContextApi.md#v1_day_context_id_put) | **PUT** /v1/day-context/{id} | Replace one DayContext
*DayContextApi* | [**v1_day_context_import_meteo_csv_source_id_post**](docs/DayContextApi.md#v1_day_context_import_meteo_csv_source_id_post) | **POST** /v1/day-context/import-meteo-csv/{sourceId} | Imports a meteo csv file for the source id
*DayContextApi* | [**v1_day_context_post**](docs/DayContextApi.md#v1_day_context_post) | **POST** /v1/day-context | Create one DayContext
*DayTrendApi* | [**v1_day_trend_bulk_post**](docs/DayTrendApi.md#v1_day_trend_bulk_post) | **POST** /v1/day-trend/bulk | Create many DayTrend
*DayTrendApi* | [**v1_day_trend_get**](docs/DayTrendApi.md#v1_day_trend_get) | **GET** /v1/day-trend | Retrieve many DayTrend
*DayTrendApi* | [**v1_day_trend_id_delete**](docs/DayTrendApi.md#v1_day_trend_id_delete) | **DELETE** /v1/day-trend/{id} | Delete one DayTrend
*DayTrendApi* | [**v1_day_trend_id_get**](docs/DayTrendApi.md#v1_day_trend_id_get) | **GET** /v1/day-trend/{id} | Retrieve one DayTrend
*DayTrendApi* | [**v1_day_trend_id_patch**](docs/DayTrendApi.md#v1_day_trend_id_patch) | **PATCH** /v1/day-trend/{id} | Update one DayTrend
*DayTrendApi* | [**v1_day_trend_id_put**](docs/DayTrendApi.md#v1_day_trend_id_put) | **PUT** /v1/day-trend/{id} | Replace one DayTrend
*DayTrendApi* | [**v1_day_trend_post**](docs/DayTrendApi.md#v1_day_trend_post) | **POST** /v1/day-trend | Create one DayTrend
*DayTrendApi* | [**v1_day_trend_replace_all_in_source_source_id_post**](docs/DayTrendApi.md#v1_day_trend_replace_all_in_source_source_id_post) | **POST** /v1/day-trend/replace-all-in-source/{sourceId} | Imports many trends and replace existing. Recomputes alerts
*ImportApi* | [**v1_import_create_source_post**](docs/ImportApi.md#v1_import_create_source_post) | **POST** /v1/import/create-source | First source creation
*ImportApi* | [**v1_import_days_post**](docs/ImportApi.md#v1_import_days_post) | **POST** /v1/import/days | Add new data to a source
*ImportApi* | [**v1_import_reprocess_days_source_id_year_post**](docs/ImportApi.md#v1_import_reprocess_days_source_id_year_post) | **POST** /v1/import/reprocess-days/{sourceId}/{year} | Reprocess days from database
*ImportApi* | [**v1_import_source_id_days_post**](docs/ImportApi.md#v1_import_source_id_days_post) | **POST** /v1/import/{sourceId}/days | Add new data to a source
*ModelApi* | [**v1_model_bulk_patch**](docs/ModelApi.md#v1_model_bulk_patch) | **PATCH** /v1/model/bulk | Model bulk update
*ModelApi* | [**v1_model_list_source_id_get**](docs/ModelApi.md#v1_model_list_source_id_get) | **GET** /v1/model/list/{sourceId} | List models data of this source
*PrevisionApi* | [**v1_prevision_group_apply_prevision_post**](docs/PrevisionApi.md#v1_prevision_group_apply_prevision_post) | **POST** /v1/prevision/group-apply-prevision | Apply a source prevision to the whole group
*PrevisionApi* | [**v1_prevision_list_source_id_year_get**](docs/PrevisionApi.md#v1_prevision_list_source_id_year_get) | **GET** /v1/prevision/list/{sourceId}/{year} | Fetch data previsions for a given year
*PrevisionApi* | [**v1_prevision_save_default_previsions_source_id_year_post**](docs/PrevisionApi.md#v1_prevision_save_default_previsions_source_id_year_post) | **POST** /v1/prevision/save-default-previsions/{sourceId}/{year} | Generate default previsions for the source and save them
*PrevisionApi* | [**v1_prevision_save_post**](docs/PrevisionApi.md#v1_prevision_save_post) | **POST** /v1/prevision/save | Save many previsions at once
*PrevisionApi* | [**v1_prevision_update_patch**](docs/PrevisionApi.md#v1_prevision_update_patch) | **PATCH** /v1/prevision/update | Update a specific prevision
*SourceApi* | [**v1_source_list_get**](docs/SourceApi.md#v1_source_list_get) | **GET** /v1/source/list | All user sources
*SourceApi* | [**v1_source_source_id_delete**](docs/SourceApi.md#v1_source_source_id_delete) | **DELETE** /v1/source/{sourceId} | Delete a source and all linked data
*SourceApi* | [**v1_source_source_id_group_patch**](docs/SourceApi.md#v1_source_source_id_group_patch) | **PATCH** /v1/source/{sourceId}/group | Update a source group
*SourceApi* | [**v1_source_source_id_patch**](docs/SourceApi.md#v1_source_source_id_patch) | **PATCH** /v1/source/{sourceId} | Update a source
*SourceGroupApi* | [**v1_source_group_create_post**](docs/SourceGroupApi.md#v1_source_group_create_post) | **POST** /v1/source-group/create | Create a new source groups
*SourceGroupApi* | [**v1_source_group_group_id_patch**](docs/SourceGroupApi.md#v1_source_group_group_id_patch) | **PATCH** /v1/source-group/{groupId} | Updates a group configuration
*SourceGroupApi* | [**v1_source_group_list_get**](docs/SourceGroupApi.md#v1_source_group_list_get) | **GET** /v1/source-group/list | All source groups
*UserApi* | [**v1_user_login_post**](docs/UserApi.md#v1_user_login_post) | **POST** /v1/user/login | Log the user in
*UserApi* | [**v1_user_me_get**](docs/UserApi.md#v1_user_me_get) | **GET** /v1/user/me | Retrieve current user information
*UserApi* | [**v1_user_register_demo_post**](docs/UserApi.md#v1_user_register_demo_post) | **POST** /v1/user/register-demo | 
*ViewHelperApi* | [**v1_view_helper_alerts_get**](docs/ViewHelperApi.md#v1_view_helper_alerts_get) | **GET** /v1/view-helper/alerts | Get the alert view data
*ViewHelperApi* | [**v1_view_helper_alerts_ref_get**](docs/ViewHelperApi.md#v1_view_helper_alerts_ref_get) | **GET** /v1/view-helper/alerts-ref | Get the alert referential view data
*ViewHelperApi* | [**v1_view_helper_days_near_date_source_id_day_date_get**](docs/ViewHelperApi.md#v1_view_helper_days_near_date_source_id_day_date_get) | **GET** /v1/view-helper/days-near-date/{sourceId}/{dayDate} | Get the alert modal view data


## Documentation For Models

 - [AlertCommentDto](docs/AlertCommentDto.md)
 - [AlertDto](docs/AlertDto.md)
 - [AlertFavoriteDto](docs/AlertFavoriteDto.md)
 - [AlertListDto](docs/AlertListDto.md)
 - [AlertRefDto](docs/AlertRefDto.md)
 - [AlertRefListDto](docs/AlertRefListDto.md)
 - [AlertRefResultDto](docs/AlertRefResultDto.md)
 - [AnomaliesResponseDto](docs/AnomaliesResponseDto.md)
 - [CreateSourceDayDto](docs/CreateSourceDayDto.md)
 - [CreateSourceDto](docs/CreateSourceDto.md)
 - [DayContext](docs/DayContext.md)
 - [DayListDto](docs/DayListDto.md)
 - [DayModelDto](docs/DayModelDto.md)
 - [DayPatchDto](docs/DayPatchDto.md)
 - [DayTrend](docs/DayTrend.md)
 - [DayTrendInput](docs/DayTrendInput.md)
 - [DayTrendInputListDto](docs/DayTrendInputListDto.md)
 - [DayTrendListDto](docs/DayTrendListDto.md)
 - [DaysNearDateResultDto](docs/DaysNearDateResultDto.md)
 - [DaysPatchDto](docs/DaysPatchDto.md)
 - [GeneratedDayContextBulkDto](docs/GeneratedDayContextBulkDto.md)
 - [GeneratedDayTrendBulkDto](docs/GeneratedDayTrendBulkDto.md)
 - [ImportDayDto](docs/ImportDayDto.md)
 - [ImportDaysDto](docs/ImportDaysDto.md)
 - [LoginDto](docs/LoginDto.md)
 - [LoginResponseDto](docs/LoginResponseDto.md)
 - [ModelDto](docs/ModelDto.md)
 - [ModelListDto](docs/ModelListDto.md)
 - [ModelPatchDto](docs/ModelPatchDto.md)
 - [ModelsPatchDto](docs/ModelsPatchDto.md)
 - [PrevisionApplyGroupDto](docs/PrevisionApplyGroupDto.md)
 - [PrevisionApplyGroupResponseDto](docs/PrevisionApplyGroupResponseDto.md)
 - [PrevisionBulkSaveDto](docs/PrevisionBulkSaveDto.md)
 - [PrevisionBulkSaveResultDto](docs/PrevisionBulkSaveResultDto.md)
 - [PrevisionDto](docs/PrevisionDto.md)
 - [PrevisionListDto](docs/PrevisionListDto.md)
 - [PrevisionPatchDto](docs/PrevisionPatchDto.md)
 - [PrevisionSaveDto](docs/PrevisionSaveDto.md)
 - [PrevisionUpdateResultDto](docs/PrevisionUpdateResultDto.md)
 - [RecomputeDayModelsResponseDto](docs/RecomputeDayModelsResponseDto.md)
 - [RecomputeDaysProjectionResponseDto](docs/RecomputeDaysProjectionResponseDto.md)
 - [RecomputeModelsResponseDto](docs/RecomputeModelsResponseDto.md)
 - [RecomputeSourceModelsResponseDto](docs/RecomputeSourceModelsResponseDto.md)
 - [RequestDemoDto](docs/RequestDemoDto.md)
 - [SourceDto](docs/SourceDto.md)
 - [SourceGroupCreateDto](docs/SourceGroupCreateDto.md)
 - [SourceGroupDto](docs/SourceGroupDto.md)
 - [SourceGroupListDto](docs/SourceGroupListDto.md)
 - [SourceGroupPatchDto](docs/SourceGroupPatchDto.md)
 - [SourceListDto](docs/SourceListDto.md)
 - [SourcePatchDto](docs/SourcePatchDto.md)
 - [SourcePatchGroupDto](docs/SourcePatchGroupDto.md)
 - [UserDto](docs/UserDto.md)


## Documentation For Authorization


## bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



