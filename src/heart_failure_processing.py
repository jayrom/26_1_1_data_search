import pandas as pd
import os

# CONFIGURATION
INPUT_FILE = 'dataset/heart_failure/heart.csv' 
OUTPUT_FILE = 'dataset/heart_failure/heart_failure_subset_300.csv'
TARGET_SIZE = 300

def run_heart_downsampler():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Could not find {INPUT_FILE}. Please check the filename!")
        return

    # 1. Load the data
    df = pd.read_csv(INPUT_FILE)
    df.columns = df.columns.str.strip() # Remove hidden spaces
    print(f"Successfully loaded {len(df)} records.")

    # 2. Identify target column
    target_col = 'HeartDisease' if 'HeartDisease' in df.columns else [c for c in df.columns if 'Heart' in c][0]
    
    # 3. Stratified Sampling (150 sick, 150 healthy) to maintain balance
    positives = df[df[target_col] == 1].sample(n=TARGET_SIZE // 2, random_state=42)
    negatives = df[df[target_col] == 0].sample(n=TARGET_SIZE // 2, random_state=42)

    # Combine and shuffle
    subset_df = pd.concat([positives, negatives]).sample(frac=1, random_state=42)
    subset_df = subset_df.reset_index(drop=True)

    # 4. Save and finish
    subset_df.to_csv(OUTPUT_FILE, index=False)
    
    print("-" * 30)
    print(f"Success! Created {OUTPUT_FILE}")
    print(f"Key Features available: Age, Sex, MaxHR, Cholesterol, RestingBP")
    print(f"Disease Distribution: {subset_df[target_col].value_counts().to_dict()}")
    print("-" * 30)

if __name__ == "__main__":
    run_heart_downsampler()