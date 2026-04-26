import pandas as pd

# load dataset
df = pd.read_csv("data/marketing_campaign_data.csv")

# inspect dataset
print(df.head())
print(df.info())

# check missing values
print(df.isnull().sum())

# remove duplicates
df = df.drop_duplicates()

# standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# convert date column
df['date'] = pd.to_datetime(df['date'])

# create CTR column
df['ctr'] = df['clicks'] / df['impressions']

# create engagement efficiency column
df['engagement_efficiency'] = df['engagement_score'] / df['clicks']

# save cleaned dataset
df.to_csv("data/cleaned_marketing_campaign_data.csv", index=False)

print("Data cleaning completed successfully.")