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


class PrevisionPatchDto(object):
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
        '_date': 'str',
        'model_id': 'float'
    }

    attribute_map = {
        'source_id': 'sourceId',
        '_date': 'date',
        'model_id': 'modelId'
    }

    def __init__(self, source_id=None, _date=None, model_id=None):  # noqa: E501
        """PrevisionPatchDto - a model defined in Swagger"""  # noqa: E501

        self._source_id = None
        self.__date = None
        self._model_id = None
        self.discriminator = None

        self.source_id = source_id
        self._date = _date
        self.model_id = model_id

    @property
    def source_id(self):
        """Gets the source_id of this PrevisionPatchDto.  # noqa: E501

        The source id of the prevision to update  # noqa: E501

        :return: The source_id of this PrevisionPatchDto.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this PrevisionPatchDto.

        The source id of the prevision to update  # noqa: E501

        :param source_id: The source_id of this PrevisionPatchDto.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def _date(self):
        """Gets the _date of this PrevisionPatchDto.  # noqa: E501

        The prevision date with a format YYYY-MM-DD  # noqa: E501

        :return: The _date of this PrevisionPatchDto.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this PrevisionPatchDto.

        The prevision date with a format YYYY-MM-DD  # noqa: E501

        :param _date: The _date of this PrevisionPatchDto.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def model_id(self):
        """Gets the model_id of this PrevisionPatchDto.  # noqa: E501

        New model id to set on the prevision  # noqa: E501

        :return: The model_id of this PrevisionPatchDto.  # noqa: E501
        :rtype: float
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this PrevisionPatchDto.

        New model id to set on the prevision  # noqa: E501

        :param model_id: The model_id of this PrevisionPatchDto.  # noqa: E501
        :type: float
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

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
        if not isinstance(other, PrevisionPatchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
