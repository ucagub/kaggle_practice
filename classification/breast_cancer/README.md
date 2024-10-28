# Summary

The **LGMBClassifier** trained on the breast cancer dataset achieved the following metrics:

|              | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| **B**        | 0.97      | 0.99   | 0.98     | 108     |
| **M**        | 0.98      | 0.95   | 0.97     | 63      |
| **Accuracy** |           |        | 0.98     | 171     |
| **Macro Avg**| 0.98      | 0.97   | 0.97     | 171     |
| **Weighted Avg** | 0.98   | 0.98   | 0.98     | 171     |

Adjusting `n_estimators` and using SMOTE did not improve the performance of the model.

## Notebook Organization

The rest of the notebook is organized as follows:
1. EDA (Exploratory Data Analysis)
2. Training
3. Adjusting `n_estimators` with Optuna and using SMOTE

Dataset from [Kaggle Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset).

## Launching MLflow Server

To launch a basic MLflow server, use the following command:

```bash
mlflow server --host 127.0.0.1 --port 8080