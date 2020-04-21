import configparser
import pandas as pd
import googlemaps
import re
import numpy

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199

english_check = re.compile(r'[a-z]')

config = configparser.RawConfigParser()
config.read(r'F:\Python Project Dependencies\Twitter Streams\twitter.properties')

get_csv_path = dict(config.items('Read CSV'))


def read_csv(path, error_bad_lines):
    df = pd.read_csv(path, error_bad_lines=error_bad_lines)
    return df


corona_confirmed_df = read_csv(get_csv_path['confirmed_csv'], False)
corona_deaths_df = read_csv(get_csv_path['deaths_csv'], False)
corona_recovered_df = read_csv(get_csv_path['recovered_csv'], False)

# Mend Dataframe
corona_confirmed_df = corona_confirmed_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long']).rename(
    {'variable': 'Date', 'value': 'Confirmed'}, axis='columns')

corona_deaths_df = corona_deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long']).rename(
    {'variable': 'Date', 'value': 'Deaths'}, axis='columns')

corona_recovered_df = corona_recovered_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long']).rename(
    {'variable': 'Date', 'value': 'Recovered'}, axis='columns')

# Joining DFs
combined_df = [corona_confirmed_df, corona_deaths_df, corona_recovered_df]
combined_df = [df.set_index(['Province/State', 'Country/Region', 'Lat', 'Long', 'Date']) for df in combined_df]
combined_df = combined_df[0].join(combined_df[1:])

# Just to remove the index attribute of the column
combined_df = combined_df.reset_index()

# convert respective columns to numeric/datetime Datatypes
combined_df[['Lat', 'Long', 'Confirmed', 'Deaths', 'Recovered']] = combined_df[
    ['Lat', 'Long', 'Confirmed', 'Deaths', 'Recovered']].apply(pd.to_numeric)
combined_df[['Date']] = combined_df[['Date']].apply(pd.to_datetime)
combined_df = combined_df.rename({'Province/State': 'State', 'Country/Region': 'Country'}, axis='columns')

combined_df = combined_df.set_index('Country').filter(like='India', axis=0)

# Get Area based on Lat and Long using Google Maps
print(googlemaps.Client)
print(config.get('twitter', 'googleapikey'))
gglmaps = googlemaps.Client(key=config.get('twitter', 'googleapikey'))
geocode_result = gglmaps.reverse_geocode((-20.23, -58.30))
print(geocode_result[0])
print(geocode_result[0]['formatted_address'])
print(geocode_result[0]['formatted_address'].split(",")[-2].strip(" "))


def get_state(lat, long):
    try:
        output = gglmaps.reverse_geocode((lat, long))[0]['formatted_address'].split(",")[-2].strip()
        if (len(output.split(" ")) > 1):
            output = "TBF"
        if not english_check.match(output.lower()):
            output = "TBF"
    except:
        # print("Error in Reverse Geo Coding")
        output = "TBF"
    return output


combined_df["state_cleaned"] = combined_df[combined_df.State.isnull()][['Lat', 'Long']].apply(
    lambda s: get_state(s['Lat'], s['Long']), axis=1)

# print(combined_df[combined_df.state_cleaned.isnull()]['Country'].value_counts())
combined_inter_df = combined_df.copy()

print(combined_df.count())
print(combined_inter_df.count())

combined_inter_df.reset_index
combined_inter_df.dtypes

combined_inter_df["state_cleaned"] = combined_inter_df.apply(
    lambda x: x['State'] if numpy.all(pd.notnull(x['State'])) else x['state_cleaned'], axis=1)

combined_inter_df[combined_inter_df.state_cleaned == "TBF"]['Country'].value_counts()

# combined_inter_df[combined_inter_df.state_cleaned == "TBF"]['Country']

capital_df = read_csv('https://raw.githubusercontent.com/icyrockcom/country-capitals/master/data/country-list.csv',
                      False)

capital_df['country'].replace({'United Kingdom; England': 'United Kingdom'}, inplace=True)
capital_df['country'] = capital_df.country.str.lower()
capital_df.head(50)
capital_df = capital_df.set_index('country')


def capital_lookup(country):
    try:
        capital = capital_df.loc[country.lower()][0]
    except:
        capital = "TBF"
    return capital


combined_inter_df['state_cleaned'] = combined_inter_df.apply(
    lambda x: capital_lookup(x['Country']) if (x['state_cleaned'] == "TBF") else x['state_cleaned'],
    axis=1)
combined_inter_df.head(20)
combined_inter_df['Country'].replace(
    {'US': 'United States', 'Holy See': 'Vatican City', 'Timor-Leste': 'East Timor (Timor-Leste)',
     'Taiwan*': 'Republic of China (Taiwan)', 'Korea, South': 'South Korea', 'Czechia': 'Czech Republic',
     'Congo (Kinshasa)': 'Democratic Republic of the Congo', 'Congo (Brazzaville)': 'Democratic Republic of the Congo',
     'North Macedonia': 'Macedonia', 'Sao Tome and Principe': 'São Tomé and Príncipe'}, inplace=True)

combined_inter_df['state_cleaned'] = combined_inter_df.apply(
    lambda x: capital_lookup(x['Country']) if (x['state_cleaned'] == "TBF") else x['state_cleaned'], axis=1)

combined_inter_df[combined_inter_df.state_cleaned == "TBF"]['Country'].value_counts()

combined_inter_df['Country'].replace(
    {'Diamond Princess': 'Haiti', 'South Sudan': 'South Sudan South Sudan', 'West Bank and Gaza': 'Israel',
     'Korea, South': 'South Korea', 'Cabo Verde': 'Cape Verde', 'Burma': 'Myanmar'}, inplace=True)

combined_inter_df['state_cleaned'] = combined_inter_df.apply(
    lambda x: capital_lookup(x['Country']) if (x['state_cleaned'] == "TBF") else x['state_cleaned'], axis=1)

combined_inter_df[combined_inter_df.state_cleaned == "TBF"]['Country'].value_counts()

combined_inter_df.head(100)
combined_inter_df['state_cleaned'] = combined_inter_df.apply(
    lambda x: capital_lookup(x['Country']) if (x['state_cleaned'] == "TBF") else x['state_cleaned'], axis=1)
combined_inter_df[combined_inter_df.state_cleaned == "TBF"]['Country'].value_counts()

combined_inter_df.to_csv(r'F:\Python Project Dependencies\Twitter Streams\corona_dataset.csv')
