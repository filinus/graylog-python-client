# coding: utf-8

"""
    127.0.0.1:9000

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.4.3+2c41897
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.histogram_result_queried_timerange import HistogramResultQueriedTimerange  # noqa: F401,E501


class TermsHistogramResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'buckets': 'object',
        'built_query': 'str',
        'interval': 'str',
        'queried_timerange': 'HistogramResultQueriedTimerange',
        'size': 'int',
        'terms': 'list[str]',
        'time': 'int'
    }

    attribute_map = {
        'buckets': 'buckets',
        'built_query': 'built_query',
        'interval': 'interval',
        'queried_timerange': 'queried_timerange',
        'size': 'size',
        'terms': 'terms',
        'time': 'time'
    }

    def __init__(self, buckets=None, built_query=None, interval=None, queried_timerange=None, size=None, terms=None, time=None):  # noqa: E501
        """TermsHistogramResult - a model defined in Swagger"""  # noqa: E501

        self._buckets = None
        self._built_query = None
        self._interval = None
        self._queried_timerange = None
        self._size = None
        self._terms = None
        self._time = None
        self.discriminator = None

        if buckets is not None:
            self.buckets = buckets
        if built_query is not None:
            self.built_query = built_query
        if interval is not None:
            self.interval = interval
        if queried_timerange is not None:
            self.queried_timerange = queried_timerange
        if size is not None:
            self.size = size
        if terms is not None:
            self.terms = terms
        if time is not None:
            self.time = time

    @property
    def buckets(self):
        """Gets the buckets of this TermsHistogramResult.  # noqa: E501


        :return: The buckets of this TermsHistogramResult.  # noqa: E501
        :rtype: object
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this TermsHistogramResult.


        :param buckets: The buckets of this TermsHistogramResult.  # noqa: E501
        :type: object
        """

        self._buckets = buckets

    @property
    def built_query(self):
        """Gets the built_query of this TermsHistogramResult.  # noqa: E501


        :return: The built_query of this TermsHistogramResult.  # noqa: E501
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """Sets the built_query of this TermsHistogramResult.


        :param built_query: The built_query of this TermsHistogramResult.  # noqa: E501
        :type: str
        """

        self._built_query = built_query

    @property
    def interval(self):
        """Gets the interval of this TermsHistogramResult.  # noqa: E501


        :return: The interval of this TermsHistogramResult.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this TermsHistogramResult.


        :param interval: The interval of this TermsHistogramResult.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def queried_timerange(self):
        """Gets the queried_timerange of this TermsHistogramResult.  # noqa: E501


        :return: The queried_timerange of this TermsHistogramResult.  # noqa: E501
        :rtype: HistogramResultQueriedTimerange
        """
        return self._queried_timerange

    @queried_timerange.setter
    def queried_timerange(self, queried_timerange):
        """Sets the queried_timerange of this TermsHistogramResult.


        :param queried_timerange: The queried_timerange of this TermsHistogramResult.  # noqa: E501
        :type: HistogramResultQueriedTimerange
        """

        self._queried_timerange = queried_timerange

    @property
    def size(self):
        """Gets the size of this TermsHistogramResult.  # noqa: E501


        :return: The size of this TermsHistogramResult.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TermsHistogramResult.


        :param size: The size of this TermsHistogramResult.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def terms(self):
        """Gets the terms of this TermsHistogramResult.  # noqa: E501


        :return: The terms of this TermsHistogramResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this TermsHistogramResult.


        :param terms: The terms of this TermsHistogramResult.  # noqa: E501
        :type: list[str]
        """

        self._terms = terms

    @property
    def time(self):
        """Gets the time of this TermsHistogramResult.  # noqa: E501


        :return: The time of this TermsHistogramResult.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TermsHistogramResult.


        :param time: The time of this TermsHistogramResult.  # noqa: E501
        :type: int
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TermsHistogramResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TermsHistogramResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
