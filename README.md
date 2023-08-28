# RealTimeFaceDetection
The "Real-Time Face Detection using Deep Learning and open-cv" app

# Description 
The "Real-Time Face Detection using Streamlit" app is an interactive web application that showcases the capabilities of deep learning and computer vision. It enables real-time face detection through a user's webcam feed, drawing bounding boxes around detected faces and providing dynamic labels for easy identification. This app seamlessly integrates OpenCV and TensorFlow, leveraging Streamlit's reactivity for a responsive and engaging user experience. By offering both educational insight and a coding demonstration, the app serves as a valuable resource for learning about AI, computer vision, and web application development. It exemplifies the synergy between cutting-edge technology and user-friendly frameworks, making complex concepts accessible to a broader audience.

## App Preview
![ezgif com-video-to-gif (2)](https://github.com/actuaryhafeez/RealTimeFaceDetection/assets/55107467/4a2bbd1a-57f7-45af-9b2d-8153c2d6e0ac)



## Features

- Real-time face detection using deep learning and OpenCV
- Bounding boxes drawn around detected faces with dynamic labels
-Seamless integration of OpenCV, TensorFlow, and Streamlit
- Utilizes a deep learning model trained on a custom dataset



## Getting Started
 How to Use
 
Clone the repository:

    git clone https://github.com/yourusername/RealTimeFaceDetection.git

Install the required dependencies:

    pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py
    


## Dataset
I captured 90 images of myself using the webcam, each serving as a unique dataset for my face detection project. To enhance the dataset's effectiveness, I utilized the LabelMe annotation tool to annotate the images. This involved outlining my face with bounding boxes and providing corresponding label information. This annotated dataset became crucial for training the deep learning model to accurately detect faces in real-time.

Furthermore, I employed the Albumentations library to perform data augmentation on the annotated images. Data augmentation is a technique that artificially diversifies the dataset by applying various transformations like cropping, flipping, and adjusting brightness. This process not only increases the dataset's size but also improves the model's ability to generalize and identify faces under different conditions. The combination of these steps—capturing images, annotating them, and augmenting the dataset—lays the foundation for building a robust and accurate face detection model.
## About the Author

This app was created by Abdul Hafeez. Connect with me on [LinkedIn](https://www.linkedin.com/in/abdul-hafeez-ds/) to stay updated on my latest projects.

## Try It Out
Feel free to clone this repository and try out the RealTimeFaceDetection yourself. If you have any questions or suggestions, please don't hesitate to open an issue or submit a pull request.

## Project Structure 

    RealTimeFaceDetection/
        ├── data/
        ├── app.py/
        ├── requirements.txt/
        ├── README.md/
        ├── facetracker.h5
        ├── model.ipynb
        ├── LICENSE/

        

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).

## Contributions
Contributions are welcome! If you find any issues or bugs, feel free to open an issue or submit a pull request.

