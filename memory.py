from langchain import OpenAI, ConversationChain

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm,verbose=True)


response = conversation.run("Hi there!!")
print(response)
response = conversation.run("Im doing well! Just having a conversation with an AI!")

print(response)