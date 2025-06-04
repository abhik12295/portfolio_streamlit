from pathlib import Path
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = str(current_dir / "styles" / "main.css")
js_file = str(current_dir / "styles" / "main.js")
resume_file = str(current_dir / "assets" / "Abhishek_Kumar_Resume.pdf")
profile_pic = str(current_dir / "assets" / "profile-pic.png")

# --- General Settings ---
EMAIL = "abhik12295@gmail.com"
SOCIAL_MEDIA = {
    "Facebook": {"url": "https://www.facebook.com/abhi120694/", "icon": "https://cdn-icons-png.flaticon.com/512/733/733547.png"},
    "Twitter": {"url": "https://x.com/abhi_1294", "icon": "https://img.icons8.com/?size=100&id=oaaSr6h7kwm6&format=png&color=000000"},
    "LinkedIn": {"url": "https://www.linkedin.com/in/abhik12295/", "icon": "https://cdn-icons-png.flaticon.com/512/174/174857.png"},
    "GitHub": {"url": "https://github.com/abhik12295", "icon": "https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000"}
}

st.set_page_config(
    page_title="Abhishek Kumar | Portfolio",
    page_icon=":computer:",
    layout="wide",
)

# --- Load Lottie Animation ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Local CSS and JS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def local_js(file_name):
    with open(file_name) as f:
        st.markdown(f"<script>{f.read()}</script>", unsafe_allow_html=True)

# Load CSS and JS files
local_css(css_file)
local_js(js_file)
# Load Font Awesome for icon support
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">',
    unsafe_allow_html=True
)

# --- Main Content Wrapper ---
with st.container():
    # --- Fixed Top Navigation ---
    st.markdown("""
    <div class='nav-container fixed'>
        <nav class='nav' aria-label='Main navigation'>
            <ul>
                <li><a href='#about' class='nav-link'><span class='nav-indicator'></span>About</a></li>
                <li><a href='#education' class='nav-link'><span class='nav-indicator'></span>Education</a></li>
                <li><a href='#experience' class='nav-link'><span class='nav-indicator'></span>Experience</a></li>
                <li><a href='#skills' class='nav-link'><span class='nav-indicator'></span>Skills</a></li>
                <li><a href='#portfolio' class='nav-link'><span class='nav-indicator'></span>Portfolio</a></li>
                <li><a href='#contact' class='nav-link'><span class='nav-indicator'></span>Contact</a></li>
            </ul>
        </nav>
    </div>
    """, unsafe_allow_html=True)

    # --- Hero Section ---
    #st.markdown("<div class='hero-section' id='about'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(profile_pic, width=350, use_column_width=False)
    with col2:
        st.markdown("<h4 class='fade-in hero-text'>Hey There, I'm</h4>", unsafe_allow_html=True)
        st.markdown("<h1 class='fade-in hero-text' id='typed-name'>Abhishek Kumar</h1>", unsafe_allow_html=True)
        st.markdown("<h3 class='fade-in hero-text typed-text'>Data Science Developer | Data Engineer | Problem Solver</h3>", unsafe_allow_html=True)
        st.markdown("""
        <p class='fade-in hero-text'>
            I’m passionate about turning raw data into actionable insights that drive impact. With a Master’s in Computer Science from IIT Chicago and over 5 years of experience, I build scalable ML models, optimize data pipelines, and create intuitive dashboards. My mission is to solve complex problems with elegant, data-driven solutions. Let’s build something extraordinary together!
        </p>
        """, unsafe_allow_html=True)
        st.markdown(f"<p class='fade-in hero-text'><a href='mailto:{EMAIL}' class='email-link'>{EMAIL}</a></p>", unsafe_allow_html=True)
        col_btn1, col_social, col_btn2 = st.columns([1, 2, 1])
        with col_btn1:
            with open(resume_file, "rb") as pdf_file:
                PDF_Byte = pdf_file.read()
            st.download_button(
                label="Download Résumé",
                data=PDF_Byte,
                file_name="Abhishek_Kumar_Resume.pdf",
                mime="application/octet-stream",
                key="resume_download"
            )
        with col_social:
            social_links_html = """
            <div class='social-links fade-in' style='display: flex; justify-content: center; gap: 20px; align-items: center; margin-top: 10px; margin-bottom: 10px;'>
            """
            for platform, data in SOCIAL_MEDIA.items():
                social_links_html += (
                    f"<a href='{data['url']}' target='_blank' class='social-link' style='display: inline-block;'>"
                    f"<img src='{data['icon']}' alt='{platform}' class='social-icon' style='width: 40px; height: 40px;'/>"
                    "</a>"
                )
            social_links_html += "</div>"
            st.markdown(social_links_html, unsafe_allow_html=True)
        with col_btn2:
            st.markdown("<a href='#portfolio' class='hero-cta'>Explore My Work</a>", unsafe_allow_html=True)
    # Lottie animation at the end of hero section
    st_lottie(load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json"), height=350, width=350)
    
    
    # --- Education ---
    st.markdown("<div id='education' class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in' style='text-align:center;'>Education & Certifications</h2>", unsafe_allow_html=True)
    # Lottie animation on top, centered
    st_lottie(load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uqsv3ztj.json"), height=350, width=350)
    # Education and Certifications below image, aligned in two columns
    col_left, col_center = st.columns([2, 1.5], gap="large")
    with col_left:
        # Beautiful Degree Cards
        st.markdown("""
        <h4 class='fade-in' style='text-align:center;'>Education</h4>
        <style>
        .degree-card-grid {
            display: flex;
            flex-direction: column;
            gap: 28px;
            align-items: center;
        }
        .degree-card {
            background: linear-gradient(120deg, #232526 0%, #3a3a3a 100%);
            border-radius: 18px;
            box-shadow: 0 4px 24px 0 rgba(0,114,255,0.10), 0 1.5px 6px 0 rgba(0,0,0,0.10);
            padding: 30px 32px 22px 32px;
            width: 390px;
            max-width: 97vw;
            color: #f8f9fa;
            position: relative;
            border: 2.5px solid #ffd700;
            transition: transform 0.15s, box-shadow 0.15s;
        }
        .degree-card:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 8px 32px 0 rgba(255,215,0,0.18), 0 2px 8px 0 rgba(0,0,0,0.13);
        }
        .degree-icon {
            position: absolute;
            top: -32px;
            left: 32px;
            background: #ffd700;
            color: #232526;
            border-radius: 50%;
            width: 56px;
            height: 56px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 2px 8px 0 rgba(255,215,0,0.18);
            border: 3px solid #fff;
        }
        .degree-title {
            font-size: 1.18rem;
            font-weight: 700;
            margin-top: 22px;
            margin-bottom: 6px;
            color: #fff;
        }
        .degree-date {
            font-size: 1.01rem;
            color: #ffe066;
            margin-bottom: 8px;
        }
        .degree-institute {
            font-size: 1.05rem;
            font-weight: 600;
            color: #ffd700;
            margin-bottom: 4px;
        }
        .degree-details {
            font-size: 0.98rem;
            color: #f8f9fa;
            margin-bottom: 6px;
        }
        .degree-badge {
            display: inline-block;
            background: #ffd700;
            color: #232526;
            font-weight: 700;
            font-size: 0.95rem;
            border-radius: 12px;
            padding: 3px 12px;
            margin-top: 8px;
            margin-bottom: 6px;
        }
        </style>
        <div class='degree-card-grid'>
            <div class='degree-card fade-in'>
                <div class='degree-icon'><i class="fas fa-graduation-cap"></i></div>
                <div class='degree-title'>Master’s in Computer Science (Data Analytics)</div>
                <div class='degree-institute'>Illinois Institute of Technology</div>
                <div class='degree-date'>Chicago, IL, USA | Jan 2021 - Dec 2022</div>
                <div class='degree-badge'>Degree Awarded</div>
                <div class='degree-details'>
                    <ul style='margin-left: 1em;'>
                        <li>GPA: 3.5/4.0</li>
                        <li>Key Courses: Machine Learning, Big Data Technologies, Data Mining</li>
                        <li>Project: Built and deployed a movie recommendation system using content-based filtering and Flask.</li>
                    </ul>
                </div>
            </div>
            <div class='degree-card fade-in'>
                <div class='degree-icon'><i class="fas fa-graduation-cap"></i></div>
                <div class='degree-title'>Bachelor’s in Computer Science and Engineering</div>
                <div class='degree-institute'>University of Petroleum and Energy Studies</div>
                <div class='degree-date'>Dehradun, UK, India | Jun 2013 - Jun 2017</div>
                <div class='degree-badge'>Degree Awarded</div>
                <div class='degree-details'>
                    <ul style='margin-left: 1em;'>
                        <li>GPA: 2.9/4.0</li>
                        <li>Project: Implemented a secure file management system with user-based encryption for uploading, listing, and accessing encrypted files via an application server.</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        with col_center:
        # Certificates in visually distinct boxes
            st.markdown("""
            <h4 class='fade-in' style='text-align:center; color:#f8f9fa;'>Certifications</h4>
            <style>
            .cert-box-grid {
                display: flex;
                flex-direction: column;
                gap: 20px;
                align-items: center;
            }
            .cert-box {
                background: linear-gradient(120deg, #232526 0%, #414345 100%);
                border-radius: 18px;
                box-shadow: 0 4px 24px 0 rgba(0,114,255,0.10), 0 1.5px 6px 0 rgba(0,0,0,0.10);
                padding: 24px 28px 18px 28px;
                width: 320px;
                max-width: 95vw;
                color: #f8f9fa;
                position: relative;
                border: 2px solid #00c6ff;
                transition: transform 0.15s, box-shadow 0.15s;
            }
            .cert-box:hover {
                transform: translateY(-4px) scale(1.03);
                box-shadow: 0 8px 32px 0 rgba(0,114,255,0.18), 0 2px 8px 0 rgba(0,0,0,0.13);
            }
            .cert-icon {
                position: absolute;
                top: -28px;
                left: 24px;
                background: #00c6ff;
                color: #fff;
                border-radius: 50%;
                width: 48px;
                height: 48px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 26px;
                box-shadow: 0 2px 8px 0 rgba(0,114,255,0.18);
                border: 3px solid #fff;
            }
            .cert-title {
                font-size: 1.1rem;
                font-weight: 700;
                margin-top: 18px;
                margin-bottom: 6px;
                color: #fff;
            }
            .cert-date {
                font-size: 0.96rem;
                color: #b2eaff;
                margin-bottom: 8px;
            }
            .cert-btn {
                display: inline-block;
                padding: 7px 18px;
                margin-top: 10px;
                font-size: 14px;
                font-weight: 600;
                color: #fff !important;
                background: linear-gradient(90deg, #0072ff 0%, #00c6ff 100%);
                border: none;
                border-radius: 20px;
                box-shadow: 0 2px 8px 0 rgba(0,114,255,0.13);
                text-decoration: none !important;
                transition: background 0.3s, transform 0.2s;
                cursor: pointer;
            }
            .cert-btn:hover {
                background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
                transform: translateY(-2px) scale(1.04);
                box-shadow: 0 6px 20px 0 rgba(0,114,255,0.25);
                color: #fff !important;
                text-decoration: none !important;
            }
            </style>
            <div class='cert-box-grid'>
                <div class='cert-box fade-in'>
                <div class='cert-icon'><i class='fas fa-certificate'></i></div>
                <div class='cert-title'>Generative AI using AWS - Udacity</div>
                <div class='cert-date'>Jun 2025</div>
                <a href='https://www.udacity.com/certificate/e/164b8aca-3c1b-11f0-b0ba-eb8cba0b3157' target='_blank' class='cert-btn'><i class="fas fa-external-link-alt"></i> View Certificate</a>
                </div>
                <div class='cert-box fade-in'>
                <div class='cert-icon'><i class='fas fa-certificate'></i></div>
                <div class='cert-title'>Machine Learning Foundation - AWS Educate</div>
                <div class='cert-date'>May 2025</div>
                <a href='https://www.credly.com/badges/827387bc-05af-4e5e-9ed5-681d1a41478e' target='_blank' class='cert-btn'><i class="fas fa-external-link-alt"></i> View Certificate</a>
                </div>
                <div class='cert-box fade-in'>
                <div class='cert-icon'><i class='fas fa-certificate'></i></div>
                <div class='cert-title'>Tableau Desktop Specialist</div>
                <div class='cert-date'>Sep 2022</div>
                <a href='https://www.credly.com/badges/286df8e4-4cc5-47f1-9f02-d6d9cefbf557/public_url' target='_blank' class='cert-btn'><i class="fas fa-external-link-alt"></i> View Certificate</a>
                </div>
                <div class='cert-box fade-in'>
                <div class='cert-icon'><i class='fas fa-certificate'></i></div>
                <div class='cert-title'>Data Structures and Algorithms Nano Degree- Udacity</div>
                <div class='cert-date'>Aug 2022</div>
                <a href='https://www.udacity.com/certificate/FD2ZPGJE' target='_blank' class='cert-btn'><i class="fas fa-external-link-alt"></i> View Certificate</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # --- Experience ---
    st.markdown("<div id='experience' class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in' style='text-align:center;'>Professional Experience</h2>", unsafe_allow_html=True)
    st_lottie(load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json"), height=250, width=250)
    st.markdown("""
    <style>
    .exp-card-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 60px;
        justify-content: center;
        margin-top: 24px;
        margin-bottom: 24px;
    }
    .exp-card {
        background: linear-gradient(120deg, #232526 0%, #3a3a3a 100%);
        border-radius: 18px;
        box-shadow: 0 4px 24px 0 rgba(0,114,255,0.10), 0 1.5px 6px 0 rgba(0,0,0,0.10);
        padding: 32px 36px 26px 36px;
        width: 420px;
        max-width: 97vw;
        color: #f8f9fa;
        position: relative;
        border: 2.5px solid #00c6ff;
        transition: transform 0.15s, box-shadow 0.15s;
        display: flex;
        flex-direction: column;
        min-height: 340px;
    }
    .exp-card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 8px 32px 0 rgba(0,198,255,0.18), 0 2px 8px 0 rgba(0,0,0,0.13);
    }
    .exp-icon {
        position: absolute;
        top: -32px;
        left: 36px;
        background: #00c6ff;
        color: #fff;
        border-radius: 50%;
        width: 56px;
        height: 56px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        box-shadow: 0 2px 8px 0 rgba(0,198,255,0.18);
        border: 3px solid #fff;
    }
    .exp-title {
        font-size: 1.22rem;
        font-weight: 700;
        margin-top: 22px;
        margin-bottom: 4px;
        color: #fff;
    }
    .exp-role {
        font-size: 1.07rem;
        font-weight: 600;
        color: #ffd700;
        margin-bottom: 6px;
    }
    .exp-date {
        font-size: 1.01rem;
        color: #b2eaff;
        margin-bottom: 10px;
    }
    .exp-points {
        font-size: 1.01rem;
        color: #f8f9fa;
        margin-bottom: 10px;
        margin-left: 1em;
        padding-left: 0.5em;
    }
    .exp-points li {
        margin-bottom: 7px;
        line-height: 1.5;
        list-style: disc;
    }
    .exp-badge {
        display: inline-block;
        background: #ffd700;
        color: #232526;
        font-weight: 700;
        font-size: 0.97rem;
        border-radius: 12px;
        padding: 3px 12px;
        margin-top: 8px;
        margin-bottom: 6px;
    }
    .exp-tech {
        font-size: 0.98rem;
        color: #00c6ff;
        margin-top: 8px;
        font-weight: 600;
    }
    </style>
    <div class='exp-card-grid'>
        <div class='exp-card fade-in'>
            <div class='exp-icon'><i class="fas fa-briefcase"></i></div>
            <div class='exp-title'>Kuehne & Nagel</div>
            <div class='exp-role'>BI & Data Science Developer</div>
            <div class='exp-date'>Apr 2023 - Present</div>
            <ul class='exp-points'>
                <li><b>Designed & deployed</b> geolocation-based ML models with AWS SageMaker, <span style="color:#ffd700;">improving delivery times by 25%</span>.</li>
                <li><b>Optimized ETL pipelines</b> using PySpark & AWS Glue, <span style="color:#ffd700;">reducing data processing costs by 30%</span>.</li>
                <li><b>Built interactive Tableau dashboards</b> for supply chain analytics, <span style="color:#ffd700;">adopted by 100+ stakeholders</span>.</li>
            </ul>
            <div class='exp-badge'>Full-Time</div>
            <div class='exp-tech'>Python · PySpark · AWS Glue · Tableau · SQL</div>
        </div>
        <div class='exp-card fade-in'>
            <div class='exp-icon'><i class="fas fa-laptop-code"></i></div>
            <div class='exp-title'>Must Discover Private Limited</div>
            <div class='exp-role'>Software Engineer</div>
            <div class='exp-date'>Jul 2017 - Apr 2020</div>
            <ul class='exp-points'>
                <li><b>Built a recommendation system</b> using AWS ML services, <span style="color:#ffd700;">boosting user engagement by 20%</span>.</li>
                <li><b>Automated data workflows</b> with Python, <span style="color:#ffd700;">saving 15+ hours/week</span> for the team.</li>
                <li><b>Collaborated cross-functionally</b> to deliver scalable backend solutions for 10K+ users.</li>
            </ul>
            <div class='exp-badge'>Full-Time</div>
            <div class='exp-tech'>AWS · Python</div>
        </div>
        <div class='exp-card fade-in'>
            <div class='exp-icon'><i class="fas fa-chart-line"></i></div>
            <div class='exp-title'>CCC Intelligent Solutions</div>
            <div class='exp-role'>Automation Analyst Intern</div>
            <div class='exp-date'>Jan 2022 - Dec 2022</div>
            <ul class='exp-points'>
                <li><b>Developed an audit dashboard</b> with Python & Streamlit, <span style="color:#ffd700;">cutting report generation time by 40%</span>.</li>
                <li><b>Integrated MongoDB</b> for real-time data querying, <span style="color:#ffd700;">enhancing audit accuracy</span>.</li>
                <li><b>Presented insights</b> to senior management, influencing key process improvements.</li>
            </ul>
            <div class='exp-badge'>Internship</div>
            <div class='exp-tech'>Python · MongoDB · Streamlit</div>
        </div>
        <div class='exp-card fade-in'>
            <div class='exp-icon'><i class="fas fa-mobile-alt"></i></div>
            <div class='exp-title'>Nuriss Private Limited</div>
            <div class='exp-role'>Android Developer Intern</div>
            <div class='exp-date'>May 2016 - Jun 2016</div>
            <ul class='exp-points'>
                <li><b>Developed an Android app</b> for inventory management, <span style="color:#ffd700;">streamlining hospital operations</span>.</li>
                <li><b>Integrated MongoDB</b> for real-time updates & analytics.</li>
                <li><b>Delivered a user-friendly UI</b> that improved staff efficiency.</li>
            </ul>
            <div class='exp-badge'>Internship</div>
            <div class='exp-tech'>Java · MongoDB</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Skills ---
    st.markdown("<div id='skills' class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in' style='text-align:center;'>Technical & Soft Skills</h2>", unsafe_allow_html=True)
    st_lottie(load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lln7m43m.json"), height=200, width=200)
    st.markdown("""
    <style>
    .skills-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 18px;
    }
    .skills-column {
        display: flex;
        flex-direction: column;
        gap: 12px;
        align-items: center;
        width: 320px;
        max-width: 95vw;
    }
    .tech-skills-card, .soft-skills-card {
        background: linear-gradient(120deg, #232526 0%, #3a3a3a 100%);
        border-radius: 14px;
        box-shadow: 0 3px 16px 0 rgba(0,114,255,0.10), 0 1px 4px 0 rgba(0,0,0,0.10);
        padding: 24px 28px 20px 28px;
        width: 100%;
        color: #f8f9fa;
        position: relative;
        border: 2px solid #ffd700;
        transition: transform 0.15s, box-shadow 0.15s;
        font-size: 0.9rem;
        min-height: 20px;
    }
    .soft-skills-card {
        border: 2px solid #00c6ff;
    }
    .tech-skills-card:hover, .soft-skills-card:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 6px 24px 0 rgba(255,215,0,0.18), 0 1.5px 6px 0 rgba(0,0,0,0.13);
    }
    .tech-skills-icon, .soft-skills-icon {
        position: absolute;
        top: -20px;
        left: 28px;
        background: #ffd700;
        color: #232526;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        box-shadow: 0 1px 6px 0 rgba(255,215,0,0.18);
        border: 2px solid #fff;
    }
    .soft-skills-icon {
        background: #00c6ff;
        color: #fff;
    }
    .tech-skills-title, .soft-skills-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-top: 16px;
        margin-bottom: 4px;
        color: #fff;
    }
    .tech-skills-bar-container {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 4px;
    }
    .tech-skills-bar-bg {
        flex-grow: 1;
        background: #343a40;
        border-radius: 4px;
        height: 6px;
        margin-top: 4px;
        margin-bottom: 4px;
    }
    .tech-skills-bar-fill {
        height: 6px;
        border-radius: 4px;
        background: linear-gradient(90deg, #ffd700 0%, #ffe066 100%);
    }
    .tech-skills-level {
        font-size: 0.95rem;
        color: #b2eaff;
        font-weight: 600;
        white-space: nowrap;
    }
    .tech-skills-keyword, .soft-skills-keyword {
        font-size: 0.85rem;
        font-weight: 700;
        color: #ffd700;
        white-space: nowrap;
    }
    .soft-skills-keyword {
        color: #00c6ff;
        margin-top: 4px;
    }
    @media (max-width: 768px) {
        .skills-column {
            width: 100%;
            max-width: 85vw;
        }
        .tech-skills-card, .soft-skills-card {
            padding: 20px 24px 16px 24px;
            min-height: 200px;
        }
        .tech-skills-icon, .soft-skills-icon {
            width: 36px;
            height: 36px;
            font-size: 20px;
            top: -18px;
            left: 24px;
        }
        .tech-skills-title, .soft-skills-title {
            font-size: 1rem;
        }
        .tech-skills-level {
            font-size: 0.85rem;
        }
        .tech-skills-keyword, .soft-skills-keyword {
            font-size: 0.8rem;
        }
    }
    @media (max-width: 480px) {
        .skills-column {
            max-width: 80vw;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Font Awesome 6.4.2 for consistency
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">', unsafe_allow_html=True)

    tech_skills = [
        {"name": "Python", "icon": "fab fa-python", "level": 90, "keyword": "Expert"},
        {"name": "AWS", "icon": "fab fa-aws", "level": 85, "keyword": "Advanced"},
        {"name": "Tableau", "icon": "fas fa-chart-bar", "level": 80, "keyword": "Advanced"},
        {"name": "SQL", "icon": "fas fa-database", "level": 80, "keyword": "Advanced"},
        {"name": "PySpark", "icon": "fas fa-fire", "level": 75, "keyword": "Proficient"},
        {"name": "Git", "icon": "fab fa-git-alt", "level": 75, "keyword": "Proficient"},
        {"name": "Machine Learning", "icon": "fas fa-robot", "level": 70, "keyword": "Proficient"},
    ]
    soft_skills = [
        {"name": "Problem Solving", "icon": "fas fa-lightbulb", "keyword": "Excellent"},
        {"name": "Team Collaboration", "icon": "fas fa-users", "keyword": "Excellent"},
        {"name": "Communication", "icon": "fas fa-comments", "keyword": "Excellent"},
        {"name": "Leadership", "icon": "fas fa-user-tie", "keyword": "Strong"},
    ]

    # Skills Column for All Skills
    st.markdown("<div class='skills-container'>", unsafe_allow_html=True)
    st.markdown("<div class='skills-column fade-in'>", unsafe_allow_html=True)
    for skill in tech_skills:
        st.markdown(f"""
        <div class='tech-skills-card fade-in'>
            <div class='tech-skills-icon'><i class='{skill['icon']}'></i></div>
            <div class='tech-skills-title'>{skill['name']}</div>
            <div class='tech-skills-bar-container'>
                <div class='tech-skills-bar-bg'>
                    <div class='tech-skills-bar-fill' style='width: {skill['level']}%;'></div>
                </div>
                <div class='tech-skills-level'>{skill['level']}%</div>
                <div class='tech-skills-keyword'>{skill['keyword']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    for skill in soft_skills:
        st.markdown(f"""
        <div class='soft-skills-card fade-in'>
            <div class='soft-skills-icon'><i class='{skill['icon']}'></i></div>
            <div class='soft-skills-title'>{skill['name']}</div>
            <div class='soft-skills-keyword'>{skill['keyword']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)    
    
    # --- Portfolio ---
    st.markdown("<div id='portfolio' class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in' style='text-align:center;'>Portfolio</h2>", unsafe_allow_html=True)
    st.markdown("<p class='fade-in' style='text-align:center;'>Explore my data-driven projects solving real-world challenges.</p>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    .portfolio-card-title-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 10px;
    }
    .portfolio-card-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #fff;
        margin: 0;
        flex: 1;
        white-space: normal;
    }
    .portfolio-github-link {
        margin-left: 12px;
        text-decoration: none !important;
        color: #00c6ff !important;
        font-size: 1.6rem; /* Increased size */
        transition: color 0.2s;
        display: flex;
        align-items: center;
        padding: 8px 16px; /* Make button area bigger */
        border-radius: 8px;
        background: #232526;
        border: 2px solid #00c6ff;
        box-shadow: 0 2px 8px 0 rgba(0,198,255,0.10);
    }
    .portfolio-github-link:hover {
        color: #ffd700 !important;
        background: #232526;
        border-color: #ffd700;
    }
    </style>
    <div class='portfolio-grid'>
    """, unsafe_allow_html=True)
    projects = [
        {
            "title": "AI-Powered PDF Reader",
            "desc": "Web app name `QueryLeaf AI` for PDF text extraction and summarization using OpenAI API. Chat with your documents.",
            "tech": ["Python", "Streamlit", "OpenAI", "Pdfminer", "Flask"],
            "img": "https://images.pexels.com/photos/7876785/pexels-photo-7876785.jpeg",
            "github": "https://github.com/abhik12295/AI-Powered-PDF-Reader"
        },
        {
            "title": "Illinois Open Cafeteria",
            "desc": "ML model predicting optimal cafeteria locations using clustering and demographic data. Achieved 90% accuracy in site selection.",
            "tech": ["Python", "Scikit-learn", "Pandas"],
            "img": "https://images.pexels.com/photos/4551158/pexels-photo-4551158.jpeg",
            "github": "https://github.com/abhik12295/illinois_open_cafetaria"
        },
        {
            "title": "COVID Text Analysis",
            "desc": "Naïve Bayes classifier for sentiment analysis of COVID-related tweets. Achieved 85% accuracy in polarity detection.",
            "tech": ["Python", "NLTK", "Scikit-learn"],
            "img": "https://images.pexels.com/photos/3936358/pexels-photo-3936358.jpeg",
            "github": "https://github.com/abhik12295/COVID_TextAnalysis_Classification"
        },
        {
            "title": "Movie Recommendation",
            "desc": "Content-based recommendation system using TF-IDF and cosine similarity. Recommends movies based on user preferences.",
            "tech": ["Python", "Vectorization", "Flask", "Scikit-learn", "TMDB-API"],
            "img": "https://images.pexels.com/photos/2335048/pexels-photo-2335048.jpeg",
            "github": "https://github.com/abhik12295/movie-recommend"
        },
        {
            "title": "Map Route Algorithm",
            "desc": "A shortest-path algorithm optimizing delivery routes using A* algorithm. Improved route efficiency by 30%.",
            "tech": ["Python", "Algorithm", "NetworkX"],
            "img": "https://images.pexels.com/photos/21014/pexels-photo.jpg",
            "github": "https://github.com/abhik12295/Map-Router-Planner"
        },
        {
            "title": "Weather App",
            "desc": "Android app fetching real-time weather data via Visual Crossing API. Rated 4.5/5 by 100+ users.",
            "tech": ["Java", "Android Studio", "REST API"],
            "img": "https://images.pexels.com/photos/1102915/pexels-photo-1102915.jpeg",
            "github": "https://github.com/abhik12295/WeatherApp"
        }
    ]
    for project in projects:
        st.markdown(f"""
        <div class='portfolio-card fade-in'>
            <img src='{project['img']}' alt='{project['title']}' class='portfolio-img'>
            <div class='portfolio-card-title-row'>
                <span class='portfolio-card-title'>{project['title']}</span>
                <a href='{project['github']}' target='_blank' class='portfolio-github-link' title='GitHub'>
                    <i class="fab fa-github"></i>
                </a>
            </div>
            <p>{project['desc']}</p>
            <ul class='tech-tags'>
                {"".join(f"<li>{tech}</li>" for tech in project['tech'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Contact ---
    st.markdown("<div id='contact' class='section'>", unsafe_allow_html=True)
    st.markdown("<h2 class='fade-in' style='text-align:center;'>Get in Touch</h2>", unsafe_allow_html=True)
    st_lottie(load_lottieurl("https://lottie.host/d18aef06-2248-47b4-a2d0-ec449568158a/RijoOeBqPJ.json"), height=180, width=180)
    st.markdown("<p class='fade-in' style='text-align:center;'>Let’s collaborate on your next data-driven project!</p>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("""
        <style>
        .contact-info {
            background: linear-gradient(120deg, #232526 0%, #3a3a3a 100%);
            border-radius: 16px;
            box-shadow: 0 3px 16px 0 rgba(0,114,255,0.10), 0 1px 4px 0 rgba(0,0,0,0.10);
            padding: 24px 22px 18px 22px;
            color: #f8f9fa;
            border: 2px solid #ffd700;
            margin-bottom: 18px;
        }
        .contact-info h4 {
            color: #ffd700;
            margin-bottom: 10px;
        }
        .contact-info p, .contact-info a {
            color: #f8f9fa;
            font-size: 1.01rem;
            margin-bottom: 8px;
        }
        .contact-info i {
            color: #ffd700;
            margin-right: 8px;
        }
        .availability {
            background: linear-gradient(120deg, #232526 0%, #414345 100%);
            border-radius: 14px;
            box-shadow: 0 2px 10px 0 rgba(0,198,255,0.10);
            padding: 18px 18px 12px 18px;
            color: #b2eaff;
            border: 2px solid #00c6ff;
            margin-top: 10px;
            font-size: 1.01rem;
        }
        .availability strong {
            color: #ffd700;
        }
        </style>
        <div class='contact-info fade-in'>
            <h4>Contact Details</h4>
            <p><i class='fas fa-envelope'></i> <a href='mailto:abhik12295@gmail.com'>abhik12295@gmail.com</a></p>
            <p><i class='fas fa-map-marker-alt'></i> Memphis, TN, USA</p>
            <p><i class='fas fa-calendar-alt'></i> <a href='https://calendly.com/abhik12295' target='_blank'>Schedule a Call</a></p>
        </div>
        <div class='availability fade-in'>
            <p><strong>Currently open to new opportunities</strong> and collaborations in data science, ML, and analytics. Feel free to reach out!</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <style>
        .contact-form {
            background: linear-gradient(120deg, #232526 0%, #3a3a3a 100%);
            border-radius: 16px;
            box-shadow: 0 3px 16px 0 rgba(0,114,255,0.10), 0 1px 4px 0 rgba(0,0,0,0.10);
            padding: 28px 32px 22px 32px;
            color: #f8f9fa;
            border: 2px solid #00c6ff;
            max-width: 500px;
            margin-right: inherit;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px 12px;
            margin-bottom: 14px;
            border-radius: 8px;
            border: 1.5px solid #343a40;
            background: #232526;
            color: #f8f9fa;
            font-size: 1rem;
            resize: vertical;
        }
        .contact-form textarea {
            min-height: 90px;
            max-height: 200px;
        }
        .pulse-btn {
            background: linear-gradient(90deg, #0072ff 0%, #00c6ff 100%);
            color: #fff;
            border: none;
            border-radius: 22px;
            padding: 10px 28px;
            font-size: 1.08rem;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 2px 8px 0 rgba(0,114,255,0.13);
            transition: background 0.3s, transform 0.2s;
            animation: pulse 1.5s infinite;
        }
        .pulse-btn:hover {
            background: linear-gradient(90deg, #00c6ff 0%, #0072ff 100%);
            transform: scale(1.04);
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(0,198,255,0.3);}
            70% { box-shadow: 0 0 0 10px rgba(0,198,255,0);}
            100% { box-shadow: 0 0 0 0 rgba(0,198,255,0);}
        }
        </style>
        <form action="https://formsubmit.co/059cd784e788c85ed5add9aed225bb53" method="POST" class="contact-form fade-in">
            <input type="hidden" name="_captcha" value="true">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit" class='pulse-btn'><i class="fas fa-paper-plane"></i> Send Message</button>
        </form>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # --- Footer ---
    st.markdown("<div class='footer'>", unsafe_allow_html=True)
    st.markdown("""
    <div class='footer-content fade-in'>
        <div class='footer-links'>
            <h4>Quick Links</h4>
            <a href='#about'>About</a>
            <a href='#portfolio'>Portfolio</a>
            <a href='#contact'>Contact</a>
        </div>
        <div class='footer-social' style='text-align: center;'>
            <h4>Connect</h4>
            <div class='social-links' style='display: flex; justify-content: center; gap: 18px; align-items: center; margin: 10px auto 10px auto;'>
                <a href='https://www.facebook.com/abhi120694/' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/733/733547.png' alt='Facebook' class='social-icon' style='width: 35px; height: 35px'></a>
                <a href='https://x.com/abhi_1294' target='_blank'><img src='https://img.icons8.com/?size=100&id=oaaSr6h7kwm6&format=png&color=000000' alt='X' class='social-icon' style='width: 35px; height: 35px'></a>
                <a href='https://www.linkedin.com/in/abhik12295/' target='_blank'><img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn' class='social-icon' style='width: 35px; height: 35px'></a>
                <a href='https://github.com/abhik12295' target='_blank'><img src='https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000' alt='GitHub' class='social-icon' style='width: 35px; height: 35px'></a>
            </div>
        </div>
        <div class='footer-newsletter'>
            <h4>Stay Updated</h4>
            <form action='https://formsubmit.co/059cd784e788c85ed5add9aed225bb53' method='POST'>
                <input type='email' name='email' placeholder='Your Email' required>
                <button type='submit'>Subscribe</button>
            </form>
        </div>
    </div>
    <p class='footer-credit'>© 2025 Abhishek Kumar. Built with <a href='https://streamlit.io/' class='footer-link'>Streamlit</a>.</p>
    <a href='#about' class='back-to-top'><i class='fas fa-arrow-up'></i></a>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)