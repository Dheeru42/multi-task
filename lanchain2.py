import os
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

# This is an LLMChain to write the name of the ecommerse store that sells product.
llm = OpenAI(temperature=.3)
prompt = PromptTemplate.from_template("what is the name of the ecommerse store that sells {product}?")
chain1 = LLMChain(llm=llm, prompt=prompt)

# This is an LLMChain to write the name of the ecommerse store name.
llm = OpenAI(temperature=.3)
prompt = PromptTemplate.from_template("what are the name of the product at {store}?")
chain2 = LLMChain(llm=llm, prompt=prompt)

# This is the overall chain where we run these two chains in sequence.
chain = SimpleSequentialChain(
  chains=[chain1, chain2], verbose=True)

chain.run("candy")