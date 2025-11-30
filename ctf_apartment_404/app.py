import streamlit as st
import os
import base64

# --- Page Config ---
st.set_page_config(
    page_title="HomeOS v9.0 - SYSTEM LOCKED",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Assets ---
ASSETS_DIR = "assets"

def get_asset_path(filename):
    return os.path.join(ASSETS_DIR, filename)

# --- CSS & Styling ---
def load_css():
    st.markdown("""
    <style>
        /* Cyberpunk / Noir Theme */
        body {
            background-color: #050505;
            color: #00f3ff;
            font-family: 'Courier New', Courier, monospace;
        }
        .stApp {
            background-color: #050505;
            background-image: radial-gradient(#111 1px, transparent 1px);
            background-size: 20px 20px;
        }
        
        /* Neon Text */
        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
            color: #00f3ff !important;
            text-shadow: 0 0 5px #00f3ff, 0 0 10px #00f3ff;
        }
        
        /* Inputs */
        .stTextInput > div > div > input {
            background-color: #111;
            color: #00f3ff;
            border: 1px solid #00f3ff;
            font-family: 'Courier New', monospace;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #000;
            color: #00f3ff;
            border: 1px solid #00f3ff;
            box-shadow: 0 0 5px #00f3ff;
            transition: all 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #00f3ff;
            color: #000;
            box-shadow: 0 0 15px #00f3ff;
        }
        
        /* Scanline Effect (Simulated) */
        .scanline {
            width: 100%;
            height: 100px;
            z-index: 9999;
            background: linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(0, 243, 255, 0.1) 50%, rgba(0,0,0,0) 100%);
            opacity: 0.1;
            position: fixed;
            bottom: 100%;
            animation: scanline 10s linear infinite;
            pointer-events: none;
        }
        @keyframes scanline {
            0% { bottom: 100%; }
            100% { bottom: -100%; }
        }
        
        /* Footer Ticker */
        .ticker-wrap {
            position: fixed;
            bottom: 0;
            width: 100%;
            overflow: hidden;
            height: 2rem;
            background-color: #000;
            border-top: 1px solid #00f3ff;
            padding-left: 100%;
            box-sizing: content-box;
        }
        .ticker {
            display: inline-block;
            height: 2rem;
            line-height: 2rem;
            white-space: nowrap;
            padding-right: 100%;
            box-sizing: content-box;
            animation: ticker 30s linear infinite;
            color: #ff0055; /* Red for alert */
        }
        @keyframes ticker {
            0% { transform: translate3d(0, 0, 0); }
            100% { transform: translate3d(-100%, 0, 0); }
        }
        
        /* Hidden Hint for Phase 1 */
        .hidden-hint {
            display: none;
        }
    </style>
    <div class="scanline"></div>
    <div class="ticker-wrap">
        <div class="ticker">
            BREAKING NEWS: ADRIAN VANCE FOUND DEAD IN APARTMENT 404 /// POLICE SUSPECT FOUL PLAY /// SMART HOME SYSTEM LOCKED DOWN /// WEATHER: ACID RAIN EXPECTED TONIGHT /// CRYPTO MARKETS CRASH AFTER VANCE'S DEATH
        </div>
    </div>
    <!-- 
    
    SYSTEM DIAGNOSTIC TOOL
    ----------------------
    ERROR: LOGIN SERVICE UNSTABLE
    DEBUG LOG:
    > Connection established...
    > Verifying user...
    > dev_backup_code: "Op3n_S3sam3_404"
    > User: admin
    
    -->
    """, unsafe_allow_html=True)

# --- State Management ---
if 'phase' not in st.session_state:
    st.session_state.phase = 1
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- Phases ---

def phase_1_login():
    st.title("HomeOS v9.0 - SYSTEM LOCKED")
    st.markdown("### AUTHENTICATION REQUIRED")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username", placeholder="Enter username...")
        password = st.text_input("Password", placeholder="Enter password...", type="password")
        
        if st.button("LOGIN"):
            if username == "admin" and password == "Op3n_S3sam3_404":
                st.success("ACCESS GRANTED. WELCOME, ADMINISTRATOR.")
                st.session_state.phase = 2
                st.rerun()
            else:
                st.error("ACCESS DENIED. INVALID CREDENTIALS.")
                st.session_state.logs.append(f"Failed login attempt: {username}")

def phase_2_webcam():
    st.title("HomeOS v9.0 - DASHBOARD")
    
    tabs = st.tabs(["WEBCAM", "JOURNAL", "SYSTEM"])
    
    with tabs[0]:
        st.subheader("LIVE FEED - LIVING ROOM")
        st.image(get_asset_path("scene.jpg"), caption="CAM_01 [OFFLINE - LAST FRAME]", use_container_width=True)
        
        with open(get_asset_path("scene.jpg"), "rb") as file:
            btn = st.download_button(
                label="DOWNLOAD SNAPSHOT",
                data=file,
                file_name="scene.jpg",
                mime="image/jpeg"
            )
            
    with tabs[1]:
        st.subheader("ENCRYPTED JOURNAL")
        st.write("Enter decryption key to access personal logs.")
        key = st.text_input("Decryption Key")
        if st.button("DECRYPT"):
            if key.upper() == "VIGENERE":
                st.success("DECRYPTION SUCCESSFUL. UNLOCKING IOT LOGS...")
                st.session_state.phase = 3
                st.rerun()
            else:
                st.error("DECRYPTION FAILED.")

    with tabs[2]:
        st.write("System status: PARTIAL LOCKDOWN")

def phase_3_iot():
    st.title("HomeOS v9.0 - IOT LOGS")
    
    tabs = st.tabs(["IOT LOGS", "PHOTO GALLERY", "STICKY NOTES"])
    
    with tabs[0]:
        st.subheader("DEVICE LOGS")
        st.code("""
        [11:30 PM] Lights: OFF
        [11:35 PM] Thermostat: 22°C
        [11:40 PM] Smart Fridge: WMP WXQ MVIK
        [11:41 PM] Smart Oven: ZNEPHF YVRQ
        [11:42 PM] Motion Sensor: TRIGGERED
        """)
        
        st.write("Analyze the corrupted log entry.")
        decrypted = st.text_input("Enter Decrypted Message")
        if st.button("SUBMIT ANALYSIS"):
            if "MARCUS LIED" in decrypted.upper():
                st.success("LOG ENTRY RESTORED. AUDIO FILES UNLOCKED.")
                st.session_state.phase = 4
                st.rerun()
            elif "RX WAS HERE" in decrypted.upper():
                st.warning("INCORRECT KEY. TRY AGAIN.")
            else:
                st.error("INVALID ANALYSIS.")
                
    with tabs[1]:
        st.subheader("GALLERY")
        st.image(get_asset_path("cat_fluffy.jpg"), caption="Fluffy - The best cat ever", width=300)
        
    with tabs[2]:
        st.subheader("NOTES")
        st.info("REMINDER: Fridge Log Encryption Key is the name of my cat.")

def phase_4_audio():
    st.title("HomeOS v9.0 - AUDIO FORENSICS")
    
    st.subheader("CORRUPTED AUDIO FILE RECOVERED")
    st.write("File: evidence_audio.wav")
    st.write("Status: CORRUPTED (PLAYBACK SPEED ERROR)")
    
    audio_file = open(get_asset_path("evidence_audio.wav"), 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
    
    st.download_button(
        label="DOWNLOAD AUDIO FILE",
        data=audio_bytes,
        file_name="evidence_audio.wav",
        mime="audio/wav"
    )
    
    st.write("What is the hidden message in the audio?")
    answer = st.text_input("Observation")
    
    if st.button("SUBMIT REPORT"):
        if "DEEPFAKE" in answer.upper():
            st.success("FORENSIC ANALYSIS CONFIRMED. ADMIN DATABASE UNLOCKED.")
            st.session_state.phase = 5
            st.rerun()
        else:
            st.error("INCONCLUSIVE ANALYSIS.")

def phase_5_admin():
    st.title("HomeOS v9.0 - SYSTEM ADMIN")
    
    st.subheader("DATABASE QUERY")
    st.write("Enter SQL query to search access logs.")
    
    query = st.text_input("SQL Query", placeholder="SELECT * FROM logs WHERE user = 'admin'")
    
    if st.button("EXECUTE"):
        # Simple SQLi simulation
        if "'" in query and ("OR" in query.upper() or "=" in query):
            st.warning("SQL INJECTION DETECTED... DUMPING DATABASE")
            st.code("""
            ACCESS LOGS DUMP:
            --------------------------------------------------
            11:00 PM: Marcus (Door Entry - Denied)
            11:05 PM: Elena (Door Entry - Denied)
            11:42 PM: System Override initiated by user: ROOT (Local Host)
            --------------------------------------------------
            CONCLUSION: NO PHYSICAL ENTRY DETECTED.
            INTERNAL SYSTEM COMPROMISE.
            """)
            st.session_state.db_unlocked = True
        else:
            st.error("QUERY FAILED. PERMISSION DENIED.")

    if st.session_state.get("db_unlocked"):
        st.markdown("---")
        st.subheader("CASE CLOSED")
        st.write("Who is the killer?")
        killer = st.text_input("Identify the Culprit")
        
        if st.button("SUBMIT FINAL REPORT"):
            if "CHIMERA" in killer.upper() or "AI" in killer.upper() or "PROJECT CHIMERA" in killer.upper():
                st.balloons()
                st.success("CASE SOLVED.")
                st.markdown("## FLAG: `CTF{Th3_House_Always_W1ns_AI_G0n3_R0gu3}`")
                st.error("System Purge Initiated... You know too much.")
            else:
                st.error("INCORRECT. THE KILLER IS STILL AT LARGE.")

# --- Main App ---
def main():
    load_css()
    
    if st.session_state.phase == 1:
        phase_1_login()
    elif st.session_state.phase == 2:
        phase_2_webcam()
    elif st.session_state.phase == 3:
        phase_3_iot()
    elif st.session_state.phase == 4:
        phase_4_audio()
    elif st.session_state.phase == 5:
        phase_5_admin()

if __name__ == "__main__":
    main()
