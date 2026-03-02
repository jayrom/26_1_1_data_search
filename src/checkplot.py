import h5py
import matplotlib.pyplot as plt
import os

# Path to one of your new subset files
subset_folder = 'ECG_Proportional_300'
first_file = os.listdir(subset_folder)[0] # Grab the first .h5 file
file_path = os.path.join(subset_folder, first_file)

with h5py.File(file_path, 'r') as f:
    # Most ECG datasets use 'signal' or 'data' as the key
    # Let's assume 'signal' based on common HDF5 cardiac structures
    signal = f['signal'][:] 
    
    # Create a plot for the first 3 leads (I, II, III)
    fig, axes = plt.subplots(3, 1, figsize=(15, 10), sharex=True)
    lead_names = ['Lead I', 'Lead II', 'Lead III']
    
    for i in range(3):
        # Plotting the first 2500 samples (5 seconds at 500Hz)
        axes[i].plot(signal[i, :2500], color='red', linewidth=0.8)
        axes[i].set_title(lead_names[i])
        axes[i].grid(True, linestyle='--', alpha=0.5)
        axes[i].set_ylabel('mv')

    plt.xlabel('Samples')
    plt.tight_layout()
    plt.show()