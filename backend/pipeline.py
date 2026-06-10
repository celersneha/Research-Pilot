from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic:str) -> dict:
    state = {}
    
    # Step -1 search agent working
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
    
    # Step - 2 Reader agent working
    print("\n"+" ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)
    
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })
    
    state["scraped_content"] = reader_result["messages"][-1].content
    
    print("\n scraped content\n", state["scraped_content"])
    
    