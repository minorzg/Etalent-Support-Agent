import streamlit as st
import f1test as ash

# =====================================================
# CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="eTalent AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CSS PRO & ULTRA-DESIGN
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Global font & smooth transitions */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Main background */
.stApp {
    background-color: #080d16;
    color: #e2e8f0;
}

/* Hide Streamlit default header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #0d1322;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

section[data-testid="stSidebar"] * {
    color: #cbd5e1;
}

/* Main container alignment */
.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 5rem;
}

/* Title & Subtitle */
.main-title {
    font-size: 32px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.5px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.main-subtitle {
    color: #94a3b8;
    font-size: 14px;
    margin-top: 4px;
}

/* Status Badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.2);
    color: #34d399;
    padding: 6px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    box-shadow: 0 0 15px rgba(16, 185, 129, 0.05);
}

/* Chat messages container */
[data-testid="stChatMessage"] {
    background-color: #111a2e;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 16px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

/* User message specific styling */
[data-testid="stChatMessage"]:has(.user-avatar) {
    background-color: #17233f;
}

/* Chat input bar */
[data-testid="stChatInput"] {
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 16px !important;
    background-color: #0f172a !important;
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3) !important;
}

[data-testid="stChatInput"] textarea {
    color: #ffffff !important;
}

/* Professional Buttons */
.stButton > button {
    background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
    transform: translateY(-1px);
}

/* Secondary / Danger Buttons (like Clear conversation) */
.sidebar .stButton > button {
    background: rgba(239, 68, 68, 0.1);
    border: 1px solid rgba(239, 68, 68, 0.2);
    color: #f87171;
    box-shadow: none;
}

.sidebar .stButton > button:hover {
    background: rgba(239, 68, 68, 0.2);
    color: #fca5a5;
    border-color: rgba(239, 68, 68, 0.4);
}

/* Dividers */
hr {
    border-color: rgba(255, 255, 255, 0.06);
    margin: 20px 0;
}

/* Modern Info Cards */
.info-card {
    background: #0f172a;
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 12px;
    transition: border-color 0.2s;
}

.info-card:hover {
    border-color: rgba(255, 255, 255, 0.12);
}

.info-label {
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #64748b;
    margin-bottom: 6px;
    font-weight: 600;
}

.info-value {
    font-size: 15px;
    font-weight: 600;
    color: #f1f5f9;
}

/* Welcome Screen Design */
.welcome {
    text-align: center;
    padding: 50px 20px 30px 20px;
}

.welcome-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    background: rgba(37, 99, 235, 0.1);
    border: 1px solid rgba(37, 99, 235, 0.2);
    border-radius: 20px;
    font-size: 28px;
    color: #60a5fa;
    margin-bottom: 20px;
    box-shadow: 0 0 30px rgba(37, 99, 235, 0.15);
}

.welcome h2 {
    color: #ffffff;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 8px;
}

.welcome p {
    color: #94a3b8;
    font-size: 14px;
}

/* Remove footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("### 🤖 eTalent AI")
    st.caption("Enterprise Intelligence Assistant")

    st.divider()

    st.markdown("#### Navigation")
    
    # Boutons de navigation stylisés (simulés en texte propre)
    st.markdown("💬 **Assistant Actif**")
    st.markdown("📚 Base de connaissances")
    st.markdown("⚙️ Paramètres")

    st.divider()

    st.markdown("#### Système")

    st.markdown("""
    <div class="info-card">
        <div class="info-label">Modèle IA</div>
        <div class="info-value">Gemini Flash Lite</div>
    </div>
    <div class="info-card">
        <div class="info-label">Moteur RAG</div>
        <div class="info-value">ChromaDB</div>
    </div>
    <div class="info-card">
        <div class="info-label">État du système</div>
        <div style="color:#34d399;font-weight:600;font-size:14px;display:flex;align-items:center;gap:6px;">
            <span style="width:8px;height:8px;background:#34d399;border-radius:50%;display:inline-block;box-shadow:0 0 8px #34d399;"></span> Opérationnel
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    if st.button("🗑️ Réinitialiser la discussion", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("<div style='text-align:center; margin-top:20px;'><span style='font-size:11px; color:#475569;'>eTalent AI · v1.2 Pro</span></div>", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(
        '<div class="main-title"><span>✦</span> eTalent AI Assistant</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="main-subtitle">Assistant intelligent et sécurisé pour vos ressources humaines.</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div style="text-align:right;padding-top:12px;">'
        '<span class="status-badge"><span style="width:6px;height:6px;background:#34d399;border-radius:50%;"></span> En Ligne</span>'
        '</div>',
        unsafe_allow_html=True
    )

st.divider()


# =====================================================
# SESSION STATE
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =====================================================
# WELCOME SCREEN
# =====================================================

if not st.session_state.messages:

    st.markdown("""
    <div class="welcome">
        <div class="welcome-icon">✦</div>
        <h2>Comment puis-je vous aider aujourd'hui ?</h2>
        <p>Interrogez la base de connaissances sur les collaborateurs, départements et processus internes.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card" style="height:100%;">
            <div style="font-size:20px;margin-bottom:8px;">👥</div>
            <div class="info-value" style="margin-bottom:4px;">Informations Collaborateurs</div>
            <p style="color:#94a3b8;font-size:13px;margin:0;">
                Trouvez rapidement les profils, rôles et affectations de l'équipe.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card" style="height:100%;">
            <div style="font-size:20px;margin-bottom:8px;">🏢</div>
            <div class="info-value" style="margin-bottom:4px;">Structure d'entreprise</div>
            <p style="color:#94a3b8;font-size:13px;margin:0;">
                Explorez l'organisation des départements et la hiérarchie interne.
            </p>
        </div>
        """, unsafe_allow_html=True)


# =====================================================
# DISPLAY CHAT HISTORY
# =====================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input("Posez votre question sur eTalent...")

if prompt:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Recherche dans la base de connaissances eTalent..."):

            try:
                # Use the RAG agent
                result = ash.rag_agent.invoke({
                    "messages": [
                        ash.HumanMessage(content=prompt)
                    ]
                })

                answer = ash.extract_answer(
                    result["messages"][-1].content
                )

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:

                st.error(f"Une erreur est survenue : {str(e)}")