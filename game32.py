"""
wizard_exe.py — Wizard.exe main game
Run with: streamlit run wizard_exe.py
"""
import time
import streamlit as st

# ── Local modules ──
from styles import inject_styles
from sound import play_sound
from ui import (
    scene_img, divider, status, story, heading,
    door_prompt, wizard_says, centered_button, render_dialogue,
)

# ── Page config ──
st.set_page_config(
    page_title="WIZARD.EXE",
    layout="centered",
    initial_sidebar_state="collapsed",
)

inject_styles()

# ── Session state ──
for k, v in [("room", "title"), ("intro_played", False), ("intro_line", 0)]:
    if k not in st.session_state:
        st.session_state[k] = v


def move(room_name: str) -> None:
    st.session_state.room = room_name
    st.rerun()


# ══════════════════════════════════════════════
# PAGES
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
        ("wizard", "Wizard", "Ah… finally. Don't look so confused, User. You aren't 'here' anymore."),
        ("player", "You",    "Where am I? Why can't I feel my hands?"),
        ("wizard", "Wizard", "I've translated your messy biology into perfect code. You're inside the System now."),
        ("wizard", "Wizard", "There are many doors between you and the Shutdown button. Each one is a test."),
        ("player", "You",    "You're insane. I'm getting out of here."),
        ("wizard", "Wizard", "Good luck, User. The System doesn't forgive mistakes."),
    ]
    placeholder = st.empty()
    if not st.session_state.intro_played:
        n = st.session_state.intro_line
        placeholder.markdown(render_dialogue(lines, n), unsafe_allow_html=True)
        if n < len(lines):
            time.sleep(0.85)
            st.session_state.intro_line += 1
            st.rerun()
        else:
            st.session_state.intro_played = True
    else:
        placeholder.markdown(render_dialogue(lines, len(lines)), unsafe_allow_html=True)
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
# ENDINGS
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
