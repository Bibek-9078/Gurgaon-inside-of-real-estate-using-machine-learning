
# Flat-Price-Predictor

The Flat-Price-Predictor in Gurgaon is a tool or system designed to forecast and estimate the prices of flats or apartments in the Indian state of Haryana. It utilizes various data and factors, including market trends, location, property features, and economic indicators, to provide potential buyers or investors with insights into expected flat prices in the region.

## Roadmap

![Static Badge](https://img.shields.io/badge/1.Data_gathering-grey) ![Static Badge](https://img.shields.io/badge/2.Data_preprossing%2FCleaning-grey) ![Static Badge](https://img.shields.io/badge/3.Feature_Engineering-grey) ![Static Badge](https://img.shields.io/badge/4.Exploratory_data%20analysis%20(EDA)%20-grey) ![Static Badge](https://img.shields.io/badge/5.Outlier_%20Detection%20and%20Removal%20-grey) ![Static Badge](https://img.shields.io/badge/6.Missing_%20Value%20imputation%20-grey) ![Static Badge](https://img.shields.io/badge/7.Feature%20_selection%20-grey) ![Static Badge](https://img.shields.io/badge/8.Model%20_Selection%20%26%20Productionalization%20-grey) ![Static Badge](https://img.shields.io/badge/9.%20Building%20_the%20Recommender%20System%20-grey)

## dataset


## installation 


## 1.Data gathering 

        a. Project overview in details

        b. Gather data for the project

        c. Details of the data

## 2.Data preprossing/Cleaning

        a. Merging House and Flats Data

        b. Basic Level Data Cleaning

## 3.Feature Engineering

    A. Feature Engineering on Columns:

        i.Additional Room

        ii.Area With Type

        iii.Age Possession

        iv.Furnish Details

        v.features : luxury Score
        
## 4.Exploratory data analysis (EDA) 

        A. Univariate Analysis

        B. PandsProfiling

        C. Multivariate Analysis

## 5.Outlier Detection and Removal

        a. Outlier Detection And removal

## 6.Missing Value imputation

        a. Outlier Detection and Removal on area and bedroom

        b. Missing Value Imputation

## 7.Feature Selection

          a. Feature Selection

        i.Correlation Technique

        ii.Random Forest Feature Importance

        iii.Gradient Boosting Feature Importance

        iv.Permutation Importance

        v.LASSO

        vi.Recursive Feature Elimination

        vii.Linear Regression with Weights

        viii.SHAP (Explainable AI)

             b. Linear Regression - Base Model

        i. One-Hot Encoding

        ii. Transformation

        iii. Pipeline for Linear Regression
           c. SVR
           
## 8. Model Selection & Productionalization

        a.Price Prediction Pipeline
        
                i. Encoding Selection
                
                        1. Ordinal Encoding
                        
                        2. OHE
                        
                        3. OHE with PCA
                        
                        4. Target Encoding
                        
                ii. Model Selection
                
b.Price Prediction Web Interface -Streamlit

 ## 9. Building the Recommender System

        a. Recommender System using Top Facilities

        b. Recommender System using Price Details

        c. Recommender System using Location Advantages

        d.Evaluating Recommendation Results

        e.Web Interface for Recommendation (Streamlit)

## setup
## Demo






# Gurgaon-inside-of-real-estate-using-machine-learning
The Flat-Price-Predictor in Gurgaon is a tool or system designed to forecast and estimate the prices of flats or apartments in the Indian state of Haryana. It utilizes various data and factors, including market trends, location, property features, and economic indicators, to provide potential buyers or investors with insights.

## Roadmap

![Static Badge](https://img.shields.io/badge/1.Data_gathering-grey) ![Static Badge](https://img.shields.io/badge/2.Data_preprossing%2FCleaning-grey) ![Static Badge](https://img.shields.io/badge/3.Feature_Engineering-grey) ![Static Badge](https://img.shields.io/badge/4.Exploratory_data%20analysis%20(EDA)%20-grey) ![Static Badge](https://img.shields.io/badge/5.Outlier_%20Detection%20and%20Removal%20-grey) ![Static Badge](https://img.shields.io/badge/6.Missing_%20Value%20imputation%20-grey) ![Static Badge](https://img.shields.io/badge/7.Feature%20_selection%20-grey) ![Static Badge](https://img.shields.io/badge/8.Model%20_Selection%20%26%20Productionalization%20-grey)


### 2 DATA CLEANNING
**Data Cleaning of flat**:
   - Dropped unnecessary columns ('link', 'property_id') using `df.drop(columns=['link','property_id'], inplace=True)`.
   - Renamed the 'area' column to 'price_per_sqft' using `df.rename(columns={'area':'price_per_sqft'},inplace=True)`.
   - Cleaned the 'society' column by removing numeric ratings and converting to lowercase.
   - Removed rows with 'Price on Request' in the 'price' column.
   - Converted the 'price' column values to numeric format.
   - Cleaned the 'price_per_sqft' column by removing unwanted characters and converting to float.
   - Cleaned and converted the 'bedRoom', 'bathroom', 'balcony', and 'floorNum' columns to appropriate data types.
   - Filled missing values in the 'additionalRoom' column with 'not available' and converted to lowercase.
   - Cleaned the 'floorNum' column by extracting numeric values and handling special cases.
   - Filled missing values in the 'facing' column with 'NA'.
   - Added new columns ('area' and 'property_type').
   - Saved the cleaned DataFrame to a new CSV file named 'flats_cleaned.csv' using `df.to_csv('flats_cleaned.csv',index=False)`.

**Data Cleaning of house**:
   - Dropped unnecessary columns ('link', 'property_id') using `df.drop(columns=['link','property_id'], inplace=True)`.
   - Renamed the 'rate' column to 'price_per_sqft' using `df.rename(columns={'rate':'price_per_sqft'},inplace=True)`.
   - Cleaned the 'society' column by removing numeric ratings and converting to lowercase.
   - Replaced 'nan' values in the 'society' column with 'independent'.
   - Removed rows with 'Price on Request' in the 'price' column.
   - Converted the 'price' column values to numeric format.
   - Cleaned the 'price_per_sqft' column by removing unwanted characters and converting to float.
   - Cleaned and converted the 'bedRoom', 'bathroom', and 'balcony' columns to appropriate data types.
   - Cleaned and renamed the 'noOfFloor' column to 'floorNum'.
   - Filled missing values in the 'facing' column with 'NA'.
   - Added new columns ('area' and 'property_type').

### ADVANCE LABEL DATA CLEANNING

   - Extracted the 'sector' information from the 'property_name' column and cleaned it.
   - Standardized sector names by replacing variations with common sector names.
   - Removed sectors with less than 3 occurrences.
   - Standardized sector names for specific cases.
   - Corrected inconsistencies in sector names.
   - Handled specific cases of incorrect sector names.
   - Corrected additional sectors named 'new'.
   - Updated sector names for specific rows with incorrect values.
   - Dropped unnecessary columns ('property_name', 'address', 'description', 'rating').
   - No feature engineering was mentioned in the provided code.
   - Saved the cleaned DataFrame to a new CSV file named 'gurgaon_properties_cleaned_v1.csv' using `df.to_csv('gurgaon_properties_cleaned_v1.csv',index=False)`.

### 3.Feature Engineering:

   - Extracted and converted various types of property area from the 'areaWithType' column.
   - Extracted and categorized additional room details.
   - Categorized age of possession into different groups.
   - Extracted and categorized furnish details into different types.
   - Extracted, imputed, and categorized features based on societal amenities.
   - Saved the cleaned DataFrame to a new CSV file named 'gurgaon_properties_cleaned_v2.csv' using `df.to_csv('gurgaon_properties_cleaned_v2.csv',index=False)`.
   - Extracted and converted area types (Super Built up, Built Up, Carpet).
   - Categorized additional room details.
   - Categorized age of possession.
   - Extracted and categorized furnish details.
   - Imputed and categorized features based on societal amenities.
   - Calculated the luxury score for each property based on societal amenities.
   - Dropped unnecessary column ('nearbyLocations','furnishDetails','features','features_list','additionalRoom').

### 4.Exploratory data analysis (EDA)
