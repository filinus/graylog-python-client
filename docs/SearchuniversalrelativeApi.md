# swagger_client.SearchuniversalrelativeApi

All URIs are relative to *http://127.0.0.1:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_search_relative_chunked**](SearchuniversalrelativeApi.md#export_search_relative_chunked) | **GET** /search/universal/relative/export | Export message search with relative timerange.
[**field_histogram_relative**](SearchuniversalrelativeApi.md#field_histogram_relative) | **GET** /search/universal/relative/fieldhistogram | Field value histogram of a query using a relative timerange.
[**histogram_relative**](SearchuniversalrelativeApi.md#histogram_relative) | **GET** /search/universal/relative/histogram | Datetime histogram of a query using a relative timerange.
[**search_relative**](SearchuniversalrelativeApi.md#search_relative) | **GET** /search/universal/relative | Message search with relative timerange.
[**stats_relative**](SearchuniversalrelativeApi.md#stats_relative) | **GET** /search/universal/relative/stats | Field statistics for a query using a relative timerange.
[**terms_histogram_relative**](SearchuniversalrelativeApi.md#terms_histogram_relative) | **GET** /search/universal/relative/terms-histogram | Most common field terms of a query over time using a relative timerange.
[**terms_relative**](SearchuniversalrelativeApi.md#terms_relative) | **GET** /search/universal/relative/terms | Most common field terms of a query using a relative timerange.
[**terms_stats_relative**](SearchuniversalrelativeApi.md#terms_stats_relative) | **GET** /search/universal/relative/termsstats | Ordered field terms of a query computed on another field using a relative timerange.


# **export_search_relative_chunked**
> export_search_relative_chunked(query, range, fields, limit=limit, offset=offset, filter=filter)

Export message search with relative timerange.

Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
range = 56 # int | Relative timeframe to search in. See method description.
fields = 'fields_example' # str | Comma separated list of fields to return
limit = 56 # int | Maximum number of messages to return. (optional)
offset = 56 # int | Offset (optional)
filter = 'filter_example' # str | Filter (optional)

try:
    # Export message search with relative timerange.
    api_instance.export_search_relative_chunked(query, range, fields, limit=limit, offset=offset, filter=filter)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->export_search_relative_chunked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **range** | **int**| Relative timeframe to search in. See method description. | 
 **fields** | **str**| Comma separated list of fields to return | 
 **limit** | **int**| Maximum number of messages to return. | [optional] 
 **offset** | **int**| Offset | [optional] 
 **filter** | **str**| Filter | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **field_histogram_relative**
> HistogramResult field_histogram_relative(query, field, interval, range, filter=filter, cardinality=cardinality)

Field value histogram of a query using a relative timerange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
field = 'field_example' # str | Field of whose values to get the histogram of
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
range = 56 # int | Relative timeframe to search in. See search method description.
filter = 'filter_example' # str | Filter (optional)
cardinality = true # bool | Calculate the cardinality of the field as well (optional)

try:
    # Field value histogram of a query using a relative timerange.
    api_response = api_instance.field_histogram_relative(query, field, interval, range, filter=filter, cardinality=cardinality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->field_histogram_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **field** | **str**| Field of whose values to get the histogram of | 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **filter** | **str**| Filter | [optional] 
 **cardinality** | **bool**| Calculate the cardinality of the field as well | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **histogram_relative**
> HistogramResult histogram_relative(query, interval, range, filter=filter)

Datetime histogram of a query using a relative timerange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
range = 56 # int | Relative timeframe to search in. See search method description.
filter = 'filter_example' # str | Filter (optional)

try:
    # Datetime histogram of a query using a relative timerange.
    api_response = api_instance.histogram_relative(query, interval, range, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->histogram_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **filter** | **str**| Filter | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_relative**
> SearchResponse search_relative(query, range, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)

Message search with relative timerange.

Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
range = 56 # int | Relative timeframe to search in. See method description.
limit = 56 # int | Maximum number of messages to return. (optional)
offset = 56 # int | Offset (optional)
filter = 'filter_example' # str | Filter (optional)
fields = 'fields_example' # str | Comma separated list of fields to return (optional)
sort = 'sort_example' # str | Sorting (field:asc / field:desc) (optional)
decorate = true # bool | Run decorators on search result (optional) (default to true)

try:
    # Message search with relative timerange.
    api_response = api_instance.search_relative(query, range, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->search_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **range** | **int**| Relative timeframe to search in. See method description. | 
 **limit** | **int**| Maximum number of messages to return. | [optional] 
 **offset** | **int**| Offset | [optional] 
 **filter** | **str**| Filter | [optional] 
 **fields** | **str**| Comma separated list of fields to return | [optional] 
 **sort** | **str**| Sorting (field:asc / field:desc) | [optional] 
 **decorate** | **bool**| Run decorators on search result | [optional] [default to true]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_relative**
> FieldStatsResult stats_relative(field, query, range, filter=filter)

Field statistics for a query using a relative timerange.

Returns statistics like min/max or standard deviation of numeric fields over the whole query result set.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of numeric type to return statistics for
query = 'query_example' # str | Query (Lucene syntax)
range = 56 # int | Relative timeframe to search in. See search method description.
filter = 'filter_example' # str | Filter (optional)

try:
    # Field statistics for a query using a relative timerange.
    api_response = api_instance.stats_relative(field, query, range, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->stats_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of numeric type to return statistics for | 
 **query** | **str**| Query (Lucene syntax) | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **filter** | **str**| Filter | [optional] 

### Return type

[**FieldStatsResult**](FieldStatsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_histogram_relative**
> TermsHistogramResult terms_histogram_relative(field, query, size, range, stacked_fields=stacked_fields, interval=interval, filter=filter, order=order)

Most common field terms of a query over time using a relative timerange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of to return terms of
query = 'query_example' # str | Query (Lucene syntax)
size = 56 # int | Maximum number of terms to return
range = 56 # int | Relative timeframe to search in. See search method description.
stacked_fields = 'stacked_fields_example' # str | Fields to stack (optional)
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) (optional)
filter = 'filter_example' # str | Filter (optional)
order = 'order_example' # str | Sorting (field:asc / field:desc) (optional)

try:
    # Most common field terms of a query over time using a relative timerange.
    api_response = api_instance.terms_histogram_relative(field, query, size, range, stacked_fields=stacked_fields, interval=interval, filter=filter, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->terms_histogram_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of to return terms of | 
 **query** | **str**| Query (Lucene syntax) | 
 **size** | **int**| Maximum number of terms to return | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **stacked_fields** | **str**| Fields to stack | [optional] 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | [optional] 
 **filter** | **str**| Filter | [optional] 
 **order** | **str**| Sorting (field:asc / field:desc) | [optional] 

### Return type

[**TermsHistogramResult**](TermsHistogramResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_relative**
> TermsResult terms_relative(field, query, range, stacked_fields=stacked_fields, size=size, filter=filter, order=order)

Most common field terms of a query using a relative timerange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of to return terms of
query = 'query_example' # str | Query (Lucene syntax)
range = 56 # int | Relative timeframe to search in. See search method description.
stacked_fields = 'stacked_fields_example' # str | Fields to stack (optional)
size = 56 # int | Maximum number of terms to return (optional)
filter = 'filter_example' # str | Filter (optional)
order = 'order_example' # str | Sorting (field:asc / field:desc) (optional)

try:
    # Most common field terms of a query using a relative timerange.
    api_response = api_instance.terms_relative(field, query, range, stacked_fields=stacked_fields, size=size, filter=filter, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->terms_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of to return terms of | 
 **query** | **str**| Query (Lucene syntax) | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **stacked_fields** | **str**| Fields to stack | [optional] 
 **size** | **int**| Maximum number of terms to return | [optional] 
 **filter** | **str**| Filter | [optional] 
 **order** | **str**| Sorting (field:asc / field:desc) | [optional] 

### Return type

[**TermsResult**](TermsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_stats_relative**
> TermsStatsResult terms_stats_relative(key_field, value_field, order, query, range, size=size, filter=filter)

Ordered field terms of a query computed on another field using a relative timerange.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.SearchuniversalrelativeApi(swagger_client.ApiClient(configuration))
key_field = 'key_field_example' # str | Message field of to return terms of
value_field = 'value_field_example' # str | Value field used for computation
order = 'order_example' # str | What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)
query = 'query_example' # str | Query (Lucene syntax)
range = 56 # int | Relative timeframe to search in. See search method description.
size = 56 # int | Maximum number of terms to return (optional)
filter = 'filter_example' # str | Filter (optional)

try:
    # Ordered field terms of a query computed on another field using a relative timerange.
    api_response = api_instance.terms_stats_relative(key_field, value_field, order, query, range, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalrelativeApi->terms_stats_relative: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_field** | **str**| Message field of to return terms of | 
 **value_field** | **str**| Value field used for computation | 
 **order** | **str**| What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) | 
 **query** | **str**| Query (Lucene syntax) | 
 **range** | **int**| Relative timeframe to search in. See search method description. | 
 **size** | **int**| Maximum number of terms to return | [optional] 
 **filter** | **str**| Filter | [optional] 

### Return type

[**TermsStatsResult**](TermsStatsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

