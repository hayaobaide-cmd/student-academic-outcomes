 # 🎓 Student Academic Outcomes Prediction

## Project Overview

This project uses machine learning to predict student academic outcomes (Pass or Fail) based on academic performance, study habits, attendance, and other relevant factors.

The goal is to support the early identification of students who may be at risk of failing, allowing educational institutions to provide additional academic support.

## Dataset

The dataset contains:

- **100,000 student records**
- **44 original columns**
- **Target variable:** `pass_status` (Pass or Fail)

The prediction model uses 10 selected features:

1. Attendance Percentage
2. Study Hours Per Day
3. Previous Exam Score
4. Previous GPA
5. Assignment Completion Rate
6. Study Consistency
7. Revision Frequency
8. Motivation Level
9. Time Management Score
10. Sleep Hours

## Data Preprocessing

The following preprocessing steps were implemented:

- Checked missing values and duplicate records.
- Used median imputation for missing numerical values.
- Used most-frequent imputation for missing categorical values.
- Applied StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.
- Split the dataset into 80% training and 20% testing data.
- Used a scikit-learn Pipeline to reduce data leakage during model training and evaluation.

## Machine Learning Models

Two classification algorithms were trained and compared:

- Logistic Regression
- Decision Tree Classifier

The models were evaluated using accuracy, precision, recall, F1-score, and confusion matrices.

## Model Evaluation and Results

| Model | Test Accuracy |
|---|---|
| Logistic Regression | 81.10% |
| Decision Tree | 80.08% |
| Tuned Logistic Regression | 72.67% |

The tuned Logistic Regression model was selected for deployment because it achieved approximately **74.5% recall for the Fail class**, compared with approximately 35.5% for the original Logistic Regression model.

This improves the identification of students at risk of failing, although it reduces overall accuracy and increases false-positive predictions.

## Hyperparameter Tuning

GridSearchCV was used with five-fold cross-validation to optimize Logistic Regression.

The tested parameters included:

- Regularization parameter `C`: 0.1, 1, 10
- Class weights: None and balanced

The best parameters were:

- `C = 1`
- `class_weight = balanced`

The tuning process prioritized recall for students in the Fail category.

## Streamlit Application

An interactive web application was developed using Streamlit.

Users can enter student information and receive a predicted academic outcome:

- **PASS 🎉**
- **FAIL ⚠️**

The application uses the trained machine learning pipeline saved in `student_outcome_model.pkl`.

### Live Application

https://student-academic-outcomes-4haux9nuzpdswb3wddkssc.streamlit.app/

## How to Run the Application

1. Download or clone this GitHub repository.
2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in the terminal.

## Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit application |
| `student_outcome_model.pkl` | Trained machine learning pipeline |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |

## Team Members

Add the names of all group members and their respective contributions here.

## AI Tool Usage Disclosure

ChatGPT (OpenAI) was used to support Python coding, machine learning implementation, debugging, and the setup of GitHub and Streamlit deployment.

The application was tested using sample inputs that produced both PASS and FAIL predictions.

## Limitations

- The model produces predictions, not guaranteed academic outcomes.
- The selected model prioritizes identifying at-risk students, which can increase false-positive predictions.
- The dataset contains 100,000 records; any larger minimum dataset requirement must be addressed separately.
- Predictions should be used as supporting information rather than as the sole basis for academic decisions.
