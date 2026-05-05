"""
ui.py — Wizard.exe UI helper functions
All reusable rendering helpers used across the game's rooms and endings.
"""
import streamlit as st


def scene_img(url: str) -> None:
    """Render a full-width scene image with neon border and corner brackets."""
    st.markdown(
        f'<div class="scene-image-wrap">'
        f'<img src="{url}&auto=format&fit=crop" alt="scene">'
        f'</div>',
        unsafe_allow_html=True,
    )


def divider() -> None:
    """Render a thin neon horizontal divider."""
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)


def status(node: str, room_num: int = None, total: int = 10) -> None:
    """Render the top status bar with optional progress bar and room counter."""
    prog = ""
    room_tag = ""
    if room_num is not None:
        pct = int(room_num / total * 100)
        prog = (
            f'<div class="progress-wrap">'
            f'<div class="progress-fill" style="width:{pct}%"></div>'
            f'</div>'
        )
        room_tag = f'&nbsp;|&nbsp; NODE <span>{room_num:02d}&nbsp;/&nbsp;{total}</span>'
    st.markdown(
        f'{prog}<p class="status-bar">SYSTEM: <span>{node}</span>{room_tag}</p>',
        unsafe_allow_html=True,
    )


def story(text: str) -> None:
    """Render centered story/description text."""
    st.markdown(f'<p class="story-text">{text}</p>', unsafe_allow_html=True)


def heading(text: str) -> None:
    """Render a neon Orbitron section heading."""
    st.markdown(f'<h2 class="section-heading">{text}</h2>', unsafe_allow_html=True)


def door_prompt(text: str) -> None:
    """Render a small centered prompt shown above door choices."""
    st.markdown(
        f'<p class="door-prompt">&#8594;&nbsp; {text} &nbsp;&#8592;</p>',
        unsafe_allow_html=True,
    )


def wizard_says(text: str) -> None:
    """Render a single Wizard dialogue bubble."""
    st.markdown(
        f'<div class="dialogue">'
        f'<div class="dialogue-line wizard">'
        f'<span class="speaker">Wizard</span>{text}'
        f'</div></div>',
        unsafe_allow_html=True,
    )


def centered_button(label: str, key: str = None) -> bool:
    """Render a single button centred in a narrow column. Returns True when clicked."""
    _, col, _ = st.columns([1, 2, 1])
    with col:
        return st.button(label, key=key)


def render_dialogue(lines: list, count: int) -> str:
    """
    Build the HTML string for the intro dialogue animation.

    Args:
        lines:  List of (role, speaker, text) tuples.
        count:  How many lines to render (used for the typewriter effect).

    Returns:
        HTML string ready for st.markdown().
    """
    html = '<div class="dialogue">'
    for role, speaker, text in lines[:count]:
        html += (
            f'<div class="dialogue-line {role}">'
            f'<span class="speaker">{speaker}</span>{text}'
            f'</div>'
        )
    html += '</div>'
    return html
