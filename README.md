# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.4.3+2c41897
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:9000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SearchuniversalabsoluteApi* | [**export_search_absolute_chunked**](docs/SearchuniversalabsoluteApi.md#export_search_absolute_chunked) | **GET** /search/universal/absolute/export | Export message search with absolute timerange.
*SearchuniversalabsoluteApi* | [**field_histogram_absolute**](docs/SearchuniversalabsoluteApi.md#field_histogram_absolute) | **GET** /search/universal/absolute/fieldhistogram | Field value histogram of a query using an absolute timerange.
*SearchuniversalabsoluteApi* | [**histogram_absolute**](docs/SearchuniversalabsoluteApi.md#histogram_absolute) | **GET** /search/universal/absolute/histogram | Datetime histogram of a query using an absolute timerange.
*SearchuniversalabsoluteApi* | [**search_absolute**](docs/SearchuniversalabsoluteApi.md#search_absolute) | **GET** /search/universal/absolute | Message search with absolute timerange.
*SearchuniversalabsoluteApi* | [**stats_absolute**](docs/SearchuniversalabsoluteApi.md#stats_absolute) | **GET** /search/universal/absolute/stats | Field statistics for a query using an absolute timerange.
*SearchuniversalabsoluteApi* | [**terms_absolute**](docs/SearchuniversalabsoluteApi.md#terms_absolute) | **GET** /search/universal/absolute/terms | Most common field terms of a query using an absolute timerange.
*SearchuniversalabsoluteApi* | [**terms_histogram_absolute**](docs/SearchuniversalabsoluteApi.md#terms_histogram_absolute) | **GET** /search/universal/absolute/terms-histogram | Most common field terms of a query over time using an absolute timerange.
*SearchuniversalabsoluteApi* | [**terms_stats_absolute**](docs/SearchuniversalabsoluteApi.md#terms_stats_absolute) | **GET** /search/universal/absolute/termsstats | Ordered field terms of a query computed on another field using an absolute timerange.
*SearchuniversalrelativeApi* | [**export_search_relative_chunked**](docs/SearchuniversalrelativeApi.md#export_search_relative_chunked) | **GET** /search/universal/relative/export | Export message search with relative timerange.
*SearchuniversalrelativeApi* | [**field_histogram_relative**](docs/SearchuniversalrelativeApi.md#field_histogram_relative) | **GET** /search/universal/relative/fieldhistogram | Field value histogram of a query using a relative timerange.
*SearchuniversalrelativeApi* | [**histogram_relative**](docs/SearchuniversalrelativeApi.md#histogram_relative) | **GET** /search/universal/relative/histogram | Datetime histogram of a query using a relative timerange.
*SearchuniversalrelativeApi* | [**search_relative**](docs/SearchuniversalrelativeApi.md#search_relative) | **GET** /search/universal/relative | Message search with relative timerange.
*SearchuniversalrelativeApi* | [**stats_relative**](docs/SearchuniversalrelativeApi.md#stats_relative) | **GET** /search/universal/relative/stats | Field statistics for a query using a relative timerange.
*SearchuniversalrelativeApi* | [**terms_histogram_relative**](docs/SearchuniversalrelativeApi.md#terms_histogram_relative) | **GET** /search/universal/relative/terms-histogram | Most common field terms of a query over time using a relative timerange.
*SearchuniversalrelativeApi* | [**terms_relative**](docs/SearchuniversalrelativeApi.md#terms_relative) | **GET** /search/universal/relative/terms | Most common field terms of a query using a relative timerange.
*SearchuniversalrelativeApi* | [**terms_stats_relative**](docs/SearchuniversalrelativeApi.md#terms_stats_relative) | **GET** /search/universal/relative/termsstats | Ordered field terms of a query computed on another field using a relative timerange.


## Documentation For Models

 - [FieldStatsResult](docs/FieldStatsResult.md)
 - [HistogramResult](docs/HistogramResult.md)
 - [HistogramResultQueriedTimerange](docs/HistogramResultQueriedTimerange.md)
 - [SearchResponse](docs/SearchResponse.md)
 - [SearchResponseDecorationStats](docs/SearchResponseDecorationStats.md)
 - [SearchResponseDecorationStats1](docs/SearchResponseDecorationStats1.md)
 - [SearchResponseMessages](docs/SearchResponseMessages.md)
 - [SearchResponseUsedIndices](docs/SearchResponseUsedIndices.md)
 - [TermsHistogramResult](docs/TermsHistogramResult.md)
 - [TermsResult](docs/TermsResult.md)
 - [TermsStatsResult](docs/TermsStatsResult.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author



