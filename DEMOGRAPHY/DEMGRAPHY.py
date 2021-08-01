import pandas as pd

def calculate_demographic_data(print_data = True):
  # Read data from file
  df = pd.read_csv('adult.data.csv')

  # How many of each race are represented in this dataset?
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

  # What is the percentage of people who have a Bachelors degree?
  percentage_bachelors = round(float(((df['education'] == 'Bachelors').sum()) / len(df))*100, 1)

  # What percentage of the people with AND without `education` equal to `Bachelors`, `Masters`, or `Doctorate` also have a `salary` of `>50K` (Note: Every row of data has salary of either '>50K' or '<=50K')?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_eduction = df.loc[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
  lower_education = df.loc[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

  # percentage with salary >50K
  higher_education_rich = round((higher_eduction['salary'] == '>50K').sum() / len(higher_eduction) * 100, 1)
  lower_education_rich = round((lower_education['salary'] == '>50K').sum() / len(lower_education) * 100, 1)

  # What is the minumum number of hours a person works per week (hours-per-week feature)?
  # What percentage of the people who work the minumum number of hours per week have a salary of >50K?
  min_work_hours = df['hours-per-week'].min()

  num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]

  rich_percentage = round((float(df[(df['hours-per-week'] == min_work_hours)
                  & (df['salary'] == '>50K')].shape[0]) / num_min_workers) * 100, 1)


 # What country has the highest percentage of people that earn >50K?
    

  all = df[['salary', 'native-country']]
  every = all.groupby(['native-country']).count()
  add50k = all[all['salary'] == '>50k']
  add50k = add50k.groupby(['native-country']).count()
  add50k = (add50k * 100) / every
  add50k.sort_values(by=['salary'], inplace=True, ascending=False)
  hence = pd.Series(add50k['salary'])
  hence.index[0]
  round(hence.values[0], 1)


  # Identify the most popular occupation for those who earn >50K in India.

  top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].value_counts().keys()[0]

  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {'race_count': race_count, 'average_age_men': average_age_men, 'percentage_bachelors': percentage_bachelors, 'higher_education_rich': higher_education_rich, 'lower_education_rich': lower_education_rich, 'min_work_hours': min_work_hours, 'rich_percentage': rich_percentage, 'top_IN_occupation': top_IN_occupation}