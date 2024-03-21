import os

import openai

from langchain.chains import LLMChain

from langchain.llms import OpenAI

from langchain.prompts import PromptTemplate

cities = ["Delhi","Jaipur","Uttar Pradesh"]

llm = OpenAI(temperature=0.3)
# print(llm.predict("What is the capital of india"))

prompt = PromptTemplate.from_template("What was the capital of {place}?")
#print(prompt.format(place="INDIA"))

chain = LLMChain(llm=llm, prompt=prompt)
output = chain.run("Uttar Pradesh")
print(output)

"""
for city in cities:
  output = chain.run(city)
  print(output)
"""
