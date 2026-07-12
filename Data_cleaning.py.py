# ==========================================
# Project 1: Data Cleaning & Preparation
# E-Commerce Sales Dataset
# ==========================================

import pandas as pd

# Load Dataset
df = pd.read_excel("Dataset for Data Analytics project1.xlsx")

print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)

# Dataset Information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

if "TrackingNumber" in df.columns:
    df["TrackingNumber"] = df["TrackingNumber"].fillna("Not Available")

if "ReferralSource" in df.columns:
    df["ReferralSource"] = df["ReferralSource"].fillna("Unknown")

# Remove Duplicates
print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# Convert Date
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])

# Remove Extra Spaces
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].str.strip()

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Shape:")
print(df.shape)

# Save Cleaned Dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned file saved as: Cleaned_Dataset.xlsx")