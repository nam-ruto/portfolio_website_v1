import streamlit as st

pg = st.navigation([st.Page("app.py", title="Home", icon="🎯"), 
                    st.Page("blog.py", title="Blog", icon="📖")])

pg.run()