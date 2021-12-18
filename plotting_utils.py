import pandas as pd
import plotly.express as px

from sentiment_analysis_utils import get_polarity, get_analysis



def create_plotting_daily_data(processed_dataframe):
    '''
    create_plotting_daily_data
    Create a dataframe with counts of each type of sentiment for each date
    '''
    plotting_data = []
    for date in processed_dataframe['date'].unique():
        date_dataframe = processed_dataframe.loc[processed_dataframe['date'] == date]
        negative_count = len(date_dataframe.loc[date_dataframe['sentiment'] == 'Negative'])
        neutral_count = len(date_dataframe.loc[date_dataframe['sentiment'] == 'Neutral'])
        positive_count = len(date_dataframe.loc[date_dataframe['sentiment'] == 'Positive'])
        plotting_data.append([date,'Negative',negative_count])
        plotting_data.append([date,'Neutral',neutral_count])
        plotting_data.append([date,'Positive',positive_count])
    
    plotting_dataframe = pd.DataFrame(plotting_data,columns = ['date', 'sentiment', 'count'])
    return plotting_dataframe



def create_plotting_averages_data(processed_dataframe):
    '''
    create_plotting_averages_data
    Create a dataframe with average sentiment and average polarity for each date

    Required for the coding Assessment
    '''
    plotting_data = []
    for date in processed_dataframe['date'].unique():
        date_dataframe = processed_dataframe.loc[processed_dataframe['date'] == date]
        avg_polarity = date_dataframe['message_polarity'].mean()
        avg_sentiment = get_analysis(avg_polarity)
        plotting_data.append([date,avg_polarity,avg_sentiment])
    
    plotting_dataframe = pd.DataFrame(plotting_data,columns = ['date', 'average_polarity', 'average_sentiment'])
    return plotting_dataframe


def generate_grouped_barplot(dataframe, 
                            x_col, 
                            y_col, 
                            color_col, 
                            barmode, 
                            file_name):
    '''
    generate_grouped_barplot
    Generates a Bar plot for Visualization 
    Saves it to specified location
    '''
    fig = px.bar(dataframe,
                x= x_col,
                y= y_col,
                color = color_col,
                barmode = barmode)
    fig.write_html(file_name)


def generate_barplot(dataframe, 
                    x_col, 
                    y_col, 
                    color_col, 
                    file_name):
    '''
    generate_barplot
    Generates a Bar plot for Visualization 
    Saves it to specified location
    '''
    fig = px.bar(dataframe,
                x= x_col,
                y= y_col,
                color = color_col)
    fig.write_html(file_name)

def generate_scatterplot(dataframe, 
                    x_col, 
                    y_col, 
                    color_col, 
                    file_name):
    '''
    generate_scatterplot
    Generates a Scatter plot for Visualization 
    Saves it to specified location
    '''
    fig = px.scatter(dataframe,
                    x= x_col,
                    y= y_col,
                    color = color_col,
                    symbol=color_col)

    fig.update_traces(marker_size=10)
    fig.write_html(file_name)


