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


class AlertRefDto(object):
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
        'comment': 'str',
        'day_activity': 'list[float]',
        'better_model_name': 'str',
        'better_model_value': 'float',
        'better_model_color': 'str',
        'better_model_activity': 'list[float]',
        'better_model_top_tolerance': 'list[float]',
        'better_model_bottom_tolerance': 'list[float]',
        'closest_model_name': 'str',
        'closest_model_value': 'float',
        'closest_model_color': 'str',
        'closest_model_activity': 'list[float]',
        'closest_model_top_tolerance': 'list[float]',
        'closest_model_bottom_tolerance': 'list[float]',
        'day_model_name': 'str',
        'day_model_value': 'float',
        'day_model_color': 'str',
        'day_model_activity': 'list[float]',
        'day_model_top_tolerance': 'list[float]',
        'day_model_bottom_tolerance': 'list[float]',
        'day_prevision_model_name': 'str',
        'day_prevision_model_value': 'float',
        'day_prevision_model_color': 'str',
        'day_prevision_model_activity': 'list[float]',
        'day_prevision_model_top_tolerance': 'list[float]',
        'day_prevision_model_bottom_tolerance': 'list[float]'
    }

    attribute_map = {
        'id': 'id',
        'source_id': 'source_id',
        '_date': 'date',
        'criticity': 'criticity',
        'shape': 'shape',
        'activity': 'activity',
        'comment': 'comment',
        'day_activity': 'dayActivity',
        'better_model_name': 'betterModelName',
        'better_model_value': 'betterModelValue',
        'better_model_color': 'betterModelColor',
        'better_model_activity': 'betterModelActivity',
        'better_model_top_tolerance': 'betterModelTopTolerance',
        'better_model_bottom_tolerance': 'betterModelBottomTolerance',
        'closest_model_name': 'closestModelName',
        'closest_model_value': 'closestModelValue',
        'closest_model_color': 'closestModelColor',
        'closest_model_activity': 'closestModelActivity',
        'closest_model_top_tolerance': 'closestModelTopTolerance',
        'closest_model_bottom_tolerance': 'closestModelBottomTolerance',
        'day_model_name': 'dayModelName',
        'day_model_value': 'dayModelValue',
        'day_model_color': 'dayModelColor',
        'day_model_activity': 'dayModelActivity',
        'day_model_top_tolerance': 'dayModelTopTolerance',
        'day_model_bottom_tolerance': 'dayModelBottomTolerance',
        'day_prevision_model_name': 'dayPrevisionModelName',
        'day_prevision_model_value': 'dayPrevisionModelValue',
        'day_prevision_model_color': 'dayPrevisionModelColor',
        'day_prevision_model_activity': 'dayPrevisionModelActivity',
        'day_prevision_model_top_tolerance': 'dayPrevisionModelTopTolerance',
        'day_prevision_model_bottom_tolerance': 'dayPrevisionModelBottomTolerance'
    }

    def __init__(self, id=None, source_id=None, _date=None, criticity=None, shape=None, activity=None, comment=None, day_activity=None, better_model_name=None, better_model_value=None, better_model_color=None, better_model_activity=None, better_model_top_tolerance=None, better_model_bottom_tolerance=None, closest_model_name=None, closest_model_value=None, closest_model_color=None, closest_model_activity=None, closest_model_top_tolerance=None, closest_model_bottom_tolerance=None, day_model_name=None, day_model_value=None, day_model_color=None, day_model_activity=None, day_model_top_tolerance=None, day_model_bottom_tolerance=None, day_prevision_model_name=None, day_prevision_model_value=None, day_prevision_model_color=None, day_prevision_model_activity=None, day_prevision_model_top_tolerance=None, day_prevision_model_bottom_tolerance=None):  # noqa: E501
        """AlertRefDto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._source_id = None
        self.__date = None
        self._criticity = None
        self._shape = None
        self._activity = None
        self._comment = None
        self._day_activity = None
        self._better_model_name = None
        self._better_model_value = None
        self._better_model_color = None
        self._better_model_activity = None
        self._better_model_top_tolerance = None
        self._better_model_bottom_tolerance = None
        self._closest_model_name = None
        self._closest_model_value = None
        self._closest_model_color = None
        self._closest_model_activity = None
        self._closest_model_top_tolerance = None
        self._closest_model_bottom_tolerance = None
        self._day_model_name = None
        self._day_model_value = None
        self._day_model_color = None
        self._day_model_activity = None
        self._day_model_top_tolerance = None
        self._day_model_bottom_tolerance = None
        self._day_prevision_model_name = None
        self._day_prevision_model_value = None
        self._day_prevision_model_color = None
        self._day_prevision_model_activity = None
        self._day_prevision_model_top_tolerance = None
        self._day_prevision_model_bottom_tolerance = None
        self.discriminator = None

        self.id = id
        self.source_id = source_id
        self._date = _date
        self.criticity = criticity
        self.shape = shape
        self.activity = activity
        self.comment = comment
        self.day_activity = day_activity
        self.better_model_name = better_model_name
        self.better_model_value = better_model_value
        self.better_model_color = better_model_color
        self.better_model_activity = better_model_activity
        self.better_model_top_tolerance = better_model_top_tolerance
        self.better_model_bottom_tolerance = better_model_bottom_tolerance
        self.closest_model_name = closest_model_name
        self.closest_model_value = closest_model_value
        self.closest_model_color = closest_model_color
        self.closest_model_activity = closest_model_activity
        self.closest_model_top_tolerance = closest_model_top_tolerance
        self.closest_model_bottom_tolerance = closest_model_bottom_tolerance
        self.day_model_name = day_model_name
        self.day_model_value = day_model_value
        self.day_model_color = day_model_color
        self.day_model_activity = day_model_activity
        self.day_model_top_tolerance = day_model_top_tolerance
        self.day_model_bottom_tolerance = day_model_bottom_tolerance
        self.day_prevision_model_name = day_prevision_model_name
        self.day_prevision_model_value = day_prevision_model_value
        self.day_prevision_model_color = day_prevision_model_color
        self.day_prevision_model_activity = day_prevision_model_activity
        self.day_prevision_model_top_tolerance = day_prevision_model_top_tolerance
        self.day_prevision_model_bottom_tolerance = day_prevision_model_bottom_tolerance

    @property
    def id(self):
        """Gets the id of this AlertRefDto.  # noqa: E501


        :return: The id of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertRefDto.


        :param id: The id of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def source_id(self):
        """Gets the source_id of this AlertRefDto.  # noqa: E501


        :return: The source_id of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this AlertRefDto.


        :param source_id: The source_id of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def _date(self):
        """Gets the _date of this AlertRefDto.  # noqa: E501


        :return: The _date of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AlertRefDto.


        :param _date: The _date of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def criticity(self):
        """Gets the criticity of this AlertRefDto.  # noqa: E501


        :return: The criticity of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._criticity

    @criticity.setter
    def criticity(self, criticity):
        """Sets the criticity of this AlertRefDto.


        :param criticity: The criticity of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if criticity is None:
            raise ValueError("Invalid value for `criticity`, must not be `None`")  # noqa: E501

        self._criticity = criticity

    @property
    def shape(self):
        """Gets the shape of this AlertRefDto.  # noqa: E501


        :return: The shape of this AlertRefDto.  # noqa: E501
        :rtype: bool
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this AlertRefDto.


        :param shape: The shape of this AlertRefDto.  # noqa: E501
        :type: bool
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def activity(self):
        """Gets the activity of this AlertRefDto.  # noqa: E501


        :return: The activity of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this AlertRefDto.


        :param activity: The activity of this AlertRefDto.  # noqa: E501
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
    def comment(self):
        """Gets the comment of this AlertRefDto.  # noqa: E501


        :return: The comment of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AlertRefDto.


        :param comment: The comment of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def day_activity(self):
        """Gets the day_activity of this AlertRefDto.  # noqa: E501


        :return: The day_activity of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_activity

    @day_activity.setter
    def day_activity(self, day_activity):
        """Sets the day_activity of this AlertRefDto.


        :param day_activity: The day_activity of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_activity is None:
            raise ValueError("Invalid value for `day_activity`, must not be `None`")  # noqa: E501

        self._day_activity = day_activity

    @property
    def better_model_name(self):
        """Gets the better_model_name of this AlertRefDto.  # noqa: E501


        :return: The better_model_name of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._better_model_name

    @better_model_name.setter
    def better_model_name(self, better_model_name):
        """Sets the better_model_name of this AlertRefDto.


        :param better_model_name: The better_model_name of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if better_model_name is None:
            raise ValueError("Invalid value for `better_model_name`, must not be `None`")  # noqa: E501

        self._better_model_name = better_model_name

    @property
    def better_model_value(self):
        """Gets the better_model_value of this AlertRefDto.  # noqa: E501


        :return: The better_model_value of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._better_model_value

    @better_model_value.setter
    def better_model_value(self, better_model_value):
        """Sets the better_model_value of this AlertRefDto.


        :param better_model_value: The better_model_value of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if better_model_value is None:
            raise ValueError("Invalid value for `better_model_value`, must not be `None`")  # noqa: E501

        self._better_model_value = better_model_value

    @property
    def better_model_color(self):
        """Gets the better_model_color of this AlertRefDto.  # noqa: E501


        :return: The better_model_color of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._better_model_color

    @better_model_color.setter
    def better_model_color(self, better_model_color):
        """Sets the better_model_color of this AlertRefDto.


        :param better_model_color: The better_model_color of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if better_model_color is None:
            raise ValueError("Invalid value for `better_model_color`, must not be `None`")  # noqa: E501

        self._better_model_color = better_model_color

    @property
    def better_model_activity(self):
        """Gets the better_model_activity of this AlertRefDto.  # noqa: E501


        :return: The better_model_activity of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._better_model_activity

    @better_model_activity.setter
    def better_model_activity(self, better_model_activity):
        """Sets the better_model_activity of this AlertRefDto.


        :param better_model_activity: The better_model_activity of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if better_model_activity is None:
            raise ValueError("Invalid value for `better_model_activity`, must not be `None`")  # noqa: E501

        self._better_model_activity = better_model_activity

    @property
    def better_model_top_tolerance(self):
        """Gets the better_model_top_tolerance of this AlertRefDto.  # noqa: E501


        :return: The better_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._better_model_top_tolerance

    @better_model_top_tolerance.setter
    def better_model_top_tolerance(self, better_model_top_tolerance):
        """Sets the better_model_top_tolerance of this AlertRefDto.


        :param better_model_top_tolerance: The better_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if better_model_top_tolerance is None:
            raise ValueError("Invalid value for `better_model_top_tolerance`, must not be `None`")  # noqa: E501

        self._better_model_top_tolerance = better_model_top_tolerance

    @property
    def better_model_bottom_tolerance(self):
        """Gets the better_model_bottom_tolerance of this AlertRefDto.  # noqa: E501


        :return: The better_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._better_model_bottom_tolerance

    @better_model_bottom_tolerance.setter
    def better_model_bottom_tolerance(self, better_model_bottom_tolerance):
        """Sets the better_model_bottom_tolerance of this AlertRefDto.


        :param better_model_bottom_tolerance: The better_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if better_model_bottom_tolerance is None:
            raise ValueError("Invalid value for `better_model_bottom_tolerance`, must not be `None`")  # noqa: E501

        self._better_model_bottom_tolerance = better_model_bottom_tolerance

    @property
    def closest_model_name(self):
        """Gets the closest_model_name of this AlertRefDto.  # noqa: E501


        :return: The closest_model_name of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._closest_model_name

    @closest_model_name.setter
    def closest_model_name(self, closest_model_name):
        """Sets the closest_model_name of this AlertRefDto.


        :param closest_model_name: The closest_model_name of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if closest_model_name is None:
            raise ValueError("Invalid value for `closest_model_name`, must not be `None`")  # noqa: E501

        self._closest_model_name = closest_model_name

    @property
    def closest_model_value(self):
        """Gets the closest_model_value of this AlertRefDto.  # noqa: E501


        :return: The closest_model_value of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._closest_model_value

    @closest_model_value.setter
    def closest_model_value(self, closest_model_value):
        """Sets the closest_model_value of this AlertRefDto.


        :param closest_model_value: The closest_model_value of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if closest_model_value is None:
            raise ValueError("Invalid value for `closest_model_value`, must not be `None`")  # noqa: E501

        self._closest_model_value = closest_model_value

    @property
    def closest_model_color(self):
        """Gets the closest_model_color of this AlertRefDto.  # noqa: E501


        :return: The closest_model_color of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._closest_model_color

    @closest_model_color.setter
    def closest_model_color(self, closest_model_color):
        """Sets the closest_model_color of this AlertRefDto.


        :param closest_model_color: The closest_model_color of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if closest_model_color is None:
            raise ValueError("Invalid value for `closest_model_color`, must not be `None`")  # noqa: E501

        self._closest_model_color = closest_model_color

    @property
    def closest_model_activity(self):
        """Gets the closest_model_activity of this AlertRefDto.  # noqa: E501


        :return: The closest_model_activity of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._closest_model_activity

    @closest_model_activity.setter
    def closest_model_activity(self, closest_model_activity):
        """Sets the closest_model_activity of this AlertRefDto.


        :param closest_model_activity: The closest_model_activity of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if closest_model_activity is None:
            raise ValueError("Invalid value for `closest_model_activity`, must not be `None`")  # noqa: E501

        self._closest_model_activity = closest_model_activity

    @property
    def closest_model_top_tolerance(self):
        """Gets the closest_model_top_tolerance of this AlertRefDto.  # noqa: E501


        :return: The closest_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._closest_model_top_tolerance

    @closest_model_top_tolerance.setter
    def closest_model_top_tolerance(self, closest_model_top_tolerance):
        """Sets the closest_model_top_tolerance of this AlertRefDto.


        :param closest_model_top_tolerance: The closest_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if closest_model_top_tolerance is None:
            raise ValueError("Invalid value for `closest_model_top_tolerance`, must not be `None`")  # noqa: E501

        self._closest_model_top_tolerance = closest_model_top_tolerance

    @property
    def closest_model_bottom_tolerance(self):
        """Gets the closest_model_bottom_tolerance of this AlertRefDto.  # noqa: E501


        :return: The closest_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._closest_model_bottom_tolerance

    @closest_model_bottom_tolerance.setter
    def closest_model_bottom_tolerance(self, closest_model_bottom_tolerance):
        """Sets the closest_model_bottom_tolerance of this AlertRefDto.


        :param closest_model_bottom_tolerance: The closest_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if closest_model_bottom_tolerance is None:
            raise ValueError("Invalid value for `closest_model_bottom_tolerance`, must not be `None`")  # noqa: E501

        self._closest_model_bottom_tolerance = closest_model_bottom_tolerance

    @property
    def day_model_name(self):
        """Gets the day_model_name of this AlertRefDto.  # noqa: E501


        :return: The day_model_name of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._day_model_name

    @day_model_name.setter
    def day_model_name(self, day_model_name):
        """Sets the day_model_name of this AlertRefDto.


        :param day_model_name: The day_model_name of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if day_model_name is None:
            raise ValueError("Invalid value for `day_model_name`, must not be `None`")  # noqa: E501

        self._day_model_name = day_model_name

    @property
    def day_model_value(self):
        """Gets the day_model_value of this AlertRefDto.  # noqa: E501


        :return: The day_model_value of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._day_model_value

    @day_model_value.setter
    def day_model_value(self, day_model_value):
        """Sets the day_model_value of this AlertRefDto.


        :param day_model_value: The day_model_value of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if day_model_value is None:
            raise ValueError("Invalid value for `day_model_value`, must not be `None`")  # noqa: E501

        self._day_model_value = day_model_value

    @property
    def day_model_color(self):
        """Gets the day_model_color of this AlertRefDto.  # noqa: E501


        :return: The day_model_color of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._day_model_color

    @day_model_color.setter
    def day_model_color(self, day_model_color):
        """Sets the day_model_color of this AlertRefDto.


        :param day_model_color: The day_model_color of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if day_model_color is None:
            raise ValueError("Invalid value for `day_model_color`, must not be `None`")  # noqa: E501

        self._day_model_color = day_model_color

    @property
    def day_model_activity(self):
        """Gets the day_model_activity of this AlertRefDto.  # noqa: E501


        :return: The day_model_activity of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_model_activity

    @day_model_activity.setter
    def day_model_activity(self, day_model_activity):
        """Sets the day_model_activity of this AlertRefDto.


        :param day_model_activity: The day_model_activity of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_model_activity is None:
            raise ValueError("Invalid value for `day_model_activity`, must not be `None`")  # noqa: E501

        self._day_model_activity = day_model_activity

    @property
    def day_model_top_tolerance(self):
        """Gets the day_model_top_tolerance of this AlertRefDto.  # noqa: E501


        :return: The day_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_model_top_tolerance

    @day_model_top_tolerance.setter
    def day_model_top_tolerance(self, day_model_top_tolerance):
        """Sets the day_model_top_tolerance of this AlertRefDto.


        :param day_model_top_tolerance: The day_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_model_top_tolerance is None:
            raise ValueError("Invalid value for `day_model_top_tolerance`, must not be `None`")  # noqa: E501

        self._day_model_top_tolerance = day_model_top_tolerance

    @property
    def day_model_bottom_tolerance(self):
        """Gets the day_model_bottom_tolerance of this AlertRefDto.  # noqa: E501


        :return: The day_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_model_bottom_tolerance

    @day_model_bottom_tolerance.setter
    def day_model_bottom_tolerance(self, day_model_bottom_tolerance):
        """Sets the day_model_bottom_tolerance of this AlertRefDto.


        :param day_model_bottom_tolerance: The day_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_model_bottom_tolerance is None:
            raise ValueError("Invalid value for `day_model_bottom_tolerance`, must not be `None`")  # noqa: E501

        self._day_model_bottom_tolerance = day_model_bottom_tolerance

    @property
    def day_prevision_model_name(self):
        """Gets the day_prevision_model_name of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_name of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._day_prevision_model_name

    @day_prevision_model_name.setter
    def day_prevision_model_name(self, day_prevision_model_name):
        """Sets the day_prevision_model_name of this AlertRefDto.


        :param day_prevision_model_name: The day_prevision_model_name of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if day_prevision_model_name is None:
            raise ValueError("Invalid value for `day_prevision_model_name`, must not be `None`")  # noqa: E501

        self._day_prevision_model_name = day_prevision_model_name

    @property
    def day_prevision_model_value(self):
        """Gets the day_prevision_model_value of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_value of this AlertRefDto.  # noqa: E501
        :rtype: float
        """
        return self._day_prevision_model_value

    @day_prevision_model_value.setter
    def day_prevision_model_value(self, day_prevision_model_value):
        """Sets the day_prevision_model_value of this AlertRefDto.


        :param day_prevision_model_value: The day_prevision_model_value of this AlertRefDto.  # noqa: E501
        :type: float
        """
        if day_prevision_model_value is None:
            raise ValueError("Invalid value for `day_prevision_model_value`, must not be `None`")  # noqa: E501

        self._day_prevision_model_value = day_prevision_model_value

    @property
    def day_prevision_model_color(self):
        """Gets the day_prevision_model_color of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_color of this AlertRefDto.  # noqa: E501
        :rtype: str
        """
        return self._day_prevision_model_color

    @day_prevision_model_color.setter
    def day_prevision_model_color(self, day_prevision_model_color):
        """Sets the day_prevision_model_color of this AlertRefDto.


        :param day_prevision_model_color: The day_prevision_model_color of this AlertRefDto.  # noqa: E501
        :type: str
        """
        if day_prevision_model_color is None:
            raise ValueError("Invalid value for `day_prevision_model_color`, must not be `None`")  # noqa: E501

        self._day_prevision_model_color = day_prevision_model_color

    @property
    def day_prevision_model_activity(self):
        """Gets the day_prevision_model_activity of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_activity of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_prevision_model_activity

    @day_prevision_model_activity.setter
    def day_prevision_model_activity(self, day_prevision_model_activity):
        """Sets the day_prevision_model_activity of this AlertRefDto.


        :param day_prevision_model_activity: The day_prevision_model_activity of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_prevision_model_activity is None:
            raise ValueError("Invalid value for `day_prevision_model_activity`, must not be `None`")  # noqa: E501

        self._day_prevision_model_activity = day_prevision_model_activity

    @property
    def day_prevision_model_top_tolerance(self):
        """Gets the day_prevision_model_top_tolerance of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_prevision_model_top_tolerance

    @day_prevision_model_top_tolerance.setter
    def day_prevision_model_top_tolerance(self, day_prevision_model_top_tolerance):
        """Sets the day_prevision_model_top_tolerance of this AlertRefDto.


        :param day_prevision_model_top_tolerance: The day_prevision_model_top_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_prevision_model_top_tolerance is None:
            raise ValueError("Invalid value for `day_prevision_model_top_tolerance`, must not be `None`")  # noqa: E501

        self._day_prevision_model_top_tolerance = day_prevision_model_top_tolerance

    @property
    def day_prevision_model_bottom_tolerance(self):
        """Gets the day_prevision_model_bottom_tolerance of this AlertRefDto.  # noqa: E501


        :return: The day_prevision_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :rtype: list[float]
        """
        return self._day_prevision_model_bottom_tolerance

    @day_prevision_model_bottom_tolerance.setter
    def day_prevision_model_bottom_tolerance(self, day_prevision_model_bottom_tolerance):
        """Sets the day_prevision_model_bottom_tolerance of this AlertRefDto.


        :param day_prevision_model_bottom_tolerance: The day_prevision_model_bottom_tolerance of this AlertRefDto.  # noqa: E501
        :type: list[float]
        """
        if day_prevision_model_bottom_tolerance is None:
            raise ValueError("Invalid value for `day_prevision_model_bottom_tolerance`, must not be `None`")  # noqa: E501

        self._day_prevision_model_bottom_tolerance = day_prevision_model_bottom_tolerance

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
        if issubclass(AlertRefDto, dict):
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
        if not isinstance(other, AlertRefDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
