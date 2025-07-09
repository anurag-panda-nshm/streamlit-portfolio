import streamlit as st

st.title("💼 My Projects")

projects = [
    {
        "title": "Smart Attendance System (Face Recognition)",
        "desc": "Face detection and attendance tracking using Python, SQLite, and OpenCV with Supabase dashboards.",
        "demo": "",
        "repo": "https://github.com/anurag-panda-nshm/face-attendance-maker"
    },
    {
        "title": "NeuroFit Band (Mental Wellness Device)",
        "desc": "ESP32 + EEG + Pulse sensor-based wearable to track mood, stress, focus using ML and mobile app.",
        "demo": "",
        "repo": "https://github.com/anurag1818/NeuroFit-v0.2"
    },
    {
        "title": "Math Graphing & Integration Tool",
        "desc": "Do graphing, derivatives, integration and more easily in a math web app.",
        "demo": "https://calculator-anurag-nshm.streamlit.app",
        "repo": "https://github.com/anurag1818/scientific-cum-graph-calculator"
    },
    {
        "title": "Interactive Periodic Table Tool",
        "desc": "Know about Elements and explore by the interaction of color coding easily in a chemistry web app.",
        "demo": "https://interactive-periodic-table-anurag.streamlit.app",
        "repo": "https://github.com/anurag-panda-dev/interactive-periodic-table"
    },
    {
        "title": "Math Graphing Tool (2D & 3D)",
        "desc": "Do graphing (2D & 3D) and download easily in a math web app.",
        "demo": "https://graph-plotter-2d-3d-anurag.streamlit.app",
        "repo": "https://github.com/anurag-panda-dev/graph-plotter-2D-3D"
    }
]

for proj in projects:
    st.subheader(proj["title"])
    st.write(proj["desc"])
    if proj["demo"]:
        st.markdown(f"[🔗 Live Demo]({proj['demo']})")
    st.markdown(f"[💻 GitHub Repo]({proj['repo']})")
    st.markdown("---")
