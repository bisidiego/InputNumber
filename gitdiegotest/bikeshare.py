import time
import pandas as pd
import numpy as np

"""
  Explore US Bikeshare data.
  By Diego Fernando Sanabria.
  date:  Oct 19 2021.

  UDACITY
  Programming for datascience with Python.

"""

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
def get_filtres():
    print('Hello! Let\'s explore some US bikeshare data!')

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    user = city = month = day = userDay = userCity = userMonth = ""
    while user != "no":
        userCity = input("If you would like to see data for\n"
                         "Chicago please type 1\nfor New York type 2\n for Washington type 3\n ")
        if userCity == "1":
            city = "chicago"

        elif userCity == "2":
            city = "new york city"

        elif userCity == "3":
            city = "washington"

        userDay = input(
            "if want to filter by day,select a number from 1 to 7, otherwise  type none,:\n 1.Monday \n 2.Tuesday\n 3.Wdnesday"
            "\n 4. Thursday \n 5 Friday\n 6.Saturday \n 7 Sunday\n  ")

        if userDay == "1":
            day = "monday"

        elif userDay == str(2):
            day = "tuesday"

        elif userDay == '3':
            day = "Wednesday"

        elif userDay == '4':
            day = "thursday"

        elif userDay == '5':
            day = "friday"

        elif userDay == '6':
            day = "saturday"

        elif userDay == '7':
            day = "sunday"
        elif userDay == 'none':
            day = "all"

        userMonth = input(
            "if you do not want to use filter type: none \n but if you want to choose a month, please select a number for:\n 1.January \n 2.February\n 3.March"
            "\n 4. April \n 5 May \n 6.June \n 7 July\n ")

        if userMonth == "1":
            month = "january"

        elif userMonth == "2":
            month = "february"

        elif userMonth == "3":
            month = "march"

        elif userMonth == "4":
            month = "april"

        elif userMonth == "5":
            month = "may"

        elif userMonth == "6":
            month = "june"

        elif userMonth == "none":
            month = "all"
        print("you have chosen:", "\nCity : ", city, "\nMonth : ", month, "\nDay : ", day)
        print('-' * 40)

        # print("Return Values: ",city,month,day)

        return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    #line 127 solved using this reference:
    #https://newbedev.com/datetimeproperties-object-has-no-attribute-weekday-name-code-example
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


# print(df)  # until here the program is working and getting data from csv document.

#
def time_stats(df):
    """
    gets the dataframe as an argument,

    Prints:
        The most popular month, day and hour, where people is using
        the biskeshare service,
        according to the previous filters, could be day month or none.
    """
    print("\ncalculating  the most frequent times of travel\n")
    start_time = time.time()
    # print(start_time)
    # print(df.head(10))
    df['Start time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    common_month = df['month'].mode()[0]
    popular_day = df['day'].mode()[0]
    popular_hour = df['hour'].mode()[0]

    print("The most popular month is: {0}\nThe most popular day is: {1}\nThe most popular hour  is: {2}".format(
        common_month, popular_day, popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    '''Display statistics on the most popular stations and trip.

    Prints:
        1- The most popular start station.
        2- The most popular End Station.
        3- and finnally it prints the most popular combination of start and end station
    '''

    print("Calculating the most popular stations and Trip")
    start_time = time.time()

    popular_start_station = df['Start Station'].mode()
    print("Most popular Start Station", popular_start_station)

    popular_end_station = df['End Station'].mode()
    print("Most popular End Station", popular_end_station)

    start_station = df['Start Station']

    end_station = df['End Station']

    newcol = start_station + end_station
    popular_combination = newcol.mode()

    print("Most popular combination ", popular_combination)

    # print(df.head(3))

    # print(newcol)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    '''This method is in charge of displaying the duration of trips,

    Prints:
        1- it calculates the total travel time.
        2- The mean travel time.

    '''
    print("Calculating  Trip  duration")
    start_time = time.time()

    trip_duration_column = df['Trip Duration']

    # print(df.columns)

    total = trip_duration_column.sum()
    print("The total durations of all the trips   : ", total)

    mean = trip_duration_column.mean()
    print("The mean travel time is : ", mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    '''Display statistics on bikeshare users.

    Prints:
        1- The earlist year of birth of the users.
        2- The most recent year of birth of the users.
        3- and the most popular year of birth os the users.
    '''

    print("Calculating User Stats...\n")
    start_time = time.time()
    # Count of user types

    ut = df["User Type"]
    print("What is the breakdown of users: \n", ut.value_counts())

    gender = df["Gender"]
    print("Count of gender : \n", gender.value_counts())

    year = df['Birth Year']
    print("Earlist year of birth", year.min())
    print("Recent year of birth", year.max())
    print("The most common year of birth", year.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    '''Finnally here is where all the magic happends

    this method create the variables in order to put in to the filter, that
    the it will be passed through the other statistical methods.

    '''
    while True:
        city, month, day = get_filtres()
        df = load_data(city, month, day)
        print("time Statistics")
        print('=' * 40)
        time_stats(df)
        print("Station Statistics")
        print('=' * 40)
        station_stats(df)

        print("Trip duration Statistics")
        print('=' * 40)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print("Thanks for Using Diego Sanabria's version of the Bikeshare data project!")


if __name__ == '__main__':
    main()
