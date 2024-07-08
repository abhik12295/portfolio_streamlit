from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# --Path Setting--
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Abhishek_Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# ---General Setting ---#
EMAIL = "abhik12295@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/abhishek12295/",
    "GitHub": "https://github.com/abhik12295",
    "Facebook": "https://www.facebook.com/abhi120694/",
    "Twitter": "https://twitter.com/abhi_1294"
}

st.set_page_config(
    page_title="Abhishek Kumar Portfolio",
    page_icon=":computer:",
    layout="wide",
)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load CSS
local_css(css_file)


# Background
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/7130490/pexels-photo-7130490.jpeg");
             background-attachment: fixed;
             background-size: cover;
             backdrop-filter: blur(2px);
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

# --- INTRO ---
# Profile pic and Resume
with open(resume_file, "rb") as pdf_file:
    PDF_Byte = pdf_file.read()
pro_pic = Image.open(profile_pic)

with st.container():
    col1, col2 = st.columns((2, 2))

    with col1:
        st.image(pro_pic, width=200)
    with col2:
        st.title("Abhishek Kumar")
        st.subheader("Software Developer | Automation | Data Enthusiast")
        st.download_button(
            label="📄 Download Resume",
            data=PDF_Byte,
            file_name=resume_file.name,
            mime="application/octet-stream"
        )
        st.write(f"📧 {EMAIL}")

# --- ABOUT ME ---
with st.container():
    st.write("---")
    st.header("About Me")
    st.write(
        """
        Hi, I am Abhishek, a Software Developer specializing in Automation, Tech, and Data. 
        Passionate about solving complex problems and delivering efficient solutions.
        """
    )
    st_lottie(
        load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json"),
        height=300,
    )

# --- EDUCATION ---
with st.container():
    st.write("---")
    st.header("Education")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Illinois Institute of Technology")
        st.write(
            """
            📍 Chicago, Illinois, US
            📅 Jan 2021 - Dec 2022
            🧑‍💻 Master's in Computer Science (Data Analytics)
            """
        )

    with col2:
        st.subheader("University of Petroleum and Energy Studies")
        st.write(
            """
            📍 Dehradun, Uttarakhand, India
            📅 June 2013 - Jun 2017
            🧑‍💻 Bachelor's in Computer Science and Engineering
            """
        )

# --- WORK EXPERIENCE ---
with st.container():
    st.write("---")
    st.header("Work Experience")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Kuehne & Nagel Inc.")
        st.write(
            """
            📅 Apr 2023 - Present
            🏷️ BI & Data Science Developer
            - Data Engineering | ETL | Python | AWS Glue | Tableau | AWS
            - Built ETL pipelines, optimized processing time by 50% for automated report generation
            """
        )

        st.subheader("CCC Intelligent Solutions")
        st.write(
            """
            📅 Jan 2022 - Dec 2022
            🏷️ Automation Analyst Intern
            - Automation | Data Analytics | Python | MongoDB
            - Built Audit Dashboard which reduced time to prepare reports by 40%
            """
        )

    with col2:
        st.subheader("Must Discover Private Limited")
        st.write(
            """
            📅 Jul 2017 - Apr 2020
            🏷️ Software Engineer
            - Software Engineer skills | Web Development | Development | Codes | AWS | Data Science
            - Achieved 60% accuracy in targeted marketing campaigns.
            """
        )

        st.subheader("Nuriss LifeCare Private Limited")
        st.write(
            """
            📅 May 2016 - Jul 2016
            🏷️ Android Developer Intern
            - Android Development | Java | RESTful API | Firebase | E-commerce
            - Developed an application for medical representatives and pharmacies.
            """
        )

# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    st.header("Tech Stack / Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.write(
            """
            **Languages:** Python, Spark, Javascript, Java
            **Frameworks:** PySpark, FastAPI, Django, Flask, Bootstrap, Node.js
            **Databases:** MySQL, PostgreSQL, MongoDB
            **Hosting & Cloud:** AWS, Azure, Heroku, Streamlit Cloud
            **Miscellaneous:** Git, Github, Gitlab, CI/CD, Docker, ML/AI, Tableau
            """
        )

    with col2:
        st_lottie(
            load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lln7m43m.json"),
            height=300,
        )

# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.subheader("Take a look at some of my works!")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://images.pexels.com/photos/21014/pexels-photo.jpg")
        st.subheader("Map Route Algorithm")
        st.write(
            "Built a route-planning algorithm like the one used in Google Maps to calculate the shortest path between two points on a map.")
        if st.button('Github', key="ews_github"):
            link = '[Click here](https://github.com/abhik12295/Map-Router-Planner)'
            st.markdown(link, unsafe_allow_html=True)

    with col2:
        st.image("https://images.pexels.com/photos/1046398/pexels-photo-1046398.jpeg")
        st.subheader("Civil Advocacy")
        st.write("Android Application using Google Civic Information API to acquire government official data.")
        if st.button('Github', key="gee_github"):
            link = '[Click here](https://github.com/abhik12295/Civil-Advocacy)'
            st.markdown(link, unsafe_allow_html=True)

    with col3:
        st.image("https://images.pexels.com/photos/4551158/pexels-photo-4551158.jpeg")
        st.subheader("Illinois Open Cafeteria")
        st.write("Created a Machine Learning model to suggest a location to open a cafeteria in Illinois.")
        if st.button('Github', key="ccw_github"):
            link = '[Click here](https://github.com/abhik12295/illinois_open_cafetaria)'
            st.markdown(link, unsafe_allow_html=True)

# Additional Portfolio Items
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://images.pexels.com/photos/3936358/pexels-photo-3936358.jpeg")
        st.subheader("COVID Text Analysis Classification")
        st.write("Worked on Gaussian Naïve Bayes, Random Forest, and TF-IDF Vectorizer to improve model performance.")
        if st.button('Github', key="qrc_github"):
            link = '[Click here](https://github.com/abhik12295/COVID_TextAnalysis_Classification)'
            st.markdown(link, unsafe_allow_html=True)

    with col2:
        st.image("https://images.pexels.com/photos/2335048/pexels-photo-2335048.jpeg")
        st.subheader("Movie Recommendation Content-Based Filtering")
        st.write("Developed a content-based recommendation system to suggest items based on user preferences.")
        if st.button('Github', key="spw_github"):
            link = '[Click here](https://github.com/abhik12295/movie-recommend)'
            st.markdown(link, unsafe_allow_html=True)

    with col3:
        st.image("https://images.pexels.com/photos/1102915/pexels-photo-1102915.jpeg")
        st.subheader("Weather Application")
        st.write("Developed an Android application in Java using Visual Crossing Web API.")
        if st.button('Github', key="xrf_github"):
            link = '[Click here](https://github.com/abhik12295/weather_application)'
            st.markdown(link, unsafe_allow_html=True)

# --- SOCIAL LINKS ---
with st.container():
    st.write("---")
    st.header("Social Media Links")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']})")

    with col2:
        st.markdown(f"[GitHub]({SOCIAL_MEDIA['GitHub']})")

    with col3:
        st.markdown(f"[Facebook]({SOCIAL_MEDIA['Facebook']})")

    with col4:
        st.markdown(f"[Twitter]({SOCIAL_MEDIA['Twitter']})")

# --- CONTACT ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write(
        "I'd love to hear from you. Whether you have a question or just want to say hi, feel free to drop me a message!")
    contact_form = """
    <form action="https://formsubmit.co/059cd784e788c85ed5add9aed225bb53" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
