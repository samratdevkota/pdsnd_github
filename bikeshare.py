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
    city = input("Which city would you like to filter by? (chicago, new york city, washington)\n :  ").lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Invalid input! Please select one of these cities (chicago, new york city, washington)\n :  ").lower()
 
    


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to filter by? (all, january, february, ... , june)\n :  ").lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Invalid input! Please select one of these options. (all, january, february, ... , june)\n :  ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day would you like to filter by? (all, monday, tuesday, ... sunday)\n :  ").lower()
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        day = input("Invalid input! Please select one of these options. (all, monday, tuesday, ... sunday)\n :  ").lower()


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
    
    # load data into dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # print(df.dtypes)
    # here the datatype of start time and end time is object (ie strings) in pandas
    # convert to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # make a new column "month" and "day_of_week" in the dataframe by extracting month and day from "start time" datetime object
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    print("Most common month is", common_month)
    

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of week is", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("Most common start hour is", common_start_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used start station is", start_station)



    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used end station is", end_station)
    

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).idxmax()
    print("Most frequent combination of start station and end station trip is", combo_station)
    # I HAVE A DOUBT HERE PLEASE CHECK IT IF I GOT THE QUESTION RIGHT   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time    
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is", total_travel_time)



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("mean travel time is", mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types: ", user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['gender'].value_counts()
        print("Counts of gender is", gender_types)
    except KeyError:
        print("Gender data is not available")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print("Earliest year of birth is", earliest_birth)
    except KeyError:
        print("Birth data is not available")
        
    try:
        recent_birth = df['Birth Year'].max()
        print("Most recent year of birth is", recent_birth)
    except:
        print("Birth data is not available")
        
    try:
        common_birth_year = df['Birth Year'].value_counts().idxmax()
        print("Most common year of birth is", common_birth_year)
    except:
        print("Birth data is not available")
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
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
