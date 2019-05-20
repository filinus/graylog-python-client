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


class SearchResponseUsedIndices(object):
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
        'begin': 'datetime',
        'calculated_at': 'datetime',
        'end': 'datetime',
        'index_name': 'str',
        'took_ms': 'int'
    }

    attribute_map = {
        'begin': 'begin',
        'calculated_at': 'calculated_at',
        'end': 'end',
        'index_name': 'index_name',
        'took_ms': 'took_ms'
    }

    def __init__(self, begin=None, calculated_at=None, end=None, index_name=None, took_ms=None):  # noqa: E501
        """SearchResponseUsedIndices - a model defined in Swagger"""  # noqa: E501

        self._begin = None
        self._calculated_at = None
        self._end = None
        self._index_name = None
        self._took_ms = None
        self.discriminator = None

        if begin is not None:
            self.begin = begin
        if calculated_at is not None:
            self.calculated_at = calculated_at
        if end is not None:
            self.end = end
        if index_name is not None:
            self.index_name = index_name
        if took_ms is not None:
            self.took_ms = took_ms

    @property
    def begin(self):
        """Gets the begin of this SearchResponseUsedIndices.  # noqa: E501


        :return: The begin of this SearchResponseUsedIndices.  # noqa: E501
        :rtype: datetime
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this SearchResponseUsedIndices.


        :param begin: The begin of this SearchResponseUsedIndices.  # noqa: E501
        :type: datetime
        """

        self._begin = begin

    @property
    def calculated_at(self):
        """Gets the calculated_at of this SearchResponseUsedIndices.  # noqa: E501


        :return: The calculated_at of this SearchResponseUsedIndices.  # noqa: E501
        :rtype: datetime
        """
        return self._calculated_at

    @calculated_at.setter
    def calculated_at(self, calculated_at):
        """Sets the calculated_at of this SearchResponseUsedIndices.


        :param calculated_at: The calculated_at of this SearchResponseUsedIndices.  # noqa: E501
        :type: datetime
        """

        self._calculated_at = calculated_at

    @property
    def end(self):
        """Gets the end of this SearchResponseUsedIndices.  # noqa: E501


        :return: The end of this SearchResponseUsedIndices.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SearchResponseUsedIndices.


        :param end: The end of this SearchResponseUsedIndices.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def index_name(self):
        """Gets the index_name of this SearchResponseUsedIndices.  # noqa: E501


        :return: The index_name of this SearchResponseUsedIndices.  # noqa: E501
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this SearchResponseUsedIndices.


        :param index_name: The index_name of this SearchResponseUsedIndices.  # noqa: E501
        :type: str
        """

        self._index_name = index_name

    @property
    def took_ms(self):
        """Gets the took_ms of this SearchResponseUsedIndices.  # noqa: E501


        :return: The took_ms of this SearchResponseUsedIndices.  # noqa: E501
        :rtype: int
        """
        return self._took_ms

    @took_ms.setter
    def took_ms(self, took_ms):
        """Sets the took_ms of this SearchResponseUsedIndices.


        :param took_ms: The took_ms of this SearchResponseUsedIndices.  # noqa: E501
        :type: int
        """

        self._took_ms = took_ms

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
        if issubclass(SearchResponseUsedIndices, dict):
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
        if not isinstance(other, SearchResponseUsedIndices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other