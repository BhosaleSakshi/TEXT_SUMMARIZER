
# spaCy, a free and open-source library with a lot of built-in capabilities for processing and analyzing data in the field of NLP.
# Installation of spaCy
import spacy 
import pathlib

def summary(choice,text,percentage1):
  print("hey")
  print(type(percentage1))
  print(text)
  print(choice)
  #percentage = float(percentage1)
  # The default model for the English language is en_core_web_sm
  # verify that models and data were successfully downloaded
  

  nlp=spacy.load('en_core_web_sm')

  # spaCy stores a list of stop words for the English language
  from spacy.lang.en.stop_words import STOP_WORDS
  from string import punctuation 
  stopwords = list(STOP_WORDS)

  punctuation=punctuation+'\n';
  punctuation=punctuation+'"';
  punctuation=punctuation+'—';
  punctuation=punctuation+'-';  
  punctuation=punctuation+'‘';
  punctuation=punctuation+'’';

  # Initiating A Doc object - is a sequence of Token objects representing a lexical token.
  doc=nlp(text)

  if choice == 3 :
    fileObj = pathlib.Path(text).read_text(encoding="utf-8")
    doc = nlp(fileObj)

  # Word Tokenization
  # Removing stopwords and punctuations
  # Then creating list of root words of all words
  print("sum")
  word_Tokens=[]
  for word in doc:
    if word.text.lower() not in stopwords:
      if word.text.lower() not in punctuation:
        w = (word.lemma_)
        word_Tokens.append(w.lower())



  # Calculating word frequency or count
  word_frequencies = {}
  for word in word_Tokens:
    if word.lower() not in word_frequencies.keys():
      word_frequencies[word.lower()]=1
    else:
      word_frequencies[word.lower()]+=1


  # Highest word frequency or count
  max_freq = max(word_frequencies.values())


  # Top Words 
  from collections import Counter 
  top_words = dict(Counter(word_frequencies).most_common(7))
  cnt = 0 
  for word in top_words:
    cnt+=1
    print(cnt,":",word)

  # Normalize frequency
  for word in word_frequencies.keys():
    word_frequencies[word]=word_frequencies[word]/max_freq

  # Sentence Tokenization from given text
  sentence_tokens = [sent for sent in doc.sents]
  print(sentence_tokens)


  # Calculating Sentence Score = addition of word_score of words in particular sentence
  sentence_scores ={}
  for sent in sentence_tokens:
    for word in sent:
      if word.text.lower() in word_frequencies.keys():
        if sent not in sentence_scores.keys():
          sentence_scores[sent] = word_frequencies[word.text.lower()]
        else:
          sentence_scores[sent] += word_frequencies[word.text.lower()]
  print("sentence ",sent,"  \nscore : ",sentence_scores[sent],"")
  # Length Of Summary
  # Number of sentences in summary w.r.t original text
  # Here 30% of original text
  select_length = int(len(sentence_tokens)*percentage1*0.01)
  if select_length < 1 :
    select_length=1;


  # Extracting top sentences 
  from heapq import nlargest
  top_sents = nlargest(select_length, sentence_scores,key = sentence_scores.get)
  cnt=0
  for sent in top_sents:
    cnt+=1
    print(cnt,":",sent,)

  # Summarize sentences according to order in given text for coherence or context flow: 
  summary=[]
  for sent in sentence_tokens:
    if sent in top_sents:
      summary.append(sent)

  # Creating Summary paragraph of list of top sentences in order
  final_words = [word.text for word in summary]
  final_summary = ' '.join(final_words)
  print("\nExtractive Summary of News Article\n")
  print("\n\n",final_summary,"\n\n")
  return final_summary


# text = """The inaugural edition of the Women’s Premier League is set to be played in Mumbai from 4th – 26th March, 2023. A total of 22 matches will be played with the Brabourne Stadium & D.Y. Patil Stadium playing hosts to the marquee tournament. The Women’s Premier League Player Auction list is out with a total of 409 cricketers set to go under the hammer at the Jio World Convention Centre in Mumbai on February 13th, 2023. A total of 1525 players registered for the inaugural Women’s Premier League Player Auction & the final list was pruned to 409 players.  Out of 409 players, 246 are Indians and 163 are overseas players of which 8 players are from associate nations. The total capped players are 202, uncapped players are 199 and 8 from associate nations. A maximum of 90 slots are available with the five teams, with 30 being slotted for overseas players. INR 50 Lakhs is the highest reserve price with 24 players choosing to be slotted in the highest bracket. Team India Captain Harmanpret Kaur, Smriti Mandhana, Deepti Sharma and India’s Under-19 T20 World Cup-winning captain Shafali Verma are amongst the few Indians who have slotted themselves in the highest bracket. 13 overseas players have also slotted themselves under the INR 50 Lakh reserve price with the likes of Ellyse Perry, Sophie Ecclestone, Sophie Devine & Deandra Dottin to name a few. 30 players are in the auction list with a base price of INR 40 Lakh. The Auction will start at 14:30 IST."""
# summary(text,20)