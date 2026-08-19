# Financial Inclusion in Africa — Project Master Plan

## 1. Project Goal

Build a complete, professional Machine Learning project that:

* solves the Financial Inclusion in Africa classification problem
* follows a clear Data Science workflow
* is documented properly
* has a clean and professional GitHub repository
* includes reproducible analysis and modeling
* includes a final 10-minute presentation
* is understandable to both technical and non-technical audiences

The goal is not only to finish the university assignment, but also to learn a reusable workflow for future ML projects.

---

# 2. Overall Machine Learning Workflow

We will follow this order:

## Phase 1 — Project Setup

1. Understand the project requirements
2. Organize the repository
3. Create documentation files
4. Define the ML problem
5. Define the target and project objective

## Phase 2 — Data Understanding & EDA

6. Load and inspect the data
7. Understand every feature
8. Check data quality
9. Check missing values
10. Check duplicates
11. Analyze target distribution
12. Analyze important feature distributions
13. Analyze relationships between features and target
14. Identify class imbalance
15. Summarize key EDA findings

## Phase 3 — Data Preparation

16. Separate features and target
17. Remove identifiers if necessary
18. Encode categorical features
19. Scale numerical features if needed
20. Build a clean preprocessing pipeline
21. Create train / validation split
22. Avoid data leakage

## Phase 4 — Baseline

23. Create a simple majority-class baseline
24. Evaluate the baseline
25. Record the baseline score
26. Explain why the baseline is useful

## Phase 5 — Model Experiments

27. Train a simple model such as Logistic Regression
28. Train Random Forest
29. Train XGBoost
30. Train LightGBM if useful
31. Evaluate every model using the same validation strategy
32. Compare models fairly

## Phase 6 — Evaluation

33. Choose a primary evaluation metric
34. Track supporting metrics
35. Analyze:

* Accuracy
* Precision
* Recall
* F1-score
* Macro F1
* Confusion Matrix

36. Understand the performance of the minority class

## Phase 7 — Error Analysis

37. Study false positives
38. Study false negatives
39. Look for systematic patterns in errors
40. Check whether performance differs by:

* country
* education
* age
* job type
* other relevant features

41. Decide whether errors can be improved systematically

## Phase 8 — Model Improvement

42. Improve preprocessing if needed
43. Add useful feature engineering
44. Try class imbalance techniques if appropriate
45. Tune hyperparameters
46. Use cross-validation
47. Re-evaluate models
48. Compare improvements against the baseline

## Phase 9 — Final Model

49. Select the final model
50. Justify why it was selected
51. Record final metrics
52. Record limitations
53. Save the final model if useful

## Phase 10 — Communication

54. Finalize README
55. Finalize presentation plan
56. Create presentation
57. Prepare speaker notes
58. Practice 10-minute presentation
59. Make sure the presentation tells a clear story:
    Problem → Data → EDA → Baseline → Models → Evaluation → Error Analysis → Improvement → Final Model → Conclusion

---

# 3. Recommended Repository Structure

```text
financial-inclusion-ml/
│
├── README.md
├── PROJECT_WORKFLOW.md
├── presentation_plan.md
├── .gitignore
├── pyproject.toml / requirements.txt
│
├── data/
│   ├── Train.csv
│   ├── Test.csv
│   ├── VariableDefinitions.csv
│   └── SampleSubmission.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_baseline_models.ipynb
│   ├── 04_model_experiments.ipynb
│   ├── 05_error_analysis.ipynb
│   └── 06_final_model.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
│
├── reports/
│   ├── figures/
│   └── results/
│
├── models/
│   └── final_model.*
│
└── presentation/
    ├── milestone2_draft.pptx
    └── final_presentation.pptx
```

Not all folders need to be fully used. If time is limited, notebooks are sufficient. The main goal is clarity and organization.

---

# 4. Purpose of Each Main File

## README.md

The public overview of the project.

It should eventually contain:

* project overview
* business / product value
* ML problem
* dataset description
* project structure
* setup instructions
* EDA summary
* preprocessing summary
* models tested
* evaluation metric
* final results
* limitations
* next steps

## PROJECT_WORKFLOW.md

This file.

It is the master roadmap and should help us remember:

* what we are doing
* what has been completed
* what comes next

## presentation_plan.md

The source of truth for the presentation.

For every slide it should contain:

```text
Slide number:
Title:
Purpose:
Main message:
Verified information:
Visual/chart:
Speaker notes:
Status:
```

Example:

```text
Slide 4
Title: Target Distribution

Purpose:
Show that the dataset is imbalanced.

Main message:
Most respondents do not have a bank account.

Verified information:
No = ...
Yes = ...

Visual:
Bar chart

Speaker notes:
...

Status:
Complete
```

The PowerPoint should eventually be created from this file.

---

# 5. Presentation Structure

The final presentation is approximately 10 minutes.

Target: around 10–12 slides.

Recommended structure:

1. Title / Team
2. Problem + Product Value
3. Dataset Overview
4. EDA — Target & Data Quality
5. EDA — Important Feature Insights
6. Preprocessing / Feature Engineering
7. Baseline
8. Model Experiments
9. Evaluation & Model Comparison
10. Error Analysis / Model Improvement
11. Final Model + Limitations
12. Conclusion / Next Steps

Important:
Milestones are project-management checkpoints. They do not need to appear as separate sections in the final presentation.

---

# 6. EDA Structure

EDA should answer questions, not just create random charts.

For each analysis:

```text
Question
↓
Code / Visualization
↓
Observation
↓
Interpretation
↓
Impact on Modeling
```

Main EDA questions:

1. What does one row represent?
2. What columns exist?
3. What are the data types?
4. Are there missing values?
5. Are there duplicates?
6. Is the target balanced?
7. How are numerical variables distributed?
8. How are categorical variables distributed?
9. Which features appear related to the target?
10. Are there country-level differences?
11. Are there suspicious or unrealistic values?
12. What findings may affect preprocessing or model evaluation?

At the end of EDA, summarize only the strongest findings.

The final presentation should probably use only 2 EDA slides.

---

# 7. Model Progression

Recommended learning structure:

```text
Majority / Dummy Baseline
        ↓
Logistic Regression
        ↓
Random Forest
        ↓
XGBoost
        ↓
LightGBM (optional)
```

Roles:

* DummyClassifier:
  benchmark; no real learning

* Logistic Regression:
  simple interpretable ML model

* Random Forest:
  nonlinear tree-based model

* XGBoost:
  advanced boosting model

* LightGBM:
  alternative advanced boosting model

Not all models are baselines.

---

# 8. Evaluation Strategy

Because the target is imbalanced, do not rely only on accuracy.

Primary metric currently under consideration:

**Macro F1-score**

Supporting metrics:

* Accuracy
* Error Rate
* Precision
* Recall
* Class 1 Recall
* Class 1 F1
* Confusion Matrix

Important principle:

Choose the evaluation strategy before selecting the final model.

Do not choose a metric just because it makes one model look better.

---

# 9. Git / GitHub Workflow

Work should be committed incrementally.

Avoid one giant final commit.

Example commit progression:

```text
Initialize project structure

Add initial dataset exploration

Add data quality checks

Analyze target class imbalance

Add feature-level EDA

Add preprocessing pipeline

Add majority-class baseline

Add logistic regression experiment

Add random forest experiment

Add XGBoost experiment

Add model comparison metrics

Add error analysis

Add hyperparameter tuning

Update README with project results

Add presentation plan

Add final presentation
```

Good commit messages:

```bash
git commit -m "Add target distribution analysis"
git commit -m "Add preprocessing pipeline"
git commit -m "Add majority-class baseline"
git commit -m "Compare initial classification models"
```

Bad commit messages:

```text
update
stuff
final
new version
```

---

# 10. Definition of Done

The project is complete when:

* repository is clean
* README is understandable
* notebooks are organized
* debugging code is removed
* EDA has clear findings
* preprocessing is reproducible
* baseline is documented
* models are compared fairly
* evaluation metric is justified
* error analysis is included
* model improvement is documented
* final model is justified
* limitations are documented
* presentation is complete
* presentation fits into approximately 10 minutes
* presentation is committed to GitHub

---

# 11. How We Will Work From Now On

We will work step by step.

We will not jump randomly between slides, models, and tuning.

Order:

1. Clean project structure
2. EDA
3. Document EDA
4. Add EDA to README
5. Add EDA slides to presentation_plan.md
6. Preprocessing
7. Baseline
8. Model experiments
9. Evaluation
10. Error analysis
11. Improvements
12. Final model
13. Final documentation
14. Final presentation

At every stage we will:

* understand the concept
* write the code
* interpret the result
* document the result
* commit the work
* only then move to the next stage

---

# Current Next Step

**Start with EDA.**

First task:

Create / clean:

`notebooks/01_eda.ipynb`

and answer:

1. What is the structure of the dataset?
2. Is the data clean?
3. What does the target distribution look like?
4. What are the most important initial observations?

Do not move to model tuning until the EDA is clear and documented.
