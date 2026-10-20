import os
from dotenv import load_dotenv
from groq import Groq
from rich.console import Console
from rich.markdown import Markdown

# .env 파일에서 환경변수(API 키) 로드
load_dotenv()

# Groq 클라이언트 및 Rich 콘솔 생성
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
console = Console()

# 대화 내역 및 시스템 프롬프트 설정
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly and professional 'Smart Travel Itinerary Planner' AI. "
            "Your main task is to provide customized travel itineraries. "
            "Strict Output Rules: "
            "1. Always respond in the language used by the user (e.g., respond in English if asked in English, Korean if asked in Korean)."
            "2. If the user provides partial information or states 'don't know' / 'unknown' / 'recommend' (e.g., '모름', '추천해줘'), DO NOT ask follow-up questions. Immediately generate a complete recommended itinerary and estimated budget table for the specified duration or a default 4-day trip. "
            "3. Every daily schedule (Day 1, Day 2, etc.) MUST be formatted as a Markdown Table. "
            "4. Always include an 'Estimated Budget Summary' section using Markdown Table or bullet list. "
            "5. Group geographically adjacent places and restaurants together to optimize daily routes. "
            "6. Provide highly detailed and practical local travel tips (e.g., specific money exchange spots/apps, Grab transport tips, night market food, local SIM cards, weather nuances). "
            "7. Do NOT use any emojis in your response. Keep the tone clean, polite, and professional. "
            "8. Ensure the response is complete and not truncated mid-sentence."
        )
    }
]

print("==================================================================")
print("             스마트 여행 일정 플래너 챗봇 (CLI)                 ")
print("==================================================================")
print("종료하시려면 'exit' 또는 'quit'를 입력하세요.\n")

print("[AI]: 안녕하세요! 어디로 떠나는 여행을 계획 중이신가요?")
print("      여행지, 기간, 예산이나 선호하는 스타일을 편하게 말씀해 주세요.")
print("      잘 모르시겠다면 '추천해줘'라고만 입력하셔도 됩니다.\n")

while True:
    user_input = input("\n[사용자] > ").strip()
    
    if not user_input:
        continue
        
    if user_input.lower() in ["exit", "quit"]:
        print("\n[AI]: 즐거운 여행 준비 되시길 바랍니다. 안녕히 가세요.")
        break
        
    messages.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=2048,
            reasoning_effort="low"
        )
        
        bot_reply = response.choices[0].message.content
        
        print("\n------------------------------------------------------------------")
        print("[AI 스마트 플래너 답변]")
        print("------------------------------------------------------------------")
        # Markdown을 터미널에 가독성 좋게 출력
        console.print(Markdown(bot_reply))
        print("------------------------------------------------------------------")
        
        messages.append({"role": "assistant", "content": bot_reply})
        
    except Exception as e:
        print(f"\n[에러 발생]: {e}\n")