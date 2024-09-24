# Topic-Modeling-Honkai-Star-Rail 

### In this project, the objective is to analyze player feedback on Honkai Impact Star Rail by applying LDA, NMF, top2Vec, and bertopic modeling techniques. The analysis focuses on extracting key themes from player reviews, particularly highlighting both complaints and appreciations. To achieve a more nuanced understanding, the reviews have been divided into positive and negative categories, enabling a detailed exploration of the aspects players either criticized or valued. 

### 1) The project starts with scraping reviews from google play store by serpapi which is a useful API to scrape text from google platforms [Link](https://github.com/JunJul/Sentiment-Analysis-Honkai-Star-Rail/blob/Master/web_srcaping.py).

### 2) LDA and NMF model from scikit-Learn [Link](https://github.com/JunJul/Sentiment-Analysis-Honkai-Star-Rail/blob/Master/DLA%20and%20NMF.ipynb)

### 3) Top2Vec [Link](https://github.com/JunJul/Sentiment-Analysis-Honkai-Star-Rail/blob/Master/Top2Vec.ipynb)

### 4) BERTopic [Link](https://github.com/JunJul/Topic-Modeling-Honkai-Star-Rail/blob/Master/BERTopic.ipynb)

### Conclusion: By applying LDA, NMF, and Top2Vec models, distinct themes were identified in the Honkai Impact Star Rail player reviews. Players commonly complained about the game's difficulty, login issues, and mandatory story segments. On the other hand, they expressed appreciation for the detailed character development and scene design. Addintionally, BERTopic uncovers extra insights: some players have requested the inclusion of a controller system, allowing gameplay with controllers. A further development would involve integrating BERTopic with Llama2 to create a more robust sentiment analysis pipeline. This would help identify negative sentiment in player reviews and then feed those negative reviews into the topic model to uncover specific complaints. By doing so, the insights would be more granular, focusing on areas of dissatisfaction among players. To enhance the analysis, it would be beneficial to expand the data set beyond Google Play reviews, incorporating feedback from other gaming platforms for a more comprehensive understanding of player sentiment.
