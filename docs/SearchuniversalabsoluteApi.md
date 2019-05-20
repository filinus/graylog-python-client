# swagger_client.SearchuniversalabsoluteApi

All URIs are relative to *http://127.0.0.1:9000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_search_absolute_chunked**](SearchuniversalabsoluteApi.md#export_search_absolute_chunked) | **GET** /search/universal/absolute/export | Export message search with absolute timerange.
[**field_histogram_absolute**](SearchuniversalabsoluteApi.md#field_histogram_absolute) | **GET** /search/universal/absolute/fieldhistogram | Field value histogram of a query using an absolute timerange.
[**histogram_absolute**](SearchuniversalabsoluteApi.md#histogram_absolute) | **GET** /search/universal/absolute/histogram | Datetime histogram of a query using an absolute timerange.
[**search_absolute**](SearchuniversalabsoluteApi.md#search_absolute) | **GET** /search/universal/absolute | Message search with absolute timerange.
[**stats_absolute**](SearchuniversalabsoluteApi.md#stats_absolute) | **GET** /search/universal/absolute/stats | Field statistics for a query using an absolute timerange.
[**terms_absolute**](SearchuniversalabsoluteApi.md#terms_absolute) | **GET** /search/universal/absolute/terms | Most common field terms of a query using an absolute timerange.
[**terms_histogram_absolute**](SearchuniversalabsoluteApi.md#terms_histogram_absolute) | **GET** /search/universal/absolute/terms-histogram | Most common field terms of a query over time using an absolute timerange.
[**terms_stats_absolute**](SearchuniversalabsoluteApi.md#terms_stats_absolute) | **GET** /search/universal/absolute/termsstats | Ordered field terms of a query computed on another field using an absolute timerange.


# **export_search_absolute_chunked**
> export_search_absolute_chunked(query, _from, to, fields, limit=limit, offset=offset, filter=filter)

Export message search with absolute timerange.

Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
_from = '_from_example' # str | Timerange start. See description for date format
to = 'to_example' # str | Timerange end. See description for date format
fields = 'fields_example' # str | Comma separated list of fields to return
limit = 56 # int | Maximum number of messages to return. (optional)
offset = 56 # int | Offset (optional)
filter = 'filter_example' # str | Filter (optional)

try:
    # Export message search with absolute timerange.
    api_instance.export_search_absolute_chunked(query, _from, to, fields, limit=limit, offset=offset, filter=filter)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->export_search_absolute_chunked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **_from** | **str**| Timerange start. See description for date format | 
 **to** | **str**| Timerange end. See description for date format | 
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

# **field_histogram_absolute**
> HistogramResult field_histogram_absolute(query, field, interval, _from, to, filter=filter, cardinality=cardinality)

Field value histogram of a query using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
field = 'field_example' # str | Field of whose values to get the histogram of
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
filter = 'filter_example' # str | Filter (optional)
cardinality = true # bool | Calculate the cardinality of the field as well (optional)

try:
    # Field value histogram of a query using an absolute timerange.
    api_response = api_instance.field_histogram_absolute(query, field, interval, _from, to, filter=filter, cardinality=cardinality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->field_histogram_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **field** | **str**| Field of whose values to get the histogram of | 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
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

# **histogram_absolute**
> HistogramResult histogram_absolute(query, interval, _from, to, filter=filter)

Datetime histogram of a query using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
filter = 'filter_example' # str | Filter (optional)

try:
    # Datetime histogram of a query using an absolute timerange.
    api_response = api_instance.histogram_absolute(query, interval, _from, to, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->histogram_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
 **filter** | **str**| Filter | [optional] 

### Return type

[**HistogramResult**](HistogramResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_absolute**
> SearchResponse search_absolute(query, _from, to, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)

Message search with absolute timerange.

Search for messages using an absolute timerange, specified as from/to with format yyyy-MM-ddTHH:mm:ss.SSSZ (e.g. 2014-01-23T15:34:49.000Z) or yyyy-MM-dd HH:mm:ss.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
query = 'query_example' # str | Query (Lucene syntax)
_from = '_from_example' # str | Timerange start. See description for date format
to = 'to_example' # str | Timerange end. See description for date format
limit = 56 # int | Maximum number of messages to return. (optional)
offset = 56 # int | Offset (optional)
filter = 'filter_example' # str | Filter (optional)
fields = 'fields_example' # str | Comma separated list of fields to return (optional)
sort = 'sort_example' # str | Sorting (field:asc / field:desc) (optional)
decorate = true # bool | Run decorators on search result (optional) (default to true)

try:
    # Message search with absolute timerange.
    api_response = api_instance.search_absolute(query, _from, to, limit=limit, offset=offset, filter=filter, fields=fields, sort=sort, decorate=decorate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->search_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query (Lucene syntax) | 
 **_from** | **str**| Timerange start. See description for date format | 
 **to** | **str**| Timerange end. See description for date format | 
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

# **stats_absolute**
> FieldStatsResult stats_absolute(field, query, _from, to, filter=filter)

Field statistics for a query using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of numeric type to return statistics for
query = 'query_example' # str | Query (Lucene syntax)
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
filter = 'filter_example' # str | Filter (optional)

try:
    # Field statistics for a query using an absolute timerange.
    api_response = api_instance.stats_absolute(field, query, _from, to, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->stats_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of numeric type to return statistics for | 
 **query** | **str**| Query (Lucene syntax) | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
 **filter** | **str**| Filter | [optional] 

### Return type

[**FieldStatsResult**](FieldStatsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terms_absolute**
> TermsResult terms_absolute(field, query, _from, to, stacked_fields=stacked_fields, size=size, filter=filter, order=order)

Most common field terms of a query using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of to return terms of
query = 'query_example' # str | Query (Lucene syntax)
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
stacked_fields = 'stacked_fields_example' # str | Fields to stack (optional)
size = 56 # int | Maximum number of terms to return (optional)
filter = 'filter_example' # str | Filter (optional)
order = 'order_example' # str | Sorting (field:asc / field:desc) (optional)

try:
    # Most common field terms of a query using an absolute timerange.
    api_response = api_instance.terms_absolute(field, query, _from, to, stacked_fields=stacked_fields, size=size, filter=filter, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->terms_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of to return terms of | 
 **query** | **str**| Query (Lucene syntax) | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
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

# **terms_histogram_absolute**
> TermsHistogramResult terms_histogram_absolute(field, query, size, _from, to, interval, stacked_fields=stacked_fields, filter=filter, order=order)

Most common field terms of a query over time using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
field = 'field_example' # str | Message field of to return terms of
query = 'query_example' # str | Query (Lucene syntax)
size = 56 # int | Maximum number of terms to return
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
interval = 'interval_example' # str | Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute)
stacked_fields = 'stacked_fields_example' # str | Fields to stack (optional)
filter = 'filter_example' # str | Filter (optional)
order = 'order_example' # str | Sorting (field:asc / field:desc) (optional)

try:
    # Most common field terms of a query over time using an absolute timerange.
    api_response = api_instance.terms_histogram_absolute(field, query, size, _from, to, interval, stacked_fields=stacked_fields, filter=filter, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->terms_histogram_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| Message field of to return terms of | 
 **query** | **str**| Query (Lucene syntax) | 
 **size** | **int**| Maximum number of terms to return | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
 **interval** | **str**| Histogram interval / bucket size. (year, quarter, month, week, day, hour or minute) | 
 **stacked_fields** | **str**| Fields to stack | [optional] 
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

# **terms_stats_absolute**
> TermsStatsResult terms_stats_absolute(key_field, value_field, order, query, _from, to, size=size, filter=filter)

Ordered field terms of a query computed on another field using an absolute timerange.

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
api_instance = swagger_client.SearchuniversalabsoluteApi(swagger_client.ApiClient(configuration))
key_field = 'key_field_example' # str | Message field of to return terms of
value_field = 'value_field_example' # str | Value field used for computation
order = 'order_example' # str | What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN)
query = 'query_example' # str | Query (Lucene syntax)
_from = '_from_example' # str | Timerange start. See search method description for date format
to = 'to_example' # str | Timerange end. See search method description for date format
size = 56 # int | Maximum number of terms to return (optional)
filter = 'filter_example' # str | Filter (optional)

try:
    # Ordered field terms of a query computed on another field using an absolute timerange.
    api_response = api_instance.terms_stats_absolute(key_field, value_field, order, query, _from, to, size=size, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchuniversalabsoluteApi->terms_stats_absolute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_field** | **str**| Message field of to return terms of | 
 **value_field** | **str**| Value field used for computation | 
 **order** | **str**| What to order on (Allowed values: TERM, REVERSE_TERM, COUNT, REVERSE_COUNT, TOTAL, REVERSE_TOTAL, MIN, REVERSE_MIN, MAX, REVERSE_MAX, MEAN, REVERSE_MEAN) | 
 **query** | **str**| Query (Lucene syntax) | 
 **_from** | **str**| Timerange start. See search method description for date format | 
 **to** | **str**| Timerange end. See search method description for date format | 
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

