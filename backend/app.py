import streamlit as st
import time
from pipeline import run_research_pipeline

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Research Pilot",
    page_icon="🔬",
    layout="wide",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

  html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
  }

  /* ── Background ── */
  .stApp {
    background: #0d0f14;
    color: #c8cdd8;
  }

  /* ── Header strip ── */
  .header-strip {
    display: flex;
    align-items: baseline;
    gap: 12px;
    padding: 2rem 0 1.2rem;
    border-bottom: 1px solid #1e2230;
    margin-bottom: 2rem;
  }
  .header-strip h1 {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1.5rem;
    font-weight: 600;
    color: #e8ecf4;
    margin: 0;
    letter-spacing: -0.02em;
  }
  .header-strip .badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #5b8dee;
    border: 1px solid #5b8dee44;
    padding: 2px 8px;
    border-radius: 3px;
    text-transform: uppercase;
  }

  /* ── Input area ── */
  .stTextInput > div > div > input {
    background: #13151c !important;
    border: 1px solid #252836 !important;
    border-radius: 6px !important;
    color: #e8ecf4 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
  }
  .stTextInput > div > div > input:focus {
    border-color: #5b8dee !important;
    box-shadow: 0 0 0 2px #5b8dee22 !important;
  }
  .stTextInput > label {
    color: #7a8194 !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
  }

  /* ── Button ── */
  .stButton > button {
    background: #5b8dee !important;
    color: #0d0f14 !important;
    border: none !important;
    border-radius: 6px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.65rem 2rem !important;
    transition: background 0.15s !important;
  }
  .stButton > button:hover {
    background: #7aa3f2 !important;
  }
  .stButton > button:disabled {
    background: #252836 !important;
    color: #4a5068 !important;
  }

  /* ── Step cards ── */
  .step-card {
    background: #13151c;
    border: 1px solid #1e2230;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
  }
  .step-card.active {
    border-color: #5b8dee55;
    box-shadow: 0 0 0 1px #5b8dee22;
  }
  .step-card.done {
    border-color: #3dd68c44;
  }
  .step-label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 0.5rem;
  }
  .step-num {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    color: #5b8dee;
    background: #5b8dee18;
    padding: 2px 7px;
    border-radius: 3px;
    letter-spacing: 0.1em;
  }
  .step-num.done {
    color: #3dd68c;
    background: #3dd68c18;
  }
  .step-title {
    font-size: 0.85rem;
    font-weight: 600;
    color: #c8cdd8;
    letter-spacing: 0.01em;
  }
  .step-title.muted {
    color: #4a5068;
  }

  /* ── Output panels ── */
  .output-panel {
    background: #0a0c11;
    border: 1px solid #1e2230;
    border-radius: 8px;
    padding: 1.2rem 1.4rem;
    margin-top: 0.5rem;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    line-height: 1.7;
    color: #9ca3b4;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 320px;
    overflow-y: auto;
  }

  /* ── Final report ── */
  .report-panel {
    background: #0d1117;
    border: 1px solid #3dd68c33;
    border-radius: 8px;
    padding: 1.8rem;
    margin-top: 1rem;
    color: #c8cdd8;
    line-height: 1.8;
    font-size: 0.92rem;
  }
  .report-panel h3 {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    color: #3dd68c;
    text-transform: uppercase;
    margin-bottom: 1rem;
  }

  /* ── Feedback panel ── */
  .feedback-panel {
    background: #0d1117;
    border: 1px solid #f5a62333;
    border-radius: 8px;
    padding: 1.8rem;
    margin-top: 1rem;
    color: #c8cdd8;
    line-height: 1.8;
    font-size: 0.92rem;
  }
  .feedback-panel h3 {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    color: #f5a623;
    text-transform: uppercase;
    margin-bottom: 1rem;
  }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 4px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: #252836; border-radius: 2px; }

  /* ── Spinner color ── */
  .stSpinner > div { border-top-color: #5b8dee !important; }

  /* ── Hide default streamlit chrome ── */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding-top: 0 !important; max-width: 900px; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-strip">
  <h1>🔬 Research Pilot</h1>
  <span class="badge">Multi-Agent</span>
</div>
""", unsafe_allow_html=True)

# ── Input ───────────────────────────────────────────────────────────────────────
topic = st.text_input(
    "RESEARCH TOPIC",
    placeholder="e.g. Quantum error correction breakthroughs 2025",
    key="topic_input",
)

col1, col2 = st.columns([1, 6])
with col1:
    run_btn = st.button("Run →", disabled=not topic.strip())

# ── Pipeline steps definition ───────────────────────────────────────────────────
STEPS = [
    ("01", "Search Agent", "Finds recent, reliable information across the web"),
    ("02", "Reader Agent", "Scrapes top resource for deeper content"),
    ("03", "Writer", "Drafts a structured research report"),
    ("04", "Critic", "Reviews and provides feedback on the report"),
]

# ── Render idle step cards ───────────────────────────────────────────────────────
def render_step(num, title, desc, state="idle"):
    num_class = "step-num done" if state == "done" else "step-num"
    title_class = "step-title" if state in ("active", "done") else "step-title muted"
    icon = "✓" if state == "done" else ("●" if state == "active" else "○")
    card_class = f"step-card {state}" if state in ("active", "done") else "step-card"
    st.markdown(f"""
    <div class="{card_class}">
      <div class="step-label">
        <span class="{num_class}">{num}</span>
        <span class="{title_class}">{icon} {title}</span>
      </div>
      <div style="font-size:0.78rem; color:#4a5068; padding-left:2px">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Show idle pipeline on first load ────────────────────────────────────────────
if "result" not in st.session_state and not run_btn:
    for num, title, desc in STEPS:
        render_step(num, title, desc, state="idle")

# ── Run pipeline ─────────────────────────────────────────────────────────────────
if run_btn and topic.strip():
    step_placeholders = []

    # Pre-render step slots
    for i, (num, title, desc) in enumerate(STEPS):
        ph = st.empty()
        step_placeholders.append(ph)
        with ph.container():
            render_step(num, title, desc, state="idle")

    result_ph = st.empty()

    def update_step(active_idx):
        for i, (num, title, desc) in enumerate(STEPS):
            if i < active_idx:
                state = "done"
            elif i == active_idx:
                state = "active"
            else:
                state = "idle"
            with step_placeholders[i].container():
                render_step(num, title, desc, state=state)

    # ── Step 1: Search ────────────────────────────────────────────────────────
    update_step(0)
    with st.spinner("Search agent scanning the web…"):
        from agents import build_search_agent
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about {topic}")]
        })
        search_content = search_result["messages"][-1].content

    # ── Step 2: Reader ────────────────────────────────────────────────────────
    update_step(1)
    with st.spinner("Reader agent scraping top resource…"):
        from agents import build_reader_agent
        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{search_content[:800]}"
            )]
        })
        scraped_content = reader_result["messages"][-1].content

    # ── Step 3: Writer ────────────────────────────────────────────────────────
    update_step(2)
    with st.spinner("Writer drafting the report…"):
        from agents import writer_chain
        research_combined = (
            f"SEARCH RESULTS:\n{search_content}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{scraped_content}\n\n"
        )
        report = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })

    # ── Step 4: Critic ────────────────────────────────────────────────────────
    update_step(3)
    with st.spinner("Critic reviewing the report…"):
        from agents import critic_chain
        feedback = critic_chain.invoke({"report": report})

    # Mark all done
    for i, (num, title, desc) in enumerate(STEPS):
        with step_placeholders[i].container():
            render_step(num, title, desc, state="done")

    # Store in session
    st.session_state["result"] = {
        "topic": topic,
        "search_results": search_content,
        "scraped_content": scraped_content,
        "report": report,
        "feedback": feedback,
    }

# ── Display results ──────────────────────────────────────────────────────────────
if "result" in st.session_state:
    res = st.session_state["result"]

    st.markdown("---")

    # Intermediate outputs in expanders
    with st.expander("Search Results", expanded=False):
        st.markdown(res["search_results"])

    with st.expander("Scraped Content", expanded=False):
        st.markdown(res["scraped_content"])

    # Final report
    st.markdown("### 📄 Final Report")
    st.markdown(res["report"])

    # Critic feedback
    st.markdown("### 🧪 Critic Feedback")
    st.markdown(res["feedback"])

    # Download button
    st.markdown("<br>", unsafe_allow_html=True)
    full_output = (
        f"# Research Report: {res['topic']}\n\n"
        f"## Report\n{res['report']}\n\n"
        f"## Critic Feedback\n{res['feedback']}\n"
    )
    st.download_button(
        label="↓ Download Report",
        data=full_output,
        file_name=f"report_{res['topic'][:30].replace(' ', '_')}.md",
        mime="text/markdown",
    )