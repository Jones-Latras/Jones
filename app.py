from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
default_profile_pic_path = current_dir / "assets" / "profile-pic.png"
current_profile_pic_path = current_dir / "assets" / "current_profile.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Jones T. Latras // Biography"
PAGE_ICON = ":wave:"
NAME = "Latras, Jones T."
DESCRIPTION = """
Bachelor of Science in Computer Engineering - BSCpE 1A
"""
EMAIL = "jlatras1@ssct.edu.ph"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/jonescantfocus",
    "Instagram": "https://www.instagram.com/jltrs_/",
    "Tiktok": "https://www.tiktok.com/@jonesswho"
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- SESSION STATE FOR PROFILE PICTURE ---
if "profile_pic_path" not in st.session_state:
    # Initialize session state with the current profile picture
    if current_profile_pic_path.exists():
        st.session_state.profile_pic_path = current_profile_pic_path
    else:
        st.session_state.profile_pic_path = default_profile_pic_path

# --- PROFILE ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # Load and display the current profile picture
    profile_pic = Image.open(st.session_state.profile_pic_path)
    st.image(profile_pic, width=250, caption="Profile Picture")
    
# Upload a new profile picture
uploaded_file = st.file_uploader("Change Profile Pic:", type=["png", "jpg", "jpeg"])
    
if uploaded_file is not None:
    # Save the uploaded file as the new profile picture
    with open(current_profile_pic_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
    # Update session state to point to the new profile picture
    st.session_state.profile_pic_path = current_profile_pic_path
        

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write ("---")


# --- BACKGROUND ---
st.markdown ("""
My name is Jones Latras, and I am currently a freshman pursuing a degree in Computer Engineering at Surigao del Norte State University. I am passionate about understanding how technology shapes the world and aspire to contribute innovative solutions in the future. From an early age, I have been fascinated by the mechanics behind devices and systems, which inspired me to take this path.

Outside of academics, I immerse myself in activities that fuel my creativity and imagination. I enjoy reading manhwa, where I explore compelling stories and artwork, and watching anime, which provides me with both entertainment and inspiration. I am also an avid reader of books, always on the lookout for stories and ideas that broaden my perspective.

Gaming is another hobby I deeply enjoy—it challenges my strategic thinking and allows me to connect with others who share similar interests. Whether it’s solving puzzles in a game or tackling a complex problem in engineering, I thrive on challenges that push me to think critically.

I see myself as a curious and driven individual, eager to grow and make the most of every opportunity. My journey in Computer Engineering is just beginning, and I am excited to explore the possibilities ahead while staying grounded in the hobbies and passions that bring me joy.""",
unsafe_allow_html=True,
)

# --- EDUCATIONAL ATTAINMENT ---
st.write('\n')
st.write ("---")
tab1, tab2, tab3, tab4 = st.tabs(["📚 Educational Attainments", "🎯 Accomplishments", "📸Gallery", "👨‍👩‍👧‍👦Family Background",])
with tab1:
    st.write("### Educational Attainments:")
    tab1.markdown(
        """
        ELEMENTARY:
        <ul style="margin-left: 20px; font-size: 16px;">
            <ul style="margin-left: 20px;">
                <li>Malinao Elementary School</li>
                <li>Brgy. Malinao, Tubajon Dinagat Islands</li>
                <li>2017-2018</li>
            </ul>
        </ul>
        
        SECONDARY:
        <ul style="margin-left: 20px; font-size: 16px;">
            <ul style="margin-left: 20px;">
                <li>Malinao National High School</li>
                <li>Brgy. Malinao Tubajon, Dinagat Islands</li>
                <li>2023-2024</li>
            </ul>
        </ul>
        
        TERTIARY:
        <ul style="margin-left: 20px; font-size: 16px;">
            <ul style="margin-left: 20px;">
                <li>Surigao Del Norte State University</li>
                <li>Narciso Street, Surigao City, 8400 Surigao del Norte</li>
            </ul>
        </ul>
        
        """,
        unsafe_allow_html=True,
    )

# Initialize session state for accomplishments if not present
if 'accomplishments' not in st.session_state:
    st.session_state.accomplishments = {
        'elementary': [
            "🏅Grade 3: 4th Place",
            "🏅Grade 4: First Place",
            "🏅Grade 5: With Honors",
            "🏅Grade 6: With High Honors (Valedictorian)",
        ],
        'secondary': [
            "🏅Grade 7: With Honors",
            "🏅Grade 8: With Honors",
            "🏅Grade 9: With Honors",
            "🏅Grade 10: With High Honors",
            "🏅Grade 11: With High Honors",
            "🏅Grade 12: With High Honors (Valedictorian)"
        ],
        'journalism': [
            "🏅Grade 5 - 6th Place Feature Writing in English",
            "🏅RSPC 2017 Feature Writing in English",
            "🏅Grade 11 - 5th Place Feature Writing in English",
            "🏅Grade 12 - 2rd Place Feature Writing in English"
        ],
        'school organizations': [
            "🏅Grade 10 - SSG President",
            "🏅Grade 10 - Math Club President",
            "🏅Grade 11 - English Club President",
            "🏅Grade 12 - SSG Vice President",
            "🏅Grade 12 - English Club President",
        ]
    }

# Function to display accomplishments
def display_accomplishments(data):
    for key, values in data.items():
        st.markdown(f"**{key.upper()}**:")
        st.markdown("<ul style='margin-left: 20px;'>", unsafe_allow_html=True)
        for value in values:
            st.markdown(f"<li>{value}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)

# --- Tab 2: Accomplishments ---
with tab2:
    st.write("### Current Accomplishments:")
    display_accomplishments(st.session_state.accomplishments)

    # --- Add/Update Accomplishment ---
    st.write("### Add/Update Accomplishment")
    level = st.selectbox("Choose accomplishment level:", ["Elementary", "Secondary", "Journalism", "School Organizations"])
    accomplishment = st.text_input(f"Enter accomplishment for {level}:")

    # Button to add or update
    if st.button(f"Add/Update {level}"):
        level_key = level.lower()
        if accomplishment:
            st.session_state.accomplishments[level_key].append(accomplishment)
            st.success(f"Accomplishment added/updated for {level}!")
        else:
            st.warning("Please enter an accomplishment.")

    # --- Remove Accomplishment ---
    st.write("### Remove Accomplishment")
    remove_level = st.selectbox("Select level to remove an accomplishment from:", ["Elementary", "Secondary", "Extracurricular Activities"])
    accomplishments_to_remove = st.session_state.accomplishments[remove_level.lower()]
    accomplishment_to_remove = st.selectbox("Select accomplishment to remove:", accomplishments_to_remove)

    # Button to remove an accomplishment
    if st.button(f"Remove Accomplishment from {remove_level}"):
        if accomplishment_to_remove in accomplishments_to_remove:
            st.session_state.accomplishments[remove_level.lower()].remove(accomplishment_to_remove)
            st.success(f"Accomplishment removed from {remove_level}!")
        else:
            st.warning("Accomplishment not found.")

# --- Tab 3: Gallery ---
with tab3:
    st.write("### Gallery:")
    st.write("This is where you can display your gallery of images or videos.")
    col1, col2 = st.columns(2)
    with col1:
        st.image("assets/1.jpg", width=250, caption="Babies")
        st.image("assets/3.jpg", width=250, caption="Sunset")
        st.image("assets/5.jpg", width=250, caption="HS Days")
        st.image("assets/7.jpg", width=250, caption="Miya")
        st.image("assets/9.jpg", width=250, caption="Smurfette")
        st.image("assets/11.jpg", width=250, caption="School Boy")
        st.image("assets/13.jpg", width=250, caption="Pretty Mama🥰")
        st.image("assets/15.jpg", width=250, caption="Late Night Walk")
    with col2:
        st.image("assets/2.jpg", width=250, caption="Babies")
        st.image("assets/4.jpg", width=250, caption="Sunset")
        st.image("assets/6.jpg", width=250, caption="HS Days")
        st.image("assets/8.jpg", width=250, caption="Miya")
        st.image("assets/10.jpg", width=250, caption="Smurfette")
        st.image("assets/12.jpg", width=250, caption="School Boy")
        st.image("assets/14.jpg", width=250, caption="Pretty Mama🥰")
        st.image("assets/16.jpg", width=250, caption="Late Night Walk")


# --- Tab 4: Family Background ---
with tab4:
    st.write("### Family Background:")
    st.markdown(
    """
    Mother:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Josefina Galinzoga Tumangan</li>
            <li>October 04, 1976</li>
        </ul>
    </ul>
    
    Father:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Mario Palomares Latras</li>
            <li>February 08, 1976</li>
        </ul>
    </ul>
    
    Brother:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>James Tumangan Latras</li>
            <li>October 07, 1999</li>
        </ul>
    </ul>
    
    Me:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Jones Tumangan Latras</li>
            <li>November 02, 2005</li>
        </ul>
    </ul>
    """,
    unsafe_allow_html=True,
)