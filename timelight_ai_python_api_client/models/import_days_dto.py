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


class ImportDaysDto(object):
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
        'source_id': 'float',
        'days': 'list[ImportDayDto]'
    }

    attribute_map = {
        'source_id': 'sourceId',
        'days': 'days'
    }

    def __init__(self, source_id=None, days=None):  # noqa: E501
        """ImportDaysDto - a model defined in Swagger"""  # noqa: E501

        self._source_id = None
        self._days = None
        self.discriminator = None

        self.source_id = source_id
        self.days = days

    @property
    def source_id(self):
        """Gets the source_id of this ImportDaysDto.  # noqa: E501

        The source id to add data to  # noqa: E501

        :return: The source_id of this ImportDaysDto.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this ImportDaysDto.

        The source id to add data to  # noqa: E501

        :param source_id: The source_id of this ImportDaysDto.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def days(self):
        """Gets the days of this ImportDaysDto.  # noqa: E501

        The list of days to add  # noqa: E501

        :return: The days of this ImportDaysDto.  # noqa: E501
        :rtype: list[ImportDayDto]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this ImportDaysDto.

        The list of days to add  # noqa: E501

        :param days: The days of this ImportDaysDto.  # noqa: E501
        :type: list[ImportDayDto]
        """
        if days is None:
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

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
        if issubclass(ImportDaysDto, dict):
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
        if not isinstance(other, ImportDaysDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
