# Zillow 2017 Predictions

# Project Description

Like all businesses, Zillow wants to make a profit and keep the profit machine going. We will be looking into the Zillow 2017 transactions and will be able to help predict (with confidence) home values based on certain drivers, statisitical tests, and regression machine learning algorithms..

# Project Goal

- Discover drivers of Single Family home value for Zillow in 2017.
- Use drivers to develop a machine learning model that accurately predicts home value
- This information could be used for furture years in helping Zillow achieve max profit

# Initial Thoughts

- Does more square footage of a home equate more tax value?
- Does the number of bathrooms affect number of bathrooms?
- Does lot size affect tax value?
- Does number of bedrooms have an affect on tax value?


# The Plan

- Acquire data from Sequel Ace database
- Renamed columns to promote readability
- Checked for nulls and outliers
- Checked that data types were appropriate and changed what was necessary  
- Split data into train/validate/test samples

#### Explore data in search of drivers of home value

##### Answer the following initial questions
- Does more square footage of a home equate more tax value?
- Does the number of bathrooms affect tax value?
- Does lot size affect tax value?
- Does the number of bedrooms affect tax value?

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|bedroomcnt|Specifies the number of bedrooms in the home|
|bathroomcnt|Specifies the number of bathrooms in the home|
|calculatedfinishedsquarefeet|Specifies the total finished square footage of the home|
|taxvaluedollarcnt|The total tax assessed value of the parcel|
|lotsizesquarefeet|Specifies total square footage of lot the home sits on|
|yearbuilt|Year that the home was built|

# Steps to Reproduce

- Clone this repo.
- Acquire the data from Kaggle
- Put the data in the file containing the cloned repo.
- Run notebook.

# Takeaways and Conclusions

- Square feet, bedrooms, and bathrooms are all drivers to tax value
- Higher bedroom count, higher bathroom count, and higher square footage amount all contribute to a higher tax value of a home


# Recommendations

- Push the homes with above average bedroom count and bathroom count
- Push homes with above average home square footage
