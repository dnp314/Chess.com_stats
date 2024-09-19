import streamlit as st
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


# Custom CSS to improve the app's appearance
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom right, #1e1e1e, #2d3748);
    }
    .main-container {
        background-color: #2d3748;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: 2rem auto;
    }
    .stTextInput > div > div > input {
        background-color: #4a5568;
        color: white;
        border: 1px solid #4a5568;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 20px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s;
        display: block;
        margin: 1rem auto;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem;
    }
    .player-stats {
        background-color: #4a5568;
        border-radius: 10px;
        padding: 1rem;
        margin-top: 1rem;
    }
    .player-stats h3 {
        color: #3498db;
    }
    /* Hide Streamlit's default header */
    header {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.markdown('<h1>Chess.com Player Stats Comparison</h1>', unsafe_allow_html=True)

def valid_username(player_name): 
    link = "https://www.chess.com/stats/overview/" + player_name 
    service = Service(executable_path="chromedriver.exe") 
    driver = webdriver.Chrome(service=service) 
    driver.get(link) 
     
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
     
    # Check if 404 page is present 
    sp = soup.find('div', class_="_404-header") 
     
    try: 
        temp = sp.find('h1').text 
    except: 
        temp = "" 
     
    driver.quit() 
     
    return temp != "404 Page not found", soup 

# Function to get personal information of the player 
def get_personal_info(soup): 
    sp = soup.find_all('div', class_="profile-card-info-item-value") 
    labels = ["Joined", "Followers", "Views"] 
    personal_info = {} 

    for i, label in enumerate(labels, start=1): 
        personal_info[label] = sp[i].text 

    username = soup.find('h1', class_="profile-card-username").text.strip() 
    personal_info["Username"] = username 

    flag_div = soup.find('div', {'data-cy': 'user-country-flag'}) 
    flag_name = flag_div.get('v-tooltip') 

    personal_info["Country"] = flag_name 

    return personal_info 

def get_format_stats(player_name,format):
    new_link=f"https://www.chess.com/stats/live/{format}/"+player_name+"/0"
    service =Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(new_link)
    soup =BeautifulSoup(driver.page_source,'html.parser')

    labels=["HighestRating","CurrentRating","GlobalRank","TotalGames","AvgOppoRating","AvgOppoRatingW","AvgOppoRatingD","AvgOppoRatingL","GameswithWhite","GameswithBlack"]
    format={}
    hr   = soup.find('div',{'style':'text-align: center;'}).text.strip()
    cr   = soup.find('div',class_="rating-block-container").text[:4]
    rank = soup.find_all('div',class_="icon-block-small-content")
    rank = rank[1].text.strip()[1:]
    games = soup.find_all('div',{'style':'text-align: center;'})[1].text
    avg_or = soup.find_all('div',{'style':'text-align: center;'})[2].text
    avg_orw= soup.find('span',class_="game-bar game-green").text
    avg_ord= soup.find('span',class_="game-bar game-grey").text
    avg_orl= soup.find('span',class_="game-bar game-red").text

    format["HighestRating"]=hr
    format["CurrentRating"]=cr
    format["GlobalRank"]=rank
    format["TotalGames"]=games
    format["AvgOppoRating"]=avg_or
    format["AvgOppoRatingW"]=avg_orw
    format["AvgOppoRatingD"]=avg_ord
    format['AvgOppoRatingL']=avg_orl

    return format

# Input fields for player usernames
player1_name = st.text_input("Enter Player 1 Username", key="player1")
player2_name = st.text_input("Enter Player 2 Username", key="player2")

# Compare button
compare_button = st.button("Compare Players")

if compare_button:
    if player1_name and player2_name:
        with st.spinner("Fetching player stats..."):
            valid1, soup1 = valid_username(player1_name)
            valid2, soup2 = valid_username(player2_name)
                
            if valid1 and valid2:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown("### Stats")
                    st.write("**Joined**")
                    st.write("**Followers**")
                    st.write("**Views**")
                    st.write("**Country**")
                    st.write("### Rapid Stats")
                    st.write("**Highest Rating**")
                    st.write("**Current Rating**")
                    st.write("**Global Rank**")
                    st.write("**Total Games**")
                    st.write("**Avg Oppo Rating**")
                    st.write("**Avg Oppo Rating W**")
                    st.write("**Avg Oppo Rating D**")
                    st.write("**Avg Oppo Rating L**")
                    st.write("### Blitz Stats")
                    st.write("**Highest Rating**")
                    st.write("**Current Rating**")
                    st.write("**Global Rank**")
                    st.write("**Total Games**")
                    st.write("**Avg Oppo Rating**")
                    st.write("**Avg Oppo Rating W**")
                    st.write("**Avg Oppo Rating D**")
                    st.write("**Avg Oppo Rating L**")
                    st.write("### Bullet Stats")
                    st.write("**Highest Rating**")
                    st.write("**Current Rating**")
                    st.write("**Global Rank**")
                    st.write("**Total Games**")
                    st.write("**Avg Oppo Rating**")
                    st.write("**Avg Oppo Rating W**")
                    st.write("**Avg Oppo Rating D**")
                    st.write("**Avg Oppo Rating L**")
                
                with col2:
                    player1_info = get_personal_info(soup1)
                    st.subheader(f"{player1_info['Username']}")
                    st.write(player1_info["Joined"])
                    st.write(player1_info["Followers"])
                    st.write(player1_info["Views"])
                    st.write(player1_info["Country"])
                    
                    player1_stats=get_format_stats(player1_name,"rapid")
                    
                    st.subheader("")
                    
                    st.write(player1_stats["HighestRating"])
                    st.write(player1_stats["CurrentRating"])
                    st.write(player1_stats["GlobalRank"])
                    st.write(player1_stats["TotalGames"])
                    st.write(player1_stats["AvgOppoRating"])
                    st.write(player1_stats["AvgOppoRatingW"])
                    st.write(player1_stats["AvgOppoRatingD"])
                    st.write(player1_stats["AvgOppoRatingL"])
                    
                    player1_stats=get_format_stats(player1_name,"blitz")
                    
                    st.subheader("")
                    
                    st.write(player1_stats["HighestRating"])
                    st.write(player1_stats["CurrentRating"])
                    st.write(player1_stats["GlobalRank"])
                    st.write(player1_stats["TotalGames"])
                    st.write(player1_stats["AvgOppoRating"])
                    st.write(player1_stats["AvgOppoRatingW"])
                    st.write(player1_stats["AvgOppoRatingD"])
                    st.write(player1_stats["AvgOppoRatingL"])
                    
                    player1_stats=get_format_stats(player1_name,"bullet")
                    
                    st.subheader("")
                    
                    st.write(player1_stats["HighestRating"])
                    st.write(player1_stats["CurrentRating"])
                    st.write(player1_stats["GlobalRank"])
                    st.write(player1_stats["TotalGames"])
                    st.write(player1_stats["AvgOppoRating"])
                    st.write(player1_stats["AvgOppoRatingW"])
                    st.write(player1_stats["AvgOppoRatingD"])
                    st.write(player1_stats["AvgOppoRatingL"])
                
                with col3:
                    player2_info = get_personal_info(soup2)
                    st.subheader(f"{player2_info['Username']}")
                    st.write(player2_info["Joined"])
                    st.write(player2_info["Followers"])
                    st.write(player2_info["Views"])
                    st.write(player2_info["Country"])
                    
                    player2_stats = get_format_stats(player2_name,"rapid")
                    
                    st.subheader("")
                    
                    st.write(player2_stats["HighestRating"])
                    st.write(player2_stats["CurrentRating"])
                    st.write(player2_stats["GlobalRank"])
                    st.write(player2_stats["TotalGames"])
                    st.write(player2_stats["AvgOppoRating"])
                    st.write(player2_stats["AvgOppoRatingW"])
                    st.write(player2_stats["AvgOppoRatingD"])
                    st.write(player2_stats["AvgOppoRatingL"])
                    
                    player2_stats = get_format_stats(player2_name,"blitz")
                    
                    st.subheader("")
                        
                    st.write(player2_stats["HighestRating"])
                    st.write(player2_stats["CurrentRating"])
                    st.write(player2_stats["GlobalRank"])
                    st.write(player2_stats["TotalGames"])
                    st.write(player2_stats["AvgOppoRating"])
                    st.write(player2_stats["AvgOppoRatingW"])
                    st.write(player2_stats["AvgOppoRatingD"])
                    st.write(player2_stats["AvgOppoRatingL"])
                    
                    player2_stats = get_format_stats(player2_name,"bullet")
                    
                    st.subheader("")
                    
                    st.write(player2_stats["HighestRating"])
                    st.write(player2_stats["CurrentRating"])
                    st.write(player2_stats["GlobalRank"])
                    st.write(player2_stats["TotalGames"])
                    st.write(player2_stats["AvgOppoRating"])
                    st.write(player2_stats["AvgOppoRatingW"])
                    st.write(player2_stats["AvgOppoRatingD"])
                    st.write(player2_stats["AvgOppoRatingL"])
            else:
                if not valid1:
                    st.error(f"{player1_name} is not a valid username")
                if not valid2:
                    st.error(f"{player2_name} is not a valid username")

    else:
        st.warning("Please enter both player usernames.")
