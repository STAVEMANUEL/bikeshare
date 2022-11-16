import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('Which city would you like to explore: chicago, new york city, washington? ').lower()

        if city in cities:
            break
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    month = input('Which month would you like to explore? \n> {} \n>'.format(months)).lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input('Which day would you like to explore? \n> {} \n>'.format(days)).lower()

    print('-'*40)

    
    if month == '' and day == '':
        return city, months, days
    elif month == '' and day != '':
        return city, months, day
    elif month != '' and day == '':
        return city, month, days
    else:
        return city, month, day

  
    city, month, day = get_filters()

    print(city, month, day) 


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

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       
       month = months.index(month) + 1

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
          
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = print('most common month is: ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    day_of_week = print('most common day of week:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    hour_array=[]
    for i in range(24):
          hour_array.append(0)
    for i in range(len(df)):
          j=df['hour'][i]
          hour_array[j]+=df['Trip Duration'][i]
    print(hour_array.index(max(hour_array))+1)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    cs = print('most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    cse = print('most commonly end station is: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start & End'] = df['Start Station'].str.cat(df['End Station'], sep=' --> ')
    print('most frequent combination of start station and end station trip is: ',df['Start & End'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time: ', sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print('mean travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types: ', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print('counts of gender: ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('earliest year of birth: ' , max(df['Birth Year']))
    print('most recent year of birth: ', min(df['Birth Year']))
    print('most common year of birth: ', df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
