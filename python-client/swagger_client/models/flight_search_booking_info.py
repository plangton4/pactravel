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


class FlightSearchBookingInfo(object):
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
        'travel_class': 'str',
        'cabin_code': 'str',
        'booking_code': 'str',
        'seats_remaining': 'str',
        'fare_family': 'str',
        'fare_basis': 'str'
    }

    attribute_map = {
        'travel_class': 'travel_class',
        'cabin_code': 'cabin_code',
        'booking_code': 'booking_code',
        'seats_remaining': 'seats_remaining',
        'fare_family': 'fare_family',
        'fare_basis': 'fare_basis'
    }

    def __init__(self, travel_class=None, cabin_code=None, booking_code=None, seats_remaining=None, fare_family=None, fare_basis=None):
        """
        FlightSearchBookingInfo - a model defined in Swagger
        """

        self._travel_class = None
        self._cabin_code = None
        self._booking_code = None
        self._seats_remaining = None
        self._fare_family = None
        self._fare_basis = None

        self.travel_class = travel_class
        if cabin_code is not None:
          self.cabin_code = cabin_code
        self.booking_code = booking_code
        self.seats_remaining = seats_remaining
        if fare_family is not None:
          self.fare_family = fare_family
        if fare_basis is not None:
          self.fare_basis = fare_basis

    @property
    def travel_class(self):
        """
        Gets the travel_class of this FlightSearchBookingInfo.
        The cabin class offered on this flight. An enumeration that will read either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST

        :return: The travel_class of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._travel_class

    @travel_class.setter
    def travel_class(self, travel_class):
        """
        Sets the travel_class of this FlightSearchBookingInfo.
        The cabin class offered on this flight. An enumeration that will read either ECONOMY, PREMIUM_ECONOMY, BUSINESS or FIRST

        :param travel_class: The travel_class of this FlightSearchBookingInfo.
        :type: str
        """
        if travel_class is None:
            raise ValueError("Invalid value for `travel_class`, must not be `None`")

        self._travel_class = travel_class

    @property
    def cabin_code(self):
        """
        Gets the cabin_code of this FlightSearchBookingInfo.
        A single character encoding of the travel_class, generally only available on responses from affiliates.

        :return: The cabin_code of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._cabin_code

    @cabin_code.setter
    def cabin_code(self, cabin_code):
        """
        Sets the cabin_code of this FlightSearchBookingInfo.
        A single character encoding of the travel_class, generally only available on responses from affiliates.

        :param cabin_code: The cabin_code of this FlightSearchBookingInfo.
        :type: str
        """

        self._cabin_code = cabin_code

    @property
    def booking_code(self):
        """
        Gets the booking_code of this FlightSearchBookingInfo.
        The Reservation Booking Designator code that determines the quality and terms of the flight offered for the given price. A single letter from A..Z

        :return: The booking_code of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._booking_code

    @booking_code.setter
    def booking_code(self, booking_code):
        """
        Sets the booking_code of this FlightSearchBookingInfo.
        The Reservation Booking Designator code that determines the quality and terms of the flight offered for the given price. A single letter from A..Z

        :param booking_code: The booking_code of this FlightSearchBookingInfo.
        :type: str
        """
        if booking_code is None:
            raise ValueError("Invalid value for `booking_code`, must not be `None`")

        self._booking_code = booking_code

    @property
    def seats_remaining(self):
        """
        Gets the seats_remaining of this FlightSearchBookingInfo.
        The minimum number of seats that are still available for this price at the time of search. If the value is a 4 or above, there are often more than this number of seats still available.

        :return: The seats_remaining of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._seats_remaining

    @seats_remaining.setter
    def seats_remaining(self, seats_remaining):
        """
        Sets the seats_remaining of this FlightSearchBookingInfo.
        The minimum number of seats that are still available for this price at the time of search. If the value is a 4 or above, there are often more than this number of seats still available.

        :param seats_remaining: The seats_remaining of this FlightSearchBookingInfo.
        :type: str
        """
        if seats_remaining is None:
            raise ValueError("Invalid value for `seats_remaining`, must not be `None`")

        self._seats_remaining = seats_remaining

    @property
    def fare_family(self):
        """
        Gets the fare_family of this FlightSearchBookingInfo.
        Enumeration of the type of fare which this airline is providing, eg. VALUE. This is generally only available for affiliate responses.

        :return: The fare_family of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._fare_family

    @fare_family.setter
    def fare_family(self, fare_family):
        """
        Sets the fare_family of this FlightSearchBookingInfo.
        Enumeration of the type of fare which this airline is providing, eg. VALUE. This is generally only available for affiliate responses.

        :param fare_family: The fare_family of this FlightSearchBookingInfo.
        :type: str
        """

        self._fare_family = fare_family

    @property
    def fare_basis(self):
        """
        Gets the fare_basis of this FlightSearchBookingInfo.
        See https://en.wikipedia.org/wiki/Fare_basis_code for the fare being offered.

        :return: The fare_basis of this FlightSearchBookingInfo.
        :rtype: str
        """
        return self._fare_basis

    @fare_basis.setter
    def fare_basis(self, fare_basis):
        """
        Sets the fare_basis of this FlightSearchBookingInfo.
        See https://en.wikipedia.org/wiki/Fare_basis_code for the fare being offered.

        :param fare_basis: The fare_basis of this FlightSearchBookingInfo.
        :type: str
        """

        self._fare_basis = fare_basis

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
        if not isinstance(other, FlightSearchBookingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
