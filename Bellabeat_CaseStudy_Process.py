# -*- coding: utf-8 -*-
"""Cindy_Bellabeat Case Study.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j5Z8cQIPbjccHgiTgRu4PR4wWOj0jBRU

### Import Packages and Datasets
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

daily_activity = pd.read_csv(r"Datasets\dailyActivity_merged.csv")
weight = pd.read_csv(r"Datasets\weightLogInfo_merged.csv")
sleep_day = pd.read_csv(r"Datasets\sleepDay_merged.csv")
hourly_steps = pd.read_csv(r"Datasets\hourlySteps_merged.csv")
hourly_calories = pd.read_csv(r"Datasets\hourlyCalories_merged.csv")

"""### Observing and Transforming Data Formats"""

daily_activity.info()

daily_activity['ActivityDate'] = pd.to_datetime(daily_activity['ActivityDate'], format='%m/%d/%Y')

new_cols = ['Id', 'ActivityDate', 'DayOfTheWeek', 'TotalSteps', 'TotalDistance', 'TrackerDistance', 'LoggedActivitiesDistance', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'TotalExerciseMinutes', 'TotalExerciseHours', 'Calories']
df_activity = daily_activity.reindex(columns=new_cols)
df_activity

df_activity["DayOfTheWeek"] = df_activity["ActivityDate"].dt.day_name()
df_activity["DayOfTheWeek"].head(5)

df_activity.rename(columns = {"Id":"id", "ActivityDate":"date", "DayOfTheWeek":"day_of_the_week", "TotalSteps":"total_steps", "TotalDistance":"total_dist", "TrackerDistance":"track_dist", "LoggedActivitiesDistance":"logged_dist", "VeryActiveDistance":"very_active_dist", "ModeratelyActiveDistance":"moderate_active_dist", "LightActiveDistance":"light_active_dist", "SedentaryActiveDistance":"sedentary_active_dist", "VeryActiveMinutes":"very_active_mins", "FairlyActiveMinutes":"fairly_active_mins", "LightlyActiveMinutes":"lightly_active_mins", "SedentaryMinutes":"sedentary_mins", "TotalExerciseMinutes":"total_mins","TotalExerciseHours":"total_hours","Calories":"calories"}, inplace = True)

print(df_activity.columns.values)
df_activity.head(5)

df_activity["total_mins"] = df_activity["very_active_mins"] + df_activity["fairly_active_mins"] + df_activity["lightly_active_mins"] + df_activity["sedentary_mins"]
df_activity["total_mins"].head(5)

df_activity["total_hours"] = round(df_activity["total_mins"] / 60)
df_activity["total_hours"].head(5)

df_activity.to_csv(r"Datasets\daily_activity.csv", index=False)

sleep_day['SleepDay'] = pd.to_datetime(sleep_day['SleepDay'])
sleep_day['weekday'] = sleep_day['SleepDay'].dt.day_name()
sleep_day['total_minutes_asleep_hours'] = sleep_day['TotalMinutesAsleep'] / 60
sleep_day['total_time_in_bed_hours'] = sleep_day['TotalTimeInBed'] / 60
sleep_day.columns = [col.replace(' ', '_').lower() for col in sleep_day.columns]

sleep_day.to_csv(r"Datasets\sleep_day.csv", index=False)

weight.info()

sleep_day.info()

hourly_steps.info()

hourly_calories.info()

"""### Unique Identifier Statistics"""

daily_activity.Id.nunique()

weight.Id.nunique()

sleep_day.Id.nunique()

hourly_steps.Id.nunique()

hourly_calories.Id.nunique()

"""### How many rows and columns?"""

daily_activity.shape

sleep_day.shape

hourly_steps.shape

hourly_calories.shape

"""### Descriptive Statistics"""

daily_activity.describe()

sleep_day.describe()

hourly_steps.describe()

hourly_calories.describe()

"""### Getting Information from Datasets"""

daily_activity.isnull().any()

sleep_day.isnull().any()

hourly_steps.isnull().any()

hourly_calories.isnull().any()

daily_activity.duplicated()

sleep_day.duplicated()

hourly_steps.duplicated()

hourly_calories.duplicated()