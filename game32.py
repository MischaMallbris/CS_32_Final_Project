import streamlit as st
import time

st.set_page_config(page_title="WIZARD.EXE", layout="centered", initial_sidebar_state="collapsed")

# ── FONTS ── (written with help from AI)
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Exo+2:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ── SOUND ENGINE ── (written with help from AI)
# Each play_sound() call renders a self-contained components.html block.
# The sound name is baked directly into the HTML so it plays immediately
# on render — no cross-frame messaging needed.
import streamlit.components.v1 as components
import random

SOUND_JS = {
    "click": """
        var o=c.createOscillator(),g=c.createGain();
        o.connect(g);g.connect(c.destination);
        o.type='square';o.frequency.setValueAtTime(440,t);
        o.frequency.exponentialRampToValueAtTime(220,t+0.08);
        g.gain.setValueAtTime(0.15,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.1);
        o.start(t);o.stop(t+0.1);
    """,
    "door": """
        var o=c.createOscillator(),g=c.createGain();
        o.connect(g);g.connect(c.destination);
        o.type='sawtooth';o.frequency.setValueAtTime(90,t);
        o.frequency.exponentialRampToValueAtTime(35,t+0.4);
        g.gain.setValueAtTime(0.22,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.45);
        o.start(t);o.stop(t+0.45);
    """,
    "riddle": """
        [280,380,500,640].forEach(function(f,i){
            var o=c.createOscillator(),g=c.createGain();
            o.connect(g);g.connect(c.destination);
            o.type='sine';o.frequency.value=f;
            var s=t+i*0.09;
            g.gain.setValueAtTime(0,s);g.gain.linearRampToValueAtTime(0.1,s+0.04);
            g.gain.exponentialRampToValueAtTime(0.001,s+0.16);
            o.start(s);o.stop(s+0.16);
        });
    """,
    "wrong": """
        var o=c.createOscillator(),g=c.createGain();
        o.connect(g);g.connect(c.destination);
        o.type='sawtooth';o.frequency.setValueAtTime(200,t);
        o.frequency.exponentialRampToValueAtTime(55,t+0.5);
        g.gain.setValueAtTime(0.28,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.5);
        o.start(t);o.stop(t+0.5);
    """,
    "correct": """
        [523,659,784,1047].forEach(function(f,i){
            var o=c.createOscillator(),g=c.createGain();
            o.connect(g);g.connect(c.destination);
            o.type='triangle';o.frequency.value=f;
            var s=t+i*0.1;
            g.gain.setValueAtTime(0,s);g.gain.linearRampToValueAtTime(0.12,s+0.04);
            g.gain.exponentialRampToValueAtTime(0.001,s+0.22);
            o.start(s);o.stop(s+0.22);
        });
    """,
    "delete": """
        var buf=c.createBuffer(1,Math.floor(c.sampleRate*0.7),c.sampleRate);
        var d=buf.getChannelData(0);
        for(var i=0;i<d.length;i++) d[i]=(Math.random()*2-1)*Math.pow(1-i/d.length,1.5);
        var src=c.createBufferSource(),g=c.createGain();
        src.buffer=buf;src.connect(g);g.connect(c.destination);
        g.gain.setValueAtTime(0.35,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.7);
        src.start(t);
    """,
    "win": """
        [261,330,392,523,659,784,1047].forEach(function(f,i){
            var o=c.createOscillator(),g=c.createGain();
            o.connect(g);g.connect(c.destination);
            o.type='triangle';o.frequency.value=f;
            var s=t+i*0.11;
            g.gain.setValueAtTime(0,s);g.gain.linearRampToValueAtTime(0.1,s+0.05);
            g.gain.exponentialRampToValueAtTime(0.001,s+0.28);
            o.start(s);o.stop(s+0.3);
        });
    """,
    "ambient": """
        [55,82,110].forEach(function(f,i){
            var o=c.createOscillator(),g=c.createGain();
            o.connect(g);g.connect(c.destination);
            o.type='sine';o.frequency.value=f;
            g.gain.setValueAtTime(0,t);
            g.gain.linearRampToValueAtTime(0.04,t+1.2);
            g.gain.linearRampToValueAtTime(0,t+4);
            o.start(t);o.stop(t+4);
        });
    """,
}

def play_sound(name):
    js = SOUND_JS.get(name, "")
    # Unique comment forces Streamlit to treat each call as a new component
    uid = random.randint(0, 999999)
    components.html(f"""
        <script>
        /* uid:{uid} */
        (function() {{
            try {{
                var c = new (window.AudioContext || window.webkitAudioContext)();
                var t = c.currentTime + 0.05;
                {js}
            }} catch(e) {{ console.warn('audio:', e); }}
        }})();
        </script>
    """, height=0)



# ── CSS — targets Streamlit's real DOM containers ── (Written with help from AI)
st.markdown("""
<style>
/* Fonts */
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

/* ── Hide chrome ── */
header[data-testid="stHeader"], footer, #MainMenu,
[data-testid="stDecoration"], [data-testid="stToolbar"] { display: none !important; }

/* ── Main content column — this is Streamlit's real centered container ── */
.block-container {
    max-width: 780px !important;
    padding: 48px 32px 120px !important;
    margin: 0 auto !important;
}

/* Every direct child element of the main block should be centered */
.block-container > div,
.block-container > div > div,
[data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    width: 100% !important;
}

/* Scanlines */
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

/* ── TITLE ── */
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
.game-title-glitch::before {
    color: #ff00ff; opacity: 0.55;
    animation: glitchslide 8s infinite steps(1);
}
.game-title-glitch::after {
    color: #00ffff; opacity: 0.35;
    animation: glitchslide 11s infinite steps(1) reverse;
}
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

/* ── HEADINGS ── */
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

/* ── STORY TEXT ── */
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

/* ── DOOR PROMPT ── */
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

/* ── STATUS / PROGRESS ── */
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

/* ── DIALOGUE ── */
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
.dialogue-line.player  .speaker { color: var(--accent);  }

/* ── RIDDLE BOX ── */
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

/* ── SCENE IMAGE ── */
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

/* ── DIVIDER ── */
.neon-divider {
    width: 160px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--primary), transparent);
    margin: 12px auto 26px;
    opacity: 0.5;
    display: block;
}

/* ── ENDING BADGE ── */
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
.ending-badge.good { background: var(--accent); color:#000; }

/* ── BUTTONS — target Streamlit's real button wrapper ── */
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

/* ── TEXT INPUT ── */
[data-testid="stTextInput"] {
    width: 100% !important;
}
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

/* ── COLUMNS (door buttons) ── */
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
[data-testid="stHorizontalBlock"] [data-testid="stButton"] {
    height: 100% !important;
}
[data-testid="stHorizontalBlock"] [data-testid="stButton"] > button {
    height: 100% !important;
}

/* ── KEYFRAMES ── */
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
    from { text-shadow: 0 0 10px var(--secondary); }
    to   { text-shadow: 0 0 24px var(--secondary), 0 0 60px rgba(255,0,255,0.2); }
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
""", unsafe_allow_html=True)

# ── STATE ──
for k, v in [("room","title"),("intro_played",False),("intro_line",0)]:
    if k not in st.session_state:
        st.session_state[k] = v

def move(room_name):
    st.session_state.room = room_name
    st.rerun()

# ── HELPERS ──
def scene_img(url):
    st.markdown(f'<div class="scene-image-wrap"><img src="{url}&auto=format&fit=crop" alt="scene"></div>',
                unsafe_allow_html=True)

def divider():
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

def status(node, room_num=None, total=10):
    prog = ""
    room_tag = ""
    if room_num:
        pct = int(room_num / total * 100)
        prog = f'<div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>'
        room_tag = f'&nbsp;|&nbsp; NODE <span>{room_num:02d}&nbsp;/&nbsp;{total}</span>'
    st.markdown(f'{prog}<p class="status-bar">SYSTEM: <span>{node}</span>{room_tag}</p>',
                unsafe_allow_html=True)

def story(text):
    st.markdown(f'<p class="story-text">{text}</p>', unsafe_allow_html=True)

def heading(text):
    st.markdown(f'<h2 class="section-heading">{text}</h2>', unsafe_allow_html=True)

def door_prompt(text):
    st.markdown(f'<p class="door-prompt">&#8594;&nbsp; {text} &nbsp;&#8592;</p>', unsafe_allow_html=True)

def wizard_says(text):
    st.markdown(f'''<div class="dialogue"><div class="dialogue-line wizard">
        <span class="speaker">Wizard</span>{text}</div></div>''', unsafe_allow_html=True)

def centered_button(label, key=None):
    """Single centered button in a narrow column."""
    _, col, _ = st.columns([1, 2, 1])
    with col:
        return st.button(label, key=key)

# ══════════════════════════════════════════════
# PAGES (written by me)
# ══════════════════════════════════════════════

# 1. TITLE
if st.session_state.room == "title":
    play_sound("ambient")
    st.markdown("""
        <span class="game-title-glitch" data-text="WIZARD.EXE">WIZARD.EXE</span>
        <span class="game-subtitle">A Digital Escape</span>
        <span class="version-tag">ver.&nbsp;1.0.0 &nbsp;·&nbsp; SYSTEM READY &nbsp;·&nbsp; AWAITING INPUT</span>
    """, unsafe_allow_html=True)
    if centered_button("▶  INITIALIZE SYSTEM", key="btn_init"):
        play_sound("click")
        move("intro")

# 2. INTRO
elif st.session_state.room == "intro":
    status("BOOT_SEQUENCE")
    lines = [
        ("wizard","Wizard","Ah… finally. Don't look so confused, User. You aren't 'here' anymore."),
        ("player","You",   "Where am I? Why can't I feel my hands?"),
        ("wizard","Wizard","I've translated your messy biology into perfect code. You're inside the System now."),
        ("wizard","Wizard","There are many doors between you and the Shutdown button. Each one is a test."),
        ("player","You",   "You're insane. I'm getting out of here."),
        ("wizard","Wizard","Good luck, User. The System doesn't forgive mistakes."),
    ]
    placeholder = st.empty()
    def render_dialogue(count):
        html = '<div class="dialogue">'
        for role, speaker, text in lines[:count]:
            html += f'<div class="dialogue-line {role}"><span class="speaker">{speaker}</span>{text}</div>'
        return html + '</div>'
    if not st.session_state.intro_played:
        n = st.session_state.intro_line
        placeholder.markdown(render_dialogue(n), unsafe_allow_html=True)
        if n < len(lines):
            time.sleep(0.85)
            st.session_state.intro_line += 1
            st.rerun()
        else:
            st.session_state.intro_played = True
    else:
        placeholder.markdown(render_dialogue(len(lines)), unsafe_allow_html=True)
    divider()
    story("You've been digitized by an evil wizard.<br>Navigate the System. Solve the puzzles. Find the exit — before you're deleted.")
    divider()
    if centered_button("▶  BEGIN ESCAPE PROTOCOL", key="btn_begin"):
        play_sound("door")
        move("room1")

# 3. ROOM 1
elif st.session_state.room == "room1":
    play_sound("ambient")
    status("BOOT_SECTOR", 1)
    scene_img("https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200")
    heading("The Boot Sector")
    story("The walls shimmer with cascading binary. The air hums with raw electricity. Two massive gateways loom ahead — each leading deeper into the System's unknown.")
    divider()
    door_prompt("Two paths. Only one leads forward.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  USER_FILES\nCreaking with forgotten data", key="r1a"):
            play_sound("door"); move("room2")
    with c2:
        if st.button("DOOR B  ·  SYSTEM_RECOVERY\nPulsing with erratic blue light", key="r1b"):
            play_sound("door"); move("room3")

# 4. ROOM 2
elif st.session_state.room == "room2":
    play_sound("riddle")
    status("CACHE_SECTOR", 2)
    scene_img("https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=1200")
    heading("The Cache")
    story("A guardian blocks the corridor — a shifting wall of locked logic. It speaks in riddles. Answer correctly and the path opens. Answer wrong and you cease to exist.")
    st.markdown("""<div class="riddle-box">
        <span class="riddle-label">— Access Riddle —</span>
        <span class="riddle-text">"I have keys but no locks.<br>
        I have a space but no room.<br>
        You can allow me to enter,<br>but I can never leave."</span>
    </div>""", unsafe_allow_html=True)
    ans = st.text_input("Type your answer and press Submit", key="q1")
    divider()
    if centered_button("▶  SUBMIT ANSWER", key="btn_q1"):
        if "keyboard" in ans.lower().strip():
            play_sound("correct"); move("room4")
        else:
            play_sound("wrong"); move("end3")

# 5. ROOM 3
elif st.session_state.room == "room3":
    play_sound("ambient")
    status("DEAD_SECTOR", 3)
    scene_img("https://images.unsplash.com/photo-1504333638930-c8787321eee0?w=1200")
    heading("The Dead Sector")
    story("The floor has been deleted. A cascade of 404 errors spirals into the abyss below. The air smells like burnt copper. Two exits cling to the crumbling walls.")
    divider()
    door_prompt("Something feels wrong about both. Trust your instincts.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  DANGER SIGNAL\nA red indicator blinks urgently", key="r3a"):
            play_sound("door"); move("room5")
    with c2:
        if st.button("DOOR B  ·  MEMORY FRAGMENT\nA warm, strangely familiar glow", key="r3b"):
            play_sound("wrong"); move("end3")

# 6. ROOM 4
elif st.session_state.room == "room4":
    play_sound("riddle")
    status("LOGIC_GATE", 4)
    scene_img("https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200")
    heading("The Logic Gate")
    wizard_says("You think in the language of flesh. Here, numbers obey different laws. Let's see if you can adapt.")
    st.markdown("""<div class="riddle-box">
        <span class="riddle-label">— Binary Riddle —</span>
        <span class="riddle-text">"In the Wizard's world —<br>what does 1 + 1 equal?"</span>
    </div>""", unsafe_allow_html=True)
    ans = st.text_input("Enter the answer in the Wizard's number system", key="q2")
    divider()
    if centered_button("▶  SUBMIT ANSWER", key="btn_q2"):
        if ans.strip() == "10":
            play_sound("correct"); move("room6")
        else:
            play_sound("wrong"); move("end4")

# 7. ROOM 5
elif st.session_state.room == "room5":
    play_sound("ambient")
    status("TRASH_SECTOR", 5)
    scene_img("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200")
    heading("The Compactor")
    story("The walls grind inward. Corrupted icons and shredded files rain from above. A floor hatch rattles beneath your feet. An iron door stands sealed to your right.")
    divider()
    door_prompt("The walls won't stop. Move now — or become part of the trash.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  FLOOR HATCH\nVibrating violently underfoot", key="r5a"):
            play_sound("door"); move("room7")
    with c2:
        if st.button("DOOR B  ·  IRON DOOR\nSolid, sealed, immovable", key="r5b"):
            play_sound("wrong"); move("end3")

# 8. ROOM 6
elif st.session_state.room == "room6":
    play_sound("ambient")
    status("GRAPHICS_BUFFER", 6)
    scene_img("https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=1200")
    heading("The Graphics Buffer")
    story("Raw color data floods your vision. Shadows move without light sources. Something watches you from inside the pixels. Two passages shimmer ahead.")
    divider()
    door_prompt("One door renders reality. The other renders nothing.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  CORRUPTED RENDER\nStatic bleeds from the edges", key="r6a"):
            play_sound("wrong"); move("end4")
    with c2:
        if st.button("DOOR B  ·  LIQUID LIGHT\nBeautiful and impossible", key="r6b"):
            play_sound("door"); move("room8")

# 9. ROOM 7
elif st.session_state.room == "room7":
    play_sound("ambient")
    status("REGISTRY_ARCHIVE", 7)
    scene_img("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200")
    heading("The Registry Archive")
    story("Infinite filing cabinets stretch into a ceiling you cannot see. Somewhere, a shredder runs without pause. One of these drawers holds your memories.")
    divider()
    door_prompt("Read-only is safe. Overwrite is dangerous. But safe won't get you out.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  READ_ONLY\nA calm, steady green glow", key="r7a"):
            play_sound("wrong"); move("end1")
    with c2:
        if st.button("DOOR B  ·  OVERWRITE\nSparking with raw voltage", key="r7b"):
            play_sound("door"); move("room9")

# 10. ROOM 8
elif st.session_state.room == "room8":
    play_sound("ambient")
    status("KERNEL_CORE", 8)
    scene_img("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?w=1200")
    heading("The Kernel Core")
    wizard_says("Too close, little file. You really shouldn't be here. Turn back — while you still have something left to lose.")
    story("The heart of the System pulses around you. Two passages tear open in the code itself. The Wizard's voice echoes from everywhere at once.")
    divider()
    door_prompt("This is the Wizard's domain. He wants you to choose wrong.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  GLITCHING PASSAGE\nUnstable — but open", key="r8a"):
            play_sound("door"); move("room10")
    with c2:
        if st.button("DOOR B  ·  ADMIN_ACCESS\nSmooth, polished, inviting", key="r8b"):
            play_sound("wrong"); move("end2")

# 11. ROOM 9
elif st.session_state.room == "room9":
    play_sound("riddle")
    status("SANDBOX", 9)
    scene_img("https://images.unsplash.com/photo-1506318137071-a8e063b4b519?w=1200")
    heading("The Sandbox")
    story("A grey desert stretches to a horizon that doesn't exist. The Wizard's laughter reverberates off nothing. One final riddle stands between you and the exit.")
    st.markdown("""<div class="riddle-box">
        <span class="riddle-label">— Final Riddle —</span>
        <span class="riddle-text">"I am the key that opens no door,<br>
        but I can always end your journey.<br>
        I live on every keyboard.<br>
        What am I?"</span>
    </div>""", unsafe_allow_html=True)
    ans = st.text_input("This is your last test. Answer wisely.", key="q3")
    divider()
    if centered_button("▶  SUBMIT FINAL ANSWER", key="btn_q3"):
        a = ans.lower().strip()
        if "escape" in a or a == "esc":
            play_sound("correct"); move("room10")
        else:
            play_sound("wrong"); move("end3")

# 12. ROOM 10
elif st.session_state.room == "room10":
    play_sound("ambient")
    status("EXIT_NODE", 10)
    scene_img("https://images.unsplash.com/photo-1510511459019-5dee997dd1db?w=1200")
    heading("The Exit Node")
    wizard_says("You've come so far, User. Impressive. But this — this is where you end.")
    story("A bridge of white light spans an infinite ocean of static. The exit port glows ahead. But the Wizard's hand reaches from the void, ready to delete you. One final choice.")
    divider()
    door_prompt("One leads out. One leads to him. Choose.")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("DOOR A  ·  SHUT_DOWN\nPull the plug on everything", key="r10a"):
            play_sound("win"); move("end2")
    with c2:
        if st.button("DOOR B  ·  REBOOT\nStart the cycle again", key="r10b"):
            play_sound("wrong"); move("end1")

# ══════════════════════════════════════════════
# ENDINGS (written by me)
# ══════════════════════════════════════════════
elif st.session_state.room.startswith("end"):
    if st.session_state.room == "end1":
        play_sound("delete")
        st.markdown('<span class="ending-badge mid">ENDING 01 — LIMBO</span>', unsafe_allow_html=True)
        heading("System Error")
        divider()
        story("The world dissolves into white noise.<br>You find yourself in your childhood bedroom.<br>The window shows only scrolling green code.<br><br>You are neither in nor out.<br>Neither here nor there.<br><br><em>Forever.</em>")
    elif st.session_state.room == "end2":
        play_sound("win")
        st.balloons()
        st.markdown('<span class="ending-badge good">ENDING 02 — ESCAPE</span>', unsafe_allow_html=True)
        heading("System Reboot")
        divider()
        story("You wake at your desk, gasping for air.<br>Your screen is dark — then a cursor blinks once.<br><br><em>\"Update Successful.\"</em><br><br>You made it out. But somewhere in the machine,<br>the Wizard is already waiting for next time.")
    elif st.session_state.room == "end3":
        play_sound("delete")
        st.markdown('<span class="ending-badge bad">ENDING 03 — DELETED</span>', unsafe_allow_html=True)
        heading("Permanently Deleted")
        divider()
        story("Your vision shatters into static.<br>Your consciousness is purged from the drive.<br>The System reclaims every last bit of you.<br><br><em>404: USER NOT FOUND.</em>")
    elif st.session_state.room == "end4":
        play_sound("delete")
        st.markdown('<span class="ending-badge bad">ENDING 04 — VOID</span>', unsafe_allow_html=True)
        heading("Stuck in the Void")
        divider()
        story("Everything goes pitch black.<br>You escaped the Wizard — but the exit never opened.<br>The lights won't come back on.<br><br>You wait in the silence of an empty drive.<br><br><em>Nothing comes.</em>")
    divider()
    if centered_button("↺  RELOAD PROGRAM", key="btn_reload"):
        play_sound("click")
        st.session_state.intro_played = False
        st.session_state.intro_line = 0
        move("title")
