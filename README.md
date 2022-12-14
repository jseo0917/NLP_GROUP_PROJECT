# Dialog Summarization for Customer Service via Chat

Team members: Nahyun Kwon, Ali Furkan Budak, Jung Hoon Seo, Sahithi Ravipati, Nathan McClaran

Dialog summarization is a popular NLP topic. Especially for customer service, agents are often asked to quickly summarize the dialog for the customer at the end of the conversation. The summary should contain the key information including the problem, the solution suggested, and the specific requests from the customer if any. However, in many cases, agents take care of many requests within a short time and are required to provide the summary quickly to minimize the waiting time of the customer. Having the conversation record as input and by building the model structure that can effectively extract the key information from the dialogs, we aim to support the agents in a customer chat service by providing automated summarization in real time.

## Datasets 
A Dialog Summarization Dataset for Customer Service (TweetSum)

<img src=https://i.imgur.com/nTv3Iuu.png width="650" height="400">

3 JSON Files from https://github.com/guyfe/Tweetsumm/tree/main/tweet_sum_data_files

## Baseline models 
Bart-large-Samsum, Cnn-12-6-samsum

## Evaluation Metrics
Rouge 1 and 2

## Results
### Bart-large-Samsum

<img src=https://raw.githubusercontent.com/jseo0917/imageFiles/main/Screen%20Shot%202022-11-30%20at%207.24.32%20PM.png width="600" height="300">

Rouge1 F1 Score: 0.4732<br>
Rouge2 F1 Score: 0.2259

### Cnn-12-6-Samsum

<img src=https://raw.githubusercontent.com/jseo0917/imageFiles/main/Screen%20Shot%202022-11-30%20at%206.00.13%20PM.png width="600" height="300">

Rouge1 F1 Score: 0.4684<br>
Rouge2 F1 Score: 0.2176
## How to run ipynb file

Summerize.ipynb contains the best result. 

1. Download twcs.csv file from https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter and put the file to your Google Drive
2. Download JSON files from https://github.com/guyfe/Tweetsumm/tree/main/tweet_sum_data_files and upload the files to Google Drive/content
3. Run the [summerize.ipynb](summerize.ipynb) on Google Colab using GPU

[Fine-tuned bart model](https://drive.google.com/file/d/1KziQecxDwfr07QEXGngdJMvQqkP5RYZT/view?usp=sharing)


Reference: https://github.com/guyfe/Tweetsumm
