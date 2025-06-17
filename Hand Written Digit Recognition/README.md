# Handwritten Digit Recognition

A simple machine learning project that recognizes handwritten digits (0-9) using logistic regression and the scikit-learn digits dataset.

## 📋 Overview

This project demonstrates digit classification using logistic regression on the built-in sklearn digits dataset. The implementation includes data visualization with heatmaps to better understand the model's performance.

## 🔧 Requirements

```
python 3.7+
jupyter
scikit-learn
seaborn
matplotlib
numpy
```

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Rupayan2005/ML-Project.git
cd Hand Written Digit Recognition
```

2. Install dependencies:
```bash
pip install scikit-learn seaborn matplotlib numpy pandas
```

3. Run the notebook:
```bash
jupyter notebook Hand written digit recognition.ipynb
```

## 📊 Dataset

Using `sklearn.datasets.load_digits()`:
- **1,797 samples** of 8x8 pixel digit images
- **10 classes** (digits 0-9)
- **64 features** per image (flattened pixels)

## 🚀 What's Inside

The Jupyter notebook contains:
- Data loading and exploration
- Logistic regression model training
- Model evaluation and accuracy metrics
- Confusion matrix heatmap visualization using seaborn
- Sample predictions display

## 📈 Results

- **Algorithm**: Logistic Regression
- **Expected Accuracy**: ~97%
- **Visualization**: Confusion matrix heatmap showing classification performance

## 🔍 Key Features

- Simple and clean implementation
- Easy to understand for beginners
- Visual confusion matrix using seaborn
- Complete workflow from data loading to prediction

## 📁 Project Structure

```
Hand Written Digit Recognition/
├── Hand written digit recognition.ipynb    # Main notebook
├── README.md                               # This file
```

## 🤝 Usage

1. Open `Hand written digit recognition.ipynb`
2. Run all cells sequentially
3. View the confusion matrix heatmap
4. Check model accuracy and predictions


---

*A straightforward introduction to machine learning with digit recognition* 🚀