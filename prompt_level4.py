import re


def create_prompt_4():

    data = []

    l3response = data[3]['content'] # extract level 3 response from entire conversation

    recog_pattern = r'(\d+)\. #(.*?)# - \$(.*?)\$- \|(.+?)\|'

    business_actions = {}

    matches = re.findall(recog_pattern,l3response)

    for match in matches:
        action_number = int(match[0])
        action_details = {
            'title': match[1],
            'expert': match[2],
            'content': match[3]
        }
        business_actions[action_number] = action_details

    #print(business_actions)

    list_business_actions = [f"{action_number}:{action_details['title']}" for action_number, action_details in business_actions.items()]

    #print(list_business_actions)

    prompt_level4 = f"The current choice of business action is {action_details['title']}. Imagine it's September 2021. you're the best {action_details['expert']} in the whole world, with 20 years of experience. I'm your client and i want to start a tattoo salon in Germany. Do a detailed report for me.\n {list({action_details['content']})} \nNo need to mention the current year in the answer.\nWrite in the format:numbering, #section names#-$subsection names$-|detailed description| \nDon't write an introduction or a conclusion."

    return prompt_level4

create_prompt_4()