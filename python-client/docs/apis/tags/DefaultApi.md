<a name="__pageTop"></a>
# bundestag.apis.tags.default_api.DefaultApi

All URIs are relative to *https://www.bundestag.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get**](#blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get) | **get** /blueprint/servlet/content/{ARTICLE_ID}/asAppV2NewsarticleXml | Artikel Details
[**iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get**](#iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get) | **get** /iptv/player/macros/_x_s-144277506/bttv/mobile/feed_vod.xml | Abruf eines Videos
[**static_appdata_plenum_v2_conferences_xml_get**](#static_appdata_plenum_v2_conferences_xml_get) | **get** /static/appdata/plenum/v2/conferences.xml | Sitzungstag übersicht
[**static_appdata_plenum_v2_speaker_xml_get**](#static_appdata_plenum_v2_speaker_xml_get) | **get** /static/appdata/plenum/v2/speaker.xml | Aktuelle Sprecher*in
[**xml_v2_ausschuesse_ausschussid_xml_get**](#xml_v2_ausschuesse_ausschussid_xml_get) | **get** /xml/v2/ausschuesse/{AUSSCHUSS_ID}.xml | Übersicht über die Ausschüsse
[**xml_v2_ausschuesse_index_xml_get**](#xml_v2_ausschuesse_index_xml_get) | **get** /xml/v2/ausschuesse/index.xml | Übersicht über die Ausschüsse
[**xml_v2_mdb_biografien_mdbid_xml_get**](#xml_v2_mdb_biografien_mdbid_xml_get) | **get** /xml/v2/mdb/biografien/{MDB_ID}.xml | Abruf Details eines MDBS
[**xml_v2_mdb_index_xml_get**](#xml_v2_mdb_index_xml_get) | **get** /xml/v2/mdb/index.xml | Übersicht über alle MDBS

# **blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get**
<a name="blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get"></a>
> str blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get(article_id)

Artikel Details

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'ARTICLE_ID': 849630,
    }
    try:
        # Artikel Details
        api_response = api_instance.blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get(
            path_params=path_params,
        )
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ARTICLE_ID | ARTICLEIDSchema | | 

# ARTICLEIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get.ApiResponseFor200) | OK

#### blueprint_servlet_content_articleidas_app_v2_newsarticle_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get**
<a name="iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get"></a>
> str iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(content_id)

Abruf eines Videos

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'contentId': 7529016,
    }
    try:
        # Abruf eines Videos
        api_response = api_instance.iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get(
            query_params=query_params,
        )
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/xml', ) | Tells the server the content type(s) that are accepted by the client
host_index | typing.Optional[int] | default is None | Allows one to select a different host
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
contentId | ContentIdSchema | | 


# ContentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get.ApiResponseFor200) | OK

#### iptv_player_macros_xs144277506_bttv_mobile_feed_vod_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **static_appdata_plenum_v2_conferences_xml_get**
<a name="static_appdata_plenum_v2_conferences_xml_get"></a>
> str static_appdata_plenum_v2_conferences_xml_get()

Sitzungstag übersicht

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Sitzungstag übersicht
        api_response = api_instance.static_appdata_plenum_v2_conferences_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->static_appdata_plenum_v2_conferences_xml_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#static_appdata_plenum_v2_conferences_xml_get.ApiResponseFor200) | OK

#### static_appdata_plenum_v2_conferences_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **static_appdata_plenum_v2_speaker_xml_get**
<a name="static_appdata_plenum_v2_speaker_xml_get"></a>
> str static_appdata_plenum_v2_speaker_xml_get()

Aktuelle Sprecher*in

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Aktuelle Sprecher*in
        api_response = api_instance.static_appdata_plenum_v2_speaker_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->static_appdata_plenum_v2_speaker_xml_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#static_appdata_plenum_v2_speaker_xml_get.ApiResponseFor200) | OK

#### static_appdata_plenum_v2_speaker_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **xml_v2_ausschuesse_ausschussid_xml_get**
<a name="xml_v2_ausschuesse_ausschussid_xml_get"></a>
> str xml_v2_ausschuesse_ausschussid_xml_get(ausschuss_id)

Übersicht über die Ausschüsse

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'AUSSCHUSS_ID': "a11",
    }
    try:
        # Übersicht über die Ausschüsse
        api_response = api_instance.xml_v2_ausschuesse_ausschussid_xml_get(
            path_params=path_params,
        )
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_ausschuesse_ausschussid_xml_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
AUSSCHUSS_ID | AUSSCHUSSIDSchema | | 

# AUSSCHUSSIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#xml_v2_ausschuesse_ausschussid_xml_get.ApiResponseFor200) | OK

#### xml_v2_ausschuesse_ausschussid_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **xml_v2_ausschuesse_index_xml_get**
<a name="xml_v2_ausschuesse_index_xml_get"></a>
> str xml_v2_ausschuesse_index_xml_get()

Übersicht über die Ausschüsse

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Übersicht über die Ausschüsse
        api_response = api_instance.xml_v2_ausschuesse_index_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_ausschuesse_index_xml_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#xml_v2_ausschuesse_index_xml_get.ApiResponseFor200) | OK

#### xml_v2_ausschuesse_index_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **xml_v2_mdb_biografien_mdbid_xml_get**
<a name="xml_v2_mdb_biografien_mdbid_xml_get"></a>
> str xml_v2_mdb_biografien_mdbid_xml_get(mdb_id)

Abruf Details eines MDBS

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'MDB_ID': 1769,
    }
    try:
        # Abruf Details eines MDBS
        api_response = api_instance.xml_v2_mdb_biografien_mdbid_xml_get(
            path_params=path_params,
        )
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_mdb_biografien_mdbid_xml_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
MDB_ID | MDBIDSchema | | 

# MDBIDSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#xml_v2_mdb_biografien_mdbid_xml_get.ApiResponseFor200) | OK

#### xml_v2_mdb_biografien_mdbid_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **xml_v2_mdb_index_xml_get**
<a name="xml_v2_mdb_index_xml_get"></a>
> str xml_v2_mdb_index_xml_get()

Übersicht über alle MDBS

### Example

```python
from deutschland import bundestag
from deutschland.bundestag.apis.tags import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.bundestag.de
# See configuration.py for a list of all supported configuration parameters.
configuration = bundestag.Configuration(
    host = "https://www.bundestag.de"
)

# Enter a context with an instance of the API client
with bundestag.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Übersicht über alle MDBS
        api_response = api_instance.xml_v2_mdb_index_xml_get()
        pprint(api_response)
    except bundestag.ApiException as e:
        print("Exception when calling DefaultApi->xml_v2_mdb_index_xml_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#xml_v2_mdb_index_xml_get.ApiResponseFor200) | OK

#### xml_v2_mdb_index_xml_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

