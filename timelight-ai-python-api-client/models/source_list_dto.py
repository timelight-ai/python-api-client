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

from timelight-ai-python-api-client.models.source_dto import SourceDto  # noqa: F401,E501


class SourceListDto(object):
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
        'sources': 'list[SourceDto]'
    }

    attribute_map = {
        'sources': 'sources'
    }

    def __init__(self, sources=None):  # noqa: E501
        """SourceListDto - a model defined in Swagger"""  # noqa: E501

        self._sources = None
        self.discriminator = None

        self.sources = sources

    @property
    def sources(self):
        """Gets the sources of this SourceListDto.  # noqa: E501


        :return: The sources of this SourceListDto.  # noqa: E501
        :rtype: list[SourceDto]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this SourceListDto.


        :param sources: The sources of this SourceListDto.  # noqa: E501
        :type: list[SourceDto]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")  # noqa: E501

        self._sources = sources

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
        if not isinstance(other, SourceListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
