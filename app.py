import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


from langchain_community.utilities import WikipediaAPIWrapper,ArxivAPIWrapper
from langchain_community.tools import WikipediaQueryRun,ArxivQueryRun,DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler


arxiv_wrapper = ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=400)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)

wikipedia_wrapper = WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=400)
wikipedia=WikipediaQueryRun(api_wrapper=wikipedia_wrapper)

search = DuckDuckGoSearchRun(name="Search")

st.title("Langchain - chat with search")

st.sidebar.title("Settings")
groq_api_key = st.sidebar.text_input("Enter your groq api key",type="password")

# """
# A StreamlitCallbackHandler is used in LangChain to stream the output of an LLM or agent live into a Streamlit app, showing intermediate steps like:

# Thought

# Action

# Observation

# Final answer

# It makes the agent feel interactive and real-time.
# """

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role":"assistant", "content":"Hello! I am a search agent. How can I help you today?"},
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

if prompt:=st.chat_input(placeholder="what is machine learning?"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    # Initialize the Groq model
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="meta-llama/llama-4-scout-17b-16e-instruct", streaming=True , temperature=0.1)
    tools = [arxiv, wikipedia, search]

    search_agent = initialize_agent(tools=tools, llm=llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,handling_parsing_errors=True, verbose=True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=True)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])

    st.session_state.messages.append({"role":"assistant", "content":response})
    st.write(response)