import streamlit as st

st.set_page_config(page_title="연애 지갑 유형 테스트", page_icon="💌", layout="centered")

QUESTIONS = [
    ("데이트 비용은 보통 어떻게 정해?", "G", "상황에 맞춰 내가 더 낼 수도 있지!", "서로 부담이 비슷하도록 맞추는 편"),
    ("상대가 갖고 싶어 하던 선물을 발견했다면?", "G", "내가 사주고 싶은 마음이 먼저 든다", "예산과 기념일을 보고 결정한다"),
    ("연인이 갑자기 경제적으로 어려워졌다면?", "G", "내가 여유 있는 만큼 적극 도와준다", "서로 감당할 수 있는 범위를 먼저 상의한다"),
    ("한 달 데이트비 관리 방식은?", "P", "대략적인 예산을 정해둔다", "그날그날 즐기는 편이다"),
    ("비싼 여행을 가자는 제안을 받았어!", "P", "숙박·교통비부터 계산해본다", "일단 가자! 자세한 건 나중에"),
    ("연인과 공동 통장을 만든다면?", "P", "입금액과 사용 규칙부터 정한다", "필요할 때 넣고 편하게 쓰고 싶다"),
    ("기념일에 한 가지를 고른다면?", "E", "함께하는 특별한 여행이나 체험", "오래 남는 선물이나 실용적인 물건"),
    ("뜻밖의 보너스가 생겼다면?", "E", "둘만의 특별한 데이트를 예약한다", "필요했던 물건을 함께 장만한다"),
    ("연인과 돈을 쓸 때 가장 만족스러운 순간은?", "E", "새로운 추억을 함께 만들었을 때", "오랫동안 유용하게 쓸 것을 샀을 때"),
]

TYPES = {
    "111": ("로맨틱 플렉스 기획자", "💎", "상대에게 아낌없이 표현하지만, 중요한 지출은 미리 준비해요.", "서프라이즈 예산을 따로 정해두면 만족도가 더 높아져요."),
    "110": ("든든한 선물 설계자", "🎁", "연인을 챙기는 마음과 현실적인 예산 감각을 함께 가졌어요.", "선물 가격보다 서로 원하는 것을 먼저 확인해보세요."),
    "101": ("즉흥 로맨스 메이커", "🎡", "재밌는 경험에 아낌없이 투자하며 특별한 순간을 만들어요.", "충동적인 큰 지출 전에는 하루만 생각해보세요."),
    "100": ("통 큰 현실주의자", "🧸", "연인을 위해 쓰는 돈은 아깝지 않지만, 오래 남는 가치를 좋아해요.", "도움과 선물의 범위를 미리 정하면 부담이 줄어요."),
    "011": ("스마트 데이트 전략가", "🗺️", "공정한 분담과 철저한 계획으로 알찬 추억을 쌓아요.", "가끔은 계획 밖의 소소한 데이트도 즐겨보세요."),
    "010": ("알뜰살뜰 미래 설계자", "🏡", "균형 잡힌 소비와 장기적인 안정감을 중요하게 생각해요.", "절약의 이유뿐 아니라 즐거움의 가치도 공유해보세요."),
    "001": ("자유로운 추억 수집가", "🌈", "각자의 자율성을 지키면서 즐거운 경험을 추구해요.", "여행 같은 큰 지출만큼은 사전에 상의해보세요."),
    "000": ("쿨한 실속 동반자", "🌿", "부담 없는 관계와 실용적인 소비를 편하게 느껴요.", "평소 표현이 적더라도 소소한 이벤트를 계획해보세요."),
}

st.markdown("""
<style>
.stApp {background: #fff9f8; color: #493640;}
.block-container {max-width: 690px; padding-top: 2.4rem; padding-bottom: 3rem;}
h1, h2, h3 {color: #673e53 !important;}
div.stButton > button {border-radius: 16px; padding: .7rem 1rem; border: 1px solid #eecbd7; width:100%;}
div.stButton > button[kind="primary"] {background: #c85c85; color: white; border-color: #c85c85;}
.hero {background: linear-gradient(130deg,#ffe7ef,#fff2e8); padding: 28px 20px; border-radius: 24px; text-align:center; margin-bottom:20px;}
.small {color: #8d6779; letter-spacing: 2px; font-size:12px; font-weight: 700;}
.question {font-size: 1.35rem; font-weight: 750; padding: 12px 0 20px;}
.result {background:white; border: 1px solid #f5dce4; padding:25px; border-radius:22px; text-align:center;}
</style>
""", unsafe_allow_html=True)

if "stage" not in st.session_state:
    st.session_state.stage = "intro"
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "answers" not in st.session_state:
    st.session_state.answers = []


def restart():
    st.session_state.stage = "intro"
    st.session_state.idx = 0
    st.session_state.answers = []


def answer(v):
    st.session_state.answers.append(v)
    st.session_state.idx += 1
    if st.session_state.idx >= len(QUESTIONS):
        st.session_state.stage = "result"
    st.rerun()

if st.session_state.stage == "intro":
    st.markdown('<div class="hero"><div class="small">LOVE & MONEY TEST</div><h1>💌 연애 지갑 유형 테스트</h1><p>사랑 앞에서 내 지갑은 어떤 스타일일까?</p><p>9문항 · 약 1분 · 결과 8가지</p></div>', unsafe_allow_html=True)
    st.write("데이트비, 선물, 여행에서 드러나는 나의 경제관념을 가볍게 알아봐요.")
    if st.button("내 연애 지갑 알아보기 💗", type="primary"):
        st.session_state.stage = "quiz"
        st.rerun()
    st.caption("재미를 위한 비공식 성향 테스트로, 심리검사나 재무 진단이 아닙니다. 답변은 서버 DB에 저장하지 않습니다.")

elif st.session_state.stage == "quiz":
    i = st.session_state.idx
    q, axis, a, b = QUESTIONS[i]
    st.progress(i / len(QUESTIONS))
    st.caption(f"QUESTION {i+1} / {len(QUESTIONS)}")
    st.markdown(f'<div class="question">{q}</div>', unsafe_allow_html=True)
    if st.button("A. " + a, key=f"a{i}", use_container_width=True):
        answer(1)
    if st.button("B. " + b, key=f"b{i}", use_container_width=True):
        answer(0)
    st.write("")
    if i > 0 and st.button("← 이전 질문", key="prev"):
        st.session_state.idx -= 1
        st.session_state.answers.pop()
        st.rerun()

else:
    scores = {"G": 0, "P": 0, "E": 0}
    for (_, axis, _, _), v in zip(QUESTIONS, st.session_state.answers):
        scores[axis] += v
    key = "".join("1" if scores[x] >= 2 else "0" for x in ("G", "P", "E"))
    name, emoji, desc, tip = TYPES[key]
    st.markdown('<div class="small" style="text-align:center;">YOUR LOVE & MONEY TYPE</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="result"><div style="font-size:72px">{emoji}</div><h1>{name}</h1><p>{desc}</p></div>', unsafe_allow_html=True)
    st.write("")
    st.subheader("나의 연애 경제관념")
    labels = [("G", "표현과 베풂", "균형과 독립"), ("P", "계획과 관리", "즉흥과 자유"), ("E", "경험과 추억", "실용과 소유")]
    for axis, high, low in labels:
        st.write(f"**{high if scores[axis]>=2 else low}** · {scores[axis]}/3 (왼쪽 성향 점수)")
        st.progress(scores[axis] / 3)
    st.info("💡 연애 지갑 TIP: " + tip)
    st.caption("이 유형은 답변을 세 영역으로 합산해 분류한 재미용 결과이며, 과학적으로 검증된 심리 진단은 아닙니다.")
    share_text = f"나의 연애 지갑 유형은 '{emoji} {name}'! 💌 너도 해볼래?"
    st.code(share_text, language=None)
    st.caption("위 문구를 복사하고, 배포한 웹사이트 주소와 함께 친구에게 보내보세요.")
    if st.button("다시 테스트하기 🔄", type="primary"):
        restart()
        st.rerun()
