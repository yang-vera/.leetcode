# change col names

# rename two of the columns by using the 'rename' method
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
ufo.columns

# replace all of the column names by overwriting the 'columns' attribute
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.columns

# remove col

# remove multiple columns at once
ufo.drop(['City', 'State'], axis=1, inplace=True)
ufo.head()

# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
ufo.head()

# sort by col values
df.sort_values(['a', 'b'], ascending=[True, False])

# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()


# sort in descending order instead
movies.title.sort_values(ascending=False).head()

# sort the DataFrame first by 'content_rating', then by 'duration'
movies.sort_values(['content_rating', 'duration']).head()

# filter
movies[movies.duration >= 200]

# select the 'genre' Series from the filtered DataFrame
movies[movies.duration >= 200].genre

# or equivalently, use the 'loc' method
movies.loc[movies.duration >= 200, 'genre']
df2 = df[~(df.A > 0) | ~(df.B > 0)]


# CORRECT: use the '&' operator to specify that both conditions are required
movies[(movies.duration >=200) & (movies.genre == 'Drama')]

# INCORRECT: using the '|' operator would have shown movies that are either long or dramas (or both)
movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()


# use the '|' operator to specify that a row can match any of the three criteria
movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')].head(10)

# or equivalently, use the 'isin' method
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])].head(10)

# specify which columns to include by name
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])

# or equivalently, specify columns by position
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0, 4])
ufo.columns

# specify how many rows to read
ufo = pd.read_csv('http://bit.ly/uforeports', nrows=3)
ufo

# various methods are available to iterate through a DataFrame
for index, row in ufo.iterrows():
    print(index, row.City, row.State)


# only include numeric columns in the DataFrame
import numpy as np
drinks.select_dtypes(include=[np.number]).dtypes

# pass a list of data types to only describe certain types
drinks.describe(include=['object', 'float64'])
drinks.describe(include='all')


# calculate the mean of each numeric column
drinks.mean()

# or equivalently, specify the axis explicitly
drinks.mean(axis=0)


# calculate the mean of each row
drinks.mean(axis=1).head()



# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()

# use the boolean Series to filter the DataFrame
orders[orders.item_name.str.contains('Chicken')].head()


# string methods can be chained together
orders.choice_description.str.replace('[', '').str.replace(']', '').head()

# change the data type of an existing Series
drinks['beer_servings'] = drinks.beer_servings.astype(float)
drinks.dtypes
# alternatively, change the data type of a Series while reading in a file
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks.dtypes

# multiple aggregation functions can be applied simultaneously
drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max'])

# allow plots to appear in the notebook
%matplotlib inline
# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')


# compute a cross-tabulation of two Series
pd.crosstab(movies.genre, movies.content_rating)

# count how many times each value in the Series occurs
movies.genre.value_counts()

# display the unique values in the Series
movies.genre.unique()
movies.genre.nunique()

# count the number of missing values in each Series
ufo.isnull().sum()
notnull()


# use the 'isnull' Series method to filter the DataFrame rows
ufo[ufo.City.isnull()].head()


# if 'any' values are missing in a row, then drop that row
ufo.dropna(how='any')
# if 'all' values are missing in a row, then drop that row (none are dropped in this case)
ufo.dropna(how='all')

# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='any')
# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='all')

# explicitly include missing values
ufo['Shape Reported'].value_counts(dropna=False)

# fill in missing values with a specified value
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)

# set an existing column as the index
drinks.set_index('country', inplace=True)
drinks.head()
# index name is optional
drinks.index.name = None
drinks.head()
# restore the index name, and move the index back to a column
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
drinks.head()
# you can interact with any DataFrame using its index and columns
drinks.describe().loc['25%', 'beer_servings']

# elements in a Series can be selected by index (using bracket notation)
drinks.continent.value_counts()['Africa']

# any Series can be sorted by its values
drinks.continent.value_counts().sort_values()


# any Series can also be sorted by its index
drinks.continent.value_counts().sort_index()

# create a Series containing the population of two countries
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
people

# calculate the total annual beer servings for each country
(drinks.beer_servings * people).head()

# concatenate the 'drinks' DataFrame with the 'population' Series (aligns by the index)
pd.concat([drinks, people], axis=1).head()
pd.reset_index(drop=True, inplace=True)

# row 0, all columns
ufo.loc[0, :]
# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]
# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]
# this implies "all columns", but explicitly stating "all columns" is better
ufo.loc[0:2]
# rows 0 through 2 (inclusive), column 'City'
ufo.loc[0:2, 'City']

# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ['City', 'State']]
# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, 'City':'State']
# rows in which the 'City' is 'Oakland', column 'State'
ufo.loc[ufo.City=='Oakland', 'State']


# rows in positions 0 and 1, columns in positions 0 and 3
ufo.iloc[[0, 1], [0, 3]]

# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
ufo.iloc[0:2, 0:4]


# fill missing values using "backward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='bfill').tail()


# repeat this process for the 'country' Series
drinks['country'] = drinks.country.astype('category')
drinks.memory_usage(deep=True)


# strings are now encoded (0 means 'Africa', 1 means 'Asia', 2 means 'Europe', etc.)
drinks.continent.cat.codes.head()

# memory usage increased because we created 193 categories
drinks.country.cat.categories


# define a logical ordering for the categories
df['quality'] = df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
df.quality

# comparison operators work with ordered categories
df.loc[df.quality > 'good', :]


# use the 'random_state' parameter for reproducibility
ufo.sample(n=3, random_state=42)
# sample 75% of the DataFrame's rows without replacement
train = ufo.sample(frac=0.75, random_state=99)

# store the remaining 25% of the rows in another DataFrame
test = ufo.loc[~ufo.index.isin(train.index), :]

# create the 'Sex_male' dummy variable using the 'map' method
train['Sex_male'] = train.Sex.map({'female':0, 'male':1})
train.head()

# drop the first dummy variable ('female') using the 'iloc' method
pd.get_dummies(train.Sex).iloc[:, 1:].head()

# add a prefix to identify the source of the dummy variables
pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:].head()

# save the DataFrame of dummy variables and concatenate them to the original DataFrame
embarked_dummies = pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:]
train = pd.concat([train, embarked_dummies], axis=1)

# use the 'drop_first' parameter (new in pandas 0.18) to drop the first dummy variable for each feature
pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head()

# hour could be accessed using string slicing, but this approach breaks too easily
ufo.Time.str.slice(-5, -3).astype(int).head()


# convert 'Time' to datetime format
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()

# convenient Series attributes are now available
ufo.Time.dt.hour.head()
ufo.Time.dt.weekday_name.head()
ufo.Time.dt.dayofyear.head()

# compare a datetime Series with a timestamp
ufo.loc[ufo.Time >= ts, :].head()

# timedelta objects also have attributes you can access
(ufo.Time.max() - ufo.Time.min()).days


# count the duplicate items (True becomes 1, False becomes 0)
users.zip_code.duplicated().sum()

# count the duplicate rows
users.duplicated().sum()

# examine the duplicate rows (including all duplicates)
users.loc[users.duplicated(keep=False), :]

1. keep='first' (default): Mark duplicates as True except for the first occurrence.
2. keep='last': Mark duplicates as True except for the last occurrence.
3. keep=False: Mark all duplicates as True.


# drop the duplicate rows (inplace=False by default)
users.drop_duplicates(keep='first').shape

# replace the 'NOT RATED' values with 'NaN' (does not cause a SettingWithCopyWarning)
movies.loc[movies.content_rating=='NOT RATED', 'content_rating'] = np.nan


Solution: Any time you are attempting to create a DataFrame copy, use the copy method.
# explicitly create a copy of 'movies'
top_movies = movies.loc[movies.star_rating >= 9, :].copy()

# create a new Series using the Series constructor
s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')

# concatenate the DataFrame and the Series (use axis=1 to concatenate columns)
pd.concat([df, s], axis=1)


Goal: Map the existing values of a Series to a different set of values
Method: map (Series method)
train['Sex_num'] = train.Sex.map({'female':0, 'male':1})


Goal: Apply a function to each element in a Series
Method: apply (Series method)
Note: map can be substituted for apply in many cases, but apply is more flexible and thus is recommended
# calculate the length of each string in the 'Name' Series
train['Name_length'] = train.Name.apply(len)
train.loc[0:4, ['Name', 'Name_length']]

# round up each element in the 'Fare' Series to the next integer
import numpy as np
train['Fare_ceil'] = train.Fare.apply(np.ceil)

# alternatively, use a lambda function
train.Name.str.split(',').apply(lambda x: x[0]).head()

# define a function that returns an element from a list based on position
def get_element(my_list, position):
    return my_list[position]
train.Name.str.split(',').apply(get_element, position=0).head()

train.Name.str.split(',').head()

# apply the 'max' function along axis 0 to calculate the maximum value in each column
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0)

# use 'np.argmax' to calculate which column has the maximum value for each row
drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1).head()


# overwrite the existing DataFrame columns
drinks.loc[:, 'beer_servings':'wine_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)



# What if the columns you want to join on don't have the same name?
movies.columns = ['m_id', 'title']

ratings.columns
Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')
pd.merge(movies, ratings, left_on='m_id', right_on='movie_id').head()

movies = movies.set_index('m_id')
movies.head()
pd.merge(movies, ratings, left_index=True, right_on='movie_id').head()


pd.merge(A, B, how='inner')

inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys
outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically
left: use only keys from left frame, similar to a SQL left outer join; preserve key order
right: use only keys from right frame, similar to a SQL right outer join; preserve key order