
import math


def computeClosest(number, data_struct):
    """
    Find nearest value from list of values

    :param number: value to get closest to (time, etc)
    :param data_struct: list of values
    :return closest_index: index of closest value in list
    """

    closest_index = 0
    diff_value = 10000000  # really big number
    for ii in range(len(data_struct)):
        if diff_value > abs(data_struct[ii] - number):
            diff_value = abs(data_struct[ii] - number)
            closest_index = ii
    return closest_index


def datetime2tow(datetime_string):
    """
    Converts GeoRinex time.data[idx].astype('str') string (e.g. '2020-12-15T00:00:00.000000000')
    to GPS time of week

    :param datetime_string: single time.data value from a GeoRinex object converted to a string
    :return tow: time of week [sec]
    """

    SEC_PER_WEEK = 604800

    year = int(datetime_string[2:4])
    month = int(datetime_string[5:7])
    day = int(datetime_string[8:10])

    hour = int(datetime_string[11:13])
    minute = int(datetime_string[14:16])
    second = int(datetime_string[17:19])

    # convert two digit year to four digits (assume range of 1980-2079)
    if 80 <= year <= 99:
        year = 1900 + year

    if 0 <= year <= 79:
        year = 2000 + year

    # calculate "m" and "y" terms used below from the calendar month
    if month <= 2:
        y = year - 1
        m = month + 12

    if month > 2:
        y = year
        m = month

    # compute Julian date corresponding to given calendar date
    JD = math.floor(365.25 * y) + math.floor(30.6001 * (m+1)) + \
         day + (hour + minute / 60 + second / 3600) / 24 + 1720981.5

    gps_week = math.floor((JD - 2444244.5) / 7)

    tow = round(((((JD - 2444244.5) / 7) - gps_week) * SEC_PER_WEEK) / 0.5) * 0.5

    return tow




