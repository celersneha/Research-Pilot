from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic:str) -> dict:
    state = {}
    
    # search agent working
    print("\n"+" ="*50)
    print("step 1 - search agent is working ...")
    print("="*50)
    
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages":[("user",f"Find recent, reliable and detailed information about {topic}")]
    })
    #output format
    # {
    #     "messages": [
    #         HumanMessage(content="What is the capital of France?"),
    #         AIMessage(content="", tool_calls=[{"name": "web_search", ...}]),
    #         ToolMessage(content="Title: Capital of France - Wikipedia..."),
    #         AIMessage(content="The capital of France is Paris.")
    #     ]
    # }
    state["search_results"] = search_result["messages"][-1].content
    
    print("\n search result ", state["search_results"])
    