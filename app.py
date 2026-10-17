"""EasyFin, powered by NYZTrade: money learning for ages 5 to 14.  Run:  streamlit run app.py

Practice money only. No real trading, no tips, no advice.
"""
import datetime
import random
import time

import streamlit as st

import activities
import content as C
import storage
import ui
from ui import esc, inr, md

st.set_page_config(page_title="EasyFin | powered by NYZTrade", page_icon="🐿️", layout="centered", initial_sidebar_state="collapsed")

THEMES = ["auto", "light", "dark"]
THEME_LABEL = {"auto": "🌓 Auto", "light": "☀️ Light", "dark": "🌙 Dark"}

GLOBAL_BADGES = [
    ("first", "First Step", "🌟", "Finish your first lesson"),
    ("five", "High Five", "🖐️", "Finish 5 lessons"),
    ("streak3", "On Fire", "🔥", "Learn 3 days in a row"),
    ("perfect", "Perfect Round", "💯", "Get every quiz question right first time"),
    ("xp500", "Power Up", "⚡", "Earn 500 XP"),
    ("whiz", "Quiz Whiz", "🧠", "Score 10 out of 10 in a Quick Quiz"),
    ("g_seed", "Seedling Graduate", "🌱", "Finish every Seedlings lesson"),
    ("g_explore", "Explorer Graduate", "🧭", "Finish every Explorers lesson"),
    ("g_pioneer", "Pioneer Graduate", "🚀", "Finish every Pioneers lesson"),
    ("all", "Money Master", "👑", "Finish all 22 lessons"),
]


# ------------------------------------------------------------------ state
def init():
    ss = st.session_state
    if "boot" in ss:
        return
    ss.boot = True
    s = storage.settings()
    ss.theme = s["theme"] if s["theme"] in THEMES else "auto"
    ss.listen = bool(s["listen"])
    ss.name = None
    ss.P = None
    ss.page = "learn"
    ss.lesson = None
    ss.stage = "story"
    ss.step = 0
    ss.act = {}
    ss.quiz = None
    ss.parent_ok = False
    ss.confirm_reset = False
    ss.err = ""
    ss.tick = time.time()
    ss.pick_band = "seed"
    ss.quick_band = "seed"


def commit():
    ss = st.session_state
    if ss.name and ss.P is not None:
        storage.save_profile(ss.name, ss.P)


def save_settings():
    ss = st.session_state
    storage.save_settings({"theme": ss.theme, "listen": ss.listen, "last_profile": ss.name or ""})


def tick():
    ss = st.session_state
    now = time.time()
    if ss.P is not None:
        ss.P["seconds"] += int(min(now - ss.tick, 90))
    ss.tick = now


def level(xp):
    return xp // 100 + 1, xp % 100


def total_stars(P):
    return sum(P["done"].values())


def touch_day(P):
    today = datetime.date.today()
    last = P["last_day"]
    if last == today.isoformat():
        return
    if last == (today - datetime.timedelta(days=1)).isoformat():
        P["streak"] += 1
    else:
        P["streak"] = 1
    P["last_day"] = today.isoformat()


def award(P, bid, new):
    if bid not in P["badges"]:
        P["badges"].append(bid)
        new.append(bid)


def check_badges(P, perfect=False, whiz=False):
    new = []
    done = P["done"]
    if len(done) >= 1:
        award(P, "first", new)
    if len(done) >= 5:
        award(P, "five", new)
    if P["streak"] >= 3:
        award(P, "streak3", new)
    if perfect:
        award(P, "perfect", new)
    if P["xp"] >= 500:
        award(P, "xp500", new)
    if whiz:
        award(P, "whiz", new)
    for b in C.BANDS:
        if all(l["id"] in done for l in C.lessons_for(b["id"])):
            award(P, "g_" + b["id"], new)
    if len(done) == len(C.LESSONS):
        award(P, "all", new)
    return new


def badge_info(bid):
    if bid.startswith("L:"):
        l = C.LESSON_BY_ID[bid[2:]]
        return l["badge"][0], l["badge"][1], f'Finish "{l["title"]}"'
    for gid, name, em, desc in GLOBAL_BADGES:
        if gid == bid:
            return name, em, desc
    return bid, "🏅", ""


# ------------------------------------------------------------------ callbacks
def go(page):
    ss = st.session_state
    ss.page = page
    ss.lesson = None
    ss.quiz = None
    ss.act = {}
    if page != "parent":
        ss.parent_ok = False


def cycle_theme():
    ss = st.session_state
    ss.theme = THEMES[(THEMES.index(ss.theme) + 1) % len(THEMES)]
    save_settings()


def toggle_listen():
    st.session_state.listen = not st.session_state.listen
    save_settings()


def set_band(band):
    ss = st.session_state
    ss.P["band"] = band
    commit()


def start_profile():
    ss = st.session_state
    nick = (ss.get("nick") or "").strip()[:20]
    if not nick:
        ss.err = "Please type a nickname."
        return
    if not ss.get("consent"):
        ss.err = "A parent or guardian needs to be with you. Tick the box when they are."
        return
    ss.err = ""
    open_profile(nick, ss.pick_band)


def open_profile(nick, band=None):
    ss = st.session_state
    ss.name = nick
    ss.P = storage.load_profile(nick)
    if band and not ss.P["done"] and ss.P["xp"] == 0:
        ss.P["band"] = band
    ss.tick = time.time()
    commit()
    save_settings()
    ss.page = "learn"


def switch_child():
    ss = st.session_state
    ss.name, ss.P, ss.lesson, ss.quiz, ss.parent_ok = None, None, None, None, False
    ss.act = {}


def open_lesson(lid):
    ss = st.session_state
    ss.lesson, ss.stage, ss.step, ss.act, ss.quiz = lid, "story", 0, {}, None


def story_move(delta, n):
    ss = st.session_state
    ss.step += delta
    if ss.step >= n:
        ss.stage = "game"
        ss.step = 0
    ss.step = max(0, ss.step)


def to_quiz(lid):
    ss = st.session_state
    ss.stage = "quiz"
    ss.quiz = build_quiz("lesson", C.LESSON_BY_ID[lid]["bank"], C.QUESTIONS_PER_PLAY, lid)


def build_quiz(kind, pool, n, lid=None):
    qs = []
    for q, opts, ans, why in random.sample(pool, min(n, len(pool))):
        order = list(range(len(opts)))
        random.shuffle(order)
        qs.append(dict(q=q, opts=[opts[j] for j in order], right=order.index(ans), why=why))
    return dict(kind=kind, lid=lid, qs=qs, i=0, wrong=[], answered=False, first_ok=0, xp=0, result=None)


def pick(oi):
    ss = st.session_state
    qz = ss.quiz
    q = qz["qs"][qz["i"]]
    if qz["answered"] or oi in qz["wrong"]:
        return
    if oi == q["right"]:
        first = not qz["wrong"]
        qz["answered"] = True
        ss.P["q_total"] += 1
        gain = 10 if first else 5
        if first:
            qz["first_ok"] += 1
            ss.P["q_first"] += 1
        ss.P["xp"] += gain
        qz["xp"] += gain
        commit()
    else:
        qz["wrong"].append(oi)


def next_q():
    ss = st.session_state
    qz = ss.quiz
    if qz["i"] + 1 < len(qz["qs"]):
        qz["i"] += 1
        qz["wrong"], qz["answered"] = [], False
    else:
        finish_quiz()


def finish_quiz():
    ss = st.session_state
    qz, P = ss.quiz, ss.P
    n = len(qz["qs"])
    touch_day(P)
    if qz["kind"] == "lesson":
        lid = qz["lid"]
        stars_ = 3 if qz["first_ok"] >= n - 1 else (2 if qz["first_ok"] >= n - 2 else 1)
        bonus = 20 + 10 * stars_
        P["xp"] += bonus
        qz["xp"] += bonus
        P["done"][lid] = max(P["done"].get(lid, 0), stars_)
        P["lessons_played"] += 1
        new = []
        award(P, "L:" + lid, new)
        new += check_badges(P, perfect=qz["first_ok"] == n)
        qz["result"] = dict(stars=stars_, bonus=bonus, new=new)
    else:
        band = ss.quick_band
        bonus = 20 if qz["first_ok"] >= 8 else 5
        P["xp"] += bonus
        qz["xp"] += bonus
        P["quick_best"][band] = max(P["quick_best"].get(band, 0), qz["first_ok"])
        new = check_badges(P, whiz=qz["first_ok"] == n)
        qz["result"] = dict(stars=0, bonus=bonus, new=new)
    commit()


def start_quick():
    ss = st.session_state
    ss.quiz = build_quiz("quick", C.band_question_pool(ss.quick_band), C.QUICK_QUIZ_LENGTH)


def pick_quick_band(b):
    st.session_state.quick_band = b
    st.session_state.quiz = None


def pick_onboard_band(b):
    st.session_state.pick_band = b


def check_gate():
    ss = st.session_state
    try:
        ok = int(str(ss.get("gate", "")).strip()) == ss.gate_answer
    except ValueError:
        ok = False
    ss.parent_ok = ok
    ss.err = "" if ok else "That is not right. Try again."


def lock_parent():
    st.session_state.parent_ok = False


def ask_reset():
    st.session_state.confirm_reset = True


def do_reset():
    ss = st.session_state
    storage.delete_profile(ss.name)
    ss.confirm_reset = False
    switch_child()


def cancel_reset():
    st.session_state.confirm_reset = False


# ------------------------------------------------------------------ shared UI
def band_buttons(current, on_pick, prefix):
    with st.container(key=f"ns-{prefix}-bands"):
        cols = st.columns(len(C.BANDS))
        for col, b in zip(cols, C.BANDS):
            with col:
                state = "tab-on" if b["id"] == current else "tab"
                with st.container(key=f"{state}-{prefix}-{b['id']}"):
                    st.button(f'{b["name"]}\n{b["ages"].replace("Ages ", "")}', key=f"{prefix}-{b['id']}", on_click=on_pick, args=(b["id"],))


def topbar():
    ss = st.session_state
    with st.container(key="ns-top"):
        c1, c2 = st.columns([2.2, 1.4])
        with c1:
            md('<div class="nk-row"><span style="font-size:1.8rem">🐿️</span><div><div class="nk-title" style="font-size:1.1rem;white-space:nowrap">EasyFin</div><div class="nk-sub" style="margin:0;white-space:nowrap">powered by <b>NYZTrade</b></div></div></div>')
        with c2:
            st.button(THEME_LABEL[ss.theme], key="theme-btn", on_click=cycle_theme)


def nav():
    ss = st.session_state
    items = [("learn", "🎒 Learn"), ("quick", "⚡ Quiz"), ("rewards", "🏆 Rewards"), ("parent", "👪 Parent")]
    with st.container(key="ns-nav"):
        cols = st.columns(len(items))
        for col, (pid, label) in zip(cols, items):
            with col:
                state = "tab-on" if ss.page == pid else "tab"
                with st.container(key=f"{state}-nav-{pid}"):
                    st.button(label, key=f"nav-{pid}", on_click=go, args=(pid,))


def stats_row(P):
    lv, into = level(P["xp"])
    md(f'<div class="nk-stats">'
       f'<div class="nk-stat"><b>⭐ {total_stars(P)}</b><span>stars</span></div>'
       f'<div class="nk-stat"><b>🔥 {P["streak"]}</b><span>day streak</span></div>'
       f'<div class="nk-stat"><b>⚡ {P["xp"]}</b><span>XP</span></div>'
       f'<div class="nk-stat"><b>Lv {lv}</b><span>level</span></div></div>')


def footer():
    md('<div class="nk-foot">Practice money only. EasyFin teaches ideas and habits. It gives no investment advice or tips, '
       'and no real money moves here. Examples use made-up numbers.<br><b>EasyFin</b> · powered by <b>NYZTrade</b></div>')


# ------------------------------------------------------------------ onboarding
def onboarding():
    ss = st.session_state
    md('<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">Hi, I am Chintu!</div>'
       '<small>Welcome to <b>EasyFin</b>. Learn how money works through stories, games and quizzes. Ages 5 to 14.</small><br><small style="opacity:.85">powered by NYZTrade</small></div>')
    names = storage.profile_names()
    if names:
        md('<div class="nk-title" style="font-size:1.05rem">Welcome back</div>')
        for n in names[:8]:
            st.button(f"🐿️ {n}", key=f"prof-{n}", on_click=open_profile, args=(n,))
        md('<div class="nk-sub" style="text-align:center">or start a new learner</div>')
    with st.container(key="card-new"):
        st.text_input("Pick a nickname (not your full name)", key="nick", max_chars=20, placeholder="e.g. Aarav")
        md('<div class="nk-sub">Choose your age group</div>')
        band_buttons(ss.pick_band, pick_onboard_band, "ob")
        st.checkbox("My parent or guardian is with me and agrees", key="consent")
        if ss.err:
            ui.md(f'<div class="nk-fb no">{esc(ss.err)}</div>')
        st.button("Let us start ➜", key="start", type="primary", on_click=start_profile)
    footer()


# ------------------------------------------------------------------ learn
def learn():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    done_n = len(P["done"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🐿️</div><div class="nk-title">Hi {esc(ss.name)}!</div>'
       f'<small>{done_n} of {len(C.LESSONS)} lessons done. Keep going!</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div>'
       f'<small>Level {lv}, {100 - into} XP to level {lv + 1}</small></div>')
    stats_row(P)
    band_buttons(P["band"], set_band, "lb")
    band = C.BAND_BY_ID[P["band"]]
    md(f'<div class="nk-sub" style="text-align:center">{esc(band["note"])}</div>')
    for l in C.lessons_for(P["band"]):
        s = P["done"].get(l["id"], 0)
        with st.container(key=f"card-{l['id']}"):
            md(f'<div class="nk-row"><div class="nk-art">{l["art"]}</div><div class="nk-grow"><div class="nk-title" style="font-size:1.1rem">{esc(l["title"])}</div>'
               f'<div class="nk-sub">{esc(l["blurb"])}</div></div></div>'
               f'<div class="nk-stars" style="color:var(--sun);margin:6px 0 2px">{ui.stars(s)}</div>')
            st.button("Play again" if s else "Play ➜", key=f"play-{l['id']}", type="secondary" if s else "primary",
                      on_click=open_lesson, args=(l["id"],))


# ------------------------------------------------------------------ lesson
def exit_lesson():
    go("learn")


def lesson_view():
    ss = st.session_state
    l = C.LESSON_BY_ID[ss.lesson]
    with st.container(key="ns-lhead"):
        c1, c2 = st.columns([1, 3])
        with c1:
            st.button("✕", key="exit", on_click=exit_lesson)
        with c2:
            md(f'<div class="nk-title" style="padding-top:6px">{l["art"]} {esc(l["title"])}</div>')
    if ss.stage == "story":
        story_view(l)
    elif ss.stage == "game":
        game_view(l)
    else:
        quiz_view(l["bank"], l)


def story_view(l):
    ss = st.session_state
    n = len(l["story"])
    em, text = l["story"][ss.step]
    md(ui.dots(ss.step, ss.step, n))
    md(f'<div class="nk-story nk-pop"><div class="em">{em}</div><p>{esc(text)}</p></div>')
    if ss.listen:
        ui.listen(text)
    with st.container(key="ns-story-nav"):
        c1, c2 = st.columns([1, 2])
        with c1:
            st.button("◀ Back", key="story-back", on_click=story_move, args=(-1, n), disabled=ss.step == 0)
        with c2:
            st.button("Next ▶" if ss.step < n - 1 else "Let us play! 🎮", key="story-next", type="primary", on_click=story_move, args=(1, n))


def game_view(l):
    ss = st.session_state
    finished = activities.play(l)
    if finished:
        st.button("Take the quiz ➜", key="to-quiz", type="primary", on_click=to_quiz, args=(l["id"],))


def quiz_view(bank, l=None):
    ss = st.session_state
    qz = ss.quiz
    if qz is None:
        to_quiz(l["id"])
        qz = ss.quiz
    if qz["result"]:
        return result_view(l)
    n = len(qz["qs"])
    q = qz["qs"][qz["i"]]
    md(ui.dots(qz["i"], qz["i"], n))
    md(f'<div class="nk-sub" style="text-align:center">Question {qz["i"] + 1} of {n}</div>')
    md(f'<div class="nk-q">{esc(q["q"])}</div>')
    if ss.listen:
        ui.listen(q["q"] + " " + ". ".join(q["opts"]))
    for oi, text in enumerate(q["opts"]):
        if qz["answered"]:
            state = "ok" if oi == q["right"] else "opt"
        else:
            state = "no" if oi in qz["wrong"] else "opt"
        with st.container(key=f"{state}-q{qz['i']}-{oi}"):
            st.button(text, key=f"q{qz['i']}-o{oi}", on_click=pick, args=(oi,), disabled=qz["answered"] or oi in qz["wrong"])
    if qz["answered"]:
        first = not qz["wrong"]
        ui.md(f'<div class="nk-fb ok nk-pop">{"Great job! " if first else "You got it! "}{esc(q["why"])}</div>')
        last = qz["i"] + 1 >= n
        st.button("See my results ➜" if last else "Next question ➜", key="next-q", type="primary", on_click=next_q)
    elif qz["wrong"]:
        ui.md('<div class="nk-fb hint">Not quite. That is okay. Try another answer.</div>')


def result_view(l):
    ss = st.session_state
    qz = ss.quiz
    res = qz["result"]
    n = len(qz["qs"])
    if qz["kind"] == "lesson":
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">Lesson complete!</div>'
           f'<div style="font-size:2.6rem;letter-spacing:6px;margin:6px 0">{"⭐" * res["stars"]}{"☆" * (3 - res["stars"])}</div>'
           f'<small>{qz["first_ok"]} of {n} right on the first try. +{qz["xp"]} XP</small></div>')
        md(f'<div class="nk-card"><div class="nk-title" style="font-size:1.05rem">Talk about it at home</div><div class="nk-sub">{esc(l["talk"])}</div></div>')
    else:
        md(f'<div class="nk-hero nk-pop" style="text-align:center"><div class="nk-title">Quick Quiz done!</div>'
           f'<div class="nk-big" style="color:#fff">{qz["first_ok"]} / {n}</div><small>+{qz["xp"]} XP</small></div>')
    for bid in res["new"]:
        name, em, desc = badge_info(bid)
        md(f'<div class="nk-fb hint nk-pop">{em} New badge: <b>{esc(name)}</b>. {esc(desc)}</div>')
    if qz["kind"] == "lesson":
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Play again", key="res-again", on_click=open_lesson, args=(l["id"],))
            with c2:
                st.button("Back to lessons", key="res-back", type="primary", on_click=go, args=("learn",))
    else:
        with st.container(key="ns-res-act"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Another round", key="res-again", on_click=start_quick)
            with c2:
                st.button("Back to lessons", key="res-back", type="primary", on_click=go, args=("learn",))


# ------------------------------------------------------------------ quick quiz
def quick_view():
    ss = st.session_state
    P = ss.P
    if ss.quiz and ss.quiz["kind"] == "quick":
        return quiz_view(None, None)
    md('<div class="nk-hero"><div class="nk-mascot">⚡</div><div class="nk-title">Quick Quiz</div>'
       '<small>10 mixed questions from the whole age group. Earn XP and try for 10 out of 10!</small></div>')
    band_buttons(ss.quick_band, pick_quick_band, "qb")
    pool = len(C.band_question_pool(ss.quick_band))
    best = P["quick_best"].get(ss.quick_band)
    md(f'<div class="nk-card"><div class="nk-sub">{pool} questions in this group. Best score: <b>{best if best is not None else "none yet"}</b>{" / 10" if best is not None else ""}</div></div>')
    st.button("Start 10 questions ➜", key="quick-start", type="primary", on_click=start_quick)


# ------------------------------------------------------------------ rewards
def rewards_view():
    ss = st.session_state
    P = ss.P
    lv, into = level(P["xp"])
    md(f'<div class="nk-hero"><div class="nk-mascot">🏆</div><div class="nk-title">Level {lv}</div>'
       f'<small>{P["xp"]} XP in total. {100 - into} XP to the next level.</small>'
       f'<div style="margin-top:10px;background:rgba(255,255,255,.28);border-radius:99px;height:12px;overflow:hidden"><i style="display:block;height:100%;width:{into}%;background:#FFD27A;border-radius:99px"></i></div></div>')
    stats_row(P)
    md('<div class="nk-title" style="margin-top:6px">Lesson badges</div>')
    cells = ""
    for l in C.LESSONS:
        got = "L:" + l["id"] in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{l["badge"][1]}</div><b>{esc(l["badge"][0])}</b><span>{ui.stars(P["done"].get(l["id"], 0))}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')
    md('<div class="nk-title" style="margin-top:6px">Special badges</div>')
    cells = ""
    for gid, name, em, desc in GLOBAL_BADGES:
        got = gid in P["badges"]
        cells += f'<div class="nk-badge {"" if got else "locked"}"><div class="em">{em}</div><b>{esc(name)}</b><span>{esc(desc)}</span></div>'
    md(f'<div class="nk-grid">{cells}</div>')


# ------------------------------------------------------------------ parent
def parent_view():
    ss = st.session_state
    P = ss.P
    if not ss.parent_ok:
        if "gate_answer" not in ss:
            a, b = random.randint(6, 9), random.randint(6, 9)
            ss.gate_q, ss.gate_answer = f"{a} × {b}", a * b
        md('<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">Parent corner</div><small>A quick grown-up check, then you can see progress and settings.</small></div>')
        with st.container(key="card-gate"):
            st.text_input(f"What is {ss.gate_q}?", key="gate", max_chars=3)
            if ss.err:
                ui.md(f'<div class="nk-fb no">{esc(ss.err)}</div>')
            st.button("Open", key="gate-open", type="primary", on_click=check_gate)
        return
    acc = round(P["q_first"] / P["q_total"] * 100) if P["q_total"] else 0
    minutes = round(P["seconds"] / 60)
    md(f'<div class="nk-hero"><div class="nk-mascot">👪</div><div class="nk-title">{esc(ss.name)}\'s progress</div>'
       f'<small>Age group: {esc(C.BAND_BY_ID[P["band"]]["name"])} · learning since {esc(P["created"])}</small></div>')
    md(f'<div class="nk-stats"><div class="nk-stat"><b>{len(P["done"])}/{len(C.LESSONS)}</b><span>lessons</span></div>'
       f'<div class="nk-stat"><b>{acc}%</b><span>first-try right</span></div>'
       f'<div class="nk-stat"><b>{minutes}</b><span>minutes</span></div>'
       f'<div class="nk-stat"><b>{P["streak"]}</b><span>day streak</span></div></div>')
    for b in C.BANDS:
        ls = C.lessons_for(b["id"])
        d = sum(1 for l in ls if l["id"] in P["done"])
        md(f'<div class="nk-card"><div class="nk-row"><div class="nk-grow"><div class="nk-title" style="font-size:1rem">{esc(b["name"])} · {esc(b["ages"])}</div>'
           f'<div class="nk-sub">{d} of {len(ls)} lessons</div></div></div><div style="margin-top:6px">{ui.bar(d / len(ls) * 100, True)}</div></div>')
    md('<div class="nk-title" style="margin-top:6px">Talk at home</div>')
    rows = ""
    for l in C.LESSONS:
        s = P["done"].get(l["id"], 0)
        mark = ui.stars(s) if s else "not yet"
        rows += f'<tr><td>{l["art"]} <b>{esc(l["title"])}</b><br><span class="nk-sub">{esc(l["talk"])}</span></td><td style="white-space:nowrap">{mark}</td></tr>'
    md(f'<div class="nk-card"><table class="nk-table"><tr><th>Lesson and conversation starter</th><th>Stars</th></tr>{rows}</table></div>')
    md(f'<div class="nk-card"><div class="nk-title" style="font-size:1rem">Question bank</div><div class="nk-sub">{C.total_questions()} questions across {len(C.LESSONS)} lessons. Each play draws {C.QUESTIONS_PER_PLAY} at random, so replays feel fresh.</div></div>')
    md('<div class="nk-title" style="margin-top:6px">Settings</div>')
    with st.container(key="ns-set"):
        c1, c2 = st.columns(2)
        with c1:
            st.button(THEME_LABEL[ss.theme], key="set-theme", on_click=cycle_theme)
        with c2:
            st.button("🔊 Read aloud: " + ("on" if ss.listen else "off"), key="set-listen", on_click=toggle_listen)
    st.download_button("Download progress (JSON)", storage.export_json(ss.name), file_name=f"easyfin-{ss.name}.json", mime="application/json")
    with st.container(key="ns-set2"):
        c1, c2 = st.columns(2)
        with c1:
            st.button("Switch learner", key="set-switch", on_click=switch_child)
        with c2:
            st.button("🔒 Lock", key="set-lock", on_click=lock_parent)
    if not ss.confirm_reset:
        st.button("Delete this learner's data", key="reset", on_click=ask_reset)
    else:
        ui.md('<div class="nk-fb no">This deletes all progress for this learner. It cannot be undone.</div>')
        with st.container(key="ns-reset"):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Yes, delete", key="reset-yes", on_click=do_reset)
            with c2:
                st.button("Keep it", key="reset-no", on_click=cancel_reset)
    md('<div class="nk-card"><div class="nk-title" style="font-size:1rem">Privacy and safety</div>'
       '<div class="nk-sub">Only a nickname and progress are stored, on this device. No ads, no chat, no real money. '
       'If you run this online for children, get verifiable parental consent as required by the DPDP Act and Rules, and keep the content educational only.</div></div>')


# ------------------------------------------------------------------ main
def main():
    init()
    ss = st.session_state
    ui.inject(ss.theme)
    if ss.P is None:
        topbar()
        onboarding()
        return
    tick()
    if ss.lesson:
        lesson_view()
        footer()
        return
    topbar()
    nav()
    {"learn": learn, "quick": quick_view, "rewards": rewards_view, "parent": parent_view}[ss.page]()
    footer()


main()
