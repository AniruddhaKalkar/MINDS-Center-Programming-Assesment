'''
Importing Necessary Packages for Coding Assesment
We will be using

NLTK package for basic NLP tasks like:

 a. Dictionary of English words
 b. Sentence tokenization
tqdm for tracking progress and visualization

TextBlob for calculating message polarity and sentiment scoring

json to load the input file

Pandas to manipulate data while perfroming sentiment analysis

Plotly to Visualize the results of the sentiment analysis
'''

import argparse
import nltk
from tqdm import tqdm
import pandas as pd



from utils import read_json_data

from preprocessing_utils import is_english, has_important_words, is_valid_date

from sentiment_analysis_utils import get_polarity, get_analysis

from plotting_utils import create_plotting_daily_data, create_plotting_averages_data
from plotting_utils import generate_barplot, generate_scatterplot, generate_grouped_barplot

'''
Download the words corpus from ntlk.

Important for macOS as it might not automatically download the corpus after installation of the nltk package
'''
nltk.download('words')



def pre_process(message,
				english_words,
				important_words):
	'''
	pre_process :
	to prepocess each of the messages, i.e:

	Check if the message text is in english language
	Check if the message has at least one of the important words
	Return the message content if both the conditions are satisfied
	Arguments:

	message

	 type: string 
	 The message to be checked  

	english_words:

	 type: list 
	 The words allowed in english language

	important_words:

	 type : list 
	 The words important in the given context
	'''
	processed_message = ""
	if len(message) == 0:
		return processed_message
	is_message_english = is_english(message, english_words, important_words)
	has_valid_words_in_message = has_important_words(message, important_words)
	if is_message_english and has_valid_words_in_message:
		processed_message = message
	return processed_message



def create_dataset(raw_data,
					english_words,
					important_words):
	
	'''
	create_dataset :
	to prepocess all the messages and create a dataset, i.e:

	Check if the message date is in valid range.
	Preprocess each message
	Add valid to the Dataframe
	Return the Dataframe
	Arguments:

	message

	 type: string 
	 The message to be checked  

	english_words:

	 type: list 
	 The words allowed in english language

	important_words:

	 type : list 
	 The words important in the given context
	'''
	prepared_dataset_list = []
	for i in tqdm(range(len(raw_data))):
		raw_datum = raw_data[int(i)]
		date = raw_datum['date'].split('T')[0]
		message = ""
		if is_valid_date(date):
		
			if 'text' in raw_datum.keys():
				message = raw_datum['text']
			if type(message) == str:
				processed_message = pre_process(message,
									  english_words,
									  important_words)

				if len(processed_message) !=0 :
					data_point = [processed_message, date]
					prepared_dataset_list.append(data_point)
	
	prepared_dataset_dataframe = pd.DataFrame(prepared_dataset_list, columns = ['message', 'date'])
	return prepared_dataset_dataframe

def main(args):

	input_file = 'result.json'
	if(args.inputfile != None):
		input_file = args.inputfile
	'''
	Declare The lists required for the Preprocessing
	english_words = using nltk
	important_words = given in the problem statement
	'''
	english_words = list(set(nltk.corpus.words.words()))
	important_words = ['SHIB','DOGE']

	# Read the input file

	raw_data = read_json_data(input_file)


	'''
	Create the Dataframe object
	Displaying the first 5 elements in the dataframe
	'''
	prepared_dataset_dataframe = create_dataset(raw_data['messages'],
												english_words,
												important_words)

	# calculate polarity of each message
	prepared_dataset_dataframe['message_polarity'] = prepared_dataset_dataframe['message'].apply(get_polarity)


	# calculate sentiment of each message
	prepared_dataset_dataframe['sentiment'] = prepared_dataset_dataframe['message_polarity'].apply(get_analysis)


	# Drop unnecessary columns
	processed_daily_dataframe = prepared_dataset_dataframe.drop(['message_polarity'], axis = 1)

	processed_averages_dataframe = prepared_dataset_dataframe.drop(['message', 'sentiment'], axis = 1)


	# Create appropriate Dataframe with counts of each sentiment
	plotting_daily_dataframe = create_plotting_daily_data(processed_daily_dataframe)

	# Create appropriate Dataframe with average sentiment of each day
	plotting_averages_dataframe = create_plotting_averages_data(processed_averages_dataframe)


	# Generate interactive plots and save
	generate_grouped_barplot(plotting_daily_dataframe, 'date', 'count', 'sentiment', 'group','html', 'Daily Sentiments Grouped Barplot.html')

	generate_barplot(plotting_averages_dataframe, 'date', 'average_polarity', 'average_sentiment','html' ,'Average Daily Sentiments Barplot.html')

	generate_scatterplot(plotting_averages_dataframe, 'date', 'average_polarity', 'average_sentiment','html' , 'Average Daily Sentiments Scatterplot.html')

	# Generate static plots and save
	generate_grouped_barplot(plotting_daily_dataframe, 'date', 'count', 'sentiment', 'group','png', 'Daily Sentiments Grouped Barplot.png')

	generate_barplot(plotting_averages_dataframe, 'date', 'average_polarity', 'average_sentiment','png' ,'Average Daily Sentiments Barplot.png')

	generate_scatterplot(plotting_averages_dataframe, 'date', 'average_polarity', 'average_sentiment','png'  ,'Average Daily Sentiments Scatterplot.png')




if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--inputfile',
						required=False, 
						help='Location of input file. Format allowed: JSON', 
						type = str)
	args = parser.parse_args()
	main(args)





