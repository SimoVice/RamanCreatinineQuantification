"""Inspect Princeton Instruments `.spe` files and plot a few Raman spectra.

This helper script depends on the external `spe2py` package. It opens the
package's file dialog, loads one or more `.spe` files, validates that the
wavelength grids match, and plots up to the first three spectra.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import spe2py as spe


def load_intensities() -> tuple[np.ndarray, np.ndarray]:
    """Load one or more SPE files and return a shared wavelength axis."""
    loaded = spe.load()
    objects = loaded if isinstance(loaded, list) else [loaded]

    reference_wavelength = objects[0].file.wavelength
    intensities = np.zeros((len(objects), len(reference_wavelength)))

    for index, spectrum in enumerate(objects):
        wavelength = spectrum.file.wavelength
        if not np.allclose(wavelength, reference_wavelength):
            raise ValueError(f"Wavelength mismatch in file {index}")
        intensities[index] = spectrum.file.data[0][0][0]

    return reference_wavelength, intensities


def plot_spectra(wavelength: np.ndarray, intensities: np.ndarray) -> None:
    """Plot up to the first three spectra loaded from the SPE files."""
    for index in range(min(3, intensities.shape[0])):
        plt.plot(wavelength, intensities[index], label=f"Spectrum {index + 1}")

    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity (a.u.)")
    plt.title("Raman Spectra")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Run the SPE inspection workflow."""
    wavelength, intensities = load_intensities()
    plot_spectra(wavelength, intensities)

    # Example export if you want to keep the loaded spectra on disk:
    # np.savez("raman_spectra.npz", wavelength=wavelength, intensities=intensities)


if __name__ == "__main__":
    main()
