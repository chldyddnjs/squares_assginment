import openai
import os
from Text2Web import processing
def get_openai_api_key():
    api_key = input("Enter your OpenAI GPT-3.5 API key: ")
    openai.api_key = api_key
    print("API key set successfully.")

def chat_with_gpt3(prompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages =[{
            'role':'user',
            'content': prompt + 'using by html'
        }],
        temperature = 0.8, # 모델의 출력 다양성
        max_tokens= 2048, # 응답받을 메시지 최대 토큰(단어) 수 설정
        top_p = 1, # 토큰 샘플링 확률을 설정
        frequency_penalty = 0.5, # 일반적으로 나오지 않는 단어를 억제하는 정도
        presence_penalty= 0.5, # 동일한 단어나 구문이 반복되는 것을 억제하는 정도
        stop= None, # 생성된 텍스트에서 종료 구문을 설정
    )


    choice = completion["choices"][0]
    response = choice["message"]["content"].strip()
    return response

# API 키 설정
get_openai_api_key()

# 대화 모듈
print("Welcome to the ChatGPT-3.5 Conversation Module!")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Goodbye!")
        break
    
    # 대화 모듈에 사용자 입력을 전달하고 응답을 받습니다.
    response = chat_with_gpt3(user_input)
    with open('chatlog.txt',"w",encoding='utf-8') as chat:
        chat.write(response)
    print(f"ChatGPT-3.5: {response}")
    processing()