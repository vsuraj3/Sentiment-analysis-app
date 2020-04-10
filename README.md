# Sentiment-analysis-app
Sentiment Analysis is a natural language processing task which helps to identify and categorize opinions expressed in a piece of text as positive, negative or neutral.  It helps to determine the reviewer’s point of view on a particular topic. It combines the techniques of computational linguistics and Information Retrieval (IR). The increasing user-generated content on the Internet is the motivation behind the sentiment analysis app. 

This app performs text sentiment analysis in two languages, Hindi and English

Text sentiment analysis in hindi is done by performing the Resource based classification using HindiSentiWordNet(H-SWN). Each word present in the H-SWN has a positive and a negative sentiment score. Based on the maximum of the scores, a polarity is assigned to each word in a text. The polarity which covers the maximum number of words in a text is predicted as the sentiment of that text. 

TextBlob is a Python (2 and 3) library for processing textual data. The sentiment function of textblob returns two properties, polarity, and subjectivity. Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. 
