# MINDS-Center-Programming-Assesment
Programming exercise is to demonstrate my ability to design a solution to a problem and implement this solution in Python using software engineering best practices.

### I have included both the python notebook and a python script in the project. 
Both files do essentially the same task. The notebook might be useful to glance at the results and analysis without running the entire script because the input file isn't small.


## Instructions for Running the Code

### Installing required packages
Run the following command

pip install -r requirements.txt

If your plotly package is missing orca, install plotly-orca using the following command

conda install -c plotly plotly-orca


### Running the Python Notebook
Note:  Make sure that the result.json file is in the same directory as the python notebook
Run all cells

### Running the Python Script
1. If the input file has the name result.json and is in the current directory 

    python sentiment_analysis.py 
    
2. If you want to specify the path to the json file

    python sentiment_analysis.py --inputfile result.json
    
    
### Results

The Results can be seen in the following files

Interactive Versions:
1.  Average Daily Sentiments Barplot.html
2.  Average Daily Sentiments Scatter Plot.html
3.  Daily Sentiments Grouped Barplot.html

Static Versions:

1.  Average Daily Sentiments Barplot.png 

![alt text](https://github.com/AniruddhaKalkar/MINDS-Center-Programming-Assesment/blob/main/Average%20Daily%20Sentiments%20Barplot.png?raw=true)


2.  Average Daily Sentiments Scatter Plot.png
  
![alt text](https://github.com/AniruddhaKalkar/MINDS-Center-Programming-Assesment/blob/main/Average%20Daily%20Sentiments%20Scatterplot.png?raw=true)


3. Daily Sentiments Grouped Barplot.png 
 
![alt text](https://github.com/AniruddhaKalkar/MINDS-Center-Programming-Assesment/blob/main/Daily%20Sentiments%20Grouped%20Barplot.png?raw=true)


### Insights

We see that 
1. On most days the Sentiment in the messages is mostly positive.
2. In the "Daily Sentiments Grouped Bar plot" we can clearly see that the ratio of positive messages to negative messages is higher on May 4th and 5th. Moreover, because the number of neutral comments is lower on May 5th , the average sentiment has the most positive polarity.
3. We can see this in the Average Daily Sentiments Barplot where May 5th has the highest average polarity.


 
