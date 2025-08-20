# 🎬 Movie Recommendation System (Python + ML)

![Python](https://img.shields.io/badge/Language-Python-blue)
![ML](https://img.shields.io/badge/Domain-Machine_Learning-green)
![Pandas](https://img.shields.io/badge/Library-Pandas-yellow)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)  
It suggests movies to users based on similarity scores calculated from movie features such as **genres, keywords, cast, and crew**.

---

## 🚀 Features
- 📊 Data preprocessing and cleaning of raw dataset.  
- 🧮 Content-based filtering using **cosine similarity**.  
- 🎥 Movie recommendations with titles and posters.  
- 🌐 Interactive **Streamlit web app** for easy use.  

---

## 📂 Project Structure

Movies-Recommend-System/
│
├── app.py # Streamlit app file
├── model.py # Core recommendation logic
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── data/
│ ├── movies.csv # Movies dataset
│ └── credits.csv # Credits dataset
└── notebooks/
└── Movie_Recommender.ipynb # Jupyter notebook (exploration + preprocessing)


---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Pickle** (for saving the model)

---

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/monish1716/Movies-Recommend-System.git
   cd Movies-Recommend-System

2. Download similarity.pkl:
   Download the similarity.pkl file from google drive and add it to the project folder
   
4. Install dependencies:

pip install -r requirements.txt

3. Run the Streamlit app:

streamlit run app.py

📊 Dataset

The project uses the TMDB 5000 Movies Dataset, which contains:
Movie titles
Cast & crew details
Genres
Keywords
You can download it from Kaggle
.

🎯 How It Works

Extract important features from the dataset (genres, cast, crew, keywords).
Apply preprocessing (remove duplicates, handle nulls, clean text).
Convert text data into vectors using CountVectorizer.
Compute cosine similarity between movies.
Recommend top 5 similar movies for any input.

🌐 Demo

After running the Streamlit app:
Enter a movie title in the input box.
Get top 5 recommended movies with posters.

📌 Example

![Alt Text](images/mrs.png)


🔮 Future Improvements
Add hybrid recommendation system (content + collaborative).
Deploy on Streamlit Cloud / Heroku.
Improve UI with movie posters & ratings.

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.

📜 License

This project is licensed under the MIT License.
