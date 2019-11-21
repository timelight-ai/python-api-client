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


class AlertRefListDto(object):
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
        'alert_refs': 'list[AlertRefDto]'
    }

    attribute_map = {
        'alert_refs': 'alertRefs'
    }

    def __init__(self, alert_refs=None):  # noqa: E501
        """AlertRefListDto - a model defined in Swagger"""  # noqa: E501

        self._alert_refs = None
        self.discriminator = None

        self.alert_refs = alert_refs

    @property
    def alert_refs(self):
        """Gets the alert_refs of this AlertRefListDto.  # noqa: E501

        List of alerts refs  # noqa: E501

        :return: The alert_refs of this AlertRefListDto.  # noqa: E501
        :rtype: list[AlertRefDto]
        """
        return self._alert_refs

    @alert_refs.setter
    def alert_refs(self, alert_refs):
        """Sets the alert_refs of this AlertRefListDto.

        List of alerts refs  # noqa: E501

        :param alert_refs: The alert_refs of this AlertRefListDto.  # noqa: E501
        :type: list[AlertRefDto]
        """
        if alert_refs is None:
            raise ValueError("Invalid value for `alert_refs`, must not be `None`")  # noqa: E501

        self._alert_refs = alert_refs

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
        if issubclass(AlertRefListDto, dict):
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
        if not isinstance(other, AlertRefListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
