from dotenv import load_dotenv
import os
from groq import Groq

# 1. 환경 변수 불러오기
load_dotenv()

# 2. 클라이언트 세팅
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 3. 대화 기록
messages = [
    {
        "role": "system",
        "content": "너는 아주 엄격한 CTO 개발자야. 답변을 짧게 해"
    }
]

while True:
    q = input("나 : ")
    if q == "exit":
            print("exit 를 눌러서 종료.")
            break
        
    messages.append(
            {
                "role" : "user",
                "content" : q
            }
        )
    
    res = client.chat.completions.create(
            model = "openai/gpt-oss-20b",
            messages= messages,
            temperature=0.1,    # 낮을수록 일관된 답
            max_completion_tokens=300,  # 답변 최대 길이 (오타 수정)
            reasoning_effort="low"
        )
    answer = res.choices[0].message.content
    print(f"AI의 답변 : {answer}")
    
    messages.append(
        {
            "role": "assistant",
            "content" : answer
        }
    )