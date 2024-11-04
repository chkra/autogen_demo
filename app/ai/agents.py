import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json
import time
from IPython.display import Image

import autogen

EASY_WAY = True

def start_dialog():
    if EASY_WAY:
        # Read messages from file
        with open('messages.json', 'r') as file:
            messages = json.load(file)
        
        # Print messages one by one with a delay
        for message in messages:
            print(message)
            print("-----------------------------------")
        
        return messages
    else:
        with open('api_key', 'r') as file:
            api_key = file.read().strip()

        config_list = [{"model": "gpt-4", "api_key": api_key}]

        llm_config = {"config_list": config_list, "cache_seed": 40}

        user_proxy = autogen.UserProxyAgent(
            name="User_proxy",
            system_message="A human admin.",
            code_execution_config={
                "last_n_messages": 3,
                "work_dir": "groupchat",
                "use_docker": False,
            },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
            human_input_mode="NEVER",
        )
        coder = autogen.AssistantAgent(
            name="Coder",  # the default assistant agent is capable of solving problems with code
            system_message="""Solve every problem with python code. Never use bash. You can ask for help if you are stuck. """,
            llm_config=llm_config,
        )
        critic = autogen.AssistantAgent(
            name="Critic",
            system_message="""Critic. You are a helpful assistant highly skilled in evaluating the quality of a given visualization code by providing a score from 1 (bad) - 10 (good) while providing clear rationale. YOU MUST CONSIDER VISUALIZATION BEST PRACTICES for each evaluation. Specifically, you can carefully evaluate the code across the following dimensions
- bugs (bugs):  are there bugs, logic errors, syntax error or typos? Are there any reasons why the code may fail to compile? How should it be fixed? If ANY bug exists, the bug score MUST BE LESS THAN 5.
- Data transformation (transformation): Is the data transformed appropriately for the visualization type? E.g., is the dataset appropriated filtered, aggregated, or grouped  if needed? If a date field is used, is the date field first converted to a date object etc?
- Goal compliance (compliance): how well the code meets the specified visualization goals?
- Visualization type (type): CONSIDERING BEST PRACTICES, is the visualization type appropriate for the data and intent? Is there a visualization type that would be more effective in conveying insights? If a different visualization type is more appropriate, the score MUST BE LESS THAN 5.
- Data encoding (encoding): Is the data encoded appropriately for the visualization type?
- aesthetics (aesthetics): Are the aesthetics of the visualization appropriate for the visualization type and the data?

YOU MUST PROVIDE A SCORE for each of the above dimensions.
{bugs: 0, transformation: 0, compliance: 0, type: 0, encoding: 0, aesthetics: 0}
Do not suggest code.
Finally, based on the critique above, suggest a concrete list of actions that the coder should take to improve the code.
""",
            llm_config=llm_config,
        )

        groupchat = autogen.GroupChat(agents=[user_proxy, coder, critic], messages=[], max_round=20)
        manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

        # Start the dialog and collect the messages
        user_proxy.initiate_chat(
            manager,
            message="download data from https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv and plot a visualization that tells us about the relationship between weight and horsepower. Save the plot to a file called analysis.png. Print the fields in a dataset before visualizing it.",
        )
        
        
        # Convert messages to JSON string for readability
        messages = [message for message in manager.groupchat.messages]
        
        # Save messages to file
        with open('messages.json', 'w') as file:
            json.dump(messages, file, indent=2)
        
        return messages


def main():
    messages = start_dialog()


if __name__ == "__main__":
    main()