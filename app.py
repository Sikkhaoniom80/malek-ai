import streamlit as st
import pandas as pd

st.set_page_config(page_title="Malek AI - Fabric QC", layout="wide", page_icon="🧵")

# --- Login Page ---
if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.markdown("<h1 style='text-align:center;'>🧵 Malek AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>আপনার ফ্যাক্টরির পাহারাদার | Your Factory Guard</p>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("🔐 Factory Login")
        factory = st.selectbox("Factory Name", ["Gazipur Textile", "Narayanganj Knit", "Ashulia Fabrics", "Demo Factory"])
        password = st.text_input("Password", type="password", value="1234")
        st.info("Demo Password: 1234")
        if st.button("Login to Dashboard", use_container_width=True, type="primary"):
            st.session_state.login = True
            st.session_state.factory = factory
            st.rerun()
else:
    # --- Dashboard ---
    factory_name = st.session_state.factory
    
    # Sidebar
    st.sidebar.title(f"🏭 {factory_name}")
    st.sidebar.markdown("**Malek AI v3.1**")
    st.sidebar.success("● LIVE - Connected")
    st.sidebar.divider()
    st.sidebar.write("Supervisor: Malek")
    st.sidebar.write("Support: 01XXX-XXXXXX")
    if st.sidebar.button("Logout"):
        st.session_state.login = False
        st.rerun()

    # Main
    st.title(f"AI Fabric Inspection Dashboard")
    st.caption(f"Factory: {factory_name} | Powered by Malek AI | LIVE Real-time")

    col1, col2, col3 = st.columns(3)
    col1.metric("আজকের পরীক্ষা / Today's Check", "1250 মিটার", "+120m")
    col2.metric("ত্রুটি / Defects", "14 টা", "2 critical", delta_color="inverse")
    col3.metric("নির্ভুলতা / Accuracy", "94%", "+2.1%")

    st.divider()
    
    left, right = st.columns([1.2, 1])
    
    with left:
        st.subheader("ত্রুটি তালিকা / Defect List")
        df = pd.DataFrame({
            "সময়": ["10:30 AM", "10:02 AM", "09:45 AM", "09:12 AM"],
            "ধরণ": ["Weave Gap", "Hole", "Stain", "Slub"],
            "অবস্থান": ["Line-A (12.5m)", "Line-C (45.2m)", "Line-B (89m)", "Line-A (102m)"],
            "Status": ["🔴 Flagged", "🟡 Pending", "🟢 Resolved", "🟢 Resolved"]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

    with right:
        st.subheader("সনাক্তকৃত ত্রুটি / Detected Defect")
        st.error("Hole Detected - 95% confidence")
        st.image("https://images.unsplash.com/photo-1520903924103-00d8a0452a04?q=80&w=600", caption="ID: DEF-1024 | Location: Line-C")
        st.write("Type: Hole / ছিদ্র")
        st.write("Location: Line-C, Roller-3 | Time: 10:02 AM")
        st.button("✅ Resolve / সমাধান করুন", use_container_width=True, type="primary")
    
    st.divider()
    st.caption("AI Model: FabricNet v3.1 (YOLOv11) | Running on Edge Device #GT-07 | System Status: Online ● | © 2026 Malek AI")
