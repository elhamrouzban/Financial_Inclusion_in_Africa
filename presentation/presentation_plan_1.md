# Financial Inclusion in Africa — Presentation Plan

> **Purpose of this file**
>
> This is the source of truth for the final project presentation.  
> Update this document as the project progresses.  
> Any LLM or person creating the PowerPoint should use only the verified information written here and should not invent results.
>
> **Presentation goal:** Explain the problem, data, EDA, modeling decisions, model comparison, error analysis, final model, limitations, and product value clearly to both technical and non-technical stakeholders.
>
> **Target duration:** 10–15 minutes  
> **Target slide count:** approximately 10–11 slides  
> **Style:** professional, visual, concise, minimal text, one main message per slide.


# 1. Presentation Design Principles

## General rules

- Do not copy notebook outputs directly into slides unless they are already presentation-quality.
- Prefer charts over raw tables.
- Every chart must communicate one clear message.
- Use short titles that state the insight, not just the variable name.
- Avoid showing every EDA chart. Show only the plots that support the project story.
- Do not claim causation from observational survey data. Use wording such as **associated with**, **linked to**, or **shows a higher/lower ownership rate**.
- Clearly distinguish:
  - **data distribution**
  - **association with the target**
  - **model performance**
- Keep detailed exploratory outputs in the notebook; keep only the strongest insights in the presentation.
- Future modeling results must be inserted only after they are verified.

---

# 2. Recommended Final Storyline

1. Title & Team
2. Problem & Product Value
3. EDA — Dataset Overview & Data Quality
4. EDA — Target Imbalance
5. EDA — Key Feature & Country Insights
6. Preprocessing & Feature Engineering
7. Baseline & Evaluation Strategy
8. Model Experiments & Comparison
9. Error Analysis & Model Improvement
10. Final Model, Limitations & Product Use
11. Conclusion & Next Steps

The exact number of slides may change slightly, but the final presentation should preserve this narrative:

**Problem → Data → EDA → Modeling Strategy → Baseline → Improvement → Evaluation → Error Analysis → Final Model → Value & Limitations**

---

# 3. Slide-by-Slide Plan

## Slide 1 — Title & Team

### Purpose
Introduce the project and team.

### Suggested title
**Financial Inclusion in Africa — Predicting Bank Account Ownership**

### Content
- Team members
- AI Engineering
- Course / project name if required
- Presentation date

### Visual
Keep minimal. Optional subtle Africa/financial-inclusion visual.

### Status
`TODO — update final date and team/course details`

---

## Slide 2 — Problem & Product Value

### Purpose
Explain the project to a non-technical audience.

### Main message
The project predicts whether a surveyed individual is likely to have a bank account using demographic and socioeconomic information.

### Product value
A model like this could support financial-inclusion analysis by helping identify demographic groups or regions with lower predicted likelihood of bank account ownership.

### Important wording
Do **not** describe the model as determining whether someone is “bankable.”  
The target is only whether the respondent has a bank account.

### Suggested visual
A simple visual flow:

**Survey information → ML model → Probability / prediction of bank account ownership → Decision-support insights**

### Status
`DRAFT`

---

## Slide 3 — Dataset Overview & Data Quality

### Purpose
Give the audience enough context to understand the analysis.

### Verified information
- Training observations: **23,524**
- Total columns in training data: **13**
- Target: `bank_account`
- Countries:
  - Kenya
  - Rwanda
  - Tanzania
  - Uganda
- Numerical variables include:
  - `year`
  - `household_size`
  - `age_of_respondent`
- Categorical variables include demographic, geographic, education, employment, and household information.

### Data quality
- No missing values detected.
- No fully duplicated rows detected.
- No duplicated `uniqueid + country` combinations detected.

### Suggested visual
Do **not** use a large table.

Preferred:
- 3–4 large summary cards:
  - **23,524 rows**
  - **13 columns**
  - **4 countries**
  - **0 missing values**
- Small feature-category icons or labels underneath.

### Status
`VERIFIED`

---

# 4. EDA Slides

The EDA section is intentionally limited to **3 slides**:
1. Dataset Overview & Data Quality
2. Target Imbalance
3. Key Feature & Country Insights


## Slide 4 — Target Imbalance

### Purpose
Show the most important challenge discovered during EDA.

### Main message
The target is strongly imbalanced, so accuracy alone can be misleading.

### Verified target distribution
- `bank_account = No`: **20,212 (85.92%)**
- `bank_account = Yes`: **3,312 (14.08%)**

### Primary chart
**Bar chart — Target Distribution**

X-axis:
- No
- Yes

Y-axis:
- Number of respondents or percentage

Preferred presentation version:
- Use percentages directly:
  - No: **85.92%**
  - Yes: **14.08%**

### Chart title
**Bank Account Ownership Is Strongly Imbalanced**

### Annotation
Add a small callout:
**Only 14.08% of respondents have a bank account.**

### Supporting message
Because the target is imbalanced:
- accuracy alone is insufficient;
- model evaluation should also consider class-sensitive metrics;
- Macro F1 is currently the preferred primary evaluation metric;
- minority-class recall and the confusion matrix should remain visible supporting metrics.

### Do not show
- raw `value_counts()` output
- large text paragraphs
- redundant countplot and percentage chart together

### Status
`VERIFIED`

---

## Slide 5 — Key Feature & Country Insights

### Purpose
Summarize the strongest EDA relationships in one visual slide.

### Main message
Bank account ownership differs substantially across key demographic, socioeconomic, technological-access, and country groups.

### Recommended chart strategy
Do **not** put seven separate plots on the slide.

Use one clean **horizontal bar chart** or **small multiples** showing only the strongest contrasts.

### Recommended features to visualize

#### A. Cellphone access

Ownership rate:
- No cellphone access → **1.71% Yes**
- Cellphone access → **18.38% Yes**

Main insight:
Respondents with cellphone access have a substantially higher bank account ownership rate.

#### B. Education level

Ownership rate:
- No formal education → **3.90%**
- Primary education → **8.55%**
- Secondary education → **23.28%**
- Tertiary education → **51.08%**
- Vocational/Specialised training → **57.04%**
- Other/Don't know/RTA → **31.43%**  
  Interpret cautiously because this group is small.

Main insight:
Higher education levels are associated with much higher ownership rates.

#### C. Job type

Ownership rate:
- No Income → **2.07%**
- Informally employed → **7.95%**
- Farming and Fishing → **11.67%**
- Self employed → **13.17%**
- Other Income → **18.15%**
- Government Dependent → **20.24%**
- Formally employed Private → **54.12%**
- Formally employed Government → **77.52%**
- Remittance Dependent → **9.50%**
- Don't Know/Refuse to answer → **11.11%**

Main insight:
Formal employment categories show dramatically higher bank account ownership rates.

### Additional verified associations
These can be mentioned briefly in speaker notes or a small side panel rather than all plotted:

- Urban: **17.87% Yes**
- Rural: **11.65% Yes**

- Male: **18.97% Yes**
- Female: **10.68% Yes**

- Head of Household: **17.71% Yes**

### Recommended visual layout

**Preferred**
Use a clean 2×2 small-multiple layout with four compact visuals:
1. Cellphone access
2. Education level
3. Job type
4. Country ownership rate

Each visual should show:
**Category → Bank Account Yes Rate (%)**

If the slide becomes crowded, keep cellphone access, education, and country as the three primary visuals and mention job type in a short callout.

### Important interpretation note
Use:
> “associated with higher/lower ownership”

Do not use:
> “causes bank account ownership”

### Country-level insight

Bank account ownership also varies substantially across the four countries.

### Verified ownership rates
- Kenya → **25.07%**
- Rwanda → **11.48%**
- Tanzania → **9.17%**
- Uganda → **8.61%**

### Primary chart
**Bar chart — Bank Account Ownership Rate by Country**

X-axis:
- Kenya
- Rwanda
- Tanzania
- Uganda

Y-axis:
**Bank Account = Yes (%)**

Sort descending.

### Chart title
**Bank Account Ownership Differs Strongly by Country**

### Key annotation
Kenya has more than twice the ownership rate of Rwanda and nearly three times the rate of Uganda.

### Optional secondary information
The distribution of the training dataset is:
- Rwanda: 8,735 respondents
- Tanzania: 6,620
- Kenya: 6,068
- Uganda: 2,101

This should **not** replace the ownership-rate chart because raw respondent counts answer a different question.

### Interpretation
Country is strongly associated with the target and should be retained as a categorical predictor.

### Status
`VERIFIED`

---

# 5. EDA Findings for Speaker Notes / Backup

These findings should mostly remain in speaker notes or the notebook rather than taking additional slides.

## Numerical feature findings

### `year`
- Values range from 2016 to 2018.
- No obvious unusual values detected.

### `household_size`
- Median: **3**
- Mean: approximately **3.80**
- Maximum: **21**
- Right-skewed distribution.
- Large households appear as statistical outliers but are not automatically data errors.

### `age_of_respondent`
- Median: **35**
- Mean: approximately **38.81**
- Range: **16–100**
- Right-skewed.
- Older respondents appear as statistical outliers but remain plausible.

### Modeling implication
Do not remove numerical outliers automatically. Retain them initially and evaluate scaling / feature engineering later.

---

# 6. Preprocessing & Feature Engineering Slide

## Slide 6 — Preprocessing Pipeline

### Purpose
Explain how the project prepares data consistently before model training.

### Main message
The project separates basic data cleaning from model-specific transformations so the same workflow can be reused across baseline and advanced models.

### Verified workflow

**Raw Train/Test data**  
→ **Basic cleaning in `02_preprocessing.ipynb`**  
→ **Clean reusable datasets**  
→ **Shared train/validation split**  
→ **Reusable preprocessing pipeline for models that need transformations**  
→ **Model training**

### Verified preprocessing steps
- `uniqueid` is excluded from predictive features and kept only for traceability/submission purposes.
- The target `bank_account` is converted from `Yes/No` to `1/0`.
- Cleaned datasets are saved as:
  - `Train_clean.csv`
  - `Test_clean.csv`
- A reusable split function is defined in `src/data_split.py`.
- A reusable preprocessing function is defined in `src/preprocessing.py`.
- Categorical features are handled with one-hot encoding.
- Numerical features can be standardized with `StandardScaler`.
- The preprocessing transformer is fitted only after the train/validation split to reduce data leakage risk.

### Important note
The DummyClassifier baseline does not require encoding or scaling because it does not learn from feature values. The shared preprocessing pipeline is intended for models such as Logistic Regression, Random Forest, and XGBoost where appropriate.

### Recommended visual
Use a simple horizontal pipeline diagram:

**Raw data → Clean data → Train/Validation split → Encoding & scaling → Model**

Keep code out of the main slide.

### Status
`VERIFIED — reusable preprocessing workflow created`

---

# 7. Evaluation Strategy

## Slide 7 — Baseline & Evaluation Strategy

### Purpose
Establish the minimum reference point that later models must outperform and explain why accuracy alone is not enough.

### Evaluation challenge
Only **14.08%** of respondents are in the `Yes` class, so a model can achieve high accuracy while completely missing the minority class.

### Preferred primary metric
**Macro F1**

### Supporting metrics
- Accuracy
- Error Rate
- Minority-class (`Yes`) Recall
- Minority-class (`Yes`) F1
- Confusion Matrix

### Baseline model
**DummyClassifier — `most_frequent`**

The model always predicts the majority class (`No`) and therefore provides a deliberately simple reference point.

### Verified baseline result
- Accuracy: **85.93%**
- Error Rate: **14.07%**
- Macro F1: **0.46**
- `Yes` Recall: **0.00**
- `Yes` F1: **0.00**

### Verified confusion matrix
- True `No` predicted as `No`: **4,043**
- True `No` predicted as `Yes`: **0**
- True `Yes` predicted as `No`: **662**
- True `Yes` predicted as `Yes`: **0**

### Main message
**The baseline reaches 85.93% accuracy but identifies 0% of bank-account owners.**

This demonstrates why accuracy alone is misleading for this imbalanced classification problem.

### Recommended visual
Use:
- one compact confusion matrix;
- one strong callout:

**85.93% accuracy — but 0% recall for the Yes class**

Avoid a large metric table.

### Status
`VERIFIED`

---

# 8. Model Experiments

## Slide 8 — Model Comparison

### Purpose
Compare progressively stronger models against the baseline.

### Current verified results

#### DummyClassifier
- Accuracy: **85.93%**
- Macro F1: **0.46**
- Yes Recall: **0.00**
- Yes F1: **0.00**

#### Logistic Regression
- Accuracy: **88.78%**
- Error Rate: **11.22%**
- Macro F1: **0.70**
- Yes Recall: **0.35**
- Yes F1: **0.47**

#### Random Forest
- Accuracy: **80.83%**
- Error Rate: **19.17%**
- Macro F1: **0.70**
- Yes Recall: **0.75**
- Yes F1: **0.52**

#### XGBoost
- Accuracy: **88.82%**
- Error Rate: **11.18%**
- Macro F1: **0.72**
- Yes Recall: **0.40**
- Yes F1: **0.50**

### Current interpretation
- XGBoost currently has the strongest **Macro F1**.
- Random Forest identifies a much larger share of the minority class but creates many more false positives.
- Logistic Regression gives a strong simple benchmark.
- Accuracy alone would hide these trade-offs.

### Recommended chart
**Grouped or horizontal bar chart of Macro F1 by model**

Values:
- Dummy: 0.46
- Logistic Regression: 0.70
- Random Forest: 0.70
- XGBoost: 0.72

Optional second metric:
Show `Yes Recall` as a separate small chart or annotation:
- Dummy: 0.00
- Logistic: 0.35
- Random Forest: 0.75
- XGBoost: 0.40

Do not overload one chart with every metric.

### Status
`VERIFIED — may be updated after further experiments`

---

# 9. Error Analysis & Improvement

## Slide 9 — Error Analysis & Model Improvement

### Purpose
Show that model development was iterative rather than only “train and report score.”

### Questions to answer
- Which observations are being misclassified?
- Are false positives concentrated in particular demographic groups?
- Are false negatives concentrated by country, education, age, or job type?
- Is the model systematically missing the minority class?
- Can threshold adjustment improve the desired precision/recall trade-off?
- Do class weights improve minority detection?
- Does feature engineering improve Macro F1?
- Does hyperparameter tuning improve performance consistently?

### Recommended visual
Choose one after actual analysis:
- confusion matrix
- error breakdown by country
- error breakdown by education/job type
- false-negative profile
- model comparison before/after improvement

### Rule
Do not invent error-analysis findings.  
Only add specific findings after they have been computed in the project.

### Status
`TODO`

---

# 10. Final Model & Limitations

## Slide 10 — Final Model, Limitations & Product Use

### Purpose
State the final technical decision and explain what it means in practice.

### Final model
`TODO — choose only after final evaluation`

Current leader under Macro F1:
**XGBoost — Macro F1 ≈ 0.72**

This is not yet necessarily the final model.

### Product use
Potential use:
- identify groups with lower predicted likelihood of bank account ownership;
- support financial-inclusion research;
- help prioritize outreach or further investigation;
- provide aggregate decision-support insights.

### Limitations to discuss
- Strong class imbalance.
- Observational survey data does not establish causality.
- Dataset covers four African countries and may not generalize to other populations.
- Survey years are limited to 2016–2018.
- Prediction quality may vary across demographic groups or countries.
- Model outputs should support, not replace, policy or financial decisions.

### Recommended visual
A simple two-column layout:

**What the model can do**
vs.
**What the model cannot claim**

### Status
`PARTIAL / FINAL MODEL TODO`

---

# 11. Conclusion

## Slide 11 — Conclusion & Next Steps

### Core takeaways
1. Bank account ownership is highly imbalanced in the dataset.
2. Cellphone access, education, employment type, and country show strong associations with ownership.
3. A naive majority baseline achieves high accuracy but completely misses the minority class.
4. ML models improve balanced performance substantially.
5. Macro F1 provides a more informative main comparison than accuracy alone.
6. Further error analysis and model improvement are required before final model selection.

### Next steps
Update as work progresses:
- finish preprocessing pipeline;
- test feature engineering;
- evaluate class imbalance strategies;
- perform hyperparameter tuning;
- conduct systematic error analysis;
- choose the final model;
- document limitations;
- prepare final reproducible notebook / scripts;
- finalize PowerPoint and README.

### Suggested ending sentence
**The goal is not only to maximize a score, but to build a model whose performance and limitations are understandable and useful for financial-inclusion analysis.**

### Status
`DRAFT — update at project end`

---

# 12. Chart Inventory for the Final PowerPoint

This section tells the presentation creator exactly which figures should be generated.

## Must-have charts

### Chart 1 — Target Class Distribution
**Type:** Bar chart  
**Data:**
- No: 85.92%
- Yes: 14.08%

**Purpose:** Show class imbalance.

**Use on:** EDA / Target slide.

---

### Chart 2 — Bank Account Ownership by Cellphone Access
**Type:** Bar chart  
**Metric:** Percentage with `bank_account = Yes`

**Data:**
- No cellphone: 1.71%
- Cellphone: 18.38%

**Purpose:** Show one of the clearest feature-target associations.

**Use on:** Key Feature Associations slide.

---

### Chart 3 — Bank Account Ownership by Education Level
**Type:** Horizontal bar chart  
**Metric:** Percentage with `bank_account = Yes`

**Data:**
- No formal education: 3.90%
- Primary education: 8.55%
- Secondary education: 23.28%
- Tertiary education: 51.08%
- Vocational/Specialised training: 57.04%
- Other/Don't know/RTA: 31.43%

**Purpose:** Show the strong gradient across education groups.

**Use on:** Key Feature Associations slide.

---

### Chart 4 — Bank Account Ownership by Job Type
**Type:** Horizontal bar chart  
**Metric:** Percentage with `bank_account = Yes`

**Data:**
- No Income: 2.07%
- Informally employed: 7.95%
- Remittance Dependent: 9.50%
- Don't Know/Refuse to answer: 11.11%
- Farming and Fishing: 11.67%
- Self employed: 13.17%
- Other Income: 18.15%
- Government Dependent: 20.24%
- Formally employed Private: 54.12%
- Formally employed Government: 77.52%

**Purpose:** Show major ownership differences across employment groups.

**Use on:** Key Feature Associations slide.

---

### Chart 5 — Bank Account Ownership Rate by Country
**Type:** Bar chart  
**Data:**
- Kenya: 25.07%
- Rwanda: 11.48%
- Tanzania: 9.17%
- Uganda: 8.61%

**Purpose:** Show country-level variation.

**Use on:** Key Feature & Country Insights slide.

---

### Chart 6 — Model Macro F1 Comparison
**Type:** Bar chart  
**Data:**
- Dummy: 0.46
- Logistic Regression: 0.70
- Random Forest: 0.70
- XGBoost: 0.72

**Purpose:** Compare model quality under the selected primary metric.

**Use on:** Model Comparison slide.

---

### Chart 7 — Minority-Class Recall Comparison
**Type:** Bar chart or compact callout  
**Data:**
- Dummy: 0.00
- Logistic Regression: 0.35
- Random Forest: 0.75
- XGBoost: 0.40

**Purpose:** Make the precision/recall trade-off visible.

**Use on:** Model Comparison or Error Analysis slide.

---

### Chart 8 — Final Confusion Matrix
**Type:** Confusion matrix heatmap  
**Model:** `TODO — final selected model`

**Purpose:** Explain false positives and false negatives.

**Use on:** Error Analysis / Final Model slide.

**Status:** `TODO`

---

# 13. Figures That Should Stay in the Notebook, Not the Main Presentation

Unless they become important later, these are useful for analysis but do not need dedicated final slides:

- Full categorical `value_counts()` outputs.
- Every individual categorical plot.
- Raw `describe()` tables.
- Full histograms for every numerical feature.
- All boxplots.
- Full cross-tab tables.
- Long classification reports.
- Every confusion matrix from every model.
- Raw debugging output.

These can remain documented in the EDA/modeling notebooks.

---

# 14. Instructions for an LLM Creating the PowerPoint

When creating the deck from this file:

1. Read the complete project repository before building slides.
2. Treat this `presentation_plan.md` as the narrative and visual specification.
3. Use only verified numbers from the project or this plan.
4. Do not invent missing model results, error-analysis findings, feature importance, tuning improvements, or business claims.
5. If a section is still marked `TODO`, create a clean placeholder or omit it depending on whether the deck is a draft or final version.
6. Recreate charts as clean presentation-quality graphics rather than screenshots from the notebook.
7. Prefer percentage charts for EDA comparisons.
8. Keep one main takeaway per slide.
9. Use concise text and move detailed explanation into speaker notes.
10. Preserve the distinction between correlation/association and causation.
11. Keep the target class definition explicit:
    - `Yes` = respondent has a bank account
    - `No` = respondent does not have a bank account
12. For model comparison, prioritize **Macro F1** unless the project team later documents a different final metric decision.
13. Do not select the final model solely from accuracy.
14. Do not claim the system identifies who is “bankable.”
15. Include limitations and responsible-use language in the final deck.

---

# 15. Update Log / Working Notes

Use this section while developing the project.

## EDA
- [x] Dataset structure
- [x] Missing-value check
- [x] Duplicate check
- [x] Target distribution
- [x] Numerical feature distributions
- [x] Categorical feature distributions
- [x] Feature vs target analysis
- [x] Country-level analysis

## Modeling
- [x] Majority-class baseline
- [x] Logistic Regression
- [x] Random Forest
- [x] XGBoost
- [ ] Clean preprocessing pipeline
- [ ] Feature engineering experiments
- [ ] Hyperparameter tuning
- [ ] Error analysis
- [ ] Final model selection

## Communication
- [x] Presentation storyline defined
- [x] Core EDA visuals defined
- [ ] Final model visuals
- [ ] Final PowerPoint
- [ ] Final README update
- [ ] Final repository cleanup

---

# 16. Current Verified EDA Summary

The dataset contains **23,524** training observations and has no detected missing values or duplicate rows. The target is strongly imbalanced, with **85.92% No** and **14.08% Yes**.

Several features show substantial association with bank account ownership. Cellphone access is especially notable: only **1.71%** of respondents without cellphone access have a bank account compared with **18.38%** of respondents with cellphone access. Education and employment show even larger differences, with ownership rates exceeding **50%** for tertiary/vocational education and formal private/government employment groups.

Country-level differences are also substantial. Kenya has the highest bank account ownership rate at **25.07%**, compared with **11.48%** in Rwanda, **9.17%** in Tanzania, and **8.61%** in Uganda.

These findings suggest that demographic, socioeconomic, technological-access, and geographic features may all provide useful predictive information. Because the target is imbalanced, model evaluation should not rely on accuracy alone.
