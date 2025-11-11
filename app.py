import streamlit as st

# Page configuration
st.set_page_config(page_title="TGTWRDCn", page_icon=":mortar_board:", layout="wide")

# HEADER SECTION
st.subheader("Welcome to :blue[TGTWRDC ADB College] :wave:")
st.title("Empowering Students for a Brighter Future")
st.write("Discover our departments, courses, faculty, and upcoming events — all in one place!")

# --- ABOUT SECTION ---
st.header("About Our College")
st.write("""
TGTWRDC College was established in 2018 with the vision of providing quality education 
in science, technology, and arts. Our mission is to prepare students with strong academic foundations 
and real-world skills to succeed in their chosen careers.
""")

# --- DEPARTMENTS SECTION ---
st.header("Departments")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💻 Computer Science")
    st.write("Learn programming, AI, data analytics, and software development.")
with col2:
    st.subheader("🔬 Science & Research")
    st.write("Focus on innovation and discovery in physics, chemistry, and biology.")
with col3:
    st.subheader("📊 Business & Management")
    st.write("Develop leadership, finance, and entrepreneurship skills.")

# --- COURSES SECTION ---
st.header("Popular Courses")
courses = [
    "B.Sc Computer Science",
    "B.A English Literature",
    "B.Com Accounting",
    "B.Sc Data Science"
    
]
st.write("🎯 Here are some of our most popular programs:")
for course in courses:
    st.markdown(f"- {course}")

# --- FACULTY SECTION ---
st.header("Our Faculty")
st.write("""
Our experienced faculty members are dedicated to guiding students toward academic and professional success.
""")

faculty_data = {
    "Preetham": "Head of Computer Science Department",
    "laxman": "Head of Business & Management",
    "Dr.madhukar": "Head of Science & Research"
}
for name, role in faculty_data.items():
    st.markdown(f"**{name}** — *{role}*")

# --- EVENTS SECTION ---
st.header("Upcoming Events")
st.info("""
🎓 *Annual College Fest* - December 10, 2025  
🧠 *Tech Symposium* - January 22, 2026  
🏆 *Sports Meet* - February 15, 2026
""")

# --- CONTACT SECTION ---
st.header("Contact Us")
st.write("📍 TGTWRDC College, adilabad, telangana")
st.write("📞 +91 6301643804")
st.write("✉️ naithammaruthi18@gmail.com")

st.success("Thank you for visiting our college website!")
