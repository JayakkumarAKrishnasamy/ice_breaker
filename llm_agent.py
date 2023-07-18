from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI


# The language model we're going to use to control the agent.
llm = OpenAI(temperature=0)

# The tools we'll give the Agent access to. Note that the 'llm-math tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Initialize the agent with the tools , the language model, and the agent type.

agent = initialize_agent(tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Now we can interact with the agent!

agent.run("What was the highest temperature in Pune yesterday in 'Celsius'? Do not calculate the average. What is that number raised to the power of 0.23?")