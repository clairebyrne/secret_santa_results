import streamlit as st
from streamlit_extras.let_it_rain import rain
import random

# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Page configuration
st.set_page_config(page_title="Secret Santa Christmas 2026", page_icon="🎄")

# Run snowfall animation
run_snow_animation()

# st.header(f"🎅 🤶 Secret Santa 2026- Who'd you get?! ⛄🎄", anchor=False)
st.header(f"🎅 🤶 ⛄🎄 🤶 🎅", anchor=False)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    # st.image(logo)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW1laXp6MnIxM3lhcW50bzJhNjdsaXhndGtqY2NmcmhnNDJ0dWpscSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nIIBglp9W7pBt6qGi3/giphy.gif")
    st.video('https://www.youtube.com/watch?v=yXQViqx6GMY', autoplay=True, muted=True)

result_lookup = {'buttcracker': ['Claire', 'https://b3666184.assetcdn.net/2.0/3666184/wp-content/uploads/2025/12/christmas-comics-18-12-19-2025.webp?lossy=2&strip=1&webp=1', 'Aaron'], #updated
                'pigsinblankets': ['Angela', "https://m.media-amazon.com/images/I/81t9xBz8ZwL._AC_SX679_.jpg", 'David'], #updated 
                'ohbless': ['Jen', 'https://m.media-amazon.com/images/I/710uiJrgGBL._AC_SX679_.jpg', 'Keith'], 
                'santascoming': ['Eric', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZlYXpxZHM4N3lremdrZTR3bzZ6bWxib2h4OWlkcWt4OXVseTlyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LBAv3HJDl2WwU/giphy.gif', 'Claire'],
                'crafty': ['Marcelina', 'https://img.boredpanda.com/unsafe/rs:fit:750:0/q:70/aHR0cHM6Ly9zdGF0aWMuYm9yZWRwYW5kYS5jb20vYmxvZy93cC1jb250ZW50L3VwbG9hZHMvMjAyNS8xMC9JTUdfMDg3OC02OGVhM2Q3ZDZhYTc3LWpwZWdfXzcwMC5qcGc.webp', 'Mam'], #updated 
                'whishtnow': ['Aaron', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXJjbXFyd3h4aXNsZGlnMGJtbjV4NXJuZmNzanp2MjJhdDUwcnEzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ewxD9vhchcigshopy/giphy.gif', 'Dad'], #updated
                'reelitin': ['Keith', 'https://media1.tenor.com/m/-Mf8ULUx3Q8AAAAd/fishing-gone-fishing.gif', 'Aisling'], #updated
                'pilesofstars': ['David', 'https://warandpeas.com/wp-content/uploads/2017/12/war-and-peas-christmas-tree.jpg', 'Jen'], #updated
                'whosaminion': ['Holly', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTllOGxqMXg1dXR2emtvaTZ0OG9tYnNpc21rM3llNmQ4N2N1dGc1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9w475hDWEPVlu/giphy.gif', 'Leon'], 
                'mangawha': ['Millie', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG90Nmd0cWpxaTg2bnA1NnRrcDJodjZycnZ0ZDgxaXhndTMxcXJ2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BqlIdB0bL02vGSt4Vu/giphy.gif', 'Charlie'], #updated 
                'isthatpretzelorhisfuturewife': ['Leon', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTV2OWJmcjBjaHU3bmY5b3dpb3F2MTBzZHVuanR3ZnByMnhseGFxZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/99kKoxEgOWMIBF3iOk/giphy.gif', 'Lucy'], #updated
                'whatsyourfavouritecolour': ['Lucy', 'https://media1.tenor.com/m/U7_-hprcYqoAAAAC/buddy-buddy-the-elf.gif', 'Holly'], 
                'sleighbellsring': ['Charlie', 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2FodWJieDZvejJwNDkxcm0wNHowcGFrZWJobmZkbjQ3c2xjdG05eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KyXefl39CoZWWj21w1/giphy.gif', 'Millie']} #updated

all_of_us = ['aaron', 'david', 'keith', 'claire', 'angela', 'eric', 'aisling', 'jen', 'leon', 'charlie', 'lucy', 'holly', 'millie']

user_code = st.text_input('Enter the code you were sent in your whatsapp message...').lower()

if user_code == 'takeyoursobstory':
    st.video(result_lookup[user_code][1])
    st.write('🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 ')
    st.write(f'🎁   ..... Hey {result_lookup[user_code][2]}, you are gifting to ....... 🎁  ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write(f'🎁 🎁 🎁 ............ {result_lookup[user_code][0]}! ........... 🎁🎁 🎁')
    st.write(' 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 ')
if user_code in result_lookup.keys() and user_code!= 'takeyoursobstory':
    img_url = {result_lookup[user_code][1]}
    st.image(img_url)
    st.write('🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 ')
    st.write(f'🎁   ..... Hey {result_lookup[user_code][2]}, you are gifting to ....... 🎁  ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write(f'🎁 🎁 🎁 ............ {result_lookup[user_code][0]}! ........... 🎁🎁 🎁')
    st.write(' 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 ')
if user_code in all_of_us:
    st.markdown('Names won\'t work ... you have to use the code you were sent.')
    st.markdown('If you\'re trying to check who someone else got, stop cheating! Especially you mam.')
