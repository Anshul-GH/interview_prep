1. Introduction - Self
2. Check for candidate's name
3. Explain the interview flow


```python
# Basic/Intermediate

# B1. Given a list:
[1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
# Push all the even numbers to the front and odd numbers to the back
# Expected Output:
[2,4,6,8,12,4,2,2,2,4,6,1,3,7,9,5,7,5,1,3]
# Do not use any temporary variables.
```


```python
# M2. Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:
# Input: 
nums1 = [1,2,2,1], nums2 = [2,2]
# Output: 
[2,2]
# Example 2:
# Input: 
nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: 
[4,9]
# Explanation: [9,4] is also accepted.
```

Q. End-to-end Machine Learning lifecycle
Here are the steps involved in an ML model lifecycle.

Step 1: Business context and define a problem

Step 2: Translating to AI problem and approach

Step 3: Milestones and Planning

Step 4: Data gathering and Understanding

Step 5: Data preparation

Step 6: Data Cleaning

Step 7: Exploratory data analysis

Step 8: Feature engineering and selection

Step 9: ML Model assumption and checks

Step 10: Data preparation for modelling

Step 11: Model Building

Step 12: Model Validation & Evaluation

Step 13: Predictions & Model deployment

Q. What is the Differentiate between Univariate, Bivariate, and Multivariate analysis?
1. Univariate:
    When we analyze one variable at a time, it is called univariate data analysis. 
    This analysis aims to describe the variable in question and find patterns that exist within it. 
    Example: height of students
2. Bivariate:
    Bivariate data involves two different variables. 
    The analysis of this type of data deals with causes and relationships. 
    The investigation determines the relationship between the two variables, where one of the variables is the target variable. 
    Example: temperature and ice cream sales in the summer season.
3. Multivariate: 
    Analyzing three or more variables together is categorized under multivariate data analysis. 
    It is similar to a bivariate but contains more than one dependent variable.
    Example: data for house price prediction

Q. How to perform univariate analysis for numerical and categorical variables?

    For the Numerical variables:
    One can plot a Box and Whiskers plot and KDE plot to better understand the data; below is an example of the Age column plotted using both box and KDE plot. 

    For the Categorical variables:
    Bar plots and Pie Charts are a great way to analyze categorical variables to understand the categorical data. The two plots represent the number (in a bar chart) and proportion (in a pie chart) of individuals opting for Course_types.

Q. What is regularization and what are the different types of regularization methods available.
Overfitting is a phenomenon that occurs when a Machine Learning model is constraint to training set and not able to perform well on unseen data. 

Regularization is a technique used to reduce the errors by fitting the function appropriately on the given training set and avoid overfitting. 
The commonly used regularization techniques are : 
    L1 regularization
    L2 regularization
    Dropout regularization

A regression model which uses L1 Regularization technique is called LASSO(Least Absolute Shrinkage and Selection Operator) regression.  - Lasso Regression adds “absolute value of magnitude” of coefficient as penalty term to the loss function(L). 
A regression model that uses L2 regularization technique is called Ridge regression. - Ridge regression adds “squared magnitude” of coefficient as penalty term to the loss function(L). 

Q. Hyperparameter Tuning
Hyperparameter types:

    K in K-NN
    Regularization constant, kernel type, and constants in SVMs
    Number of layers, number of units per layer, regularization in neural network

Generalization (test) error of learning algorithms has two main components:

    Bias: error due to simplifying model assumptions
    Variance: error due to randomness of the training set

The trade-off between these components is determined by the complexity of the model and the amount of training data. The optimal hyperparameters help to avoid under-fitting (training and test error are both high) and over-fitting (Training error is low but test error is high)

Hyperparameter Tuning

Hyperparameters: Vanilla linear regression does not have any hyperparameters. Variants of linear regression (ridge and lasso) have regularization as a hyperparameter. The decision tree has max depth and min number of observations in leaf as hyperparameters.

Optimal Hyperparameters: Hyperparameters control the over-fitting and under-fitting of the model. Optimal hyperparameters often differ for different datasets. To get the best hyperparameters the following steps are followed:

1. For each proposed hyperparameter setting the model is evaluated

2. The hyperparameters that give the best model are selected.

Hyperparameters Search: Grid search picks out a grid of hyperparameter values and evaluates all of them. Guesswork is necessary to specify the min and max values for each hyperparameter. Random search randomly values a random sample of points on the grid. It is more efficient than grid search. Smart hyperparameter tuning picks a few hyperparameter settings, evaluates the validation matrices, adjusts the hyperparameters, and re-evaluates the validation matrices. Examples of smart hyper-parameter are Spearmint (hyperparameter optimization using Gaussian processes) and Hyperopt (hyperparameter optimization using Tree-based estimators).
