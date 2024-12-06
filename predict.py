import streamlit as st
import joblib

# Load the trained model
# Replace "your_model_file.pkl" with the path to your trained model file
model = joblib.load("stacking_model.pkl")


def predict_cancer(radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean):
    # Make prediction using the model
    input_data = [[radius_mean, texture_mean,
                   perimeter_mean, area_mean, smoothness_mean]]
    prediction = model.predict(input_data)
    return prediction[0]


def main():
    st.title("Breast Cancer Prediction")

    st.markdown("---")

    st.write("Enter the following values to predict breast cancer:")
    radius_mean = st.text_input("Radius Mean", "")
    texture_mean = st.text_input("Texture Mean", "")
    perimeter_mean = st.text_input("Perimeter Mean", "")
    area_mean = st.text_input("Area Mean", "")
    smoothness_mean = st.text_input("Smoothness Mean", "")

    if st.button("Submit"):
        # Ensure all input fields are filled
        if radius_mean and texture_mean and perimeter_mean and area_mean and smoothness_mean:
            # Convert input values to float
            radius_mean = float(radius_mean)
            texture_mean = float(texture_mean)
            perimeter_mean = float(perimeter_mean)
            area_mean = float(area_mean)
            smoothness_mean = float(smoothness_mean)

            # Call the prediction function
            result = predict_cancer(
                radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean)
            if result == 0:
                st.write("Prediction Result: Benign")
            else:
                st.write("Prediction Result: Malignant")
        else:
            st.error("Please fill in all input fields.")


if __name__ == "__main__":
    main()
