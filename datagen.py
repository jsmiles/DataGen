import numpy as np
import pandas as pd
import re

from faker import Faker
from faker.providers.person.en import Provider
from faker_credit_score import CreditScore

fake = Faker()
fake.add_provider(CreditScore)

#############
# Functions #
#############

def random_names(name_type, size):
    """
    Generate some random names
    """
    names = getattr(Provider, name_type)
    return np.random.choice(names, size=size)


def random_dates(start, end, size):
    """
    Generate random dates within range
    Taken from here: https://www.caktusgroup.com/blog/2020/04/15/quick-guide-generating-fake-data-with-pandas/
    Who adapted from: https://stackoverflow.com/a/50668285
    """
    # Unix timestamp is in nanoseconds by default, so divide it by
    # 24*60*60*10**9 to convert to days.
    divide_by = 24 * 60 * 60 * 10**9
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, size), unit="D")

def random_email(size):
    """
    Generate a set of random emails
    """
    emails = []
    for _ in range(0, size):
        email = fake.ascii_free_email()
        email = email.split('@')[-1].split(".")[0] # parse the email
        emails.append(email)
    return emails

def random_scores(size):
    """
    Generate a set of random credit scores
    """
    scores = []
    for _ in range(0, size):
        scores.append(fake.credit_score())
    return scores

def random_binary(size, prob):
    """
    Generate a set of random binary variables
    """
    binaries = []
    for _ in range(size):
        binaries.append(fake.boolean(chance_of_getting_true=prob))
    return binaries


# Lists for data frames
id_types = ['passport', 'drivers licence', 'national id'] # id type list
id_pr = [0.6, 0.3, 0.1] # assign probabilities

country_list = ['UK', 'France', 'Germany', 'Russia']
country_pr = [0.85, 0.05, 0.05, 0.1]

device_list = ['ios', 'android', 'windows']
device_pr = [0.45, 0.5, 0.05]


# Build the Data Frame
size = 100
df = pd.DataFrame(columns=['First', 'Last', 'DOB', 'Signup'])
df['First'] = random_names('first_names', size)
df['Last'] = random_names('last_names', size)
df['DOB'] = random_dates(start=pd.to_datetime('1940-01-01'), end=pd.to_datetime('2000-01-01'), size=size)
df['Signup'] = random_dates(start=pd.to_datetime('2020-01-01'), end=pd.to_datetime('2021-01-31'), size=size)
df['Email'] = random_email(size)
df['SignupDurationSeconds'] = np.random.randint(30, 1200, size = size, dtype = 'int') # 30 seconds and 20 minutes
df['ID_Type'] = np.random.choice(id_types, size, id_pr)
df['ID_Country'] = np.random.choice(country_list, size, country_pr)
df['Nationality'] = np.random.choice(country_list, size, country_pr)
df['Domicile'] = np.random.choice(country_list, size, country_pr)
df['Device'] = np.random.choice(device_list, size, device_pr)
df['Ad_Redirect'] = random_binary(size, 30)
df['VPN'] = random_binary(size, 10)
df[['Ad_Redirect', 'VPN']] = (df[['Ad_Redirect','VPN']] == True).astype(int)
df['CreditScore'] = random_scores(size)


# Output the dataframe
df.to_csv('signup_data.csv', index=False)
