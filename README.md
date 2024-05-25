
# MovieTVShowRecommender

## Overview
This repository contains a movie and TV show recommendation system built using a dataset of Netflix titles from Kaggle. The project includes data preprocessing, exploratory data analysis (EDA), and a content-based recommendation algorithm to provide personalized suggestions.

## Dataset
The dataset `netflix_titles.csv` includes details about Netflix movies and TV shows, such as title, director, cast, country, date added, release year, rating, and duration.

## Features
- Data Preprocessing: Cleaning and preparing the data for analysis.
- Exploratory Data Analysis: Gaining insights and visualizing the data.
- Content-Based Recommendation: Implementing content-based filtering using metadata and cosine similarity.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/trnabab/Movie-TV-Show-Recommender.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Movie-TV-Show-Recommender
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Data Preprocessing
1. Load and preprocess the data:
   ```bash
   python data_preprocessing.py
   ```

### Exploratory Data Analysis
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook eda.ipynb
   ```
2. Run the notebook to generate summary statistics and visualizations.

### Content-Based Recommendation
1. Run the recommender system:
   ```bash
   python recommender_system.py
   ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The dataset is provided by [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows).

## Contact
If you have any questions, feel free to open an issue or contact me at tajkinur.rahman@outlook.com

