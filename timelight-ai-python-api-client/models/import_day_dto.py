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


class ImportDayDto(object):
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
        '_date': 'str',
        'activity': 'list[float]'
    }

    attribute_map = {
        '_date': 'date',
        'activity': 'activity'
    }

    def __init__(self, _date=None, activity=None):  # noqa: E501
        """ImportDayDto - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._activity = None
        self.discriminator = None

        self._date = _date
        self.activity = activity

    @property
    def _date(self):
        """Gets the _date of this ImportDayDto.  # noqa: E501

        The date with a format YYYY-MM-DD  # noqa: E501

        :return: The _date of this ImportDayDto.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ImportDayDto.

        The date with a format YYYY-MM-DD  # noqa: E501

        :param _date: The _date of this ImportDayDto.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def activity(self):
        """Gets the activity of this ImportDayDto.  # noqa: E501

        An array of 144 values. Each value represents a time window of 10 minutes  # noqa: E501

        :return: The activity of this ImportDayDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ImportDayDto.

        An array of 144 values. Each value represents a time window of 10 minutes  # noqa: E501

        :param activity: The activity of this ImportDayDto.  # noqa: E501
        :type: list[float]
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501

        self._activity = activity

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportDayDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
