# Introduction to DVC (Data Version Control) 📦📊

DVC is an open-source version control system for **machine learning projects**. It extends Git capabilities to handle **data files**, **ML models**, and **experiment tracking**, making it ideal for MLOps workflows.

---

## 🎯 Why DVC?

- Git is great for source code but not suitable for large data or model files.
- DVC tracks large files, datasets, and ML models **without storing them in Git**.
- Provides **reproducibility**, **collaboration**, and **experimentation** features.

---

## 🔑 Key Features

| Feature               | Description |
|-----------------------|-------------|
| 🗂️ Data Versioning     | Track data and model files with Git-like behavior |
| 🔗 Git Integration     | Works alongside Git seamlessly |
| 🔁 Pipelines           | Define and run reproducible ML workflows |
| 🚚 Remote Storage      | Store datasets and models in S3, GCS, Azure, SSH, etc. |
| 🧪 Experiment Tracking | Log experiments, hyperparameters, metrics |
| 📈 Metrics Tracking    | Track model performance over time |

---

## ⚙️ Basic DVC Workflow

```bash
# Step 1: Initialize DVC in your Git repo
dvc init

# Step 2: Add a dataset or model file
dvc add data/dataset.csv

# Step 3: Commit DVC metafile to Git
git add data/dataset.csv.dvc .gitignore
git commit -m "Add dataset with DVC tracking"

# Step 4: Push large files to remote storage
dvc remote add -d myremote <remote-url>
dvc push

# Step 5: Share with others
git push  # share code + .dvc files
