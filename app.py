# app.py

import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

# Set page configuration
st.set_page_config(
    page_title="Home$crapper - Sustainable Waste Management",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to load Lottie animations from URL
def load_lottieurl(url: str):
    """
    Loads a Lottie animation from a URL.

    Parameters:
        url (str): The URL of the Lottie JSON file.

    Returns:
        dict: The Lottie animation JSON data.
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Define each page as a separate function
def home():
    st.title("♻️ **Welcome to Home$crapper!**")
    st.markdown("### *Your Sustainable Waste Management Solution*")
    st.write("---")

    # Load and display a Lottie animation
    lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u4yrau.json")
    if lottie_animation:
        st_lottie(lottie_animation, height=300, key="home_animation")

    st.markdown("""
    **Home$crapper** is an innovative platform connecting households and vendors to promote responsible recycling and waste management. Our mission is to help users turn recyclable waste into value, ensuring proper and sustainable disposal.

    Our platform also facilitates a marketplace where users can donate or sell reusable items at minimal cost, making Home$crapper an eco-friendly and socially impactful choice.
    """)

    st.write("---")
    st.header("🔍 **Key Features**")
    st.markdown("""
    - **Trusted Vendors**: Connect with genuine, vetted vendors.
    - **Real-Time Pricing**: Access current market rates for waste materials.
    - **Verified Weighing Machines**: Ensure accurate weights for transparency.
    - **Marketplace for Donations and Resales**: Donate or sell reusable goods.
    - **Secure Transactions**: Reliable interactions between users and vendors.
    """)

    st.write("---")
    st.header("🚗 **How It Works**")
    with st.expander("♻️ Recycling Waste"):
        st.markdown("""
        1. **Select Waste Type**: Choose the recyclable waste you want to dispose of.
        2. **Find a Vendor**: View nearby vendors offering competitive prices.
        3. **Schedule Pickup**: Select a vendor and set a pickup date.
        4. **Receive Payment**: Get paid based on weight and market rate.
        """)

    with st.expander("🎁 Donate or Resell Goods"):
        st.markdown("""
        1. **List an Item**: Post items for donation or minimal sale.
        2. **Connect with a Buyer/Recipient**: Interested parties reach out.
        3. **Arrange Pickup or Delivery**: Hand over the item directly.
        """)

    st.write("---")
    st.header("🔗 **Get Started**")
    st.markdown("""
    Ready to turn waste into value? **[Join Home$crapper today](#)** to start recycling responsibly or donating unused items with ease.
    """)

    st.button("🌟 **Join Now**", help="Click to sign up and start your eco-friendly journey with Home$crapper!")

def frontend():
    st.title("🚀 **Frontend Documentation**")
    st.write("---")

    st.subheader("📝 **Design Considerations**")
    st.markdown("""
    The frontend of the **Home$crapper** project was designed with several key considerations in mind:

    - **User-Centric Design**: The interface prioritizes ease of use, ensuring that users can navigate the platform effortlessly to either list items for sale or browse available products.
    - **Responsive Layout**: The application is built to be fully responsive, providing a seamless experience across various devices, including desktops and tablets.
    - **Accessibility**: Adhering to accessibility standards ensures that the application is usable by individuals with disabilities, enhancing usability for all users.
    - **Performance Optimization**: The frontend is optimized for performance, minimizing load times and ensuring smooth interactions through efficient rendering and state management.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The frontend of **Home$crapper** includes several notable features:

    - **Authentication**: Users can easily log in and manage their profiles through a secure authentication process using auth0.
    - **Marketplace Functionality**: Users can list items for sale, view details of listed products, and make purchases directly through the platform.
    - **Garbage Scrapping Interface**: A dedicated section for users to report garbage or unwanted materials, facilitating community engagement in environmental efforts.
    - **Dynamic Content Loading**: The application dynamically loads content based on user interactions, providing a smooth and engaging experience without full page reloads.
    - **VoiceFlow ChatBot Service**: Enhances the user experience by providing answers to queries, adding to user satisfaction.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    The **Home$crapper** frontend utilizes a modern technological stack:

    - **React**: A JavaScript library for building user interfaces, allowing for the creation of reusable UI components.
    - **Vite**: A build tool that provides a fast development environment with hot module replacement (HMR).
    - **Material UI**: A popular React UI framework that offers pre-designed components to speed up development and ensure a consistent look and feel.
    - **Emotion**: A CSS-in-JS library used for styling components dynamically based on props and state.
    - **React Router**: A routing library for React that enables navigation between different views in the application.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    competition/
    ├── eslint.config.js
    ├── index.html
    ├── package-lock.json
    ├── package.json
    ├── public/
    │   └── vite.svg
    ├── README.md
    ├── src/
    │   ├── App.css
    │   ├── App.jsx
    │   ├── assets/
    │   │   ├── hero.png
    │   │   ├── logo.png
    │   │   ├── profile.png
    │   │   ├── options1.png
    │   │   ├── options2.png
    │   │   │── rudra.png
    │   │   │── sanatan.png
    │   │   │── aryan.png
    │   │   │── sagar.png
    │   │   └── react.svg
    │   ├── atom/
    │   │     └──userAtom.js
    │   ├── auth_config.json
    │   ├── components/
    │   │   └── Profile.jsx
    │   ├── hooks/
    │   │   └── usePreviewImg.jsx
    │   ├── index.css
    │   ├── main.jsx
    │   ├── pages/
    │   │   ├── Appbar.jsx
    │   │   ├── Contact.jsx
    │   │   ├── Hero.jsx
    │   │   ├── HomeOptions.jsx
    │   │   ├── Login.jsx
    │   │   └── Logout.jsx
    │   │   └── MyProfile.jsx
    │   │   └── Orders.jsx
    │   ├── part1/
    │   │   ├── Final.jsx
    │   │   ├── ModalData.jsx
    │   │   ├── ProductList.jsx
    │   │   ├── Seller.jsx
    │   │   └── Vendor.jsx
    │   │   └── VendorList.jsx
    │   └── part2/
    │       ├── Buyer.jsx
    │       └── Seller.jsx
    │       ├── ProductList.jsx
    └── vite.config.js
    ```

    **Key Files:**

    1. `index.html`: The entry point of the application. It includes meta tags for responsiveness and links to the main JavaScript file.

    ```html
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Home$crapper</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="/src/main.jsx"></script>
    </body>
    </html>
    ```

    2. `main.jsx`: Initializes the React application and renders it into the DOM, using `Auth0Provider`, `RecoilRoot`, and `StrictMode` for enhanced setup.

    ```javascript
    import { StrictMode } from 'react';
    import { createRoot } from 'react-dom/client';
    import { Auth0Provider } from '@auth0/auth0-react';
    import './index.css';
    import App from './App.jsx';
    import { RecoilRoot } from 'recoil';

    createRoot(document.getElementById('root')).render(
        <Auth0Provider
            domain="dev-ob2zgf2rb2cj4emu.us.auth0.com"
            clientId="PKriUy3BJCzcEQzBVZGG0dKjlCaXEyEs"
            authorizationParams={{
                redirect_uri: window.location.origin,
            }}
        >
            <StrictMode>
                <RecoilRoot>
                    <App />
                </RecoilRoot>
            </StrictMode>
        </Auth0Provider>
    );
    ```

    3. `App.jsx`: The root component that manages routing and layout.

    4. **Components Directory (`src/components/`)**: Contains reusable components such as `Profile.jsx`, which displays user profile information.

    5. **Pages Directory (`src/pages/`)**: Contains various page components like `Hero`, `Login`, `Logout`, etc., each responsible for rendering specific parts of the application.

    **Styling**

    The application uses **CSS Modules** and **Emotion** for styling:

    - **CSS Modules**: Styles are scoped locally to avoid conflicts between different components.
    - **Emotion**: Provides dynamic styling capabilities based on component props.

    **ESLint Configuration**

    The project uses **ESLint** to maintain code quality. The configuration file (`eslint.config.js`) sets up rules specific to React development:

    ```javascript
    import js from '@eslint/js';
    import globals from 'globals';
    import react from 'eslint-plugin-react';
    import reactHooks from 'eslint-plugin-react-hooks';
    import reactRefresh from 'eslint-plugin-react-refresh';

    export default [
      {
        ignores: ['dist'],
      },
      {
        files: ['/.{js,jsx}'],
        languageOptions: {
          ecmaVersion: 2020,
          globals: globals.browser,
          parserOptions: {
            ecmaVersion: 'latest',
            ecmaFeatures: {
              jsx: true,
            },
            sourceType: 'module',
          },
        },
        settings: {
          react: {
            version: '18.3',
          },
        },
        plugins: {
          react,
          'react-hooks': reactHooks,
          'react-refresh': reactRefresh,
        },
        rules: {
          ...js.configs.recommended.rules,
          ...react.configs.recommended.rules,
          ...react.configs['jsx-runtime'].rules,
          ...reactHooks.configs.recommended.rules,
          'react/jsx-no-target-blank': 'off',
          'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
        },
      },
    ];
    ```

    **Conclusion**

    This documentation provides a comprehensive overview of the frontend design considerations, key features, technological stack, and technical structure of the **Home$crapper** project. By adhering to these guidelines and utilizing modern technologies, the project aims to create an efficient platform for scrapping garbage and facilitating second-hand transactions.
    """)


def backend():
    st.title("🚀 **Backend Documentation**")
    st.write("---")

    st.subheader("🔧 **Design Considerations**")
    st.markdown("""
    The backend of the **Home$crapper** project was developed with several design considerations to ensure robustness, scalability, and security:

    - **Modular Architecture**: Structured in a modular fashion, allowing for easy maintenance and scalability. Each component (controllers, models, routes) is separated to enhance code readability and organization.
    - **Security**: Implementing JWT (JSON Web Tokens) for authentication ensures that user sessions are secure. Additionally, sensitive data is managed through environment variables using dotenv.
    - **Database Connection Management**: Utilizes Mongoose for MongoDB interactions, ensuring efficient database connection handling and schema validation.
    - **Error Handling**: Comprehensive error handling mechanisms are implemented to provide meaningful responses to the client while logging errors for debugging purposes.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The backend of **Home$crapper** includes several essential features:

    - **User Authentication**: Users can register and log in securely, with their credentials stored safely in the database.
    - **Product Management**: Supports CRUD operations for products, allowing sellers to add, update, and delete their listings.
    - **Buyer and Seller Profiles**: Separate models for buyers and sellers enable tailored functionalities according to user roles.
    - **Cloud Storage Integration**: Integration with Cloudinary allows for image uploads and management directly from the application.
    - **Feedback Mechanism**: Users can provide feedback on products, which is processed and stored for future reference.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    The backend of **Home$crapper** employs a modern technological stack:

    - **Node.js**: A JavaScript runtime that allows for server-side scripting.
    - **Express.js**: A web application framework for Node.js that simplifies routing and middleware management.
    - **MongoDB**: A NoSQL database used for storing user and product data.
    - **Mongoose**: An ODM (Object Data Modeling) library for MongoDB that provides schema-based solutions to model application data.
    - **Cloudinary**: A cloud service for image upload and management.
    - **JWT (JSON Web Tokens)**: Used for secure authentication.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    backend
    ├── app.js
    ├── controller/
    │   └── User.js
    ├── db/
    │   └── connectDB.js
    ├── middleware/
    │   └── protectRoute.js
    ├── model/
    │   ├── Buyer.js
    │   ├── Product.js
    │   └── Seller.js
    ├── package-lock.json
    ├── package.json
    ├── Routes/
    │   └── Router.router.js
    └── utils/
        └── helper/
            └── cookies.js
    ```

    **Key Files:**

    1. `app.js`: The main entry point of the application that initializes the server and connects to the database.

    ```javascript
    import express from "express";
    import dotenv from "dotenv";
    import cookieParser from "cookie-parser";
    import connectDB from "./db/connectDB.js";
    import { v2 as cloudinary } from "cloudinary";
    import userRouter from "./Routes/userRouter.js";

    dotenv.config();
    connectDB();

    cloudinary.config({
        cloud_name: process.env.CLOUD_NAME,
        api_key: process.env.CLOUD_API_KEY,
        api_secret: process.env.CLOUD_API_SECRET,
    });

    const app = express();
    app.use(cookieParser());
    app.use(express.json({ limit: "50mb" }));
    app.use(express.urlencoded({ extended: true }));
    app.use("/api/user", userRouter);

    const PORT = process.env.PORT || 3000;
    app.listen(PORT, () => {
        console.log("Server started on port " + PORT);
    });
    ```

    2. `connectDB.js`: Handles the connection to MongoDB.

    ```javascript
    import mongoose from "mongoose";

    const connectDB = async () => {
        try {
            const conn = await mongoose.connect(process.env.MONGODB_URL);
            console.log(`MongoDB connected: ${conn.connection.host}`);
        } catch (error) {
            console.log(`Error: ${error.message}`);
            process.exit(1);
        }
    };

    export default connectDB;
    ```

    3. **Controllers (`controller/User.js`)**: Manages user-related operations such as registration, profile updates, and product management.

    **Updated `Adduser` Controller Code:**

    ```javascript
    const Adduser = async (req, res) => {
        try {
            const { email } = req.body;
            console.log("Working:", req.body);

            if (!email) {
                return res.status(400).json({ message: "All fields are required" });
            }

            const buyer = await Buyer.create({ email });
            const seller = await Seller.create({ email });

            if (buyer && seller) {
                generateTokenAndSetCookie(buyer._id, res);
                generateTokenAndSetCookie(seller._id, res);
            }

            res.status(201).json({ buyer, seller });
        } catch (error) {
            console.log(error);
            res.status(500).json({ message: error.message });
        }
    };
    ```

    4. **Models (`model/`)**:
       - `Buyer.js`: Defines the Buyer schema with fields like name, email, password, etc.
       - `Seller.js`: Defines the Seller schema similar to Buyer but includes additional fields relevant to sellers.
       - `Product.js`: Defines the Product schema including details like name, description, price, image array, etc.

    5. **Middleware (`middleware/protectRoute.js`)**: Protects routes by verifying JWT tokens to ensure that only authenticated users can access certain endpoints.

    **Error Handling**

    The backend implements error handling in various parts of the code. For example, in the `Adduser` controller function provided above, we handle missing fields and log errors.

    **Conclusion**

    This documentation provides a comprehensive overview of the backend design considerations, key features, technological stack, and technical structure of the **Home$crapper** project. By following these guidelines and utilizing modern technologies, the project aims to create a secure and efficient platform for managing scrapping operations and facilitating second-hand transactions.
    """)



def GenAI_and_machine_learning():
    st.title("🧠 **GenAI and Machine learning Documentation**")
    st.write("---")

    st.subheader("🔬 **Design Considerations**")
    st.markdown("""
    The machine learning models in the **Home$crapper** project were developed with the following considerations in mind:

    - **Data Quality and Preprocessing**: Emphasis was placed on ensuring high-quality data input. Feedback text is cleaned and normalized, and images are processed to be compatible with image classification requirements.
    - **Model Selection**: Focus on sentiment classification and image classification for scrap items.
    - **Scalability**: Models are designed to handle increasing amounts of data efficiently, ensuring smooth scaling as user activity grows.
    - **Performance Monitoring**: Continuous monitoring of model performance metrics such as accuracy, precision, and recall helps maintain the effectiveness of these models over time.
    """)

    st.subheader("✨ **Key Features**")
    st.markdown("""
    The **Home$crapper** machine learning components include:

    - **Feedback Sentiment Analysis**: Analyzes user feedback to classify sentiments as positive or negative, helping improve user experience based on insights from customer feedback.
    - **Recommendation System**: Provides personalized product recommendations based on user preferences and historical behavior.
    - **Image Classification for Scrap**: Utilizes Google Generative AI (`google.generativeai`) to classify scrap items based on recyclability and sellability, with location-based guidelines.
    """)

    st.subheader("🛠️ **Technological Stack**")
    st.markdown("""
    - **Python**: Programming language for model development and deployment.
    - **scikit-learn**: For traditional machine learning algorithms used in feedback sentiment analysis.
    - **Pandas/Numpy**: Libraries for data manipulation and preprocessing.
    - **FastAPI**: Serves the machine learning models as RESTful APIs.
    - **google.generativeai**: Utilizes Google’s Gemini model for advanced image classification and content generation, which is crucial for classifying images based on regional recycling guidelines.
    """)

    st.subheader("📄 **Technical Documentation**")
    st.markdown("""
    **Project Structure:**

    ```
    GenAI-X-ML/
    ├── recommendation_model/
    │   ├── execution.py
    │   └── feedback_classify.py
    ├── waste_classification/
    │   ├── waste_info.py
    └── main.py (FastAPI application)
    ```

    ### Components Overview

    1. **Waste Classification Model (`waste_info.py`)**
       - **Purpose**: Classifies images of scrap items as recyclable or non-recyclable and evaluates their sellability based on user location.
       - **Technology**: Uses Google Generative AI’s `gemini-1.5-flash` model from `google.generativeai`.
       - **Example Usage**:
       ```python
       location = LocationService.get_location()
       images = ["iron1.jpg", "cell_phone.webp"]
       classifications = classify_scrap(images, location)
       ```

       - **Code Implementation**:
       ```python
       import google.generativeai as genai
       from PIL import Image
       import geocoder
       from typing import List, Dict

       # Configure the Google Generative AI API
       genai.configure(api_key="YOUR_API_KEY")  # Replace with your API key
       model = genai.GenerativeModel("gemini-1.5-flash")

       class LocationService:
           @staticmethod
           def get_location() -> Dict[str, str]:
               g = geocoder.ip("me")
               if g.ok:
                   return {
                       "city": g.city or "Unknown",
                       "state": g.state or "Unknown",
                       "country": g.country or "India"
                   }
               return {"city": "Mumbai", "state": "Maharashtra", "country": "India"}

       RECYCLING_RULES = { ... }  # Dictionary containing state-specific recycling rules

       def classify_scrap(images: List[str], location: Dict[str, str]):
           classifications = []
           state = location.get("state", "Maharashtra")

           for image_path in images:
               image = Image.open(image_path)
               prompt = f"""
               
               """
               response = model.generate_content([prompt, image])

               classifications.append({
                   "image": image_path,
                   "recyclable": "recyclable" in response.text.lower(),
                   "sellable": "sellable" in response.text.lower(),
                   "recommendation": response.text,
                   "recycling_rules": RECYCLING_RULES.get(state, "No specific rules found.")
               })

           return classifications
       ```

    2. **Feedback Sentiment Analysis Model (`feedback_classify.py`)**
       - **Purpose**: Analyzes user feedback to classify it as positive or negative.
       - **Technology**: Utilizes scikit-learn’s `LogisticRegression` with `TfidfVectorizer`.
       - **Example Usage**:
       ```python
       text_input = "Great service!"
       cleaned_input = clean_text(text_input)
       sentiment = model.predict([cleaned_input])
       sentiment_label = "Positive" if sentiment[0] == 1 else "Negative"
       ```

       - **Code Implementation**:
       ```python
       import joblib
       import re
       from sklearn.pipeline import make_pipeline
       from sklearn.linear_model import LogisticRegression
       from sklearn.feature_extraction.text import TfidfVectorizer

       # Load model
       model = joblib.load("logistic_regression_sentiment_model.pkl")

       def clean_text(text):
           text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
           text = re.sub(r"@\w+", "", text)
           text = re.sub(r"\W", " ", text)
           return text.lower()

       def predict_sentiment(text):
           cleaned_text = clean_text(text)
           prediction = model.predict([cleaned_text])
           return "Positive" if prediction[0] == 1 else "Negative"
       ```

    3. **FastAPI Application (`main.py`)**
       - **Purpose**: Exposes RESTful APIs for sentiment analysis and scrap classification.
       - **Endpoints**:
         - `/analyze-feedback/`: Analyzes feedback sentiment.
         - `/classify-scrap/`: Classifies scrap items based on image URLs and user location.
       - **Example Usage**:
       ```python
       # Analyze Feedback
       POST /analyze-feedback/
       {
           "text": "Amazing app, very helpful!"
       }

       # Classify Scrap
       POST /classify-scrap/
       {
           "image_urls": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"]
       }
       ```

       - **Code Implementation**:
       ```python
       from fastapi import FastAPI, HTTPException
       from typing import List
       import requests
       import google.generativeai as genai
       import joblib
       from PIL import Image
       from io import BytesIO

       # Configure Google Generative AI
       genai.configure(api_key="YOUR_API_KEY")
       model = genai.GenerativeModel("gemini-1.5-flash")

       # Load sentiment model
       sentiment_model = joblib.load("logistic_regression_sentiment_model.pkl")

       app = FastAPI()

       # Feedback Analysis Endpoint
       @app.post("/analyze-feedback/")
       async def analyze_feedback(text: str):
           prediction = sentiment_model.predict([text])[0]
           sentiment = "Positive" if prediction == 1 else "Negative"
           return {"sentiment": sentiment}

       # Scrap Classification Endpoint
       @app.post("/classify-scrap/")
       async def classify_scrap(image_urls: List[str]):
           classifications = []
           for url in image_urls:
               response = requests.get(url)
               image = Image.open(BytesIO(response.content))
               prompt = "Classify this scrap item based on recyclability and sellability."
               ai_response = model.generate_content([prompt, image])

               classifications.append({
                   "url": url,
                   "classification": ai_response.text
               })
           return classifications
       ```

    ### Model Training and Evaluation Details

    - **Feedback Model Training**:
      - **Dataset**: Twitter Sentiment dataset (pre-processed for positive and negative feedback).
      - **Algorithm**: Logistic Regression with TF-IDF vectorization.
      - **Metrics**: Accuracy, Precision, Recall.

    - **Scrap Image Classification**:
      - **Data Source**: User-uploaded images of scrap items.
      - **Generative AI Integration**: Generates a location-based response with recycling and resale recommendations.
      - **Output**: Recyclable/Non-Recyclable, Sellable/Non-Sellable, and recommendations based on state guidelines.

    ### Conclusion

    This documentation provides a comprehensive overview of the machine learning models and APIs integrated into the **Home$crapper** project. By leveraging machine learning and location-based recycling guidelines, the project provides valuable insights and personalized experiences for users engaged in recycling and sustainable practices.
    """)



def main():
    # Sidebar Navigation
    st.sidebar.title("🔎 **Explore Home$crapper**")
    pages = {
        "Home": home,
        "Frontend": frontend,
        "Backend": backend,
        "GenAI and Machine learning": GenAI_and_machine_learning,
        # "Investor Pitch": investor_pitch,
        # Include other pages if necessary
    }
    selected_page = st.sidebar.selectbox("Navigate to:", options=list(pages.keys()))
    st.sidebar.write("---")
    st.sidebar.write("©️ 2023 Home$crapper")

    # Display the selected page with some padding
    st.markdown(
        """
        <style>
        .reportview-container .main .block-container{
            padding-top: 1rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    pages[selected_page]()

if __name__ == "__main__":
    main()