import streamlit as st
from pathlib import Path
from PIL import Image
from blog_post import blog_1, blog_2

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "blog.css"
blog_1_pic_dir = current_dir / "assets" / "blog_thumbnail" / "hackathon.jpg"
blog_2_pic_dir = current_dir / "assets" / "blog_thumbnail" / "RAG.png"

# GENERAL SETTINGS
PAGE_TITLE = "Blog | Nam Hoang"
PAGE_ICON = "📖"
SUB_TITLE = '''👋🏻Welcome to my blog! This blog focuses on computer science topics, 
                showcasing various projects, and sharing insights to 
                promote knowledge within the community'''

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout='centered')

# LOAD CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# LOAD PICTURES
blog_1_pic = Image.open(blog_1_pic_dir)
blog_2_pic = Image.open(blog_2_pic_dir)


# Handle navigation
if "page" not in st.session_state:
    st.session_state["page"] = "home"  # Default page

# Callback functions for navigation
def navigate_to_home():
    st.session_state["page"] = "home"

def navigate_to_blog1():
    st.session_state["page"] = "blog1"

def navigate_to_blog2():
    st.session_state["page"] = "blog2"

# Render content based on current page
if st.session_state["page"] == "home":
    # INTRODUCTION
    st.title(PAGE_TITLE)
    st.write(SUB_TITLE)
    st.markdown('<hr style="height:2px;border-width:0;color:gray;background-color:gray">', unsafe_allow_html=True)

    # BLOG LAYOUT
    row1_1, row1_2 = st.columns(2, gap='large', border=True)
    with row1_1:
        st.image(blog_1_pic)
        st.markdown(':blue-background[22/12/2024]')
        st.markdown('##### I Led a team of 3 members to win the MVP title at TroyHack 2024!!!')
        st.button("Read more", on_click=navigate_to_blog1, key=1)

    with row1_2:
        st.image(blog_2_pic)
        st.markdown(':blue-background[22/12/2024]')
        st.markdown('##### Retrieval-Augmented Generation (RAG): Revolutionizing Information Retrieval')
        st.button("Read more", on_click=navigate_to_blog2, key=2)

elif st.session_state["page"] == "blog1":
    st.button("Back to Blog Page", on_click=navigate_to_home, key=3)
    blog_1.show()

elif st.session_state["page"] == "blog2":
    st.button("Back to Blog Page", on_click=navigate_to_home, key=4)
    blog_2.show()