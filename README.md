<h1>소개 (Introduction):</h1>

  <p>프로젝트의 개요와 목적에 대한 설명.</p>
  <p>스퀘어스의 요구사항 1번 CASE를 선택하여 구현</p>
      <p><tab>--Text 입력 또는 선언</tab></p>
      <p><tab>--HTML로 변환</tab></p>
  
  <p>프로젝트의 주요 기능과 장점을 간략하게 소개.</p>
    <p><tab>ChatGPT api를 사용했으며 prompt를 입력하게 될 경우 HTML코드로 변환하는 기능을 가지고 있습니다.</tab></p>
    <p><tab>(e.g) Prompt:"Make a login screen such as google style" convert to index.html</tab></p> 
  
<h1>시작하기 (Getting Started):</h1>
  <p><tab>1. git clone </tab></p>
  <p><tab>2. python -m venv Text2Web </tab></p>
  <p><tab>3. source ./Text2Web/Scripts/activate   (linux 기준) </tab></p>
  <p><tab>4. pip install requirements.txt </tab></p>
  
<h1> 사용 방법 (Usage): </h1>
  <p>1. [new Terminal] python app.py</p>
  <p>2. [new Terminal] python GPT.py</p>
     <p><tab><a>https://platform.openai.com/api-keys</a></tab></p>
     <p><tab>In the link, chatgpt apikey generation & copy and paste</tab></p>
     <p><tab>After Input Your Terminal</tab></p>
  <p>3. Input Your Prompt.</p>
  <p>4. Check GeneratedWeb Folder or flask Web page</p> 
<h1> 설계 및 아키텍처 (Design and Architecture):</h1>
  <p>프로젝트 구조</p>
  <p>프로젝트는 다음과 같은 구조를 가지고 있습니다.</p>

  <p>Text2Web_demo/</p>
    <p><tab>--app.py</tab></p>
    <p><tab>--GPT.py</tab></p>
      <p><tab>--get_openai_api_key</tab></p>
      <p><tab>--chat_with_gpt3</tab></p>
    <p><tab>--Text2Web.py</tab></p>
      <p><tab>--processing.py</tab></p>
    <p><tab><tab>--chatlog.txt</tab></p>
    <p><tab><tab>templates/</tab></p>
      <p><tab>GeneratedWeb/</tab></p>
        <p><tab>sample000/</tab></p>
          <p><tab>--index.html</tab></p>
          <p><tab>--styles.css</tab></p>
          <p><tab>--script.js</tab></p>
        <p><tab>sample001/</tab></p>
          <p><tab>--index.html</tab></p>
          <p><tab>--styles.css</tab></p>
          <p><tab>--script.js</tab></p>
        <p><tab>...</tab></p>
      <p><tab>--index.html</tab></p>
      <p><tab>--style.css</tab></p>
 
<p>기능 명세</p>
  <p><tab>GPT.py</tab></p>
    <p><tab>get_openai_api_key()</tab></p>
      <p><tab>--사용자에게 OpenAI GPT-3.5 API 키를 입력받아 설정합니다.</tab></p>
    <p><tab>chat_with_gpt3(prompt: str) -> str</tab></p>
      <p><tab>--사용자 입력을 받아 GPT-3.5-turbo 모델을 사용하여 응답을 생성합니다.</tab></p>
      <p><tab>--prompt 결과를 chatlog에 저장합니다.</tab></p>
    
  <p><tab>Text2Web.py</tab></p>
    <p><tab>processing()</tab></p>
      <p><tab>--chatlog.txt 파일에서 생성된 텍스트를 읽어와 HTML, CSS, JavaScript 파일로 변환합니다.</tab></p>
      <p><tab>--templates/GeneratedWeb/ 폴더에 샘플을 (e.g sample000) 생성합니다.</tab></p>
  
<h1> 테스트 (Testing): </h1>
  <p><tab>Prompt를 입력하면 자동으로 테스트 샘플이 생성됩니다.</tab></p>
  
<h1> 버그 보고서 및 개선 제안 방법.</h1>
  <p><tab>가끔 ChatGPT에서 환각현상을 보이고 결과물의 질이 그렇게 좋지 않습니다.</tab></p>
  <p><tab>Text2Web Task에 맞게 Prompt engineering과 FineTuning을 수행하고 추후에 RAG(retrieval-augmented generation)을 적용한다면 개선될 수 있을것 같습니다.</tab></p>
