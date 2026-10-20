# 261020 부천 AI 챗봇 실습 - 스마트 여행 일정 플래너 CLI

## 개요
- Groq API (`openai/gpt-oss-20b`)를 활용한 터미널 기반 CLI 대화형 챗봇입니다.
- 사용자의 여행지, 기간, 예산, 선호 스타일을 분석하여 **맞춤형 여행 동선 및 예상 경비**를 제공합니다.
- 영문 시스템 프롬프트(System Prompt)를 적용하여 모델의 지침 준수율을 최적화하고, 터미널 가독성을 높이기 위해 `rich` 라이브러리로 Markdown 스타일을 렌더링합니다.

## 주요 기능
- **동선 최적화 맞춤 일정 추천**: 인접한 관광지와 식당을 묶어 효율적인 일자별 여행 코스 제안
- **Markdown 표(Table) 구조화**: 일자별 세부 일정 및 항목별 예상 경비를 가독성 높은 표 형태로 출력
- **자동 예외 처리 (Default Itinerary)**: 정보가 부족하거나 '모름', '추천해줘' 입력 시 4일 기준 대표 가성비 일정 자동 생성
- **상세 현지 여행 팁**: 환전 우대 팁, 교통 앱(Grab 등), 날씨, 필수 준비물 안내
- **터미널 UI 가독성 향상**: `rich` 패키지를 통한 서식 렌더링 및 이모티콘이 배제된 깔끔하고 전문적인 톤 유지
- **대화 맥락 유지**: 연속적인 질문을 받아 세부 동선이나 일정을 유연하게 수정 가능

## 기술 스택 및 라이브러리
- **Python 3.10+**: 기본 실행 환경
- **`groq`**: Groq API 호출 및 LLM 추론 지원 (`openai/gpt-oss-20b` 모델 사용)
- **`python-dotenv`**: API 키 등 환경변수 보안 관리 (`.env` 활용)
- **`rich`**: 터미널 환경에서 Markdown 표 및 텍스트 예쁘게 렌더링

## 실행 방법

### 1. 프로젝트 클론 및 라이브러리 설치
```bash
git clone [https://github.com/nerongnyr/261020_bucheon_chatbot_nyr.git](https://github.com/nerongnyr/261020_bucheon_chatbot_nyr.git)
cd 261020_bucheon_chatbot_nyr
pip install -r requirements.txt
```

### 2. 환경변수 설정 (`.env`)
프로젝트 루트 폴더에 `.env` 파일을 생성하고 Groq API 키를 입력합니다.
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. 챗봇 실행
```bash
python v07_05_bucheon_chatbot_nyr.py
```
