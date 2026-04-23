# Raman Creatinine Quantification

This repository contains a complete Raman spectroscopy workflow for creatinine quantification, from raw acquisition parsing to preprocessing, augmentation, and model evaluation.

## Highlights

- End-to-end preprocessing pipeline for raw Raman `.npz` acquisitions.
- Cleaned and exported per-concentration spectra in `data_preprocessed/`.
- Classical and deep-learning experiments collected in Jupyter notebooks.
- Saved model weights for the current best checkpoints.

## Repository Layout

```text
.
|-- RamanPreprocessing.ipynb
|-- model.ipynb
|-- data_raw/
|-- data_preprocessed/
|-- best_model.pth
|-- best_specnet.pth
|-- scripts/
|   `-- plot_spe_spectra.py
|-- docs/
|   `-- repo-banner.svg
`-- requirements.txt
```

## Workflow

1. Open `RamanPreprocessing.ipynb` to load the raw experiment files, convert wavelengths to Raman shift, clean each spectrum, and export processed assets.
2. Use the same notebook to generate balanced augmented arrays in each concentration folder under `data_preprocessed/`.
3. Open `model.ipynb` to inspect the processed spectra, fit baseline regressors, and evaluate the neural models.

## Getting Started

```bash
pip install -r requirements.txt
jupyter lab
```

Then run the notebooks in this order:

1. `RamanPreprocessing.ipynb`
2. `model.ipynb`

## Data and Artifacts

- `data_raw/` stores the original Raman acquisitions.
- `data_preprocessed/` stores processed spectra (`.npz`), quick-look plots (`.png`), and augmented training arrays (`augmented_300.npy`).
- `best_model.pth` stores the main trained checkpoint used in the modeling notebook.
- `best_specnet.pth` stores the 1D convolutional baseline checkpoint.

## SPE Utility

The utility script in `scripts/plot_spe_spectra.py` is intended for quick inspection of Princeton Instruments `.spe` files. It depends on the external `spe2py` package, which is separate from the notebook requirements.

## Notes

- The notebooks have been cleaned so comments and explanatory text are in English throughout.
- Notebook outputs were cleared to keep the repository lighter and avoid committing stale warnings or mixed-language output.
