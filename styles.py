"""
styles.py — Wizard.exe CSS
Call inject_styles() once at app startup to apply all styling.
"""
import streamlit as st

FONT_LINK = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Exo+2:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
"""

CSS = """
<style>
*, *::before, *::after { box-sizing: border-box; }

:root {
    --bg:       #05000a;
    --primary:  #bc13fe;
    --secondary:#ff00ff;
    --accent:   #00ffff;
    --dim:      #7a0aaa;
    --text:     #e0c0ff;
    --muted:    #7755aa;
    --danger:   #ff2060;
}

/* ── App shell ── */
.stApp {
    background-color: var(--bg) !important;
    background-image:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(188,19,254,0.18) 0%, transparent 70%),
        repeating-linear-gradient(0deg,  transparent 0px, transparent 39px, rgba(188,19,254,0.04) 39px, rgba(188,19,254,0.04) 40px),
        repeating-linear-gradient(90deg, transparent 0px, transparent 39px, rgba(188,19,254,0.04) 39px, rgba(188,19,254,0.04) 40px);
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
header[data-testid="stHeader"], footer, #MainMenu,
[data-testid="stDecoration"], [data-testid="stToolbar"] { display: none !important; }

/* ── Main content column ── */
.block-container {
    max-width: 780px !important;
    padding: 48px 32px 120px !important;
    margin: 0 auto !important;
}
.block-container > div,
.block-container > div > div,
[data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
}

/* ── Scanlines ── */
body::after {
    content: '';
    position: fixed;
    inset: 0;
    background: repeating-linear-gradient(
        to bottom,
        transparent 0px, transparent 3px,
        rgba(0,0,0,0.12) 3px, rgba(0,0,0,0.12) 4px
    );
    pointer-events: none;
    z-index: 9999;
}

/* ── Title ── */
.game-title-glitch {
    font-family: 'Orbitron', monospace;
    font-size: min(9.5vw, calc((100vw - 80px) / 9));
    font-weight: 900;
    letter-spacing: 0.06em;
    white-space: nowrap;
    color: var(--primary);
    text-align: center;
    display: block;
    width: 100%;
    margin-top: 8vh;
    margin-bottom: 10px;
    text-shadow: 0 0 30px var(--primary), 0 0 80px var(--primary);
    animation: flicker 7s infinite, textpulse 3s ease-in-out infinite alternate;
    position: relative;
}
.game-title-glitch::before,
.game-title-glitch::after {
    content: attr(data-text);
    position: absolute;
    top: 0; left: 0; width: 100%;
    text-align: center;
}
.game-title-glitch::before { color:#ff00ff; opacity:0.55; animation:glitchslide 8s infinite steps(1); }
.game-title-glitch::after  { color:#00ffff; opacity:0.35; animation:glitchslide 11s infinite steps(1) reverse; }

.game-subtitle {
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    letter-spacing: 0.42em;
    color: var(--muted);
    text-align: center;
    width: 100%;
    text-transform: uppercase;
    margin-bottom: 8px;
    display: block;
}
.version-tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.22em;
    color: rgba(119,85,170,0.4);
    text-align: center;
    width: 100%;
    display: block;
    margin-bottom: 52px;
}

/* ── Headings ── */
h2.section-heading,
.section-heading {
    font-family: 'Orbitron', monospace !important;
    font-size: clamp(22px, 4.5vw, 44px) !important;
    font-weight: 700 !important;
    color: #ff00ff !important;
    text-align: center !important;
    width: 100% !important;
    margin-bottom: 18px !important;
    letter-spacing: 0.08em !important;
    line-height: 1.2 !important;
    text-shadow: 0 0 18px #ff00ff, 0 0 40px rgba(255,0,255,0.22) !important;
    animation: headingpulse 4s ease-in-out infinite alternate !important;
    display: block !important;
}

/* ── Story text ── */
.story-text {
    font-family: 'Exo 2', sans-serif;
    font-size: clamp(15px, 1.7vw, 18px);
    font-weight: 300;
    line-height: 1.85;
    color: var(--text);
    text-align: center;
    width: 100%;
    margin: 0 0 24px 0;
    display: block;
}

/* ── Door prompt ── */
.door-prompt {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.28em;
    color: var(--muted);
    text-align: center;
    width: 100%;
    text-transform: uppercase;
    margin-bottom: 16px;
    padding: 10px 0;
    border-top: 1px solid rgba(188,19,254,0.15);
    border-bottom: 1px solid rgba(188,19,254,0.15);
    display: block;
}

/* ── Status / progress ── */
.status-bar {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.22em;
    color: var(--muted);
    text-align: center;
    width: 100%;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid rgba(188,19,254,0.1);
    display: block;
}
.status-bar span { color: var(--primary); }
.progress-wrap {
    width: 100%;
    height: 2px;
    background: rgba(188,19,254,0.1);
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 6px;
}
.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--dim), var(--primary));
    box-shadow: 0 0 6px var(--primary);
    border-radius: 2px;
    transition: width 0.5s ease;
}

/* ── Dialogue ── */
.dialogue {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 11px;
    margin-bottom: 28px;
}
.dialogue-line {
    font-family: 'Share Tech Mono', monospace;
    font-size: clamp(12px, 1.4vw, 15px);
    line-height: 1.65;
    padding: 13px 18px;
    border-radius: 3px;
    width: 100%;
}
.dialogue-line.wizard {
    background: rgba(188,19,254,0.07);
    border-left: 3px solid var(--primary);
    color: var(--text);
    text-align: left;
}
.dialogue-line.player {
    background: rgba(0,255,255,0.05);
    border-right: 3px solid var(--accent);
    color: #c8f0ff;
    text-align: right;
}
.speaker {
    font-weight: 700;
    font-size: 10px;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    display: block;
    margin-bottom: 4px;
    opacity: 0.6;
}
.dialogue-line.wizard .speaker { color: var(--primary); }
.dialogue-line.player  .speaker { color: var(--accent); }

/* ── Riddle box ── */
.riddle-box {
    border: 1px solid var(--dim);
    border-radius: 4px;
    padding: 26px 30px;
    background: rgba(188,19,254,0.05);
    text-align: center;
    width: 100%;
    margin-bottom: 24px;
    animation: boxpulse 3s ease-in-out infinite alternate;
    display: block;
}
.riddle-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.45em;
    color: var(--dim);
    text-transform: uppercase;
    margin-bottom: 14px;
    display: block;
}
.riddle-text {
    font-family: 'Exo 2', sans-serif;
    font-size: clamp(14px, 1.6vw, 17px);
    font-style: italic;
    font-weight: 300;
    color: var(--secondary);
    line-height: 1.75;
    text-shadow: 0 0 14px rgba(255,0,255,0.28);
    display: block;
}

/* ── Scene image ── */
.scene-image-wrap {
    width: 100%;
    margin-bottom: 28px;
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid rgba(188,19,254,0.2);
    box-shadow: 0 0 50px rgba(188,19,254,0.1);
    position: relative;
    display: block;
}
.scene-image-wrap img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    display: block;
    filter: saturate(0.5) brightness(0.6) hue-rotate(255deg);
    transition: filter 0.5s ease;
}
.scene-image-wrap:hover img { filter: saturate(0.7) brightness(0.75) hue-rotate(255deg); }
.scene-image-wrap::before, .scene-image-wrap::after {
    content: '';
    position: absolute;
    width: 16px; height: 16px;
    border-color: var(--primary);
    border-style: solid;
    z-index: 2; opacity: 0.55;
}
.scene-image-wrap::before { top:6px;    left:6px;   border-width:2px 0 0 2px; }
.scene-image-wrap::after  { bottom:6px; right:6px;  border-width:0 2px 2px 0; }

/* ── Divider ── */
.neon-divider {
    width: 160px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    margin: 12px auto 26px;
    opacity: 0.5;
    display: block;
}

/* ── Ending badge ── */
.ending-badge {
    display: inline-block;
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.4em;
    padding: 5px 16px;
    border-radius: 2px;
    text-transform: uppercase;
    margin-bottom: 18px;
    background: var(--primary);
    color: var(--bg);
}
.ending-badge.bad  { background: var(--danger); }
.ending-badge.mid  { background: var(--muted);  }
.ending-badge.good { background: var(--accent); color: #000; }

/* ── Buttons ── */
[data-testid="stButton"] {
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
}
[data-testid="stButton"] > button {
    width: 100% !important;
    background: transparent !important;
    color: var(--primary) !important;
    border: 1px solid rgba(122,10,170,0.55) !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: clamp(11px, 1.2vw, 13px) !important;
    letter-spacing: 0.13em !important;
    text-transform: uppercase !important;
    padding: 17px 16px !important;
    margin-bottom: 6px !important;
    transition: all 0.18s ease !important;
    white-space: pre-line !important;
    line-height: 1.55 !important;
    text-align: center !important;
}
[data-testid="stButton"] > button:hover {
    background: rgba(188,19,254,0.1) !important;
    border-color: var(--primary) !important;
    color: #fff !important;
    box-shadow: 0 0 14px rgba(188,19,254,0.3), inset 0 0 20px rgba(188,19,254,0.06) !important;
    letter-spacing: 0.17em !important;
}
[data-testid="stButton"] > button:active {
    transform: scale(0.985) !important;
    background: rgba(188,19,254,0.18) !important;
}

/* ── Text input ── */
[data-testid="stTextInput"] { width: 100% !important; }
[data-testid="stTextInput"] label {
    font-family: 'Share Tech Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 0.35em !important;
    color: var(--muted) !important;
    text-transform: uppercase !important;
    text-align: center !important;
    width: 100% !important;
    display: block !important;
    margin-bottom: 8px !important;
}
[data-testid="stTextInput"] input {
    background: rgba(0,0,0,0.5) !important;
    color: var(--secondary) !important;
    border: 1px solid rgba(122,10,170,0.5) !important;
    border-radius: 3px !important;
    font-family: 'Share Tech Mono', monospace !important;
    font-size: clamp(14px, 1.4vw, 16px) !important;
    text-align: center !important;
    padding: 14px !important;
    letter-spacing: 0.1em !important;
    caret-color: var(--secondary) !important;
    width: 100% !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 10px rgba(188,19,254,0.28) !important;
    outline: none !important;
}

/* ── Columns ── */
[data-testid="stHorizontalBlock"] {
    width: 100% !important;
    gap: 12px !important;
    align-items: stretch !important;
}
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    flex: 1 !important;
    min-width: 0 !important;
    align-items: stretch !important;
    display: flex !important;
    flex-direction: column !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stButton"] { height: 100% !important; }
[data-testid="stHorizontalBlock"] [data-testid="stButton"] > button { height: 100% !important; }

/* ── Keyframes ── */
@keyframes flicker {
    0%,93%,100%{opacity:1;}
    94%{opacity:0.85;} 95%{opacity:1;}
    96%{opacity:0.68;} 97%{opacity:1;}
    98%{opacity:0.9;}  99%{opacity:1;}
}
@keyframes textpulse {
    from { text-shadow: 0 0 20px var(--primary), 0 0 60px var(--primary); }
    to   { text-shadow: 0 0 40px var(--primary), 0 0 110px var(--primary), 0 0 150px rgba(188,19,254,0.25); }
}
@keyframes headingpulse {
    from { text-shadow: 0 0 10px #ff00ff; }
    to   { text-shadow: 0 0 24px #ff00ff, 0 0 60px rgba(255,0,255,0.2); }
}
@keyframes boxpulse {
    from { box-shadow: inset 0 0 20px rgba(188,19,254,0.04), 0 0 10px rgba(188,19,254,0.05); }
    to   { box-shadow: inset 0 0 40px rgba(188,19,254,0.09), 0 0 26px rgba(188,19,254,0.1); }
}
@keyframes fadein {
    from { opacity:0; transform:translateY(5px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes glitchslide {
    0%,100%{clip-path:inset(0 0 95% 0);transform:translate(-3px,0);}
    20%    {clip-path:inset(30% 0 50% 0);transform:translate(3px,0);}
    40%    {clip-path:inset(70% 0 10% 0);transform:translate(-2px,0);}
    60%    {clip-path:inset(10% 0 80% 0);transform:translate(2px,0);}
    80%    {clip-path:inset(50% 0 30% 0);transform:translate(-2px,0);}
}
</style>
"""


def inject_styles() -> None:
    """Inject fonts and all CSS into the Streamlit app."""
    st.markdown(FONT_LINK, unsafe_allow_html=True)
    st.markdown(CSS, unsafe_allow_html=True)
