# Financial Inclusion in Africa

This is a machine learning project predicting which individuals in Kenya, Rwanda, Tanzania, and Uganda are most likely to have or use a bank account, built for the Zindi "Financial Inclusion in Africa" competition. The goal is a working submission and a demonstration of the full data science lifecycle: EDA, preprocessing, baseline and iterative modeling, and error analysis.

[Data](https://zindi.world/competitions/financial-inclusion-in-africa/data) comes from Finscope surveys conducted in 2016–2018 across 33,600 individuals in the four countries. `Train.csv` includes the target (`bank_account`); `Test.csv` mirrors it without the target. The target is binary and notably imbalanced (far more "No" than "Yes"). `VariableDefinitions.csv` documents every column.

Model quality is scored by Mean Absolute Error (MAE) between predicted values (0 to 1) and the true labels for a person having a bank account or not (Yes = 1, No = 0), so submissions need exactly two columns: `unique_id` (which combines the individual's ID with their country name) and `bank_account`.

<br>

**Project structure:**
```
data/ # Zindi datasets — see Setup below (gitignored, not in the repo)
notebooks/ # 01_eda -> 02_preprocessing -> 03_baseline_models -> 04_model_experiments -> 05_error_analysis
src/ # reusable preprocessing and data-splitting functions
models/ # saved trained models
presentation/ # milestone and final presentation materials
docs/ # legacy assignment/kanban materials — not used, gitignored
```

<br>

**Setup instructions:**

1. Clone the repo and move into the project folder:
```bash
   git clone git@github.com:elhamrouzban/Financial_Inclusion_in_Africa.git
   cd Financial_Inclusion_in_Africa
```
1. Install dependencies:
```bash
   uv sync
```
1. Download the competition data from the [competition's Data tab](https://zindi.africa/competitions/financial-inclusion-in-africa/data) (Zindi account required): `Train.csv`, `Test.csv`, `SampleSubmission.csv`, and `VariableDefinitions.csv`. Place all four files in `data/`.
2. Open the project in VS Code (`code .`) and select the Python environment created by `uv sync` as the kernel before running any notebook in `/notebooks`.

> Competition data cannot be shared publicly or uploaded to external platforms, so `/data` is gitignored:

```
# Competition data (must not be committed — see README)
data/*
!data/.gitkeep
```

## Steps to Get Started

| # | Step | What it involves |
|---|------|-------------------|
| 1 | Read the rules and data dictionary | Review the competition page and `data/VariableDefinitions.csv`. |
| 2 | Set up your environment | `uv sync` to install dependencies from `pyproject.toml`. |
| 3 | Load and explore the data | `notebooks/01_eda.ipynb` |
| 4 | Exploratory data analysis (EDA) | `notebooks/01_eda.ipynb` |
| 5 | Preprocess the data consistently | `notebooks/02_preprocessing.ipynb`, using `src/preprocessing.py`'s `build_preprocessor()` |
| 6 | Split out a validation set | `src/data_split.py`'s `load_and_split_data()` (stratified 80/20 split) |
| 7 | Train a baseline model | `notebooks/03_baseline_models.ipynb` |
| 8 | Train and compare stronger models | `notebooks/04_model_experiments.ipynb` (in progress) |
| 9 | Tune hyperparameters | `notebooks/04_model_experiments.ipynb` (in progress) |
| 10 | Refit on the full training data | `notebooks/04_model_experiments.ipynb` (in progress) |
| 11 | Generate predictions on `Test.csv` | `notebooks/05_error_analysis.ipynb` (in progress), or a future `06_final_model.ipynb` |
| 12 | Build the submission file | Match `data/SampleSubmission.csv`'s format exactly |
| 13 | Submit and check the leaderboard | Upload on Zindi (10-submissions/day cap) |
| 14 | Iterate | Revisit steps 8–11 based on leaderboard feedback |

## Folders and Files

| File / Folder | Description |
|---|---|
| **Git Repo** | [Git Repo](https://github.com/elhamrouzban/Financial_Inclusion_in_Africa) |
| [**assets**](assets/) | Assets used for this project. |
| **data** | Where the Zindi datasets go locally. Gitignored — see Setup above to download them. |
| [**docs**](docs/) | Legacy materials. Not used by the current pipeline; gitignored. |
| [**models**](models/) | Where trained models are saved. |
| [**notebooks**](notebooks/) | Notebooks used for the competition. |
| [**notebooks/01_eda.ipynb**](notebooks/01_eda.ipynb) | Exploratory Data Analysis |
| [**notebooks/02_preprocessing.ipynb**](notebooks/02_preprocessing.ipynb) | Preprocessing Data |
| [**notebooks/03_baseline_models.ipynb**](notebooks/03_baseline_models.ipynb) | Baseline Models |
| [**notebooks/04_model_experiments.ipynb**](notebooks/04_model_experiments.ipynb) | Model Experiments (in progress) |
| [**notebooks/05_error_analysis.ipynb**](notebooks/05_error_analysis.ipynb) | Error Analysis (in progress) |
| [**src**](src/) | Source files |
| [**src/data_split.py**](src/data_split.py) | Does a stratified 80/20 train/validation split, reading from `data/Train_clean.csv` (produced by `02_preprocessing.ipynb`). |
| [**src/preprocessing.py**](src/preprocessing.py) | Builds a `ColumnTransformer` (StandardScaler on the numeric columns, `OneHotEncoder(handle_unknown="ignore")` on the categoricals). |
| [**presentation**](presentation/) | Folder with presentation materials |
| [**PROJECT_WORKFLOW.md**](PROJECT_WORKFLOW.md) | The team's master roadmap — ML workflow phases, target repo structure, and Git/GitHub workflow. |
| [**StarterNotebook.ipynb**](StarterNotebook.ipynb) | Zindi's original walkthrough notebook. Kept for reference; superseded by the `/notebooks` pipeline above. |
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies. |
| [**uv.lock**](uv.lock) | Dependency lock file. |

<br>

---

## EDA Summary
_To be completed after `01_eda.ipynb` is finalized._

## Models Tested

**Dummy baseline** (`DummyClassifier`, `most_frequent` strategy) — always predicts the majority class, used as the floor any real model must beat:

| Metric | Value |
|---|---|
| Accuracy | 0.8593 |
| Error Rate | 0.1407 |
| Macro F1 | 0.4622 |
| Class 1 Recall | 0.0000 |
| Class 1 F1 | 0.0000 |

_Additional models to be added as `04_model_experiments.ipynb` is filled in._

## Final Results
_Pending — no model beyond the dummy baseline has been trained on the new preprocessing pipeline yet._

## Limitations
_To be completed alongside error analysis (`05_error_analysis.ipynb`)._

## Next Steps
- Fill in `04_model_experiments.ipynb` and `05_error_analysis.ipynb`.
- Once a final model is chosen, generate a submission and record results here.