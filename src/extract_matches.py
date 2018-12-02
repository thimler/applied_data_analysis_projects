# Imports
import re
import nltk
import json
import folium
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#stop words
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

#spark
import findspark
findspark.init('/opt/spark/spark-2.3.2-bin-hadoop2.7/')

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import min
from pyspark.sql.functions import udf
from pyspark.sql.functions import split
from pyspark.sql.functions import explode

from pyspark.sql.types import StringType
from pyspark.sql.types import TimestampType

from pyspark.sql import SparkSession
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()

# Addition of english stop words

def init_stopwords():
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    stop_words.add('&')
    stop_words.add('co')
    stop_words.add('co.')
    stop_words.add('co.,')
    stop_words.add('co.,ltd.')
    stop_words.add('corp')
    stop_words.add('corp.')
    stop_words.add('corp.,')
    stop_words.add('de')
    stop_words.add('foundation')
    stop_words.add('inc')
    stop_words.add('inc.')
    stop_words.add('limited')
    stop_words.add('international')
    stop_words.add('ltd')
    stop_words.add('ltd.')
    stop_words.add('s.a.')
    stop_words.add('world')
    stop_words.add('global')

    stop_words = list(stop_words)
    return stop_words


def check_for_words(charity, shell, stop_words, tuning):
    
    percentage = 0.6
    
    if charity is None or shell is None:
        return False
    
    charity_words = [x.lower() for x in charity.split()]
    shell_words = [x.lower() for x in shell.split()]
    len_charity = len(charity_words)
    len_shell = len(shell_words)
    
    count_random_matches = 0
    stop_word_random_matches = 0
    
    for i in range(len_charity):
        word = charity_words[i]
        if word in shell_words:
            count_random_matches += 1
            
            if word in stop_words:
                stop_word_random_matches += 1
                
    if tuning:
        #if only stopwords match, not valid
        if count_random_matches - stop_word_random_matches < 1:
            return False

        #"Family foundations are tricky -> make sure they are not the only matching parts"
        if ('family' in shell_words 
            and 'foundation' in shell_words 
            and 'family' in charity_words 
            and 'foundation' in charity_words 
            and count_random_matches < 3 
            and len_shell > 2 
            and len_charity > 2):
            return False

    if len_charity == 1 or len_shell == 1:
        return (np.abs(len_charity - len_shell) < 2  and count_random_matches == 1)
        
    return ((count_random_matches/len_charity >= percentage) 
            and (count_random_matches/len_shell >= percentage))

def extract_matches_between(leak, charity, sharp):
    
    stop_words = init_stopwords()
    
    charity_location = '../generated/' + charity + '/' + charity + '_charity_info.csv'
    leak_location = '../data/' + leak + '/' + leak + '_papers.nodes.entity.csv'
    
    leak_data = spark.read.csv(leak_location, header=True)

    charity_data = spark.read.csv(charity_location, header=True)
    
    charity_names = charity_data.select('name').selectExpr('name as CharityName')
    shell_names = leak_data.select('name').selectExpr('name as ShellName')
    
    shells_vs_charities = shell_names.crossJoin(charity_names)
    
    filtered_names = shells_vs_charities.rdd.filter(lambda r: check_for_words(r[0], r[1], stop_words, sharp) == True)
    
    matches = filtered_names.toDF()
    
    matches.repartition(1)\
    .write.format("csv")\
    .mode('overwrite').save('../generated/' + leak +'_'+ charity +'_matches.csv')
    
import sys

leak = sys.argv[1]
charity = sys.argv[2]
    
if __name__ == '__main__':
    extract_matches_between(leak, charity, True)
        
