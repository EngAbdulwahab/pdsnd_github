import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Which city you want to show\nPlease choose on of the following: 'chicago' , 'new york' or 'washington'?")

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input()
        city = city.lower()
        if city not in ['washington','new york','chicago']:
            print("this city is not on the list \nplease choose from the list")
            continue
        else:
            print("Which month you want to show? please write the month or write all if you want")
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input()
        month = month.lower()
        if month not in ['january','february','march','april','may','june','all']:
            print("invalid input \nplease choose between january and june, or choose all if you want")
            continue
        else:
            print("Which day you choose? if you want the whole week write all")
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input()
        day = day.lower()
        if day not in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']:
            print("invalid input \nplease try again")
            continue
        else:
            break
    print('-'*40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time']) # create df for time
    df['month'] = df['Start Time'].dt.month             # column for month
    df['day_of_week'] = df['Start Time'].dt.weekday_name    # column for day
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('the most common month is ' , common_month )



    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the most common day is ' , common_day )


    # TO DO: display the most common start hour

    common_hour = df['hour'].mode()[0]
    print('the most common hour is ' , common_hour )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most common start station is ' , df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('the most common end station is ' , df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print('the most common frequent combination of the trip is ' , df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('the total travel time is ' , df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print('the mean travel time is ' , df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('count of each user types ' , user_types)

    # TO DO: Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()
        print('Gender Count', gender_count)
    except KeyError:
        print('No data available')

    # Display earliest, most recent, and most common year of birth
    try:
        old_year = int(df['Birth Year'].min())
        print('earliest year is', old_year)
    except KeyError:
        print('No data available')

    try:
        recent_year = int(df['Birth Year'].max())
        print('recent year is', recent_year)
    except KeyError:
        print('No data available.')

    try:
        common_birth = int(df['Birth Year'].mode()[0])
        print('Most common year is', common_birth)
    except KeyError:
        print('No data available.')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    raw = input('Would you like to see the original data? yes or no').lower()
    if raw != 'no':
        i = 0
        while (i < df['Start Time'].count() and raw != 'no'):
            print(df.iloc[ i : i+5 ])
            i += 5
            keep_showing = input('Would you like to show more? yes or no').lower()
            if keep_showing != 'yes':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
