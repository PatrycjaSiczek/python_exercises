from langchain_community.llms import Ollama

llm = Ollama(model="llama2:13b", base_url= 'https://gpt.skni.umcs.pl/')
print(llm.invoke("Tell me a joke"))