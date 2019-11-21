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


class DaysNearDateResultDto(object):
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
        'models': 'list[ModelDto]',
        'days': 'list[DayModelDto]',
        'nearest_distance_days': 'list[DayModelDto]',
        'day': 'DayModelDto',
        'source': 'SourceDto',
        'previsions': 'list[PrevisionDto]',
        'alerts': 'list[AlertDto]',
        'alert_refs': 'list[AlertRefDto]'
    }

    attribute_map = {
        'models': 'models',
        'days': 'days',
        'nearest_distance_days': 'nearestDistanceDays',
        'day': 'day',
        'source': 'source',
        'previsions': 'previsions',
        'alerts': 'alerts',
        'alert_refs': 'alertRefs'
    }

    def __init__(self, models=None, days=None, nearest_distance_days=None, day=None, source=None, previsions=None, alerts=None, alert_refs=None):  # noqa: E501
        """DaysNearDateResultDto - a model defined in Swagger"""  # noqa: E501

        self._models = None
        self._days = None
        self._nearest_distance_days = None
        self._day = None
        self._source = None
        self._previsions = None
        self._alerts = None
        self._alert_refs = None
        self.discriminator = None

        self.models = models
        self.days = days
        self.nearest_distance_days = nearest_distance_days
        self.day = day
        self.source = source
        self.previsions = previsions
        self.alerts = alerts
        self.alert_refs = alert_refs

    @property
    def models(self):
        """Gets the models of this DaysNearDateResultDto.  # noqa: E501

        List of models  # noqa: E501

        :return: The models of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[ModelDto]
        """
        return self._models

    @models.setter
    def models(self, models):
        """Sets the models of this DaysNearDateResultDto.

        List of models  # noqa: E501

        :param models: The models of this DaysNearDateResultDto.  # noqa: E501
        :type: list[ModelDto]
        """
        if models is None:
            raise ValueError("Invalid value for `models`, must not be `None`")  # noqa: E501

        self._models = models

    @property
    def days(self):
        """Gets the days of this DaysNearDateResultDto.  # noqa: E501

        List of days around the target date  # noqa: E501

        :return: The days of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[DayModelDto]
        """
        return self._days

    @days.setter
    def days(self, days):
        """Sets the days of this DaysNearDateResultDto.

        List of days around the target date  # noqa: E501

        :param days: The days of this DaysNearDateResultDto.  # noqa: E501
        :type: list[DayModelDto]
        """
        if days is None:
            raise ValueError("Invalid value for `days`, must not be `None`")  # noqa: E501

        self._days = days

    @property
    def nearest_distance_days(self):
        """Gets the nearest_distance_days of this DaysNearDateResultDto.  # noqa: E501

        List of days near the target date in distance  # noqa: E501

        :return: The nearest_distance_days of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[DayModelDto]
        """
        return self._nearest_distance_days

    @nearest_distance_days.setter
    def nearest_distance_days(self, nearest_distance_days):
        """Sets the nearest_distance_days of this DaysNearDateResultDto.

        List of days near the target date in distance  # noqa: E501

        :param nearest_distance_days: The nearest_distance_days of this DaysNearDateResultDto.  # noqa: E501
        :type: list[DayModelDto]
        """
        if nearest_distance_days is None:
            raise ValueError("Invalid value for `nearest_distance_days`, must not be `None`")  # noqa: E501

        self._nearest_distance_days = nearest_distance_days

    @property
    def day(self):
        """Gets the day of this DaysNearDateResultDto.  # noqa: E501


        :return: The day of this DaysNearDateResultDto.  # noqa: E501
        :rtype: DayModelDto
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this DaysNearDateResultDto.


        :param day: The day of this DaysNearDateResultDto.  # noqa: E501
        :type: DayModelDto
        """
        if day is None:
            raise ValueError("Invalid value for `day`, must not be `None`")  # noqa: E501

        self._day = day

    @property
    def source(self):
        """Gets the source of this DaysNearDateResultDto.  # noqa: E501


        :return: The source of this DaysNearDateResultDto.  # noqa: E501
        :rtype: SourceDto
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DaysNearDateResultDto.


        :param source: The source of this DaysNearDateResultDto.  # noqa: E501
        :type: SourceDto
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def previsions(self):
        """Gets the previsions of this DaysNearDateResultDto.  # noqa: E501

        List of previsions  # noqa: E501

        :return: The previsions of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[PrevisionDto]
        """
        return self._previsions

    @previsions.setter
    def previsions(self, previsions):
        """Sets the previsions of this DaysNearDateResultDto.

        List of previsions  # noqa: E501

        :param previsions: The previsions of this DaysNearDateResultDto.  # noqa: E501
        :type: list[PrevisionDto]
        """
        if previsions is None:
            raise ValueError("Invalid value for `previsions`, must not be `None`")  # noqa: E501

        self._previsions = previsions

    @property
    def alerts(self):
        """Gets the alerts of this DaysNearDateResultDto.  # noqa: E501

        List of alerts  # noqa: E501

        :return: The alerts of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[AlertDto]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this DaysNearDateResultDto.

        List of alerts  # noqa: E501

        :param alerts: The alerts of this DaysNearDateResultDto.  # noqa: E501
        :type: list[AlertDto]
        """
        if alerts is None:
            raise ValueError("Invalid value for `alerts`, must not be `None`")  # noqa: E501

        self._alerts = alerts

    @property
    def alert_refs(self):
        """Gets the alert_refs of this DaysNearDateResultDto.  # noqa: E501

        List of alerts refs  # noqa: E501

        :return: The alert_refs of this DaysNearDateResultDto.  # noqa: E501
        :rtype: list[AlertRefDto]
        """
        return self._alert_refs

    @alert_refs.setter
    def alert_refs(self, alert_refs):
        """Sets the alert_refs of this DaysNearDateResultDto.

        List of alerts refs  # noqa: E501

        :param alert_refs: The alert_refs of this DaysNearDateResultDto.  # noqa: E501
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
        if issubclass(DaysNearDateResultDto, dict):
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
        if not isinstance(other, DaysNearDateResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
