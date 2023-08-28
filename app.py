import streamlit as st
import cv2
import numpy as np
import tensorflow as tf

# Load the face detection model
facetracker = tf.keras.models.load_model('facetracker.h5')

def main():
    st.title("Live Face Detection with Streamlit")

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resized = tf.image.resize(rgb, (120, 120))

        yhat = facetracker.predict(np.expand_dims(resized / 255, 0))
        confidence, sample_coords = yhat[0][0], yhat[1][0]

        if confidence > 0.5:
            # Draw a rectangle around the detected face
            x1, y1, x2, y2 = np.multiply(sample_coords, [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Display the frame with the face detection overlay
        cv2.imshow("Live Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
