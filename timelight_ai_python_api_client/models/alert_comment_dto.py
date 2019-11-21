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


class AlertCommentDto(object):
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
        'comment': 'str'
    }

    attribute_map = {
        'comment': 'comment'
    }

    def __init__(self, comment=None):  # noqa: E501
        """AlertCommentDto - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self.discriminator = None

        self.comment = comment

    @property
    def comment(self):
        """Gets the comment of this AlertCommentDto.  # noqa: E501

        The text comment to set on the alert, max of 5000 characters  # noqa: E501

        :return: The comment of this AlertCommentDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AlertCommentDto.

        The text comment to set on the alert, max of 5000 characters  # noqa: E501

        :param comment: The comment of this AlertCommentDto.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

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
        if issubclass(AlertCommentDto, dict):
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
        if not isinstance(other, AlertCommentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
