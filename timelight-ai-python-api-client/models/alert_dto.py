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


class AlertDto(object):
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
        'id': 'float',
        'source_id': 'float',
        '_date': 'str',
        'criticity': 'float',
        'shape': 'bool',
        'activity': 'str',
        'better_model_id': 'float',
        'closest_model_id': 'float',
        'favorite': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'source_id': 'source_id',
        '_date': 'date',
        'criticity': 'criticity',
        'shape': 'shape',
        'activity': 'activity',
        'better_model_id': 'better_model_id',
        'closest_model_id': 'closest_model_id',
        'favorite': 'favorite'
    }

    def __init__(self, id=None, source_id=None, _date=None, criticity=None, shape=None, activity=None, better_model_id=None, closest_model_id=None, favorite=None):  # noqa: E501
        """AlertDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._source_id = None
        self.__date = None
        self._criticity = None
        self._shape = None
        self._activity = None
        self._better_model_id = None
        self._closest_model_id = None
        self._favorite = None
        self.discriminator = None

        self.id = id
        self.source_id = source_id
        self._date = _date
        self.criticity = criticity
        self.shape = shape
        self.activity = activity
        self.better_model_id = better_model_id
        self.closest_model_id = closest_model_id
        self.favorite = favorite

    @property
    def id(self):
        """Gets the id of this AlertDto.  # noqa: E501


        :return: The id of this AlertDto.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertDto.


        :param id: The id of this AlertDto.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def source_id(self):
        """Gets the source_id of this AlertDto.  # noqa: E501


        :return: The source_id of this AlertDto.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this AlertDto.


        :param source_id: The source_id of this AlertDto.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def _date(self):
        """Gets the _date of this AlertDto.  # noqa: E501


        :return: The _date of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AlertDto.


        :param _date: The _date of this AlertDto.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def criticity(self):
        """Gets the criticity of this AlertDto.  # noqa: E501


        :return: The criticity of this AlertDto.  # noqa: E501
        :rtype: float
        """
        return self._criticity

    @criticity.setter
    def criticity(self, criticity):
        """Sets the criticity of this AlertDto.


        :param criticity: The criticity of this AlertDto.  # noqa: E501
        :type: float
        """
        if criticity is None:
            raise ValueError("Invalid value for `criticity`, must not be `None`")  # noqa: E501

        self._criticity = criticity

    @property
    def shape(self):
        """Gets the shape of this AlertDto.  # noqa: E501


        :return: The shape of this AlertDto.  # noqa: E501
        :rtype: bool
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this AlertDto.


        :param shape: The shape of this AlertDto.  # noqa: E501
        :type: bool
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def activity(self):
        """Gets the activity of this AlertDto.  # noqa: E501


        :return: The activity of this AlertDto.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this AlertDto.


        :param activity: The activity of this AlertDto.  # noqa: E501
        :type: str
        """
        if activity is None:
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501
        allowed_values = ["over", "under"]  # noqa: E501
        if activity not in allowed_values:
            raise ValueError(
                "Invalid value for `activity` ({0}), must be one of {1}"  # noqa: E501
                .format(activity, allowed_values)
            )

        self._activity = activity

    @property
    def better_model_id(self):
        """Gets the better_model_id of this AlertDto.  # noqa: E501


        :return: The better_model_id of this AlertDto.  # noqa: E501
        :rtype: float
        """
        return self._better_model_id

    @better_model_id.setter
    def better_model_id(self, better_model_id):
        """Sets the better_model_id of this AlertDto.


        :param better_model_id: The better_model_id of this AlertDto.  # noqa: E501
        :type: float
        """
        if better_model_id is None:
            raise ValueError("Invalid value for `better_model_id`, must not be `None`")  # noqa: E501

        self._better_model_id = better_model_id

    @property
    def closest_model_id(self):
        """Gets the closest_model_id of this AlertDto.  # noqa: E501


        :return: The closest_model_id of this AlertDto.  # noqa: E501
        :rtype: float
        """
        return self._closest_model_id

    @closest_model_id.setter
    def closest_model_id(self, closest_model_id):
        """Sets the closest_model_id of this AlertDto.


        :param closest_model_id: The closest_model_id of this AlertDto.  # noqa: E501
        :type: float
        """
        if closest_model_id is None:
            raise ValueError("Invalid value for `closest_model_id`, must not be `None`")  # noqa: E501

        self._closest_model_id = closest_model_id

    @property
    def favorite(self):
        """Gets the favorite of this AlertDto.  # noqa: E501


        :return: The favorite of this AlertDto.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this AlertDto.


        :param favorite: The favorite of this AlertDto.  # noqa: E501
        :type: bool
        """
        if favorite is None:
            raise ValueError("Invalid value for `favorite`, must not be `None`")  # noqa: E501

        self._favorite = favorite

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
        if not isinstance(other, AlertDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
