# The Taxonomy of Terror
An NLP-centered project for capstone 2 of the Galvanize Data Science Intensive.<br><br>
## Rationale:


I used a supervised approach to text classification among three authors.<br><br>
The dataset I used came from a 2017 Kaggle competition using individual lines of text as predictors of the author. <br> The target would be the author and the goal is to train a model that can identify the author of an unseen piece of text, out of three authors whose work is included in the corpus. 
The three authors represented are: Edgar Allan Poe, H.P. Lovecraft, and Mary Wollstonecraft Shelley. 
<br><br>
## Exploratory Data Analysis:<br>
![Line Distribution](/images/lines_by_author.png)
<br><br>

## Most commonly used words for each author:
![Poe Words](/images/poe_words.png)
![Lovecraft Words](/images/lovecraft_words.png)
![Shelley Words](/images/shelley_words.png)
<br><br>
Author | Vocabulary Size
------------ | -------------
Edgar Allan Poe | 15,261
H.P. Lovecraft | 14, 504
Mary Shelley | 11,515
<br><br>

I also applied NLTK's Sentiment Intensity Analyzer on each line for each author's work. The following table shows those sentiments averaged by author: <br><br>
Author | Negative | Neutral | Positive | Compound
------------ | ------------- | ------------- | ------------- | ------------- 
Edgar Allan Poe | .07 | .84 | .09 | .04
H.P. Lovecraft | .09 | .84 | .07 | -.06
Mary Shelley | .10 | .77 | .13 | .06

<br>

## Model

The model I used to classify the texts was Multinomial Naive Bayes. When tested, the following accuracy scores and predictive features were noted. 

Author Classifiers | Accuracy | Predictive Feature Samples
------ | ----------| --------
Poe/Lovecraft/Shelley | 81% | Aberrant, abhor, little, good, great, time, eye, think, far, word, mean, look
Poe/Lovecraft | 88% | Abandonment, abdication, man, old, house, say, night, know, night, dream, day, look
Poe/Shelley | 83% | Love, life, man, eye, heart, time, father, hope, little, friend, death, think

<br>
I chose to keep what I saw as "victorian stop-words" because they seemed to be highly predictive for each author. Therefore, I am curious as to wheter that decision may have led to an overfit model or if it's a good application in a purpose-built model for classifying authors by their syntactic signatures. 
<br><br>

![Word2Vec Similarities](/images/wordvecs.png)

<br><br>
Notes: Each of these writers makes some unusual stylistic and vocabulary choices. I wondered if those are easily spotted in machine learning. In the story "X-ing a Paragrab" there is a letter wherein all of the "o"s in the text are replaced with x. So, there is a line for example that reads: "Gxxd Lxrd, Jxhn, hxw yxu dx lxxk!" and goes on to write "X-cellent" in place of excellent and "X-entric" in place of eccentric.  
<br>

## Next Steps
- Explore AI text generation and chatbots
- Explore ways models might “reward” words from the taxonomy of terror in classifying within the genre
- Incorporate more authors and time-periods in the corpus


## References 
Benzahra, Marc. 2019. “How to Evaluate Text Readability with NLP.” Medium. https://medium.com/glose-team/how-to-evaluate-text-readability-with-nlp-9c04bd3f46a2 (March 24, 2021). <br><br>

Dare, Eleanor. 2021. “Rear Psycho: Hitchcock’s Horror Language Mediated by AI.” Leonardo Electronic Almanac 23(1). https://www.leoalmanac.org/rear-psycho-hitchcocks-horror-language-mediated-by-ai-eleanor-dare/ (March 29, 2021).<br><br>


Pearl, Mike. “Behold the Incredible Horror Stories an AI Will Write If You Let It.” The Outline. https://theoutline.com/post/8302/ai-incredible-horror-stories (March 29, 2021). <br><br>

Rahwan, Iyad. “Can AI Learn to Scare Us? With Shelley, MIT Researchers Aim for Goosebumps.” MIT Media Lab. https://www.media.mit.edu/posts/can-ai-learn-to-scare-us-with-shelley-mit-researchers-aim-for-goosebumps/ (March 29, 2021). <br><br>

“Spooky Author Identification.” https://kaggle.com/c/spooky-author-identification (April 1, 2021). <br><br>

Steger, Sara. 2013. “Patterns of Sentimentality in Victorian Novels.” Digital Studies/Le champ numérique 3(2). http://www.digitalstudies.org/articles/10.16995/dscn.235/print/ (April 1, 2021). <br><br>

Zimmer, Ben. 2011. “The Jargon of the Novel, Computed.” The New York Times. https://www.nytimes.com/2011/07/31/books/review/the-mechanic-muse-the-jargon-of-the-novel-computed.html (April 1, 2021).
