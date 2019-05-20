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


class FieldStatsResult(object):
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
        'built_query': 'str',
        'cardinality': 'int',
        'count': 'int',
        'max': 'float',
        'mean': 'float',
        'min': 'float',
        'std_deviation': 'float',
        'sum': 'float',
        'sum_of_squares': 'float',
        'time': 'int',
        'variance': 'float'
    }

    attribute_map = {
        'built_query': 'built_query',
        'cardinality': 'cardinality',
        'count': 'count',
        'max': 'max',
        'mean': 'mean',
        'min': 'min',
        'std_deviation': 'std_deviation',
        'sum': 'sum',
        'sum_of_squares': 'sum_of_squares',
        'time': 'time',
        'variance': 'variance'
    }

    def __init__(self, built_query=None, cardinality=None, count=None, max=None, mean=None, min=None, std_deviation=None, sum=None, sum_of_squares=None, time=None, variance=None):  # noqa: E501
        """FieldStatsResult - a model defined in Swagger"""  # noqa: E501

        self._built_query = None
        self._cardinality = None
        self._count = None
        self._max = None
        self._mean = None
        self._min = None
        self._std_deviation = None
        self._sum = None
        self._sum_of_squares = None
        self._time = None
        self._variance = None
        self.discriminator = None

        if built_query is not None:
            self.built_query = built_query
        if cardinality is not None:
            self.cardinality = cardinality
        if count is not None:
            self.count = count
        if max is not None:
            self.max = max
        if mean is not None:
            self.mean = mean
        if min is not None:
            self.min = min
        if std_deviation is not None:
            self.std_deviation = std_deviation
        if sum is not None:
            self.sum = sum
        if sum_of_squares is not None:
            self.sum_of_squares = sum_of_squares
        if time is not None:
            self.time = time
        if variance is not None:
            self.variance = variance

    @property
    def built_query(self):
        """Gets the built_query of this FieldStatsResult.  # noqa: E501


        :return: The built_query of this FieldStatsResult.  # noqa: E501
        :rtype: str
        """
        return self._built_query

    @built_query.setter
    def built_query(self, built_query):
        """Sets the built_query of this FieldStatsResult.


        :param built_query: The built_query of this FieldStatsResult.  # noqa: E501
        :type: str
        """

        self._built_query = built_query

    @property
    def cardinality(self):
        """Gets the cardinality of this FieldStatsResult.  # noqa: E501


        :return: The cardinality of this FieldStatsResult.  # noqa: E501
        :rtype: int
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """Sets the cardinality of this FieldStatsResult.


        :param cardinality: The cardinality of this FieldStatsResult.  # noqa: E501
        :type: int
        """

        self._cardinality = cardinality

    @property
    def count(self):
        """Gets the count of this FieldStatsResult.  # noqa: E501


        :return: The count of this FieldStatsResult.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this FieldStatsResult.


        :param count: The count of this FieldStatsResult.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def max(self):
        """Gets the max of this FieldStatsResult.  # noqa: E501


        :return: The max of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this FieldStatsResult.


        :param max: The max of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._max = max

    @property
    def mean(self):
        """Gets the mean of this FieldStatsResult.  # noqa: E501


        :return: The mean of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._mean

    @mean.setter
    def mean(self, mean):
        """Sets the mean of this FieldStatsResult.


        :param mean: The mean of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._mean = mean

    @property
    def min(self):
        """Gets the min of this FieldStatsResult.  # noqa: E501


        :return: The min of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this FieldStatsResult.


        :param min: The min of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._min = min

    @property
    def std_deviation(self):
        """Gets the std_deviation of this FieldStatsResult.  # noqa: E501


        :return: The std_deviation of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._std_deviation

    @std_deviation.setter
    def std_deviation(self, std_deviation):
        """Sets the std_deviation of this FieldStatsResult.


        :param std_deviation: The std_deviation of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._std_deviation = std_deviation

    @property
    def sum(self):
        """Gets the sum of this FieldStatsResult.  # noqa: E501


        :return: The sum of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """Sets the sum of this FieldStatsResult.


        :param sum: The sum of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._sum = sum

    @property
    def sum_of_squares(self):
        """Gets the sum_of_squares of this FieldStatsResult.  # noqa: E501


        :return: The sum_of_squares of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._sum_of_squares

    @sum_of_squares.setter
    def sum_of_squares(self, sum_of_squares):
        """Sets the sum_of_squares of this FieldStatsResult.


        :param sum_of_squares: The sum_of_squares of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._sum_of_squares = sum_of_squares

    @property
    def time(self):
        """Gets the time of this FieldStatsResult.  # noqa: E501


        :return: The time of this FieldStatsResult.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FieldStatsResult.


        :param time: The time of this FieldStatsResult.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def variance(self):
        """Gets the variance of this FieldStatsResult.  # noqa: E501


        :return: The variance of this FieldStatsResult.  # noqa: E501
        :rtype: float
        """
        return self._variance

    @variance.setter
    def variance(self, variance):
        """Sets the variance of this FieldStatsResult.


        :param variance: The variance of this FieldStatsResult.  # noqa: E501
        :type: float
        """

        self._variance = variance

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
        if issubclass(FieldStatsResult, dict):
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
        if not isinstance(other, FieldStatsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other