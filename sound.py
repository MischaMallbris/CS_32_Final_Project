"""
sound.py — Wizard.exe sound engine
Each play_sound() call renders a self-contained components.html block with the
Web Audio code baked in. A unique uid forces Streamlit to treat each call as a
new component so the script always executes.
"""
import random
import streamlit.components.v1 as components

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


def play_sound(name: str) -> None:
    """Play a synthesised sound effect by name."""
    js = SOUND_JS.get(name, "")
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
