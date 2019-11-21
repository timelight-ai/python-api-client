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

from timelight-ai-python-api-client.models.alert_dto import AlertDto  # noqa: F401,E501
from timelight-ai-python-api-client.models.prevision_dto import PrevisionDto  # noqa: F401,E501


class PrevisionBulkSaveResultDto(object):
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
        'previsions': 'list[PrevisionDto]',
        'alerts': 'list[AlertDto]'
    }

    attribute_map = {
        'previsions': 'previsions',
        'alerts': 'alerts'
    }

    def __init__(self, previsions=None, alerts=None):  # noqa: E501
        """PrevisionBulkSaveResultDto - a model defined in Swagger"""  # noqa: E501

        self._previsions = None
        self._alerts = None
        self.discriminator = None

        self.previsions = previsions
        self.alerts = alerts

    @property
    def previsions(self):
        """Gets the previsions of this PrevisionBulkSaveResultDto.  # noqa: E501

        The updated prevision objects  # noqa: E501

        :return: The previsions of this PrevisionBulkSaveResultDto.  # noqa: E501
        :rtype: list[PrevisionDto]
        """
        return self._previsions

    @previsions.setter
    def previsions(self, previsions):
        """Sets the previsions of this PrevisionBulkSaveResultDto.

        The updated prevision objects  # noqa: E501

        :param previsions: The previsions of this PrevisionBulkSaveResultDto.  # noqa: E501
        :type: list[PrevisionDto]
        """
        if previsions is None:
            raise ValueError("Invalid value for `previsions`, must not be `None`")  # noqa: E501

        self._previsions = previsions

    @property
    def alerts(self):
        """Gets the alerts of this PrevisionBulkSaveResultDto.  # noqa: E501

        List of newly created alerts  # noqa: E501

        :return: The alerts of this PrevisionBulkSaveResultDto.  # noqa: E501
        :rtype: list[AlertDto]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this PrevisionBulkSaveResultDto.

        List of newly created alerts  # noqa: E501

        :param alerts: The alerts of this PrevisionBulkSaveResultDto.  # noqa: E501
        :type: list[AlertDto]
        """
        if alerts is None:
            raise ValueError("Invalid value for `alerts`, must not be `None`")  # noqa: E501

        self._alerts = alerts

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
        if not isinstance(other, PrevisionBulkSaveResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
