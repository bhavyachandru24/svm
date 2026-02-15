# Support Vector Machine Model

**Model Overview**

This project implements a Support Vector Machine (SVM) algorithm for classification. The objective of the model is to classify data points into predefined categories by finding the optimal hyperplane that maximizes the margin between different classes.

Two kernel functions are used to evaluate performance:

Linear Kernel

Radial Basis Function (RBF) Kernel

The Linear kernel is suitable when the data is linearly separable, while the RBF kernel is effective for capturing non-linear relationships in the dataset.

**Dataset Description**

The dataset contains both numerical and categorical features. Before training the SVM model, categorical variables are encoded and numerical features are scaled.

Typical structure:

Numerical features (e.g., Age, Income, Score)

Categorical features (e.g., Gender, City)

Target variable (binary or multiclass classification)

**Data Preprocessing**

The following preprocessing steps are applied:

1. Handling Missing Values
Missing values are imputed using appropriate strategies such as median (for numerical features) and mode (for categorical features).

2. Encoding Categorical Variables
Categorical features are converted into numerical format using Label Encoding or OneHot Encoding.

3. Feature Scaling
StandardScaler is applied to normalize numerical features. Scaling is essential for SVM because it is sensitive to feature magnitude.

4. Train-Test Split
The dataset is split into training and testing sets using an 80:20 ratio to evaluate model performance.

5. Model Implementation

Two SVM models are trained:

SVM with Linear Kernel

SVM with RBF Kernel

Both models are trained on the same training dataset and evaluated on the test dataset for comparison.

6. Evaluation Metrics

The following metrics are used to evaluate performance:

Accuracy Score

Confusion Matrix

Accuracy measures the proportion of correct predictions.
The confusion matrix provides detailed insight into classification performance across classes.

**Model Comparison**

Linear Kernel:

Suitable for linearly separable data

Faster training time

Simpler decision boundary

RBF Kernel:

Handles non-linear data effectively

More flexible decision boundary

May require tuning of hyperparameters such as gamma

The best-performing kernel is selected based on test accuracy and confusion matrix analysis.

**Requirements**

The project requires the following Python libraries:

pandas

numpy

scikit-learn

matplotlib

Ensure these libraries are installed in your Python environment before running the script.

**How to Run the Code**

1. Place the dataset file (for example, svm_mixed_dataset.csv) in the same directory as the Python script file (for example, svm_model.py).

2. Open the project folder in a Python development environment such as VS Code or PyCharm.

3. Open the file svm_model.py.

4. Run the script using your IDE’s run option.

5. After execution, the program will:

6. Load the dataset

Perform preprocessing

Train SVM models with Linear and RBF kernels

Evaluate accuracy

Display confusion matrices

Print performance comparison

Conclusion

The SVM model demonstrates strong classification capability using both linear and non-linear kernels. Kernel selection depends on the structure of the dataset. Proper preprocessing and feature scaling are essential for achieving optimal SVM performance.
