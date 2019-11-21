# coding: utf-8

"""
    timelight

    This is the timelight api.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DayTrendListDto(object):
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
        'day_trends': 'list[DayTrend]'
    }

    attribute_map = {
        'day_trends': 'dayTrends'
    }

    def __init__(self, day_trends=None):  # noqa: E501
        """DayTrendListDto - a model defined in Swagger"""  # noqa: E501

        self._day_trends = None
        self.discriminator = None

        self.day_trends = day_trends

    @property
    def day_trends(self):
        """Gets the day_trends of this DayTrendListDto.  # noqa: E501

        List of day trends  # noqa: E501

        :return: The day_trends of this DayTrendListDto.  # noqa: E501
        :rtype: list[DayTrend]
        """
        return self._day_trends

    @day_trends.setter
    def day_trends(self, day_trends):
        """Sets the day_trends of this DayTrendListDto.

        List of day trends  # noqa: E501

        :param day_trends: The day_trends of this DayTrendListDto.  # noqa: E501
        :type: list[DayTrend]
        """
        if day_trends is None:
            raise ValueError("Invalid value for `day_trends`, must not be `None`")  # noqa: E501

        self._day_trends = day_trends

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
        if issubclass(DayTrendListDto, dict):
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
        if not isinstance(other, DayTrendListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
