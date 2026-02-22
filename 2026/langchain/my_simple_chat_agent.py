from langchain_community.chat_models import ChatLlamaCpp
from langchain_core.prompts import ChatPromptTemplate

# 1. Create the local Llama chat model
model = ChatLlamaCpp(
    model_path="models/llama-2-7b.Q5_K_M.gguf",
    temperature=0.7,
    max_tokens=256,
)

# 2. Define a simple prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful Python tutor."),
        ("human", "Explain what LangChain is in simple terms."),
    ]
)

# 3. Build a chain: prompt -> model
chain = prompt | model

# 4. Invoke the chain
response = chain.invoke({})
print(response.content)
