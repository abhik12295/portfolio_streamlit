from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import altair

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
    page_title="Abhishek Kr🧊",
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


#  To get rid of the Streamlit branding stuff
local_css(css_file)

#  Anchor
st.title("#")  # This anchor is needed for the page to start at the top when it is called.


# background
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
        pass
        # st.write("Click Below to download the file :point_down: ")
        # st.download_button(
        #     label="Download Resume :page_facing_up:",
        #     data=PDF_Byte,
        #     file_name=resume_file.name,
        #     mime="application/octet-stream", )
        # st.write(":email:", EMAIL)


with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
        st.title("Welcome to my Portfolio Page!")
        st.subheader("Hi, I am Abhishek :desktop_computer:")
        st.subheader(
            """
            I am a *Software Developer* who specializes in the broad fields of *Automation*, *Tech* & *Data*.
            """
        )
        st.write("""""")
        st.subheader(
            """
            Love for 👩‍💻 :cricket_bat_and_ball: and :soccer:
            Technical leader, devise effective solutions to complex business challenges with an innate ability for 
            teamwork, task prioritization, big picture vision, and dedication. 
            Masterfully code key projects to enable on-time delivery of key milestones within budget constraints.
            """
        )
    with col2:
        st_lottie(
            load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json"),
            height=300,
        )

# --- Education ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st_lottie(
            load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uqsv3ztj.json"),
            height=300,
        )
    with col2:
        st.header("Education")
        st.subheader(
            """
             	:male-student: Illinois Institute of Technology \n
             	:round_pushpin: Chicago, Illinois, US \n 
             	:calendar: Jan 2021 - Dec 2022 \n
             	🧑‍💻 Master's in Computer Science (with specialialization in Data Analytics) \n
            """
        )
        st.subheader(
            """
                :male-student: University of Petroleum and Energy Studies \n
                :round_pushpin: Dehradun, Uttarakhand, India \n
                :calendar: June 2013 - Jun 2017 \n
                🧑‍💻 Bachelor's in Computer Science and Engineering \n
            """
        )

# --- Work Experience---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st_lottie(
            load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json"),
            height=300,
        )
    with col1:
        st.header("Work Experience")
        st.subheader(
            """
                💼  Kuehne & Nagel Inc. \n
                :bookmark_tabs: BI & Data Science Developer \n 
                :calendar: Apr 2023 - Now \n
                :pushpin: | Data Engineering | ETL | Python | AWS Glue | Tableau | AWS |
                 Built ETL pipelines, optimized processing time by 50% for automated report generation \n
            """
        )
        st.subheader(
            """
                💼  CCC Intelligent Solutions \n
                :bookmark_tabs: Automation Analyst Intern \n 
                :calendar: Jan 2022 - Dec 2022 \n
                :pushpin: | Automation | Data Analytics | Python | MongoDB |
                 Built Audit Dashboard which reduced time to prepare reports by 40% \n
            """
        )
        st.subheader(
            """
                 💼 Must Discover Private Limited \n
                :bookmark_tabs: Software Engineer\n
                :calendar: Jul 2017 - Apr 2020 \n
                :pushpin: | Software Engineer skills | Web Development | Development | Codes | AWS | Data Science |
                Achieved 60% accuracy in targeted marketing campaigns.  \n
            """
        )
        st.subheader(
            """
                 💼 Nuriss LifeCare Private Limited \n
                :bookmark_tabs: Android Developer Intern \n
                :calendar: May 2016 - Jul 2016 \n
                :pushpin: | Android Development | Java | RESTful API | Firebase | E-commerce |
                Application for medical representatives and pharmacies with customized medicine inventory and orders.\n
            """
        )

# --- TECH STACK / SKILLS ---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col2:
        st.header("Tech Stack / Skills")
        st.write(
            """
            Languages
            - Python, Spark, Javascript, Java
            Frameworks
            - PySpark, FastAPI, Django, Flask, Bootstrap, Node.js
            Databases
            - MySQL, PostgreSQL, MongoDB
            Hosting & Cloud
            - AWS, Azure, Heroku, Streamlit Cloud
            Miscellaneous
            - Git, Github, Gitlab, CI/CD, Docker, ML/AI, Tableau
             """
        )

    with col1:
        st_lottie(
            load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lln7m43m.json"),
            height=300,
        )

# --- PORTFOLIO ---
with st.container():
    st.write("---")
    st.header("Portfolio")
    st.subheader("Take a look at some of my works. !")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "https://images.pexels.com/photos/21014/pexels-photo.jpg")
        st.subheader("Map Route Algorithm")
        st.write("Built a route-planning algorithm like the one used in Google Maps to calculate the shortest path "
                 "between two points on a map.")

        if st.button('Github', key="ews_github"):
            st.write('Github opens in new browser tab')
            #js = "window.open('https://github.com/abhik12295/Map-Router-Planner')"  # New tab or window
            # html = '<img src onerror="{}">'.format(js)
            # div = Div(text=html)
            # st.bokeh_chart(div)
            link = '[Click here](https://github.com/abhik12295/Map-Router-Planner)'
            st.markdown(link, unsafe_allow_html=True)
    with col2:
        st.image(
            "https://images.pexels.com/photos/1046398/pexels-photo-1046398.jpeg")
        st.subheader("Civil Advocacy")
        st.write("Android Application and Google Civic Information API will be used to acquire the government "
                 "official data (via REST service and JSON results).")
        if st.button('Github', key="gee_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/abhik12295/Civil-Advocacy)'
            st.markdown(link, unsafe_allow_html=True)
    with col3:
        st.image(
            "https://images.pexels.com/photos/4551158/pexels-photo-4551158.jpeg")
        st.subheader("Illinois Open Cafeteria")
        st.write("Created a Machine Learning model which suggests a location to open a Cafeteria in Illinois")
        st.write("""""")
        if st.button('Github', key="ccw_github"):
            st.write('Github opens in new browser tab')
            link = '[Click here](https://github.com/abhik12295/illinois_open_cafetaria)'
            st.markdown(link, unsafe_allow_html=True)

    with st.container():
        col4, col5, col6 = st.columns(3)
        with col4:
            st.image(
                "https://images.pexels.com/photos/3936358/pexels-photo-3936358.jpeg")
            st.subheader("COVID Text Analysis Classification")
            st.write(
                "Worked on Gaussian Naïve Bayes, Random Forest, and TF-IDF Vectorizer which affected the performance "
                "of the models")
            if st.button('Github', key="qrc_github"):
                st.write('Github opens in new browser tab')
                link = '[Click here](https://github.com/abhik12295/COVID_TextAnalysis_Classification)'
                st.markdown(link, unsafe_allow_html=True)
        with col5:
            st.image(
                "https://images.pexels.com/photos/2335048/pexels-photo-2335048.jpeg")
            st.subheader("Movie Recommendation Content-Based Filtering")
            st.write("Content-based (cognitive filtering) recommendation system is to suggest an item based on a "
                     "comparison of the item's content and a user profile")
            # if st.button('Enter App', key="ccw_enter"):
            #     link = '[Click here](https://movie-igniter.herokuapp.com/)'
            #     st.markdown(link, unsafe_allow_html=True)
            if st.button('Github', key="spw_github"):
                st.write('Github opens in new browser tab')
                link = '[Click here](https://github.com/abhik12295/movie-recommend)'
                st.markdown(link, unsafe_allow_html=True)
        with col6:
            st.image(
                "https://images.pexels.com/photos/1102915/pexels-photo-1102915.jpeg")
            st.subheader("Weather Application")
            st.write("Android Application in Java using Visual Crossing Web API")
            st.write("""""")
            if st.button('Github', key="bpw_github"):
                st.write('Github opens in new browser tab')
                link = '[Click here](https://github.com/abhik12295/WeatherApp)'
                st.markdown(link, unsafe_allow_html=True)

# --- CONTACT ---
with st.container():
    st.write("---")
    st.markdown("<h2 style='text-align: center;'>Feedback</h2>", unsafe_allow_html=True)
    st.write("##")

    col1, col2, col3 = st.columns(3)
    with col2:
        contact_form = """
        <form action="https://formsubmit.co/059cd784e788c85ed5add9aed225bb53" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your name" required = True>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

with st.container():
    for i in range(8):
        st.write("##")
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            ABHISHEK KUMAR :copyright: 2024
            """
        )
    with col2:
        st.markdown("<p style='text-align: right;'>Made in 2022 with ❤, 🐍 and Streamlit</p>", unsafe_allow_html=True)
    st.write("---")
