import streamlit as st
from streamlit_extras.let_it_rain import rain
import random

# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Page configuration
st.set_page_config(page_title="Secret Santa Christmas 2025", page_icon="🎄")

# Run snowfall animation
run_snow_animation()

st.header(f"🎅 🤶 Secret Santa 2025- Who'd you get?! ⛄🎄", anchor=False)
st.markdown("![Alt Text](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjB3b2FodmRjNW5tdWhsZGtzdWozZGlhbmF4NmtoZGZubnJseGtrYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HBMCmtsPEUShG/giphy.gif)")

result_lookup = {'takeyoursobstory': ['Claire', 'https://youtu.be/7Ec3zIyt4Yg', 'Aaron'],
                'noneedforthat': ['Angela', "https://media1.tenor.com/m/Guu-fazdXi4AAAAd/merry-christmas-2024.gif", 'David'], 
                'turkeyontheside': ['Jen', 'https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3RwcTJjY2F6NW9haGJvemxvdmlleTNycGV3ZmVpOTZodWxudDU4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RlkxV4vKnKqtXLj2qw/giphy.gif', 'Keith'], 
                'santascoming': ['Eric', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTZlYXpxZHM4N3lremdrZTR3bzZ6bWxib2h4OWlkcWt4OXVseTlyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LBAv3HJDl2WwU/giphy.gif', 'Claire'],
                'giveusahand': ['Marcelina', 'https://media1.tenor.com/m/kYTF8A-XkYcAAAAd/snowman-dog.gif', 'Mam'], 
                'whatapup': ['Aaron', 'https://media1.tenor.com/m/B-DElu_sxdoAAAAd/atv-sledding-pupper-atv.gif', 'Dad'],
                'wouldyoulook': ['Keith', 'https://firebox.com/blog/wp-content/uploads/2022/10/2pf7wi.jpg', 'Aisling'], 
                'wellthatsdisturbing': ['David', 'https://firebox.com/blog/wp-content/uploads/2022/10/giphy-16.gif', 'Jen'], 
                'bundleup': ['Aisling', 'https://media1.tenor.com/m/a6BJsB4KADMAAAAd/wrapped-up-bundled-up.gif', 'Marcelina'],
                'whosaminion': ['Holly', 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTllOGxqMXg1dXR2emtvaTZ0OG9tYnNpc21rM3llNmQ4N2N1dGc1eiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9w475hDWEPVlu/giphy.gif', 'Leon'], 
                'grinchoff': ['Millie', 'https://media.tenor.com/S8fkU5FEppoAAAAj/sportsmanias-emoji.gif', 'Charlie'], 
                'whichsideout': ['Leon', 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDRwa2pncTR4bW8ydmduYzRpZnNzbzNjcmVzbDRtN3hwYXdvNjdjZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y4PUPG0d2In8bimcIm/giphy.gif', 'Lucy'],
                'whatsyourfavouritecolour': ['Lucy', 'https://media1.tenor.com/m/U7_-hprcYqoAAAAC/buddy-buddy-the-elf.gif', 'Holly'], 
                'suitsyou': ['Charlie', 'https://media1.tenor.com/m/VYNmmNbag84AAAAd/santa-kitty.gif', 'Millie']}

user_code = st.text_input('Enter your secret code...').lower()

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
    st.markdown(f"![Alt Text]({result_lookup[user_code][1]})")
    st.write('🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 🎅 ')
    st.write(f'🎁   ..... Hey {result_lookup[user_code][2]}, you are gifting to ....... 🎁  ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write('🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 🎄 ')
    st.write(f'🎁 🎁 🎁 ............ {result_lookup[user_code][0]}! ........... 🎁🎁 🎁')
    st.write(' 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 🤶 ')


if user_code in ['Aaron', 'David', 'Keith', 'Claire', 'Angela', 'Eric', 'Aisling', 'Jen', 'Marcelina', 'Leon', 'Charlie', 'Lucy', 'Holly', 'Millie']:
    st.markdown('Names won\'t work ... you have to use the code you were sent.')
    st.markdown('If you\'re trying to check who someone else got, stop cheating! Especially you mam.')