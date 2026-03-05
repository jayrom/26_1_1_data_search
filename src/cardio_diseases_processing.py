import pandas as pd
import os

FILE_PATH = 'dataset/cardiovascular_disease/cardio_train.csv'
OUTPUT_NAME = 'dataset/cardiovascular_disease/cardio_subset_300.csv'
TARGET_SIZE = 300

def run_smart_sampler():
    if not os.path.exists(FILE_PATH):
        print(f"Error: Could not find {FILE_PATH}.")
        return

    # 1. Load data
    df = pd.read_csv(FILE_PATH, sep=';')
    df.columns = df.columns.str.strip() # Clean column names
    print(f"Loaded {len(df)} original records.")

    # 2. Find the target column
    target_col = [c for c in df.columns if 'cardio' in c.lower()]
    if not target_col:
        print(f"Available columns: {df.columns.tolist()}")
        return
    cardio_col = target_col[0]

    # 3. Add Clinical Calculations
    df['age_years'] = (df['age'] / 365.25).round(1)
    df['BMI'] = (df['weight'] / ((df['height'] / 100) ** 2)).round(1)
    
    # Simple Risk Score
    df['Risk_Score'] = (
        (df['age_years'] * 0.1) + 
        (df['cholesterol'] * 2) + 
        (df['ap_hi'] / 100) + 
        (df['BMI'] * 0.05)
    ).round(2)

    # 4. Stratified sampling
    positives = df[df[cardio_col] == 1].sample(n=TARGET_SIZE // 2, random_state=42)
    negatives = df[df[cardio_col] == 0].sample(n=TARGET_SIZE // 2, random_state=42)
    
    subset_df = pd.concat([positives, negatives]).sample(frac=1, random_state=42)
    subset_df = subset_df.reset_index(drop=True)

    # 5. Save and finish
    subset_df.to_csv(OUTPUT_NAME, index=False)
    
    print("-" * 30)
    print(f"Success! Created {OUTPUT_NAME}")
    if cardio_col in subset_df.columns:
        dist = subset_df[cardio_col].value_counts().to_dict()
        print(f"Cardio Distribution (0=Healthy, 1=Disease): {dist}")
    print("-" * 30)

if __name__ == "__main__":
    run_smart_sampler()