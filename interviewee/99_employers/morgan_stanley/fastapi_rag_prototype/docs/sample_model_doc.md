# Sample Model: Credit Risk Probability Model

## Overview
Predicts the probability of default for consumer credit products.

## Inputs
- Applicant income
- Credit score
- Employment history
- Past default history
- Loan amount

## Outputs
- Probability of default (0–1)
- Risk band (Low, Medium, High)

## Method
- Uses a gradient boosting classifier.
- Trained on historical customer data.
- Features are engineered from raw application data.

## assumptions
- Data is representative of future applicants.
- No major regulatory or market regime changes.

## Risks
- Bias in training data
- Over-reliance on model without human review
- Insufficient monitoring of model drift
