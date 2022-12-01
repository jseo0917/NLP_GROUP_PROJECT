# NLP_GROUP_PROJECT

Team members: Nahyun Kwon, Ali Furkan Budak, Jung Hoon Seo, Sahithi Ravipati, Nathan McClaran

Dialog summarization is a popular NLP topic. Especially for customer service, agents are often asked to quickly summarize the dialog for the customer at the end of the conversation. The summary should contain the key information including the problem, the solution suggested, and the specific requests from the customer if any. However, in many cases, agents take care of many requests within a short time and are required to provide the summary quickly to minimize the waiting time of the customer. Having the conversation record as input and by building the model structure that can effectively extract the key information from the dialogs, we aim to support the agents in a customer chat service by providing automated summarization in real time.

## Datasets 
A Dialog Summarization Dataset for Customer Service (TweetSum)

![alt text](https://i.imgur.com/nTv3Iuu.png)

3 JSON Files from https://github.com/guyfe/Tweetsumm/tree/main/tweet_sum_data_files

## Baseline models 
Bart-large-Samsum, Cnn-12-6-samsum

## Evaluation Metrics
Rouge 1 and 2

## Results
1[alt text](https://github.com/jseo0917/imageFiles/blob/main/Screen%20Shot%202022-11-30%20at%206.00.13%20PM.png?raw=true)


## How to run ipynb file

Summerize.ipynb contains the best result. 

1. Download twcs.csv file from https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter and put the file to your Google Drive
2. Download JSON files from https://github.com/guyfe/Tweetsumm/tree/main/tweet_sum_data_files and upload the files to Google Drive/content
3. Run the summerize.ipynb on Google Colab using GPU

Reference: https://github.com/guyfe/Tweetsumm
