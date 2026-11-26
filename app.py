import streamlit as st
from streamlit_extras.let_it_rain import rain
import random
from datetime import datetime

st.snow()

# Page configuration
st.set_page_config(page_title="Secret Santa Christmas 2026", page_icon="🎄")
# CSS to keep items in a single row on mobile and style the boxes
st.markdown(
    """
    <style>
    .countdown-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
        width: 100%;
        max-width: 500px;
        margin: 20px auto;
    }
    .time-box {
        flex: 1;
        background-color: #165B33;
        color: #FFFFFF;
        border: 2px solid #BB2528;
        border-radius: 10px;
        padding: 12px 4px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .time-val {
        font-size: clamp(1.5rem, 6vw, 2.5rem);
        font-weight: 800;
        line-height: 1.1;
        font-variant-numeric: tabular-nums;
    }
    .time-label {
        font-size: clamp(0.65rem, 2.5vw, 0.85rem);
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 4px;
        color: #F8B229;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎄 Christmas Countdown")


@st.fragment(run_every="1s")
def show_countdown():
  now = datetime.now()
  christmas = datetime(now.year, 12, 25, 0, 0, 0)

  # If Christmas has passed this year, target next year
  if now > christmas:
    christmas = datetime(now.year + 1, 12, 25, 0, 0, 0)

  diff = christmas - now

  if diff.total_seconds() <= 0:
    st.success("🎅 Merry Christmas!")
    return

  days = diff.days
  hours, remainder = divmod(diff.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)

  st.markdown(
      f"""
        <div class="countdown-container">
            <div class="time-box">
                <div class="time-val">{days:02d}</div>
                <div class="time-label">Days</div>
            </div>
            <div class="time-box">
                <div class="time-val">{hours:02d}</div>
                <div class="time-label">Hours</div>
            </div>
            <div class="time-box">
                <div class="time-val">{minutes:02d}</div>
                <div class="time-label">Mins</div>
            </div>
            <div class="time-box">
                <div class="time-val">{seconds:02d}</div>
                <div class="time-label">Secs</div>
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )


show_countdown()

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    # st.image(logo)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW1laXp6MnIxM3lhcW50bzJhNjdsaXhndGtqY2NmcmhnNDJ0dWpscSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/nIIBglp9W7pBt6qGi3/giphy.gif")

st.header(f"🎅 Secret Santa 2026- Who'd you get?! 🤶", anchor=False)

st.markdown('# Gifting theme:')
st.markdown('Inspired by sheep. Wool? Fleece? White and fluffy? has a sheep on it?! What a bleatin joke ... ')
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('https://images.cartoonstock.com/lowres_800/seasonal-celebrations-nativity-nativity_scene-christian-christianity-fleece-dren2799_low.jpg')

# user_code: from, to, media
result_lookup = {'buttcracker': ['Aaron', 'Keith', 'https://b3666184.assetcdn.net/2.0/3666184/wp-content/uploads/2025/12/christmas-comics-18-12-19-2025.webp?lossy=2&strip=1&webp=1'], 
                'pigsinblankets': ['David', 'Jen', "https://m.media-amazon.com/images/I/81t9xBz8ZwL._AC_SX679_.jpg"],  
                'ohbless': ['Keith', 'Aisling', 'https://m.media-amazon.com/images/I/710uiJrgGBL._AC_SX679_.jpg'], 
                'santascoming': ['Claire', 'Eric', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZlYXpxZHM4N3lremdrZTR3bzZ6bWxib2h4OWlkcWt4OXVseTlyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LBAv3HJDl2WwU/giphy.gif'],
                'crafty': ['Mam', 'Aaron', 'https://img.boredpanda.com/unsafe/rs:fit:750:0/q:70/aHR0cHM6Ly9zdGF0aWMuYm9yZWRwYW5kYS5jb20vYmxvZy93cC1jb250ZW50L3VwbG9hZHMvMjAyNS8xMC9JTUdfMDg3OC02OGVhM2Q3ZDZhYTc3LWpwZWdfXzcwMC5qcGc.webp'],
                'whishtnow': ['Dad', 'David', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXJjbXFyd3h4aXNsZGlnMGJtbjV4NXJuZmNzanp2MjJhdDUwcnEzbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ewxD9vhchcigshopy/giphy.gif'], 
                'reelitin': ['Aisling', 'Claire', 'https://media1.tenor.com/m/-Mf8ULUx3Q8AAAAd/fishing-gone-fishing.gif'],
                'pilesofstars': ['Jen', 'Angela', 'https://warandpeas.com/wp-content/uploads/2017/12/war-and-peas-christmas-tree.jpg'],
                'spideychristmas': ['Leon', 'Millie', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c405972b-1540-4ed9-af40-b157bea4bb53/deww8gw-2ca407d4-3ccb-432a-a4a4-865fb17a2b65.png/v1/fill/w_894,h_894,q_70,strp/spider_man_wishes_you_a_merry_christmas__by_aurteloess_deww8gw-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiIvZi9jNDA1OTcyYi0xNTQwLTRlZDktYWY0MC1iMTU3YmVhNGJiNTMvZGV3dzhndy0yY2E0MDdkNC0zY2NiLTQzMmEtYTRhNC04NjVmYjE3YTJiNjUucG5nIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.6F8tqpRs8wrsB0EvVVAXDGxZns-2GfiNjs5421CxKww'], 
                'mangaxmas': ['Charlie', 'Lucy', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaG90Nmd0cWpxaTg2bnA1NnRrcDJodjZycnZ0ZDgxaXhndTMxcXJ2YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BqlIdB0bL02vGSt4Vu/giphy.gif'],
                'isthatpretzelorhisfuturewife': ['Lucy', 'Leon', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTV2OWJmcjBjaHU3bmY5b3dpb3F2MTBzZHVuanR3ZnByMnhseGFxZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/99kKoxEgOWMIBF3iOk/giphy.gif'],
                'christmasregrets': ['Holly', 'Charlie', 'https://www.youtube.com/watch?v=HePQnzc-Vto'], 
                'sleighbellsring': ['Millie', 'Holly', 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExN2FodWJieDZvejJwNDkxcm0wNHowcGFrZWJobmZkbjQ3c2xjdG05eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KyXefl39CoZWWj21w1/giphy.gif']} 

all_of_us = ['aaron', 'david', 'keith', 'claire', 'angela', 'eric', 'aisling', 'jen', 'leon', 'charlie', 'lucy', 'holly', 'millie']

user_code = st.text_input('Enter the code you were sent in your whatsapp message...').lower()

if user_code == 'christmasregrets':
    st.video(result_lookup[user_code][2])
    st.write('🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 ')
    st.write(f'🎁   ..... Hey {result_lookup[user_code][0]}, you are gifting to ....... 🎁  ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write(f'🎁 🎁 🎁 ............ {result_lookup[user_code][1]}! ........... 🎁🎁 🎁')
    st.write(' 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 ')
if user_code in result_lookup.keys() and user_code!= 'christmasregrets':
    img_url = {result_lookup[user_code][2]}
    st.image(img_url)
    st.write('🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 ')
    st.write(f'🎁   ..... Hey {result_lookup[user_code][0]}, you are gifting to ....... 🎁  ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write(f'🎁 🎁 🎁 ............ {result_lookup[user_code][1]}! ........... 🎁🎁 🎁')
    st.write(' 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 ')
if user_code in all_of_us:
    st.markdown('Names won\'t work ... you have to use the code you were sent.')
    st.markdown('If you\'re trying to check who someone else got, stop cheating! Especially you mam.')

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.video('https://www.youtube.com/watch?v=yXQViqx6GMY', autoplay=True, muted=True)
