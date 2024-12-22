from llama_index.core.tools import FunctionTool
from llama_index.llms.groq import Groq
from math_stuff import *
import os
import dotenv
from llama_index.core.agent import ReActAgent

from tools.guidelines import guidelines_engine
dotenv.load_dotenv()

llm = Groq(model="llama3-groq-8b-8192-tool-use-preview", api_key=os.getenv("GROQ"))

add_tool = FunctionTool.from_defaults(fn=addition, name="addition", description="Returns the sum of two numbers.")
multiply_tool = FunctionTool.from_defaults(fn=multiplication, name="multiplication", description="Returns the product of two numbers.")
division_tool = FunctionTool.from_defaults(fn=division, name="division", description="Returns the quotient of two numbers.")
subtract_tool = FunctionTool.from_defaults(fn=subtraction, name="subtraction", description="Return the difference of two numbers.")

query = "Multiply 8 and 30 and add 20"
tools=[add_tool, multiply_tool, division_tool, subtract_tool, guidelines_engine]
response = llm.predict_and_call(
    tools=tools,
    user_msg=query, verbose = True
)

agent = ReActAgent.from_tools(
    tools=tools, llm=llm, verbose=True
)
print(response)