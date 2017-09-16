# coding: utf-8

"""
    Amadeus Travel Innovation Sandbox

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Airport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'airport': 'str',
        'terminal': 'str'
    }

    attribute_map = {
        'airport': 'airport',
        'terminal': 'terminal'
    }

    def __init__(self, airport=None, terminal=None):
        """
        Airport - a model defined in Swagger
        """

        self._airport = None
        self._terminal = None

        self.airport = airport
        if terminal is not None:
          self.terminal = terminal

    @property
    def airport(self):
        """
        Gets the airport of this Airport.
        The 3 character <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA airport code</a> of the airport in question for this flight

        :return: The airport of this Airport.
        :rtype: str
        """
        return self._airport

    @airport.setter
    def airport(self, airport):
        """
        Sets the airport of this Airport.
        The 3 character <a href=\"https://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code\">IATA airport code</a> of the airport in question for this flight

        :param airport: The airport of this Airport.
        :type: str
        """
        if airport is None:
            raise ValueError("Invalid value for `airport`, must not be `None`")

        self._airport = airport

    @property
    def terminal(self):
        """
        Gets the terminal of this Airport.
        The terminal identifier at which this flight will arrive or depart in the given airport

        :return: The terminal of this Airport.
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """
        Sets the terminal of this Airport.
        The terminal identifier at which this flight will arrive or depart in the given airport

        :param terminal: The terminal of this Airport.
        :type: str
        """

        self._terminal = terminal

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Airport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other