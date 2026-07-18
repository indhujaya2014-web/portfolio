import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Jayapoorani M | Data Science Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# LOAD CSS
# =========================================================
CSS_FILE = Path(__file__).parent / "style.css"
if CSS_FILE.exists():
    st.markdown(
        f"<style>{CSS_FILE.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True,
    )

# =========================================================
# PORTFOLIO DATA
# =========================================================
DATA = {
    "profile": {
        "name": "Jayapoorani M",
        "headline": "Data Analyst • Data Scientist",
        "tagline": "Turning enterprise data into reliable insights, intelligent models, and deployable solutions.",
        "location": "Chennai, Tamil Nadu, India",
        "email": "indhujaya2014@gmail.com",
        "phone": "+91-9176252250",
        "github": "https://github.com/indhujaya2014-web",
        "linkedin": "https://linkedin.com/in/jayapoorani-m-2b4501120",
        "summary": (
            "Data Analyst and aspiring Data Scientist with 5+ years of IT experience in "
            "data validation, SQL analytics, automation, and cloud data migration. "
            "Completed the Master Data Science Program at GUVI with hands-on experience "
            "in Python, SQL, Machine Learning, Deep Learning, ETL, Power BI, Streamlit, "
            "and Data Visualization."
        ),
    },
    "metrics": [
        ("5+", "Years IT Experience"),
        ("3", "Featured DS Projects"),
        ("95.8%", "Best Classification"),
        ("60%", "Manual Effort Reduced"),
    ],
    "skills": {
        "Programming": [("Python", 95), ("SQL", 90), ("Java", 82), ("JavaScript", 65)],
        "Analytics": [("Pandas / NumPy", 95), ("EDA", 92), ("Feature Engineering", 88), ("Statistics", 85)],
        "Machine Learning": [("Scikit-learn", 90), ("Random Forest", 92), ("XGBoost", 90), ("Model Tuning", 85)],
        "Deep Learning": [("TensorFlow / Keras", 80), ("CNN", 82), ("YOLOv8", 85), ("OpenCV", 78)],
        "Data & Cloud": [("Power BI", 90), ("Streamlit", 92), ("MySQL", 88), ("BigQuery / Vertica", 85)],
    },
    "experience": [
        {
            "role": "Data Validation & Automation Engineer",
            "company": "Mphasis",
            "period": "09/2019 – 03/2025",
            "description": "Validated enterprise-scale data across cloud and database environments while automating quality and reconciliation workflows.",
            "achievements": [
                "Validated large-scale datasets between Google BigQuery and Vertica.",
                "Supported AWS-to-GCP migration validation across millions of records.",
                "Automated data validation workflows using Selenium and Java.",
                "Performed SQL-based root cause analysis for complex data mapping issues.",
            ],
        },
        {
            "role": "Automation & Data Quality Analyst",
            "company": "Mphasis",
            "period": "09/2019 – 03/2025",
            "description": "Built quality automation and API validation frameworks integrated with enterprise delivery workflows.",
            "achievements": [
                "Reduced manual validation effort by 60%.",
                "Designed REST API validation frameworks using Postman.",
                "Integrated automated validation into Azure DevOps CI/CD pipelines.",
            ],
        },
        {
            "role": "QA Automation Engineer",
            "company": "Mphasis",
            "period": "09/2019 – 03/2025",
            "description": "Developed reusable automation frameworks and contributed to continuous quality improvement.",
            "achievements": [
                "Developed Selenium automation frameworks using Java.",
                "Automated regression testing across enterprise applications.",
                "Contributed to a 15% reduction in critical software defects.",
            ],
        },
    ],
    "projects": [
        {
            "title": "Harvard's Artifacts Collection",
            "icon": "🏛️",
            "category": "ETL & Analytics",
            "stack": ["Python", "SQL", "MySQL", "REST API", "ETL", "Streamlit"],
            "metric": "End-to-end ETL",
            "objective": "Build a scalable data engineering and analytics platform for museum artifact metadata.",
            "workflow": "API Extraction → JSON Cleaning → Transformation → MySQL Storage → SQL Analytics → Streamlit Exploration",
            "outcome": "Automated the complete data ingestion and analytics workflow for interactive artifact exploration.",
            "github": "https://github.com/indhujaya2014-web",
        },
        {
            "title": "EcoType — Forest Cover Prediction",
            "icon": "🌲",
            "category": "Machine Learning",
            "stack": ["Python", "Scikit-learn", "Random Forest", "XGBoost", "Streamlit"],
            "metric": "95.4% Accuracy",
            "objective": "Predict dominant forest cover types from environmental and geographical features.",
            "workflow": "EDA → Preprocessing → Feature Engineering → Model Comparison → Evaluation → Deployment",
            "outcome": "Created a complete multi-class machine learning pipeline with real-time Streamlit prediction.",
            "github": "https://github.com/indhujaya2014-web",
        },
        {
            "title": "Aerial Object Classification & Detection",
            "icon": "🚁",
            "category": "Deep Learning",
            "stack": ["TensorFlow", "Keras", "CNN", "YOLOv8", "OpenCV"],
            "metric": "95.8% Classification",
            "objective": "Identify birds and drones from aerial imagery for surveillance and wildlife monitoring.",
            "workflow": "Image Preprocessing → CNN Classification → YOLOv8 Detection → Real-time Inference",
            "outcome": "Delivered an end-to-end computer vision pipeline with 95.8% classification and 89.4% detection performance.",
            "github": "https://github.com/indhujaya2014-web",
        },
    ],
    "education": [
        {
            "degree": "Bachelor of Engineering (B.E.)",
            "field": "Electronics & Communication Engineering",
            "institution": "Agni College of Technology",
            "location": "Chennai",
            "year": "2017",
            "icon": "🎓"
        },
        {
            "degree": "Advanced Professional Program in Master Data Science",
            "field": "Data Science",
            "institution": "GUVI",
            "location": "India",
            "year": "Completed",
            "icon": "📊"
        }
    ],
    "certifications": [
        ("🎓", "B.E. Electronics & Communication Engineering", "AGNI COLLEGE OF TECHNOLOGY"),
        ("🎓", "Master Data Science Program", "GUVI"),
        ("🏆", "Selenium & Java Foundation Certification", "Professional Certification"),
        ("🥇", "Summit Award for Excellence", "Mphasis"),
        ("⭐", "SPOT Award", "Mphasis"),
    ],
}

# =========================================================
# HELPERS
# =========================================================
def section_title(kicker, title, description=""):
    st.markdown(
        f"""
        <div class="section-heading">
            <div class="section-kicker">{kicker}</div>
            <h2>{title}</h2>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def open_link(url, label):
    st.markdown(f'<a class="premium-link" href="{url}" target="_blank">{label} ↗</a>', unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    # st.markdown('<div class="sidebar-brand">JM<span>.</span></div>', unsafe_allow_html=True)
    # st.markdown(f"### {DATA['profile']['name']}")
    # st.caption(DATA["profile"]["headline"])
    # st.divider()
    st.markdown("### Navigation")
    st.markdown(
        """
        <div class="sidebar-menu">
            <a href="#home">⌂ Home</a>
            <a href="#about">◉ About</a>
            <a href="#experience">◈ Experience</a>
            <a href="#skills">✦ Skills</a>
            <a href="#projects">▣ Projects</a>
            <a href="#education">✎ Education</a>
            <a href="#contact">✉ Contact</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()
    st.caption("Open to Data Analyst, Data Scientist and Machine Learning opportunities.")
    # st.markdown(
    #     f'<a class="sidebar-social" href="{DATA["profile"]["github"]}" target="_blank">GitHub ↗</a>',
    #     unsafe_allow_html=True,
    # )
    # st.markdown(
    #     f'<a class="sidebar-social" href="{DATA["profile"]["linkedin"]}" target="_blank">LinkedIn ↗</a>',
    #     unsafe_allow_html=True,
    # )

# =========================================================
# DECORATIVE BACKGROUND
# =========================================================
st.markdown(
    """
    <div class="ambient ambient-one"></div>
    <div class="ambient ambient-two"></div>
    <div class="grid-overlay"></div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HERO
# =========================================================
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

hero_left, hero_right = st.columns([1.7, 1], gap="large")

with hero_left:
    st.markdown(
        """
        <div class="eyebrow"><span class="pulse-dot"></span> AVAILABLE FOR DATA & AI OPPORTUNITIES</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="hero-title">
            <span class="hero-small">Hello, I'm</span>
            <span class="hero-name">{DATA['profile']['name']}</span>
            <span class="hero-role">{DATA['profile']['headline']}</span>
        </div>
        <div class="typing-line">
            Python <span>•</span> SQL <span>•</span> Machine Learning <span>•</span> Deep Learning <span>•</span> Power BI
        </div>
        <p class="hero-tagline">{DATA['profile']['tagline']}</p>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 1, 1], gap="medium")
    with c1:
        try:
            with open("assets/resume.pdf", "rb") as r_file:
                r_bytes = r_file.read()
            st.download_button("Download Resume (PDF)", data=r_bytes, file_name="Jayapoorani_Resume.pdf", mime="application/pdf")
        except FileNotFoundError:
            st.download_button("Download CV portfolio", data="Standard resume file is currently being prepared.", file_name="readme.txt")

    with c2:
        st.link_button("GitHub ↗", DATA["profile"]["github"], use_container_width=True)
    with c3:
        st.link_button("LinkedIn ↗", DATA["profile"]["linkedin"], use_container_width=True)

with hero_right:
    st.markdown(
        """
        <div class="profile-orbit">
            <div class="orbit orbit-a"></div>
            <div class="orbit orbit-b"></div>
            <div class="profile-core">
                <div class="profile-initials">JM</div>
                <div class="profile-status"><span></span> DATA + AI</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

metric_cols = st.columns(4)
for col, (value, label) in zip(metric_cols, DATA["metrics"]):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-value">{value}</div>
                <div class="metric-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# ABOUT
# =========================================================
st.markdown('<div id="about" class="anchor-offset"></div>', unsafe_allow_html=True)
section_title(
    "01 / PROFILE",
    "Building reliable data products from messy data.",
    "A career shaped by quality engineering, analytics, automation and applied data science.",
)

about_left, about_right = st.columns([1.35, 1], gap="large")

with about_left:
    st.markdown(
        f"""
        <div class="glass-panel about-panel">
            <div class="quote-mark">“</div>
            <p>{DATA['profile']['summary']}</p>
            <div class="about-tags">
                <span>Data Quality</span>
                <span>Analytics</span>
                <span>Machine Learning</span>
                <span>Cloud Data</span>
                <span>Deployment</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with about_right:
    st.markdown(
        """
        <div class="glass-panel">
            <div class="mini-label">CURRENT FOCUS</div>
            <h3>From validation to intelligence.</h3>
            <p class="muted">
            I combine enterprise data experience with modern data science to create
            solutions that are measurable, explainable and ready to deploy.
            </p>
            <div class="focus-row"><span>01</span><b>Discover</b><small>Understand the data and business problem</small></div>
            <div class="focus-row"><span>02</span><b>Build</b><small>Engineer features and develop robust models</small></div>
            <div class="focus-row"><span>03</span><b>Deploy</b><small>Turn analysis into accessible applications</small></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# EXPERIENCE
# =========================================================
st.markdown('<div id="experience" class="anchor-offset"></div>', unsafe_allow_html=True)
section_title(
    "02 / EXPERIENCE",
    "Enterprise experience with a data-first mindset.",
    "Building quality systems, validating large-scale data and automating repeatable workflows.",
)

for index, exp in enumerate(DATA["experience"], start=1):
    with st.expander(f"{index:02d}  {exp['role']}  ·  {exp['company']}  ·  {exp['period']}", expanded=(index == 1)):
        left, right = st.columns([1.1, 1.9])
        with left:
            st.markdown(f'<div class="role-badge">{exp["company"]}</div>', unsafe_allow_html=True)
            st.markdown(f"### {exp['role']}")
            st.caption(exp["period"])
        with right:
            st.markdown(exp["description"])
            for achievement in exp["achievements"]:
                st.markdown(f'<div class="achievement">↳ {achievement}</div>', unsafe_allow_html=True)

# =========================================================
# SKILLS
# =========================================================
st.markdown('<div id="skills" class="anchor-offset"></div>', unsafe_allow_html=True)
section_title(
    "03 / TECHNICAL CORE",
    "A practical toolkit across the data lifecycle.",
    "From Python and SQL to machine learning, deep learning, visualization and cloud data platforms.",
)

skill_left, skill_right = st.columns([1, 1.2], gap="large")

with skill_left:
    radar_categories = ["Python", "SQL", "Analytics", "ML", "DL", "Deployment"]
    radar_values = [95, 90, 92, 90, 82, 90]
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=radar_values + [radar_values[0]],
            theta=radar_categories + [radar_categories[0]],
            fill="toself",
            line=dict(color="#8b5cf6", width=3),
            fillcolor="rgba(139,92,246,0.20)",
        )
    )
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 100], showticklabels=False, gridcolor="rgba(255,255,255,0.08)"),
            angularaxis=dict(color="#cbd5e1", gridcolor="rgba(255,255,255,0.05)"),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=30, r=30, t=20, b=20),
        height=430,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

with skill_right:
    tabs = st.tabs(list(DATA["skills"].keys()))
    for tab, category in zip(tabs, DATA["skills"].keys()):
        with tab:
            for name, score in DATA["skills"][category]:
                st.markdown(
                    f"""
                    <div class="skill-row">
                        <div class="skill-name"><span>{name}</span><span>{score}%</span></div>
                        <div class="skill-track"><div class="skill-fill" style="width:{score}%"></div></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# =========================================================
# PROJECTS
# =========================================================
st.markdown('<div id="projects" class="anchor-offset"></div>', unsafe_allow_html=True)
section_title(
    "04 / SELECTED WORK",
    "Projects that move from idea to deployment.",
    "A selection of applied projects demonstrating ETL, analytics, machine learning and computer vision.",
)

categories = ["All"] + sorted({p["category"] for p in DATA["projects"]})

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

st.markdown(
    '<div class="filter-label">FILTER BY DISCIPLINE</div>',
    unsafe_allow_html=True
)

filter_cols = st.columns(len(categories))

for col, category in zip(filter_cols, categories):
    with col:
        if st.button(
            category,
            key=f"filter_{category}",
            use_container_width=True
        ):
            st.session_state.selected_category = category

selected = st.session_state.selected_category

visible_projects = DATA["projects"] if selected == "All" else [p for p in DATA["projects"] if p["category"] == selected]

for p in visible_projects:
    st.markdown(
        f"""
        <div class="project-card">
            <div class="project-topline">
                <span class="project-icon">{p['icon']}</span>
                <span class="project-category">{p['category']}</span>
            </div>
            <h3>{p['title']}</h3>
            <div class="project-metric">{p['metric']}</div>
            <p class="project-objective">{p['objective']}</p>
            <div class="tech-list">
                {"".join([f"<span>{tech}</span>" for tech in p["stack"]])}
            </div>
            <div class="project-divider"></div>
            <div class="project-grid">
                <div><small>WORKFLOW</small><p>{p['workflow']}</p></div>
                <div><small>OUTCOME</small><p>{p['outcome']}</p></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    a, b = st.columns([1, 5])
    with a:
        st.link_button("Repository ↗", p["github"])

# =========================================================
# Education & CERTIFICATIONS
# =========================================================
st.markdown(
    '<div id="education" class="anchor-offset"></div>',
    unsafe_allow_html=True
)
section_title(
    "05 / CREDENTIALS",
    "Education, Continuous Learning & recognized performance.",
    "Certifications and recognition supporting a career transition into data science.",
)

cert_cols = st.columns(5)
for col, (icon, title, issuer) in zip(cert_cols, DATA["certifications"]):
    with col:
        st.markdown(
            f"""
            <div class="cert-card">
                <div class="cert-icon">{icon}</div>
                <h4>{title}</h4>
                <p>{issuer}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# =========================================================
# CONTACT
# =========================================================
st.markdown('<div id="contact" class="anchor-offset"></div>', unsafe_allow_html=True)
section_title(
    "06 / CONTACT",
    "Let's build something meaningful with data.",
    "Open to conversations about data analytics, data science, machine learning and applied AI opportunities.",
)

contact_left, contact_right = st.columns([1.1, 1], gap="large")

with contact_left:
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        message = st.text_area("Message", height=140)
        submitted = st.form_submit_button("Send Message →")
        if submitted:
            if name and email and message:
                st.success(f"Thanks, {name}. Your message has been prepared successfully.")
            else:
                st.warning("Please complete all fields before submitting.")

with contact_right:
    st.markdown(
        f"""
        <div class="glass-panel contact-card">
            <div class="mini-label">DIRECT CHANNELS</div>
            <p>📍 {DATA['profile']['location']}</p>
            <p>✉️ <a href="mailto:{DATA['profile']['email']}">{DATA['profile']['email']}</a></p>
            <p>📞 {DATA['profile']['phone']}</p>
            <div class="contact-links">
                <a href="{DATA['profile']['github']}" target="_blank">GitHub ↗</a>
                <a href="{DATA['profile']['linkedin']}" target="_blank">LinkedIn ↗</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
    <div class="footer">
        <div>© {datetime.now().year} {DATA['profile']['name']}</div>
        <div>Designed with Python · Streamlit · Data</div>
    </div>
    """,
    unsafe_allow_html=True,
)
