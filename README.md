# Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit. Enter your favorite movie and get smart recommendations instantly.

🚀 Features
-Movie recommendations based on cosine similarity
-Interactive web app using Streamlit
-Clean UI with custom CSS
-Dataset includes thousands of movies

🛠️ Tech Stack
-Python
-Streamlit
-Pandas / NumPy
-Scikit-learn (cosine similarity)
-Pickle (for saving similarity matrix)

📂 Project Structure
├── app.py              # Main Streamlit app  
├── movies.pkl          # Preprocessed movies dataset  
├── similarity.pkl      # Similarity matrix  
├── style.css           # Custom styles  
└── README.md           # Project documentation

⚡ How to Run Locally

-Clone the repository

git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system


-Install dependencies

pip install -r requirements.txt


-Run the app

streamlit run app.py


🌟 Learnings

Handling large datasets and pickle files

Debugging Streamlit deployment issues

Integrating custom CSS for better UI

🔗 Links

Live Demo: https://movie-recommender-system-ercfmcyk3azqr8trezndrn.streamlit.app/
