import streamlit as st 
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import Tool,initialize_agent

##now  we will create streamlit app
st.set_page_config(page_title="Text to Math Problem Solver and Data Search Assistant")
st.title("Text to math problem solver using Google Gemma-2")

groq_api_key=st.sidebar.text_input(label="Groq API Key",type="password")

if not  groq_api_key:
    st.info("Please add your Groq API Key to continue")
    st.stop()

llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
   

##Initalize the tools
  
wikipeadia_wrapper=WikipediaAPIWrapper()
wikipeadia_tool=Tool(
    name="Wikipedia",
    func=wikipeadia_wrapper.run,
    description="A tool for searching the internet t find the various information on the topic mentioned"
    
)     

## Initalize the Math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool for answering math related questions.Only input mathematical expressions needs to be provided "
    )

prompt="""
You are a agnt tasked for solving users mathematical question. Logically arrive at the solution and provide the solution and provide a detailed explanation
and display it  point wise for the question below.
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

## Combine all the tools into a chain

chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic based and reasoning related questions. Only input mathematical expressions needs to be provided"
)

## Initalize the agent

assistant_agent=initialize_agent(
    tools=[wikipeadia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)


if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a Math Chatbot who can answer all your reasoning questions. How can I help you?"}
        
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


## Function to generate resonse

# def generate_response(user_question):
#     response=assistant_agent.invoke({"input":question})
#     return response

## Lets start the interaction
question=st.text_area("Enter youe question:","I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?")

if st.button("find my answer"):     
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
                   
            st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,callbacks=[st_cb])
               
            st.session_state.messages.append({"role":"assistant","content":response})
            st.write("### Response:")
            st.success(response) 

    else:
        st.warning("Please enter the question")