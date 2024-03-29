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


class PrevisionBulkSaveDto(object):
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
        'year': 'float',
        'source_id': 'float',
        'previsions': 'list[PrevisionSaveDto]'
    }

    attribute_map = {
        'year': 'year',
        'source_id': 'sourceId',
        'previsions': 'previsions'
    }

    def __init__(self, year=None, source_id=None, previsions=None):  # noqa: E501
        """PrevisionBulkSaveDto - a model defined in Swagger"""  # noqa: E501

        self._year = None
        self._source_id = None
        self._previsions = None
        self.discriminator = None

        self.year = year
        self.source_id = source_id
        self.previsions = previsions

    @property
    def year(self):
        """Gets the year of this PrevisionBulkSaveDto.  # noqa: E501

        The year to update the prevision, must be in the future  # noqa: E501

        :return: The year of this PrevisionBulkSaveDto.  # noqa: E501
        :rtype: float
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this PrevisionBulkSaveDto.

        The year to update the prevision, must be in the future  # noqa: E501

        :param year: The year of this PrevisionBulkSaveDto.  # noqa: E501
        :type: float
        """
        if year is None:
            raise ValueError("Invalid value for `year`, must not be `None`")  # noqa: E501

        self._year = year

    @property
    def source_id(self):
        """Gets the source_id of this PrevisionBulkSaveDto.  # noqa: E501

        The source id to update previsions on  # noqa: E501

        :return: The source_id of this PrevisionBulkSaveDto.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this PrevisionBulkSaveDto.

        The source id to update previsions on  # noqa: E501

        :param source_id: The source_id of this PrevisionBulkSaveDto.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def previsions(self):
        """Gets the previsions of this PrevisionBulkSaveDto.  # noqa: E501

        List of previsions to update  # noqa: E501

        :return: The previsions of this PrevisionBulkSaveDto.  # noqa: E501
        :rtype: list[PrevisionSaveDto]
        """
        return self._previsions

    @previsions.setter
    def previsions(self, previsions):
        """Sets the previsions of this PrevisionBulkSaveDto.

        List of previsions to update  # noqa: E501

        :param previsions: The previsions of this PrevisionBulkSaveDto.  # noqa: E501
        :type: list[PrevisionSaveDto]
        """
        if previsions is None:
            raise ValueError("Invalid value for `previsions`, must not be `None`")  # noqa: E501

        self._previsions = previsions

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
        if issubclass(PrevisionBulkSaveDto, dict):
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
        if not isinstance(other, PrevisionBulkSaveDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
