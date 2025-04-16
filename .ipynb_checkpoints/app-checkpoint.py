import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Model accuracy results
results = {
    "Model": ["Logistic Regression", "Random Forest", "XGBoost", "DNN", "LSTM"],
    "Accuracy": [0.467, 0.932, 0.946, 0.885, 0.990]
}

# Convert the results to a DataFrame
df = pd.DataFrame(results)

# Streamlit app
st.title("Model Performance Comparison")
st.write("Comparison of accuracy across different models:")

# Plot the accuracies
fig, ax = plt.subplots()
ax.barh(df['Model'], df['Accuracy'], color=['blue', 'green', 'red', 'purple', 'orange'])
ax.set_xlabel("Accuracy")
ax.set_title("Accuracy of Different Models")
ax.set_xlim(0.0, 1.00)  # Setting the x-axis limit for better visualization

# Display the plot in Streamlit
st.pyplot(fig)

# Display the data in a table
st.write("Model Accuracy Data")
st.dataframe(df)
