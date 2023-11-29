<h1>소개 (Introduction):</h1>

  <p> 프로젝트의 개요와 목적에 대한 설명.</p>
    스퀘어스의 요구사항 1번 CASE를 선택하여 구현
      --Text 입력 또는 선언
      --HTML로 변환
  
  <p>프로젝트의 주요 기능과 장점을 간략하게 소개.</p>
    ChatGPT api를 사용했으며 prompt를 입력하게 될 경우 HTML코드로 변환하는 기능을 가지고 있습니다.
    (e.g) Prompt:"Make a login screen such as google style" convert to index.html 
  
<h1>시작하기 (Getting Started):</h1>
  1. git clone
  2. python -m venv Text2Web
  3. source ./Text2Web/Scripts/activate   (linux 기준)
  4. pip install requirements.txt
  
<h1> 사용 방법 (Usage): </h1>
  1. [new Terminal] python app.py
  2. [new Terminal] python GPT.py
     <a>https://platform.openai.com/api-keys</a>
     In the link, chatgpt apikey generation & copy and paste
     After Input Your Terminal
  3. Input Your Prompt.
  4. Check GeneratedWeb Folder or flask Web page 
<h1> 설계 및 아키텍처 (Design and Architecture):</h1>
  프로젝트 구조
  프로젝트는 다음과 같은 구조를 가지고 있습니다.

  Text2Web_demo/
    --app.py
    --GPT.py
      --get_openai_api_key
      --chat_with_gpt3
    --Text2Web.py
      --processing.py
    --chatlog.txt
    templates/
      GeneratedWeb/
        sample000/
          --index.html
          --styles.css
          --script.js
        sample001/
          --index.html
          --styles.css
          --script.js
        ...
      --index.html
      --style.css
 
기능 명세
  GPT.py
    get_openai_api_key()
      --사용자에게 OpenAI GPT-3.5 API 키를 입력받아 설정합니다.
    chat_with_gpt3(prompt: str) -> str
      --사용자 입력을 받아 GPT-3.5-turbo 모델을 사용하여 응답을 생성합니다.
      --prompt 결과를 chatlog에 저장합니다.
    
  Text2Web.py
    processing()
      --chatlog.txt 파일에서 생성된 텍스트를 읽어와 HTML, CSS, JavaScript 파일로 변환합니다.
      --templates/GeneratedWeb/ 폴더에 샘플을 (e.g sample000) 생성합니다.
  
<h1> 테스트 (Testing): </h1>

테스트 스위트 및 테스트 케이스에 대한 설명.
로컬 개발 환경에서의 테스트 실행 방법.
디버깅 및 문제 해결 (Debugging and Troubleshooting):

주요 문제에 대한 디버깅 방법.
자주 발생하는 문제에 대한 해결 방법.
배포 (Deployment):

프로젝트를 실제 환경에 배포하는 방법.
프로덕션 환경에서의 설정 방법.
<h1>기여 및 개선 (Contribution and Enhancement):</h1>

<h1> 프로젝트에 기여하는 방법.</h1>
<h1> 버그 보고서 및 개선 제안 방법.</h1>
라이선스 (License):
프로젝트의 라이선스 정보.
이러한 섹션들은 프로젝트의 특성과 요구에 따라 조절될 수 있습니다. 일부 프로젝트에서는 문서화 도구를 사용하여 자동으로 문서를 생성하기도 합니다.
