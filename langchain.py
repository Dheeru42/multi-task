import os
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.agents import AgentType,initialize_agent,Tool,load_tools 

llm = OpenAI(temperature=0.7)
tools = load_tools(["wikipedia","llm-math"],llm = llm)
agent = initialize_agent(tools,llm,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose = True)
output = agent.run("Age of MS Dhoni in 2023")
print(output)