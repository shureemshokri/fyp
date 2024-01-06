import streamlit as st
# from tensorflow.keras.models import load_model
# # from flower_classification_model import flowers
# import cv2
# import numpy as np


# flowers = ['tulip', 'orchids', 'peonies', 'hydrangeas', 'lilies', 'gardenias', 'garden_roses', 'daisies', 'hibiscus', 'bougainvillea']


# # Load the trained model
# model = load_model(r"C:\Users\Shureem Shokri\Documents\DEGREE\YEAR 3\SEM 2\FYP\code\flower_classification_model")


# # Function to preprocess a single image for prediction
# def preprocess_single_image(image):
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
#     image = cv2.resize(image, (256, 256))  # Resize the image to desired dimensions
#     image = image / 255.0  # Normalize the image
#     return image

# # Function to predict the class of a single image
# def predict_image_class(image):
#     preprocessed_image = preprocess_single_image(image)
#     preprocessed_image = np.expand_dims(preprocessed_image, axis=0)
#     prediction = model.predict(preprocessed_image)
#     predicted_class_index = np.argmax(prediction)
#     predicted_class = flowers[predicted_class_index]
#     return predicted_class



def main():
    st.title("BUNGA.COM")
    st.subheader("Welcome to BUNGA.COM where you can predict the image of your flower!")
    # st.button("Next", on_click=project_page)

if __name__ == "__main__":
    main()



