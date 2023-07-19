from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "The following is a friendly conversation between a human and an AI. The AI is talkative and"
        "provides a lot of specific details from its context. If the AI does not know the answer to a"
        "question, it truthfully says 'I do not know'."
    ),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

llm = ChatOpenAI(temperature=0)

memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    prompt=prompt,
    llm=llm,
    memory=memory,
)

response = conversation.predict(input="Hi there! How are you?")
print(response)

response = conversation.predict(input="I'm sorry, I am not doing well enough today. Please suggest something fun to do now.")
print(response)

print(conversation.predict(input="Let me about yourself..."))