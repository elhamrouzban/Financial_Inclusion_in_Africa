# Financial Inclusion in Africa

This is a machine learning competition centered on financial inclusion. The goal is to build a model that predicts which individuals in Kenya, Rwanda, Tanzania, and Uganda are most likely to have or use a bank account, using demographic and financial-behavior data from surveys conducted between 2016 and 2018 across roughly 33,600 people. The target is 1 if the person has a bank account, 0 if not. The model is split into a 70% training set with the target included and a 30% test set.

Model quality is scored by Mean Absolute Error (MAE) between predicted values (0 to 1) and the true labels, so submissions need exactly two columns: `unique_id` (which combines the individual's ID with their country name) and `bank_account`. 


The data comes in five files: `Train.csv`, `Test.csv`, `VariableDefinitions.csv` (a data dictionary explaining each column), `SampleSubmission.csv` (the exact format your submission file needs to match), and `StarterNotebook.ipynb` (Zindi's walkthrough notebook).

> Rules while working on the competition: only publicly available/open-source packages, no sharing the competition data outside the platform.
> Competition data cannot be shared publicly or uploaded to external platforms and needs a .`gitignore` addition:


```
# Competition data (must not be committed)
data/*
!data/.gitkeep
```

## Folders and Files

| File / Folder | Description |
|---|---|
| **Git Repo** | [Git Repo](https://github.com/elhamrouzban/Financial_Inclusion_in_Africa) |
| [**assets**](assets/) | Assets used for this project. |
| [**data**](data/) | Where your datasets go. |
| [**data/Train.csv**](data/Train.csv) | Train contains the target. This is the dataset that you will use to train your model. |
| [**data/Test.csv**](data/Test.csv) | Test resembles Train.csv but without the target-related columns. This is the dataset your model will generate predictions for.|
| [**data/VariableDefinitions.csv**](data/VariableDefinitions.csv) | Full list of variables and their explanations. |
| [**data/SampleSubmission.csv**](data/SampleSubmission.csv) | This shows the submission format for this competition, with the 'ID' column mirroring that of Test.csv and the 'bank_account' column containing your predictions. The order of the rows does not matter, but the names of the ID must be correct. Note that the variable ID in the submission file is: uniqueid + " x " + country name. |
| [**docs**](docs/) | Miscellaneous documents |
| [**models**](models/) | Where trained models are saved. |
| [**notebooks**](notebooks/) | Notebooks use for the competition. |
| [**notebooks/01_eda.ipynb**](notebooks/01_eda.ipynb) | Notebooks for Exploratory Data Analysis. |
| [**notebooks/02_preprocessing.ipynb**](notebooks/02_preprocessing.ipynb) | Notebooks for preprocessing Data. |
| [**notebooks/03_baseline_models.ipynb**](notebooks/03_baseline_models.ipynb) | Notebooks creating the baseline model. |
| [**notebooks/04_model_experiments.ipynb**](notebooks/04_model_experiments.ipynb) | Notebooks creating the baseline model. |
| [**notebooks/05_error_analysis.ipynb**](notebooks/05_error_analysis.ipynb) | Notebooks creating the baseline model. |
| [**presentation**](presentation/) | Folder with presentations |
| [**StarterNotebook.ipynb**](StarterNotebook.ipynb) | Starter notebook to help make your submission.|
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies. |
| [**uv.lock**](uv.lock) | Dependency lock file. |


<br>

---

## Steps to Complete the Competition

The Zindi data (`Train.csv`, `Test.csv`) requires a free Zindi account to download from the [competition's Data tab](https://zindi.africa/competitions/financial-inclusion-in-africa/data). Place both files in `data/` before running the notebook.


| # | Step | What it involves |
|---|------|-------------------|
| 1 | Read the rules and data dictionary | Review the competition page and `VariableDefinitions.csv` so you understand what each column means and what's off-limits (no AutoML, no external data sharing, 10 submissions/day cap). |
| 2 | Set up your environment | Confirm your project has the packages you'll actually use installed (e.g. `scikit-learn`, and `xgboost`/`lightgbm` if you plan to use them — these aren't in the current `pyproject.toml`, so they'd need to be added). |
| 3 | Load and explore the data | Read `Train.csv` and `Test.csv`, check shape, dtypes, missing values, and the class balance of `bank_account` (it's notably imbalanced — far more "No" than "Yes"). |
| 4 | Exploratory data analysis (EDA) | Visualize distributions and relationships between features (country, location type, education level, job type, etc.) and the target to build intuition before modeling. |
| 5 | Preprocess the data consistently | Encode categorical features and scale numeric ones — ideally fit any encoders/scalers once (e.g. via a `ColumnTransformer`/`Pipeline`) and reuse them on both train and test to avoid mismatched columns or leakage. |
| 6 | Split out a validation set | Hold out a portion of `Train.csv` (with stratification, given the class imbalance) so you can evaluate models before touching the real test set. |
| 7 | Train a baseline model | Start simple (e.g. logistic regression or a majority-class dummy classifier) to establish a floor to beat. |
| 8 | Train and compare stronger models | Try tree-based models (Random Forest, XGBoost) and compare using metrics that account for class imbalance — not just accuracy, but precision/recall/F1 on the minority class, and ultimately MAE since that's the actual scoring metric. |
| 9 | Tune hyperparameters | Use cross-validation (e.g. `GridSearchCV`) to search for better parameters, watching for genuine improvement rather than noise. |
| 10 | Refit on the full training data | Once you've picked a final model/parameters, retrain on all of `Train.csv` (not just the split) before predicting on the real test set. |
| 11 | Generate predictions on `Test.csv` | Apply the exact same preprocessing pipeline used on the training data, then predict `bank_account` for every row. |
| 12 | Build the submission file | Format it to match `SampleSubmission.csv` exactly — an `ID` column combining `unique_id` and country, plus the predicted `bank_account` value. |
| 13 | Submit and check the leaderboard | Upload the CSV on Zindi (mind the 10-per-day cap), review your MAE score, and note what to try next. |
| 14 | Iterate | Revisit feature engineering, try new models, or adjust preprocessing based on leaderboard feedback, then repeat steps 8–13. |
