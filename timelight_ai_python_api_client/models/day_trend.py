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


class DayTrend(object):
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
        'created_date': 'str',
        'updated_date': 'str',
        'source_id': 'float',
        'start_day_date': 'str',
        'stop_day_date': 'str',
        'unit': 'str',
        'type': 'str',
        'value': 'float'
    }

    attribute_map = {
        'id': 'id',
        'created_date': 'createdDate',
        'updated_date': 'updatedDate',
        'source_id': 'sourceId',
        'start_day_date': 'startDayDate',
        'stop_day_date': 'stopDayDate',
        'unit': 'unit',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, id=None, created_date=None, updated_date=None, source_id=None, start_day_date=None, stop_day_date=None, unit=None, type=None, value=None):  # noqa: E501
        """DayTrend - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_date = None
        self._updated_date = None
        self._source_id = None
        self._start_day_date = None
        self._stop_day_date = None
        self._unit = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.source_id = source_id
        self.start_day_date = start_day_date
        self.stop_day_date = stop_day_date
        self.unit = unit
        self.type = type
        self.value = value

    @property
    def id(self):
        """Gets the id of this DayTrend.  # noqa: E501


        :return: The id of this DayTrend.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DayTrend.


        :param id: The id of this DayTrend.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_date(self):
        """Gets the created_date of this DayTrend.  # noqa: E501


        :return: The created_date of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this DayTrend.


        :param created_date: The created_date of this DayTrend.  # noqa: E501
        :type: str
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def updated_date(self):
        """Gets the updated_date of this DayTrend.  # noqa: E501


        :return: The updated_date of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this DayTrend.


        :param updated_date: The updated_date of this DayTrend.  # noqa: E501
        :type: str
        """
        if updated_date is None:
            raise ValueError("Invalid value for `updated_date`, must not be `None`")  # noqa: E501

        self._updated_date = updated_date

    @property
    def source_id(self):
        """Gets the source_id of this DayTrend.  # noqa: E501


        :return: The source_id of this DayTrend.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this DayTrend.


        :param source_id: The source_id of this DayTrend.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def start_day_date(self):
        """Gets the start_day_date of this DayTrend.  # noqa: E501


        :return: The start_day_date of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._start_day_date

    @start_day_date.setter
    def start_day_date(self, start_day_date):
        """Sets the start_day_date of this DayTrend.


        :param start_day_date: The start_day_date of this DayTrend.  # noqa: E501
        :type: str
        """
        if start_day_date is None:
            raise ValueError("Invalid value for `start_day_date`, must not be `None`")  # noqa: E501

        self._start_day_date = start_day_date

    @property
    def stop_day_date(self):
        """Gets the stop_day_date of this DayTrend.  # noqa: E501


        :return: The stop_day_date of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._stop_day_date

    @stop_day_date.setter
    def stop_day_date(self, stop_day_date):
        """Sets the stop_day_date of this DayTrend.


        :param stop_day_date: The stop_day_date of this DayTrend.  # noqa: E501
        :type: str
        """
        if stop_day_date is None:
            raise ValueError("Invalid value for `stop_day_date`, must not be `None`")  # noqa: E501

        self._stop_day_date = stop_day_date

    @property
    def unit(self):
        """Gets the unit of this DayTrend.  # noqa: E501


        :return: The unit of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DayTrend.


        :param unit: The unit of this DayTrend.  # noqa: E501
        :type: str
        """
        if unit is None:
            raise ValueError("Invalid value for `unit`, must not be `None`")  # noqa: E501
        allowed_values = ["percent", "unit"]  # noqa: E501
        if unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def type(self):
        """Gets the type of this DayTrend.  # noqa: E501


        :return: The type of this DayTrend.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DayTrend.


        :param type: The type of this DayTrend.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["one-shot", "weekly", "monthly"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this DayTrend.  # noqa: E501


        :return: The value of this DayTrend.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DayTrend.


        :param value: The value of this DayTrend.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(DayTrend, dict):
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
        if not isinstance(other, DayTrend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
