# Similar-Questions
This is Machine Learning based project to determine whether two given questions are duplicate or not.

# Indtroduction
This project focuses on the problem of determining whether two questions are duplicates or not. The project utilizes machine learning techniques and natural language processing (NLP) to build a model that can accurately classify duplicate questions.

# Workflow
The project begins by preprocessing the data, which involves cleaning the text by converting it to lowercase, removing special characters, and decontracting words. Stop words are also eliminated to retain only relevant words.

Next, various features are engineered from the preprocessed data. These features include common word count, total word count, token-based features, length-based features, and fuzzy matching scores. These features provide valuable insights into the similarity between pairs of questions.

Machine learning models, such as Random Forest and XGBoost classifiers, are trained using the engineered features. The models are evaluated based on accuracy score to assess their performance in identifying duplicate questions.

The project aims to provide an effective solution for identifying duplicate questions, which can be valuable in applications such as question answering systems, information retrieval, and content moderation.
