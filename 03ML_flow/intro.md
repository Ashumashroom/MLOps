# MLflow Introduction & Using MLflow with DagsHub

## 1. Introduction to MLflow

**MLflow** is an open-source platform for managing the **machine learning lifecycle**, which includes:
- **Experiment tracking** (logging parameters, metrics, artifacts, models)
- **Model packaging** (storing models in a standard format)
- **Model registry** (versioning & managing models)
- **Deployment** (serving models locally or in the cloud)

It is **framework-agnostic**, meaning you can use it with TensorFlow, PyTorch, Scikit-Learn, XGBoost, LightGBM, etc.

---

## 2. Why Use MLflow?
- Keeps track of **all experiments** in one place.
- Stores **artifacts** (models, plots, datasets) with metadata.
- Makes experiments **reproducible** and **shareable**.
- Integrates well with **cloud & remote tracking servers** like DagsHub.

---

## 3. MLflow Components

| Component        | Purpose |
|------------------|---------|
| **MLflow Tracking** | Logs & queries experiments (params, metrics, artifacts) |
| **MLflow Projects** | Packages data science code for reproducibility |
| **MLflow Models** | Standard format to save & serve models |
| **MLflow Registry** | Manages model versions, stage transitions (dev → prod) |

---

## 4. Installing MLflow

```bash
pip install mlflow
