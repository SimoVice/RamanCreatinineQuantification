import spe2py as spe
import matplotlib.pyplot as plt
import numpy as np

# Load SPE files via file dialog
obj = spe.load()

# Normalize to list
if not isinstance(obj, list):
    obj = [obj]

# Extract wavelength from the first file
reference_wl = obj[0].file.wavelength
n_points = len(reference_wl)
n_files = len(obj)

# Initialize array for intensities
intensities = np.zeros((n_files, n_points))

# Fill intensity array and check wavelength consistency
for i, spe_tool in enumerate(obj):
    wl = spe_tool.file.wavelength
    if not np.allclose(wl, reference_wl):
        raise ValueError(f"Wavelength mismatch in file {i}")
    intensities[i] = spe_tool.file.data[0][0][0]

# Plot the first 3 spectra
for i in range(min(3, n_files)):
    plt.plot(reference_wl, intensities[i], label=f"Spectrum {i+1}")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity (a.u.)")
plt.title("Raman Spectra")
plt.legend()
plt.show()

# Save both arrays in a .npz file
# np.savez("raman_spectra.npz", wavelength=reference_wl, intensities=intensities)
