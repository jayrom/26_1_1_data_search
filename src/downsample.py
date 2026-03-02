import pandas as pd
import os
import shutil

# CONFIGURATION

METADATA_PATH = r'dataset/metadata.csv'     # Path to the metadata CSV file
SOURCE_H5_FOLDER = r'dataset/records'       # Folder wcontaining the original .h5 files
OUTPUT_FOLDER = 'dataset/ECG_300'
TARGET_TOTAL = 300

def run_downsample():

    # 1. Load metadata
    try:
        # Using python engine to handle mixed separators ("," and ";")
        df = pd.read_csv(METADATA_PATH, sep=None, engine='python')
        df.columns = df.columns.str.strip() # Remove spaces
        print(f"Successfully loaded {len(df)} records.")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    # Identify columns
    aha_col = 'AHA_Code' if 'AHA_Code' in df.columns else [c for c in df.columns if 'AHA' in c][0]
    id_col = 'ECG_ID' if 'ECG_ID' in df.columns else [c for c in df.columns if 'ID' in c][0]

    # 2. Manual Proportional Sampling (Avoids the GroupBy KeyError)
    # We calculate how many we need from each code manually
    counts = df[aha_col].value_counts(normalize=True)
    samples = []
    
    for code, proportion in counts.items():
        n_to_sample = max(1, int(proportion * TARGET_TOTAL))
        group = df[df[aha_col] == code]
        samples.append(group.sample(n=min(len(group), n_to_sample), random_state=42))
    
    subset_df = pd.concat(samples).sample(frac=1, random_state=42) # Combine and shuffle

    # 3. Force it to exactly 300
    if len(subset_df) > TARGET_TOTAL:
        subset_df = subset_df.head(TARGET_TOTAL)
    elif len(subset_df) < TARGET_TOTAL:
        extra = df[~df[id_col].isin(subset_df[id_col])].sample(TARGET_TOTAL - len(subset_df))
        subset_df = pd.concat([subset_df, extra])

    subset_df = subset_df.reset_index(drop=True)

    # 4. Success Check
    print("-" * 30)
    print(f"Created subset: {len(subset_df)} records.")
    # Check if column exists before printing
    if aha_col in subset_df.columns:
        print("Top 5 Diagnosis Distributions:")
        print(subset_df[aha_col].value_counts(normalize=True).head())
    else:
        print("Warning: AHA_Code column hidden. Available columns:", subset_df.columns.tolist())
    print("-" * 30)

    # 5. File Copying
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    copied = 0
    for ecg_id in subset_df[id_col]:
        filename = f"{ecg_id}.h5"
        src = os.path.join(SOURCE_H5_FOLDER, filename)
        dst = os.path.join(OUTPUT_FOLDER, filename)
        if os.path.exists(src):
            shutil.copy(src, dst)
            copied += 1
            
    subset_df.to_csv(os.path.join(OUTPUT_FOLDER, 'subset_metadata.csv'), index=False)
    print(f"Finished! {copied} files copied to {OUTPUT_FOLDER}")

if __name__ == "__main__":
    run_downsample()