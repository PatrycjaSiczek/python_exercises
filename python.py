# from langchain_community.chat_models import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# curl http://localhost:11434/api/generate -d {
#   "model": "llama2",
#   "prompt":"Why is the sky blue? }

# llm = ChatOllama(model="llama2")
# prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")


# chain = prompt | llm | StrOutputParser()

# print(chain.invoke({"topic": "Space travel"}))
# #llm = Ollama(base_path='https://llm.skni.umcs.pl/ollama', ...)
 

from langchain. import OpenAIGPT


gpt_chat = OpenAIGPT()


gpt_chat.connect()


while True:
    user_input = input("Ty: ")
    response = gpt_chat.send_message(user_input)
    print("GPT: " + response)