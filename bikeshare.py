import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Which city? Chicago, New York city or Washington: ')
            if city.lower() in CITY_DATA:
                break            
            else:
                print('Non expected value.')
        except:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month? January, February, March, April, May or June.\nPress enter to select all of them: ')
            if month.lower() in months:
                break  
            elif month == '':          
               month = 'all'
               break
            else:
                print('Non expected value.')
        except:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday..\nPress enter to select all of them: ')
            if day.lower() in days:
                break  
            elif day == '':          
               day = 'all'
               break
            else:
                print('Non expected value.')
        except:
            break
    print(city, month, day)
    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    # print(df.isna())
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
        # print('filtered by month')
        # print(df)
    if day != 'all':
        day = days.index(day.lower()) 
        df = df[df['day_of_week'] == day]
    df['hour'] = df['Start Time'].dt.hour
    # print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is {}'.format(months[df['month'].mode()[0] - 1].title()))
    # display the most common day of week
    print('The most common day of week is {}'.format(days[df['day_of_week'].mode()[0]].title()))
    # print(df['day_of_week'].mode()[0])
    # print(days[df['day_of_week'].mode()[0]])
    # display the most common start hour
    print('The most common start hour is {}'.format(df['hour'].mode()[0]))
    # print(df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is {}'.format(df['Start Station'].mode()[0]))
    # display most commonly used end station
    print('The most commonly used end station is {}'.format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    df['Trip'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    print('The most popular trip is {}'.format(df['Trip'].mode()[0]))
    # print(df['Trip'])
    # print(df['Trip'].value_counts())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Travel Time'] = df['End Time'] - df['Start Time'] 
    # display total travel time
    print('Total travel time is {}'.format(df['Travel Time'].sum()))
    # display mean travel time
    print('Mean travel time is {}'.format(df['Travel Time'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types: ')
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender: ')
        print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    # df['Birth Year'] = pd.to_datetime(df['Birth Year'])
    # df['Birth Year']
    if 'Birth Year' in df.columns:
        print('The earliest year of birth is {}'.format(int(df['Birth Year'].min())))
        print('The most recent year of birth is {}'.format(int(df['Birth Year'].max())))
        print('The most common year of birth is {}'.format(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data from dataframe."""
    more =  input('Do you want to see raw data ? (y/n)')
    i = 0
    while more.lower() == 'y':
        print(df[i:i+5])
        i += 5
        more =  input('Do you want to see more raw data ? (y/n)')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
