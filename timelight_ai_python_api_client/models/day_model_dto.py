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


class DayModelDto(object):
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
        'value': 'float',
        'inertia': 'float',
        'model_id': 'float',
        'anomaly': 'bool',
        'x': 'float',
        'y': 'float',
        'activity': 'list[float]'
    }

    attribute_map = {
        '_date': 'date',
        'value': 'value',
        'inertia': 'inertia',
        'model_id': 'model_id',
        'anomaly': 'anomaly',
        'x': 'x',
        'y': 'y',
        'activity': 'activity'
    }

    def __init__(self, _date=None, value=None, inertia=None, model_id=None, anomaly=None, x=None, y=None, activity=None):  # noqa: E501
        """DayModelDto - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._value = None
        self._inertia = None
        self._model_id = None
        self._anomaly = None
        self._x = None
        self._y = None
        self._activity = None
        self.discriminator = None

        self._date = _date
        self.value = value
        self.inertia = inertia
        self.model_id = model_id
        self.anomaly = anomaly
        self.x = x
        self.y = y
        self.activity = activity

    @property
    def _date(self):
        """Gets the _date of this DayModelDto.  # noqa: E501


        :return: The _date of this DayModelDto.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DayModelDto.


        :param _date: The _date of this DayModelDto.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def value(self):
        """Gets the value of this DayModelDto.  # noqa: E501


        :return: The value of this DayModelDto.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DayModelDto.


        :param value: The value of this DayModelDto.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def inertia(self):
        """Gets the inertia of this DayModelDto.  # noqa: E501


        :return: The inertia of this DayModelDto.  # noqa: E501
        :rtype: float
        """
        return self._inertia

    @inertia.setter
    def inertia(self, inertia):
        """Sets the inertia of this DayModelDto.


        :param inertia: The inertia of this DayModelDto.  # noqa: E501
        :type: float
        """
        if inertia is None:
            raise ValueError("Invalid value for `inertia`, must not be `None`")  # noqa: E501

        self._inertia = inertia

    @property
    def model_id(self):
        """Gets the model_id of this DayModelDto.  # noqa: E501


        :return: The model_id of this DayModelDto.  # noqa: E501
        :rtype: float
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this DayModelDto.


        :param model_id: The model_id of this DayModelDto.  # noqa: E501
        :type: float
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def anomaly(self):
        """Gets the anomaly of this DayModelDto.  # noqa: E501


        :return: The anomaly of this DayModelDto.  # noqa: E501
        :rtype: bool
        """
        return self._anomaly

    @anomaly.setter
    def anomaly(self, anomaly):
        """Sets the anomaly of this DayModelDto.


        :param anomaly: The anomaly of this DayModelDto.  # noqa: E501
        :type: bool
        """
        if anomaly is None:
            raise ValueError("Invalid value for `anomaly`, must not be `None`")  # noqa: E501

        self._anomaly = anomaly

    @property
    def x(self):
        """Gets the x of this DayModelDto.  # noqa: E501


        :return: The x of this DayModelDto.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DayModelDto.


        :param x: The x of this DayModelDto.  # noqa: E501
        :type: float
        """
        if x is None:
            raise ValueError("Invalid value for `x`, must not be `None`")  # noqa: E501

        self._x = x

    @property
    def y(self):
        """Gets the y of this DayModelDto.  # noqa: E501


        :return: The y of this DayModelDto.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this DayModelDto.


        :param y: The y of this DayModelDto.  # noqa: E501
        :type: float
        """
        if y is None:
            raise ValueError("Invalid value for `y`, must not be `None`")  # noqa: E501

        self._y = y

    @property
    def activity(self):
        """Gets the activity of this DayModelDto.  # noqa: E501


        :return: The activity of this DayModelDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this DayModelDto.


        :param activity: The activity of this DayModelDto.  # noqa: E501
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
        if issubclass(DayModelDto, dict):
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
        if not isinstance(other, DayModelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
