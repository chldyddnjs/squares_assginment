프로젝트 구조
프로젝트는 다음과 같은 구조를 가지고 있습니다.

Text2Web/
__init__.py
processing.py
chat_with_gpt3.py
styles.css
script.js
chatlog.txt
GeneratedWeb/
index.html
styles.css
script.js
기능 명세
chat_with_gpt3(prompt: str) -> str
사용자 입력을 받아 GPT-3.5-turbo 모델을 사용하여 응답을 생성합니다.

get_openai_api_key()
사용자에게 OpenAI GPT-3.5 API 키를 입력받아 설정합니다.

processing()
chatlog.txt 파일에서 생성된 텍스트를 읽어와 HTML, CSS, JavaScript 파일로 변환합니다.

테스트
프로젝트에는 자동화된 테스트가 포함되어 있지 않습니다. 사용자는 적절한 테스트를 진행하고 품질을 확인해야 합니다.

배포
프로덕션 배포나 데모 배포에 대한 추가적인 지침은 현재 문서에 포함되어 있지 않습니다. 사용자는 필요에 따라 프로젝트를 배포할 수 있습니다.
