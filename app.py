import streamlit as st
from pathlib import Path
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "NamHoang_DE.pdf"
profile_pic = current_dir / "assets" / "NamHoang.png"


# GENERAL SETTINGS
PAGE_TITLE = "Portfolio | Nam Hoang"
PAGE_ICON = "😎:"
NAME = "Nam Hoang"
DESCRIPTION = """
Software Engineer @ ISODS | Data Engineer @ FPT Software | MVP Winners @ TroyHack 2024
"""
EMAIL = "hoangducnam.work@gmail.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/nam-hd",
    "GitHub": "https://github.com/nam-ruto",
    "LeetCode": "https://leetcode.com/u/nam-ruto/",
    "Facebook": "https://www.facebook.com/nam.doffy/",
}
PROJECTS = {
    "🏆 Chancellor’s List - Spring 2024: Recognized for academic excellence": "https://www.linkedin.com/in/nam-hd",
    "🏆 MVP of TroyHack 2024: Developed an AI Chatbot solution during 24-hoursHackathon, achieving the MVP title": "https://www.linkedin.com/in/nam-hd",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=240)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(label="📃Download Resume",
                       data=PDFbyte,
                       file_name=resume_file.name,
                       mime="application/octet-stream")
    st.write("📫", EMAIL)
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    """
- ✅ Expereince in building the Data Pipeline and the ETL process
- ✅ Good understanding of Data Modeling and Query Optimization
- ✅ Excellent team-player and displaying strong sense of initiative on tasks
- ✅ Strong hands on experience and knowledge in many programming language
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 Programming: Python, R, C++, Java
- 📊 Data Cleaning: ETL, Data Pipeline
- 🗄️ Databases: Postgres, MySQL, SQL Server, MariaDB
- 📚 LLM: Langchain, Ollama, RAG, Fine-Tuning 
"""
)


# --- Experience ---
st.write('\n')
st.subheader("Hands-on Experience")
st.html('''<hr style="height:2px;border-width:0;padding-bottom:0;;color:gray;background-color:gray">''')

# --- JOB 1
st.write("📍", "**Software Engineer Intern | The George Washington Institute (ISODS)**")
st.write("June 2024 - Dec 2024")
st.write(
    """
- ► Collected data from diverse sources for the training and fine-tuning of large language models.
- ► Employed data cleaning and preprocessing, improving data quality by 30%, which resulted in optimized model performance
- ► Designed and implemented an RAG system, enhancing AI Chatbot services with a 20% increase in response accuracy and relevance
- ► Built a robust backend using Flask to handle chatbot service logic, including user query processing, model integration, session management, and interaction flow
"""
)

# --- JOB 2
st.write('\n')
st.write("📍", "**Data Engineer | FPT Software**")
st.write("May 2024 - August 2024")
st.write(
    """
- ► Developed a Data Interface library capable of retrieving data from multiple database systems and cloud platforms, enhancing data accessibility and integration
- ► Integrated this module into the ETL pipeline, enabling seamless extraction, transformation, and loading of data from diverse sources
- ► Implemented optimized database queries and efficient data handling techniques, achieving a 30% reduction in ETL execution time and significantly improving system responsiveness

"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("HONORS AND REWARD")
st.html('''<hr style="height:2px;border-width:0;padding-bottom:0;;color:gray;background-color:gray">''')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")