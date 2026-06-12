from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    temperature=0.7
)
model = ChatHuggingFace(llm=llm)
response= model.invoke("who is abdul")
print(response.content)
