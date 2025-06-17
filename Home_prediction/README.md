# Bengaluru Home Price Prediction

A machine learning web application that predicts home prices in Bengaluru using logistic regression. The project includes data preprocessing, model training, and a complete web interface.

## 📋 Overview

This project predicts home prices in Bengaluru based on various features like location, size, bhk and bath. It includes a trained machine learning model served through a Flask API with a vanilla JavaScript frontend.

## 📊 Dataset

- **File**: `bengaluru_house_prices.csv`
- **Shape**: 13,320 rows × 9 columns
- **Features**: Location, size, total_sqft, bath, bhk, price, etc.
- **Target**: Home price prediction

## 🔧 Tech Stack

- **Machine Learning**: Logistic Regression (scikit-learn)
- **Backend**: Flask (Python)
- **Frontend**: JavaScript, HTML, CSS
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/Rupayan2005/ML-Project.git
cd Home_prediction
```

2. Install Python dependencies:
```bash
pip install flask scikit-learn pandas numpy matplotlib
```

3. Start the Flask server:
```bash
cd server
python app.py
```

4. Open the frontend:
```bash
cd client
# Open index.html in your browser
```

## 📁 Project Structure

```
Home_prediction/
│
├── model/
│   ├── Project1 Real estate prediction.ipynb    # Data analysis & model training
│   ├── project1_real_estate.pkl                 # Trained logistic regression model
│   └── columns.json                             # Feature columns information
│
├── server/
│   ├── app.py                    # Flask API server
│   └── util.py                   # Utilities
│
├── client/
│   ├── index.html                # Main webpage
│   ├── style.css                 # Styling
│   └── script.js                 # Frontend JavaScript
│
└── README.md                     # This file
```

## 🚀 How It Works

### 1. Data Processing
- Load and explore the Bengaluru house prices dataset
- Handle missing values and outliers
- Feature engineering and preprocessing
- Data visualization and analysis

### 2. Model Training
- Train logistic regression model
- Evaluate model performance
- Save trained model as pickle file
- Export feature columns to JSON

### 3. Web Application
- **Flask Backend**: Serves the ML model via REST API
- **JavaScript Frontend**: User-friendly interface for price prediction
- **Real-time Predictions**: Enter house details and get instant price estimates

## 🔍 Key Features

- **Data Preprocessing**: Clean and prepare raw housing data
- **Exploratory Analysis**: Visualizations and insights
- **ML Model**: Logistic regression for price prediction
- **REST API**: Flask server with prediction endpoints
- **Web Interface**: Interactive frontend for easy use
- **Model Persistence**: Saved model and feature information

## 📈 Model Performance

- **Algorithm**: Logistic Regression
- **Dataset Size**: 13,320 samples
- **Features**: 9 columns after preprocessing
- **Evaluation**: Cross-validation and accuracy metrics

## 🌐 API Endpoints

```
POST /predict_home_price
- Input: JSON with house features
- Output: Predicted price

GET /get_location_names
- Output: Available locations list
```

## 💻 Usage

1. **Train the Model**:
   - Open `model/Project1 Real estate prediction.ipynb`
   - Run all cells to process data and train model
   - Model and columns files will be saved automatically

2. **Start the Server**:
   ```bash
   cd server
   python app.py
   ```

3. **Use the Web App**:
   - Open `client/index.html` in browser
   - Fill in house details (location, sqft, bhk, bath)
   - Click predict to get estimated price

## 🔧 Model Features

Input features for prediction:
- Location/Area
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request


---

*Predict Bengaluru home prices with machine learning* 🏠