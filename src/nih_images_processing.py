import pandas as pd
import os
import shutil

# CONFIGURATION
NIH_CSV_PATH = 'dataset/nih_chest_x-ray/sample_labels.csv'  # Original metadata
SOURCE_IMG_DIR = 'dataset/nih_chest_x-ray/images/'          # Original 5,600 images
OUTPUT_DIR = 'dataset/nih_chest_x-ray/NIH_Xray_300'
TARGET_SIZE = 300

def downsample_xray():
    df = pd.read_csv(NIH_CSV_PATH)
    
    # Prioritize Cardiomegaly (Heart) and Infiltration (Lungs). See README for details
    priority_labels = ['Cardiomegaly', 'Infiltration', 'Effusion', 'No Finding']
    
    selected_indices = []
    per_label = TARGET_SIZE // len(priority_labels)

    for label in priority_labels:
        # Filter for rows containing the label
        group = df[df['Finding Labels'].str.contains(label)].sample(n=min(per_label, len(df)), random_state=42)
        selected_indices.append(group)

    subset_df = pd.concat(selected_indices).drop_duplicates().head(TARGET_SIZE)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for img_name in subset_df['Image Index']:
        src = os.path.join(SOURCE_IMG_DIR, img_name)
        if os.path.exists(src):
            shutil.copy(src, os.path.join(OUTPUT_DIR, img_name))
            
    subset_df.to_csv(os.path.join(OUTPUT_DIR, 'xray_subset_metadata.csv'), index=False)
    print(f"Done! 300 X-rays copied to {OUTPUT_DIR}")

downsample_xray()