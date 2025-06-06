# app.py

import streamlit as st

# MBTI 유형별 가상 데이터 정의 (기존 로직과 동일)
# 이 데이터는 실제 연구가 아닌, 재미를 위해 만들어진 가상의 정보입니다.
mbti_data = {
    'INTJ': {'emoji': '🐲', 'score': 96, 'strengths': '논리적 비판, 비문학 독해, 구조 분석에 강점을 보입니다.'},
    'INTP': {'emoji': '🦉', 'score': 94, 'strengths': '복잡한 이론을 이해하고 추론하며, 독창적인 해석을 잘합니다.'},
    'ENTJ': {'emoji': '🦅', 'score': 95, 'strengths': '토론과 발표에 능하며, 글의 핵심 주장을 빠르게 파악합니다.'},
    'ENTP': {'emoji': '🦄', 'score': 93, 'strengths': '다양한 관점을 제시하고, 창의적인 문제 해결 능력이 뛰어납니다.'},
    'INFJ': {'emoji': '🐋', 'score': 95, 'strengths': '문학 작품에 깊이 공감하며, 인물의 내면 심리 분석에 탁월합니다.'},
    'INFP': {'emoji': '🌸', 'score': 93, 'strengths': '시적 표현을 잘 이해하고, 감성적이고 깊이 있는 글쓰기를 잘합니다.'},
    'ENFJ': {'emoji': '☀️', 'score': 92, 'strengths': '화법과 작문에 능숙하며, 타인을 설득하고 공감을 이끌어내는 능력이 좋습니다.'},
    'ENFP': {'emoji': '🦋', 'score': 91, 'strengths': '풍부한 상상력을 바탕으로 자유로운 형식의 글쓰기를 즐깁니다.'},
    'ISTJ': {'emoji': '🧱', 'score': 94, 'strengths': '문법, 어문 규정을 꼼꼼하게 학습하고 체계적으로 내용을 정리합니다.'},
    'ISFJ': {'emoji': '🛡️', 'score': 90, 'strengths': '세부 내용을 잘 기억하고, 안정적이고 성실한 학습 태도를 가집니다.'},
    'ESTJ': {'emoji': '🏛️', 'score': 92, 'strengths': '명확한 근거를 바탕으로 실용적인 글을 쓰는 것을 선호합니다.'},
    'ESFJ': {'emoji': '🤝', 'score': 89, 'strengths': '자신의 경험을 바탕으로 한 작문에 능하고, 의사소통 능력이 좋습니다.'},
    'ISTP': {'emoji': '🔧', 'score': 88, 'strengths': '문제 해결 중심으로 독해하며, 언어의 기술적 측면을 분석하는 것을 즐깁니다.'},
    'ISFP': {'emoji': '🎨', 'score': 87, 'strengths': '작품의 예술성을 감상하고, 미적 감수성을 바탕으로 주관적 감상을 잘 표현합니다.'},
    'ESTP': {'emoji': '⚡️', 'score': 86, 'strengths': '실전 문제 풀이에 강하고, 토론 등에서 순발력과 임기응변이 뛰어납니다.'},
    'ESFP': {'emoji': '🎤', 'score': 85, 'strengths': '생생한 경험을 바탕으로 표현력이 좋으며, 대중적인 글쓰기에 재능이 있습니다.'}
}

# --- Streamlit UI 구성 ---

# 1. 제목과 설명
st.title("👑 MBTI 유형별 국어 가상 성취도 분석기")
st.caption("재미로 보는 MBTI별 국어 강점 분석! (가상 데이터 기반)")

# 2. MBTI 유형 선택 (Selectbox 사용)
st.divider() # 구분선
mbti_options = list(mbti_data.keys())
selected_mbti = st.selectbox(
    '분석하고 싶은 MBTI 유형을 선택하세요.',
    options=mbti_options,
    index=None, # 처음에 아무것도 선택되지 않도록 설정
    placeholder="MBTI 유형을 선택해주세요..."
)

# 3. 선택된 유형에 대한 정보 표시
if selected_mbti:
    info = mbti_data[selected_mbti]
    
    # st.subheader() 와 st.markdown() 을 사용해 결과 보기 좋게 표시
    st.subheader(f"{selected_mbti} {info['emoji']} 유형 분석 결과")
    
    col1, col2 = st.columns(2) # 2개의 컬럼으로 레이아웃 나누기
    with col1:
        st.markdown("**가상 평균 점수**")
        st.metric(label="점수", value=f"{info['score']} 점")

    with col2:
        st.markdown("**주요 강점**")
        st.info(info['strengths']) # info 박스로 강조
else:
    st.info("위에서 MBTI 유형을 선택하면 결과가 여기에 표시됩니다.")

st.divider()
st.warning("🚨 주의: 이 결과는 과학적 근거가 없는 가상 데이터이며, 재미 목적으로만 참고해주세요.", icon="⚠️")
