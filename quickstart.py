"""Import packages to build a langchain solution"""
from langchain.llms import OpenAI
import os

llm = OpenAI(openai_api_key=os.environ['OPENAI_API_KEY'],temperature=0.9)

"""we pass in text and get predictions"""

print(llm.predict(
    text="What wold be a good company name for a company that makes assisted intelligence products for humans?"))
