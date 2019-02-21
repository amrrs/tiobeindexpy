import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.tiobe.com/tiobe-index/'

content = requests.get(url)

soup = BeautifulSoup(content.text,"lxml")

tables = soup.find_all("table")

def hall_of_fame():
    '''Get Programming Language Hall of Fame Table'''
    df = pd.read_html(str(tables[3]), header = 0)[0]
    return(df)

def top_20():
    '''Get Top 20 values of TIOBIE Index table for the latest month'''
    df = pd.read_html(str(tables[0]), header = 0)[0]
    return(df)

def top_50():
    '''Get Top 50 values of TIOBIE Index table for the latest month'''
    df = pd.read_html(str(tables[1]), header = 0)[0]
    return(df)
