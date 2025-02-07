# from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode
from langchain_community.chat_models import ChatOpenAI, ChatOllama


llm = ChatOpenAI(model="gpt-4o-mini")
ollama_llm = ChatOllama(model="llama2")
