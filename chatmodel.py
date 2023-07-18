from langchain.chat_models import ChatOpenAI
from langchain.schema import (AIMessage, HumanMessage, SystemMessage)

chat = ChatOpenAI(temperature=0)
#print(chat.predict_messages([HumanMessage(content="Translate this sentence from english to french. I love programming")]))
#print(chat.predict("Translate this sentence from english to french. I love programming"))
#print(chat.predict("How are feeling today?"))

print(chat.predict("Can you explain the role of a programmer in the world of AI where AI can do all the programming."))