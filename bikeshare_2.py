import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please select one of the cities: chicago, new york city or washington\n')
    while city not in ['chicago', 'new york city', 'washington']:
        city = input(
            "Incorrect Input \nPlease select one of the following cities: chicago, new york city or washington\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please any one of the months: all, january, feburary, march, april, may, june\n')
    while month not in ['all', 'january', 'feburary', 'march', 'april', 'may', 'june']:
        month = input(
            "Incorrect Input \nPlease select one of the following months: all, january, feburary, march, april, may, june\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please select one of the days: all, monday, tuesday, wednesday, thursday, friday, saturday\n')
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        city = input(
            "Incorrect Input \nPlease select one of the following days: all, monday, tuesday, wednesday, thursday, friday, saturday\n")

    print('-' * 40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'feburary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Common Month: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most Common Day: ', df['day'].mode()[0])

    # TO DO: display the most common start hour
    print('Most Common Start Hour: ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commom Start Station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Commom End Station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'] + ' - ' + df['End Station']
    print('Most Frequent Start and End Station Combination: ', df['Station Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Duration of all the trips: ', np.sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print('Average Duration of all the trips: ', np.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print('Gender Counts:')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Oldest User was born: ', int(df.sort_values(by='Birth Year').head(1)['Birth Year']))
        print('Youngest User was born: ', int(df.sort_values(by='Birth Year', ascending=False).head(1)['Birth Year']))
        print('Most Common birth year of users:', int(df['Birth Year'].mode()[0]))
    else:
        print('There is no Gender and Birth Year data for Washington City!!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # print(df.info())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
