# Financial Inclusion in Africa — Final Presentation Plan

> **Status:** FINAL SOURCE OF TRUTH FOR POWERPOINT CREATION  
> **Presentation length:** 10–15 minutes  
> **Recommended deck:** 11 slides  
> **Audience:** technical and non-technical stakeholders  
> **Primary metric:** Macro F1  
> **Final model:** Tuned, class-weighted XGBoost with decision threshold 0.55
>
> Use only the verified values in this document. Do not invent results, feature importance, causal claims, or business outcomes.

---

# 1. Executive Storyline

The presentation should tell one clear story:

**Problem → Data → Key EDA → Evaluation challenge → Baseline → Cross-validated model comparison → Error analysis → Model improvement → Final model → Value, limitations, next steps**

The deck should not feel like a notebook walkthrough. Each slide should answer one question and contain one primary message.

### Target timing

| Slide | Topic | Target time |
|---|---|---:|
| 1 | Title | 0:20 |
| 2 | Problem & Product Value | 1:00 |
| 3 | Dataset Overview & Data Quality | 0:50 |
| 4 | Target Imbalance | 1:00 |
| 5 | Key Feature & Country Insights | 1:30 |
| 6 | Preprocessing Pipeline | 1:00 |
| 7 | Baseline & Evaluation Strategy | 1:15 |
| 8 | Cross-Validated Model Comparison | 1:20 |
| 9 | Error Analysis & Model Improvement | 1:45 |
| 10 | Final Model, Product Use & Limitations | 1:30 |
| 11 | Conclusion & Next Steps | 0:50 |

**Expected total:** approximately 12 minutes, leaving time for questions.

---

# 2. Design Rules

- Professional, clean, visual, minimal text.
- One main takeaway per slide.
- Use charts and diagrams instead of notebook screenshots or raw tables.
- Avoid long classification reports on slides.
- Keep exact technical details in speaker notes when they are not essential visually.
- Use **association**, **linked to**, or **higher/lower ownership rate**; do not claim causation from survey data.
- Keep the target definition explicit:
  - `Yes / 1` = respondent has a bank account.
  - `No / 0` = respondent does not have a bank account.
- Do not describe respondents as “bankable.”
- Do not select or justify a model using accuracy alone.
- Distinguish clearly between:
  - **5-fold cross-validation results used for model selection**, and
  - **holdout validation results used for final evaluation and error inspection**.

---

# 3. Slide-by-Slide Final Plan

## Slide 1 — Title & Team

### Suggested title
**Financial Inclusion in Africa — Predicting Bank Account Ownership**

### On-slide content
- Team members
- AI Engineering / course name
- Date

### Visual
Minimal title slide. Optional subtle Africa / digital-finance visual.

### Speaker message
“We built a machine-learning workflow to predict bank account ownership from demographic and socioeconomic survey information across four African countries.”

### Status
`READY — insert final names/date`

---

## Slide 2 — Problem & Product Value

### Main message
**Can demographic and socioeconomic survey data help predict bank account ownership?**

### On-slide content
**Input:** survey information  
→ **ML model**  
→ **Probability / prediction of bank account ownership**  
→ **Decision-support insights**

Potential value:
- support financial-inclusion analysis;
- identify groups or regions with lower predicted ownership;
- help prioritize further research or outreach analysis.

### Important wording
The model predicts **bank account ownership**, not creditworthiness, eligibility, or whether someone is “bankable.”

### Suggested visual
A simple four-step flow diagram.

### Speaker message
“The model is intended as decision support. It can reveal patterns in predicted ownership, but it should not replace financial or policy decisions.”

### Status
`READY`

---

## Slide 3 — Dataset Overview & Data Quality

### Main message
**The dataset is clean and covers 23,524 respondents across four countries.**

### Verified facts
- Training observations: **23,524**
- Training columns: **13**
- Target: `bank_account`
- Countries: **Kenya, Rwanda, Tanzania, Uganda**
- No missing values detected.
- No fully duplicated rows detected.
- No duplicated `uniqueid + country` combinations detected.

### Feature groups
- Numerical: `year`, `household_size`, `age_of_respondent`
- Categorical: country, location, cellphone access, gender, household relationship, marital status, education, employment

### Visual
Use 4 large summary cards:
- **23,524 respondents**
- **13 columns**
- **4 countries**
- **0 missing values**

Do not use a large dataframe screenshot.

### Speaker message
“Data quality was strong, so most preprocessing focused on representation and reproducibility rather than repairing missing or duplicated records.”

### Status
`VERIFIED`

---

## Slide 4 — Target Imbalance

### Main message
**Only 14.08% of respondents have a bank account, so accuracy alone is misleading.**

### Verified distribution
- `No`: **20,212 — 85.92%**
- `Yes`: **3,312 — 14.08%**

### Visual
Bar chart with percentages:
- No: **85.92%**
- Yes: **14.08%**

Chart title:
**Bank Account Ownership Is Strongly Imbalanced**

### On-slide callout
**Only 14.08% are in the positive class.**

### Evaluation implication
Use **Macro F1** as the primary metric so performance on both classes receives equal importance. Keep Class 1 Recall, Class 1 F1, accuracy, and confusion matrix as supporting metrics.

### Speaker message
“A model that predicts No for everyone already gets about 86% accuracy. That is why accuracy cannot be our main success criterion.”

### Status
`VERIFIED`

---

## Slide 5 — Key Feature & Country Insights

### Main message
**Ownership rates vary strongly with cellphone access, education, employment, and country.**

### Recommended visual layout
Use a clean 2×2 small-multiple layout. Keep labels concise.

#### Cellphone access — Yes ownership rate
- No cellphone access: **1.71%**
- Cellphone access: **18.38%**

#### Education — selected ownership rates
- No formal education: **3.90%**
- Primary: **8.55%**
- Secondary: **23.28%**
- Tertiary: **51.08%**
- Vocational/Specialised: **57.04%**

#### Employment — selected ownership rates
- No Income: **2.07%**
- Informally employed: **7.95%**
- Farming/Fishing: **11.67%**
- Self employed: **13.17%**
- Formally employed Private: **54.12%**
- Formally employed Government: **77.52%**

#### Country — ownership rate
- Kenya: **25.07%**
- Rwanda: **11.48%**
- Tanzania: **9.17%**
- Uganda: **8.61%**

### Supporting insights for speaker notes only
- Urban: **17.87%** vs Rural: **11.65%**
- Male: **18.97%** vs Female: **10.68%**
- Head of Household: **17.71%**

### Interpretation rule
Say: “Higher education/formal employment/cellphone access are **associated with** higher ownership.”  
Do not say these features cause ownership.

### Speaker message
“These patterns suggested that demographic, socioeconomic, technological-access, and geographic features could provide useful predictive signal.”

### Status
`VERIFIED`

---

## Slide 6 — Preprocessing Pipeline

### Main message
**A reusable pipeline keeps preprocessing consistent and prevents leakage.**

### Verified workflow
**Raw data**  
→ **Basic cleaning**  
→ **Clean reusable data**  
→ **Stratified train/validation split**  
→ **Model-specific preprocessing**  
→ **Model training / evaluation**

### Verified preprocessing decisions
- `uniqueid` excluded from predictive features; retained only for traceability/submission.
- `bank_account`: `No/Yes` mapped to `0/1`.
- Clean datasets saved as `Train_clean.csv` and `Test_clean.csv`.
- Shared split logic in `src/data_split.py`.
- Shared transformations in `src/preprocessing.py`.
- Categorical features: one-hot encoding.
- Logistic Regression: numerical standardization + one-hot encoding.
- Tree models: numerical passthrough + one-hot encoding.
- Preprocessing is fitted inside the pipeline on training data, reducing leakage risk.

### Important note
No dedicated feature-engineering experiment was selected for the final model. Do not claim engineered features were used.

### Visual
Horizontal process diagram. Keep code off the slide.

### Speaker message
“The same reusable pipeline is used inside cross-validation, so transformations are learned only from each training fold rather than from the full dataset.”

### Status
`VERIFIED`

---

## Slide 7 — Baseline & Evaluation Strategy

### Main message
**The majority-class baseline looks accurate but completely misses bank-account owners.**

### Baseline
`DummyClassifier(strategy="most_frequent")`

### Verified holdout baseline
- Accuracy: **0.8593 / 85.93%**
- Macro F1: **0.4622**
- Class 1 Recall: **0.0000**
- Class 1 F1: **0.0000**
- Confusion matrix: **[[4043, 0], [662, 0]]**

### Strong callout
**85.93% accuracy — but 0% recall for the Yes class.**

### Final evaluation strategy
**Model selection:**
- 5-fold **Stratified Cross-Validation** on the training portion.
- Primary metric: **Macro F1**.
- Supporting metrics: Class 1 Recall, Class 1 F1, Accuracy.

**Final assessment:**
- Holdout validation set kept separate for final evaluation, threshold assessment, confusion matrix, and error inspection.

### Visual
Left: compact baseline confusion matrix.  
Right: simple evaluation flow:

**Training data → 5-fold stratified CV → model selection → holdout validation → final evaluation**

### Speaker message
“Stratification preserves the class ratio in each fold. Cross-validation reduces dependence on one random split, while the holdout set provides a separate final check.”

### Status
`VERIFIED`

---

## Slide 8 — Cross-Validated Model Comparison

### Main message
**XGBoost achieved the strongest cross-validated Macro F1, with Logistic Regression very close.**

### Use only these 5-fold CV values for the main model-comparison chart

| Model | CV Accuracy | CV Macro F1 | CV Class 1 Recall | CV Class 1 F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | **0.8840** | **0.6920** | **0.3362** | **0.4488** |
| Random Forest | **0.8613** | **0.6769** | **0.3758** | **0.4329** |
| XGBoost | **0.8878** | **0.6964** | **0.3332** | **0.4553** |

### Interpretation
- **XGBoost:** highest CV Macro F1 = **0.6964**.
- **Logistic Regression:** very close at **0.6920**.
- **Random Forest:** highest Class 1 Recall among these three = **0.3758**, but lower Macro F1.
- XGBoost selected as the model to improve.

### Visual
Primary chart: horizontal bars for **CV Macro F1** only:
- Logistic: 0.6920
- Random Forest: 0.6769
- XGBoost: 0.6964

Optional small callout:
**Random Forest had the highest Class 1 Recall, but XGBoost had the best balanced score.**

Do not mix the Dummy holdout score into the same CV bar chart. The Dummy result belongs on Slide 7 as a baseline reference.

### Speaker message
“Differences were small, so we used cross-validation rather than a single split to select the strongest candidate. XGBoost remained the leader under our primary metric.”

### Status
`VERIFIED — FINAL MODEL-SELECTION RESULTS`

---

## Slide 9 — Error Analysis & Model Improvement

### Main message
**Error analysis exposed systematic miss patterns, and class weighting produced the largest performance gain.**

### Part A — Error patterns in the original XGBoost
Error analysis was performed on the original XGBoost holdout predictions.

#### False-negative rate examples
Among actual positive cases, the model missed:
- Rwanda: **78.46%**
- Kenya: **57.64%**
- No formal education: **100.00%**
- Primary education: **98.06%**
- Informally employed: **92.94%**
- Farming/Fishing: **89.68%**

#### False-positive pattern examples
Among actual negative cases, false positives were more common in groups with stronger socioeconomic indicators:
- Tertiary education: **19.30%**
- Vocational/Specialised training: **37.50%**
- Formally employed Private: **27.17%**
- Formally employed Government: **75.00%**

**Caution:** very high percentages may come from small subgroups. Present these as error patterns, not causal findings.

### Part B — Improvement path

#### Original XGBoost — 5-fold CV
- Macro F1: **0.6964**
- Class 1 Recall: **0.3332**
- Class 1 F1: **0.4553**

#### Class weighting search
Tested `scale_pos_weight`: **1, 2, 3, 4, 6.1**.

Best tested weight: **3**
- CV Macro F1: **0.7328**
- Class 1 Recall: **0.5766**
- Class 1 F1: **0.5451**

This was the largest improvement step.

#### Hyperparameter tuning
Used `RandomizedSearchCV` with 5-fold stratified CV and `f1_macro` scoring.

Best CV Macro F1: **0.7354**

Best parameters:
- `n_estimators = 150`
- `max_depth = 4`
- `learning_rate = 0.05`
- `subsample = 0.8`
- `colsample_bytree = 1.0`
- `scale_pos_weight = 3`

Tuned CV supporting metrics:
- Class 1 Recall: **0.5770**
- Class 1 F1: **0.5491**

#### Threshold adjustment
The tuned model was evaluated across thresholds from **0.30 to 0.70** on the holdout validation set.

Best tested threshold: **0.55**.

### Recommended visual
Use a two-panel slide:

**Left — Error pattern callouts**  
Show 3–4 concise FN examples only, e.g. Rwanda, Primary education, Informal employment.

**Right — CV improvement ladder**  
- Original XGBoost: **0.6964**
- + Class weight = 3: **0.7328**
- + Hyperparameter tuning: **0.7354**

Add a small note below:
**Final decision threshold on holdout: 0.55**

Do not put every threshold value or every subgroup on the slide.

### Speaker message
“The original model missed many positives in lower-education and informal-employment groups. Moderate class weighting gave the largest improvement, increasing both Macro F1 and minority recall. Hyperparameter tuning added a smaller gain, and threshold 0.55 gave the best final holdout balance.”

### Status
`VERIFIED — FINAL`

---

## Slide 10 — Final Model, Product Use & Limitations

### Main message
**The final model improves balanced performance and identifies substantially more positive cases than the original XGBoost.**

### Final configuration
**Tuned + Class-Weighted XGBoost**
- `scale_pos_weight = 3`
- `n_estimators = 150`
- `max_depth = 4`
- `learning_rate = 0.05`
- `subsample = 0.8`
- `colsample_bytree = 1.0`
- Decision threshold = **0.55**

### Final holdout validation results
- Accuracy: **0.8763**
- Macro F1: **0.7468**
- Class 1 Recall: **0.5725**
- Class 1 F1: **0.5657**

### Final confusion matrix
**[[3744, 299], [283, 379]]**

Interpretation:
- True Negatives: **3,744**
- False Positives: **299**
- False Negatives: **283**
- True Positives: **379**

### Recommended slide layout
**Left 60%:** final confusion matrix + four metric cards.  
**Right 40%:** two compact sections.

#### What the model can support
- aggregate financial-inclusion analysis;
- identification of groups with lower predicted ownership;
- prioritization of further investigation or outreach analysis.

#### Limitations
- Strong class imbalance remains.
- Survey data is observational; no causal inference.
- Data covers only Kenya, Rwanda, Tanzania, and Uganda.
- Survey years are limited to 2016–2018.
- Performance varies across groups.
- No dedicated feature-engineering study was completed.
- Model outputs should support, not replace, policy or financial decisions.

### Speaker message
“The final model trades a small amount of overall accuracy for much stronger balanced performance and substantially better positive-class detection. It is useful as analytical decision support, but its geography, time period, and group-level error variation limit how broadly it should be applied.”

### Status
`VERIFIED — FINAL MODEL SELECTED`

---

## Slide 11 — Conclusion & Next Steps

### Main message
**A reproducible, cross-validated workflow improved balanced performance from a weak majority baseline to a substantially stronger final model.**

### Core takeaways
1. Bank account ownership is highly imbalanced: only **14.08% Yes**.
2. Cellphone access, education, employment, and country show strong associations with ownership.
3. The majority baseline achieved **85.93% accuracy but 0% Class 1 Recall**.
4. XGBoost was selected using **5-fold stratified cross-validation**.
5. Class weighting produced the largest model improvement.
6. The final tuned weighted XGBoost with threshold **0.55** achieved **Macro F1 = 0.7468** on holdout validation.

### Next steps
Keep future work realistic and concise:
- test explicit feature-engineering ideas;
- expand hyperparameter search if more compute/time is available;
- validate on newer or external data;
- investigate subgroup stability with larger samples;
- calibrate probabilities if probability quality matters for deployment;
- package the final workflow for reproducible inference/submission.

### Suggested closing sentence
**The project demonstrates that careful evaluation, error analysis, and imbalance-aware modeling matter more than accuracy alone when predicting bank account ownership.**

### Status
`READY`

---

# 4. Final Chart Inventory

Only create presentation-quality visuals. Do not paste notebook screenshots.

## Chart 1 — Target Distribution
**Slide:** 4  
**Type:** bar chart  
**Values:** No 85.92%, Yes 14.08%

## Chart 2 — Cellphone Access vs Ownership
**Slide:** 5  
**Type:** compact bar chart  
**Values:** No cellphone 1.71%, Cellphone 18.38%

## Chart 3 — Education vs Ownership
**Slide:** 5  
**Type:** horizontal bars  
**Values:** 3.90%, 8.55%, 23.28%, 51.08%, 57.04% for selected education levels

## Chart 4 — Employment vs Ownership
**Slide:** 5  
**Type:** compact horizontal bars / selected contrasts  
**Highlight:** Informal 7.95%, Formal Private 54.12%, Formal Government 77.52%

## Chart 5 — Country Ownership Rate
**Slide:** 5  
**Type:** bars sorted descending  
**Values:** Kenya 25.07%, Rwanda 11.48%, Tanzania 9.17%, Uganda 8.61%

## Chart 6 — Baseline Confusion Matrix
**Slide:** 7  
**Values:** [[4043, 0], [662, 0]]  
**Callout:** 85.93% accuracy, 0% Yes recall

## Chart 7 — CV Macro F1 by Model
**Slide:** 8  
**Type:** horizontal bar chart  
**Values:** Logistic 0.6920, Random Forest 0.6769, XGBoost 0.6964

## Chart 8 — Improvement Ladder
**Slide:** 9  
**Type:** simple bars or step/lollipop chart  
**Use only comparable 5-fold CV values:**
- Original XGBoost: 0.6964
- Weighted XGBoost: 0.7328
- Tuned Weighted XGBoost: 0.7354

Optional second annotation on same slide:
- Class 1 Recall: 0.3332 → 0.5766 → 0.5770

## Chart 9 — Final Confusion Matrix
**Slide:** 10  
**Values:** [[3744, 299], [283, 379]]

---

# 5. Numbers That Must Not Be Mixed

To keep the presentation technically correct:

### Cross-validation model-selection numbers
Use these when comparing supervised models or improvement variants:
- Logistic CV Macro F1: **0.6920**
- Random Forest CV Macro F1: **0.6769**
- Original XGBoost CV Macro F1: **0.6964**
- Weighted XGBoost (`scale_pos_weight=3`) CV Macro F1: **0.7328**
- Tuned Weighted XGBoost CV Macro F1: **0.7354**

### Holdout final-evaluation numbers
Use these only when describing the final thresholded model:
- Final Accuracy: **0.8763**
- Final Macro F1: **0.7468**
- Final Class 1 Recall: **0.5725**
- Final Class 1 F1: **0.5657**
- Final confusion matrix: **[[3744, 299], [283, 379]]**

Do not create a bar chart that directly compares the final holdout Macro F1 0.7468 against CV scores without clearly labeling the different evaluation methods.

---

# 6. Data Integrity / Notebook Notes for the Presentation Creator

- The final model-selection story should use the verified **5-fold CV table** rather than individual stale notebook outputs.
- One stored XGBoost output in `04_model_experiments.ipynb` displays a Macro F1 value inconsistent with its classification report and the later verified comparison. Do **not** use that stale displayed value in the PowerPoint.
- Use **XGBoost CV Macro F1 = 0.6964** for model selection and **final holdout Macro F1 = 0.7468** for the final thresholded model.
- Error-analysis findings refer to the **original XGBoost before the improvement stage**.
- Extremely high subgroup error rates can reflect small subgroup sizes; do not overstate them.

---

# 7. PowerPoint Creation Instructions

A person or LLM generating the final `.pptx` should:

1. Build approximately **11 slides** using the slide plan above.
2. Target **10–15 minutes**, ideally about 12 minutes.
3. Use a consistent professional visual system: one font family, strong hierarchy, generous whitespace, limited palette.
4. Recreate all charts as clean vector-style PowerPoint charts; never use notebook screenshots.
5. Put no more than 3–5 short bullets on a slide unless the content is a compact limitations panel.
6. Use the slide titles as insight statements where possible.
7. Keep detailed technical explanations in speaker notes.
8. Show Macro F1 prominently and clearly distinguish CV from holdout evaluation.
9. Use one confusion matrix for the baseline and one for the final model; do not show confusion matrices for every experiment.
10. Keep EDA to the three planned slides; do not expand the deck with every exploratory plot.
11. Use association language, not causal language.
12. Do not invent feature importance, SHAP results, deployment performance, external validation, or business ROI.
13. Do not claim feature engineering was completed; it remains a future improvement opportunity.
14. End with limitations and next steps rather than claiming the model is production-ready.

---

# 8. Final Project Status Checklist

## Data / EDA
- [x] Dataset structure and quality checks
- [x] Target distribution
- [x] Numerical and categorical exploration
- [x] Feature-target associations
- [x] Country analysis

## Modeling
- [x] Reusable preprocessing pipeline
- [x] Dummy baseline
- [x] Logistic Regression
- [x] Random Forest
- [x] XGBoost
- [x] 5-fold stratified cross-validation
- [x] Error analysis
- [x] Class imbalance experiments
- [x] Threshold experiments
- [x] Hyperparameter tuning
- [x] Final model selection
- [ ] Dedicated feature-engineering experiments

## Communication
- [x] Final presentation storyline
- [x] Final model visuals specified
- [ ] Generate final PowerPoint
- [ ] Final README update
- [ ] Final repository cleanup / reproducibility check

---

# 9. One-Sentence Final Technical Summary

**Using reusable preprocessing, 5-fold stratified cross-validation, error analysis, class weighting, randomized hyperparameter tuning, and threshold adjustment, the project selected a tuned XGBoost model that achieved a holdout Macro F1 of 0.7468 with Class 1 Recall of 0.5725.**
