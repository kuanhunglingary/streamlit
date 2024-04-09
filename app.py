from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kuan-Hung Lin"
PAGE_ICON = ":wave:"
NAME = "Kuan-Hung Lin"
# DESCRIPTION = """
# Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.
# """
EMAIL = "g12021202@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://www.youtube.com/@g12021202/",
    "LinkedIn": "https://www.linkedin.com/in/kuan-hung-lin-045874b6/",
    "GitHub": "https://github.com/kuanhunglingary",
    # "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Ollama LiteLLM": "https://github.com/kuanhunglingary/ollamaLiteLLM",
    "🏆 Use Django framewrk to present all of my projects this year": "https://github.com/kuanhunglingary/DjangoPortfolio_",
    "🏆 RPA_OCR_WebScrapy": "https://github.com/kuanhunglingary/pythonPersonalTools",
    "🏆 Preprocess yfinace and Finmind dataset and then visualizing information": "https://github.com/kuanhunglingary/stock_visualization",
    "🏆 stock SQLite GUI Tkinter and SQL to csv": "https://github.com/kuanhunglingary/SQLite",
    "🏆 stock GUI Tkinter": "https://github.com/kuanhunglingary/stock_GUI_Tkinter",
    "🏆 Web Scrapy Old Building": "https://github.com/kuanhunglingary/Web_Scrapy_Old_Building",
    "🏆 2016 Virginia job description V.S. H-1B Visa Petitions 2011-2016 Datasets": "https://github.com/kuanhunglingary/twoJobDatasetVisualization",
    "🏆 Airline Dataset: Preprocessing and clustering by RStudio & WEKA": "https://github.com/kuanhunglingary/DisasterDataset",
    "🏆 NLPdisasterDataset": "https://github.com/kuanhunglingary/NLPdisasterDataset",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    # st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Education ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- 🎓 M.S. in Data Analytics Engineering George Mason University  2015/1~2017/5
- 🎓 B.S. in Mathematics and Technology Education  National Taipei University of Education 2007/9~2011/6
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 3 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Extensive knowledge in Mathematics & data science.
- ✔️ Experienced content creator on Mathematics & administration
- ✔️ 10 Years experience with running learning institute
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: PowerBi, Tableau, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MySQL, MongoDB
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Big Data Processing Engineer | Groundhog**")
st.write("2023/02 - 2023/05")
st.write(
    """
- ► Ability to use configuration management tools and revision control system, such as Git.
- ► Experience with CI/CD & Automation systems, such as Jenkins and Gitlab.
- ► Understand Linux OS basic operations, such as Ubuntu and Rocky Linux.
- ► Solve the metadata causing the performance, expansion, and the maintenance issues.
- ► Experience coding with Erlang.
- ► Experience with Munin/Nagios/Grafana.
- ► Prepare Install Package for local testing and final release.
- ► Develop big data system and data processing platform.
- ► Develop streaming data and parallel processing program, familiar with distributed computing and parallel computing.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analysis Specialist | HOTAI DEVELOPMENT CO., LTD**")
st.write("2022/06 - 2023/02")
st.write(
    """
- ► Preprocess HOTAI's data, create data visualization, and then write HOTAI's documents
- ► Use python to read, write, and aggregate EXCEL files, and then use EXCEL to analyze the processing data.
- ► Use python to do web crawler collecting data from websites.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Academic Affair and Math teacher | Taipei learning institute**")
st.write("2017/06 - 2022/05")
st.write(
    """
- ► Teach 5-12 grade students
- ► Communicate with teachers, parents, and students.
- ► Handover administration work.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Academic Affair and Math teacher | Taipei learning institute**")
st.write("2012/07 - 2015/01")
st.write(
    """
- ► Teach 5-12 grade students
- ► Communicate with teachers, parents, and students.
- ► Handover administration work.
"""
)

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
