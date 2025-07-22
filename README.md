# Heart Disease Prediction App

A lightweight Python-based web application that predicts the likelihood of heart disease based on user-provided health metrics.

![Python](https://img.shields.io/badge/python-3.8+-blue) ![Streamlit](https://img.shields.io/badge/streamlit-web_app-green)

## 🚀 Features

- **Pre-trained ML Models**: Loads optimized machine learning models for accurate predictions
- **Health Tips Integration**: Provides personalized health recommendations via `tips_file.py`
- **Simple Interface**: Built with streamlined user interface (CLI or Streamlit)
- **PCA Processing**: Uses Principal Component Analysis for efficient data preprocessing
- **Standardized Input**: Automatic feature scaling for consistent predictions
- **Instant Results**: Real-time prediction with risk assessment and health tips

## 🛠️ Technology Stack

- **Backend**: Python
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Web Framework**: Streamlit (optional)
- **Model Format**: Pickle (.pkl) files
- **Interface**: Command Line Interface (CLI) or Streamlit Web App

## 📂 Repository Structure

```text
heart-disease-prediction-app/
├── heart-disease-prediction-app.py   # Main application file
├── main_model.pkl                    # Trained classification model
├── pca_model.pkl                     # PCA preprocessing transformer
├── scaler.pkl                        # Feature scaler for data normalization
├── tips_file.py                      # Health tips and recommendations module
├── requirements.txt                  # Python dependencies
└── .github/
    └── workflows/                    # CI/CD workflows (if any)
```

## ⚙️ Installation & Setup

### Prerequisites

```bash
Python 3.8+
pip (Python package installer)
```

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/saswattulo/heart-disease-prediction-app.git
   cd heart-disease-prediction-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   # .\venv\Scripts\activate     # Windows PowerShell
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage

### Via Command Line Interface (CLI)

```bash
python heart-disease-prediction-app.py
```

The application will prompt you to enter health parameters such as:
- Age
- Cholesterol levels
- Blood pressure
- Exercise-induced symptoms
- Other cardiovascular indicators

**Example interaction:**
```
Enter age: 55
Enter cholesterol: 240
Enter resting blood pressure: 140
Enter chest pain type (0-3): 2
...
Prediction: You are at risk of heart disease.
Tip: Consider regular exercise and avoid high-fat diet.
```

### Via Streamlit Web Interface (if supported)

```bash
streamlit run heart-disease-prediction-app.py
```

This opens an interactive web interface where you can:
- Input health parameters using sliders and forms
- View predictions in real-time
- Access personalized health recommendations
- Visualize your risk factors

## 🧠 How It Works

1. **Data Input**: User enters health parameters through CLI or web interface
2. **Data Preprocessing**: Input data is standardized using the pre-loaded `scaler.pkl`
3. **Dimensionality Reduction**: PCA model (`pca_model.pkl`) reduces data complexity
4. **Prediction**: The trained classification model (`main_model.pkl`) generates risk assessment
5. **Results Display**: Prediction is shown with personalized health tips from `tips_file.py`

## 🛠️ Model Components

- **`main_model.pkl`**: Pre-trained machine learning classifier for heart disease prediction
- **`pca_model.pkl`**: Principal Component Analysis transformer for feature reduction
- **`scaler.pkl`**: StandardScaler for data normalization and consistency
- **`tips_file.py`**: Module containing health recommendations and lifestyle tips

## 📋 Requirements

The application dependencies are listed in `requirements.txt`:

```text
numpy
pandas
scikit-learn
streamlit (optional for web interface)
pickle (included in Python standard library)
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 🛠️ Customization

### Retrain the Model
- Replace the `.pkl` files with your own trained models
- Ensure compatibility with the input format expected by the application

### Update Health Tips
- Edit `tips_file.py` to add new recommendations
- Customize tips based on different risk factors or demographics

### UI Enhancement Options
- Convert CLI to full Streamlit web application
- Add Flask-based web interface for deployment
- Implement additional visualization features

## 🧪 Example Prediction Flow

```python
# Sample prediction workflow
Enter health parameters:
├── Age: 55 years
├── Cholesterol: 240 mg/dl
├── Blood Pressure: 140/90 mmHg
├── Chest Pain Type: Typical Angina
└── Other cardiovascular indicators...

Processing:
├── Data standardization ✓
├── PCA transformation ✓
└── Model prediction ✓

Results:
├── Risk Assessment: High Risk
├── Confidence: 85%
└── Recommendations: 
    ├── Regular cardiovascular exercise
    ├── Low-sodium diet
    └── Regular medical check-ups
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve the project:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Commit your changes**: `git commit -m "Add feature"`
4. **Push to the branch**: `git push origin feature-name`
5. **Open a Pull Request**

### Contribution Guidelines
- Include tests for new features
- Update documentation when adding functionality
- Follow Python PEP 8 style guidelines
- Ensure compatibility with existing model files

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## ⚠️ Medical Disclaimer

This application is for **educational and informational purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns and before making any healthcare decisions.

## 🙏 Acknowledgements

- **Dataset**: Based on UCI Heart Disease Dataset
- **Libraries**: Thanks to the open-source community for scikit-learn, pandas, numpy, and streamlit
- **Medical Knowledge**: Health tips compiled from reputable cardiovascular health sources

## 👨‍💻 Author

**Saswat Tulo** – *Data Engineer & ML Enthusiast*

- **GitHub**: [@saswattulo](https://github.com/saswattulo)
- **Kaggle**: [@saswattulo](https://www.kaggle.com/saswattulo)
- **LinkedIn**: [Connect with me](https://linkedin.com/in/saswattulo)

## 📞 Support & Issues

If you encounter any issues or have questions:

- **Create an issue** on GitHub with detailed description
- **Check existing issues** before creating new ones
- **Provide system information** and error logs when reporting bugs

---

**⭐ If you found this project helpful, please give it a star!**

---

### 💡 Enhancement Ideas

Want to contribute? Here are some ideas for improvements:

- [ ] Add data visualization for risk factors
- [ ] Implement user authentication and history tracking
- [ ] Create mobile-responsive web interface
- [ ] Add support for multiple languages
- [ ] Integrate with wearable device APIs
- [ ] Implement batch prediction capabilities
- [ ] Add model explainability features (SHAP, LIME)

---

*Last updated: 2025*
