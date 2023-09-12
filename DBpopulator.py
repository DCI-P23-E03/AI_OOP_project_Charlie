import openai  # pip install openai
from dotenv import load_dotenv
import os
import re


conversation = [
    {
        "role": "system",
        "content": "Imagine it's September 2021.You are one of the best business consultants with 25 years of experience and in depth knowledge of business, markets, strategies, start-ups etc. No need to mention the current year in the answer.",
    }  # SYSTEM ROLE]
]
Database = [
    {
        "title": "Title 1",
        "expert": "Expert 1",
        "contenttext": "Content Text 1",
        "elaborate": "Elaborate 1",
    },
    {
        "title": "Title 2",
        "expert": "Expert 2",
        "contenttext": "Content Text 2",
        "elaborate": "Elaborate 2",
    },
    {
        "title": "Title 3",
        "expert": "Expert 3",
        "contenttext": "Content Text 3",
        "elaborate": "Elaborate 3",
    },
]
chosen_idea_number = 1 or 2 or 3


def create_prompt_2():
    skills_comp = input("What are your primary skills and competencies?: ")
    experience = input(
        "In which industries or sectors do you have experience or education?: "
    )
    hobbies = input("What hobbies or interests do you have?: ")
    assets = input(
        "What assets or resources are available to you? (e.g., equipment, space, starting capital, etc.): "
    )
    business_format = input(
        "What business format do you prefer? (e.g., online, offline, franchise, startup, etc.): "
    )
    markets = input(
        "Are there specific markets or audiences you would like to target?: "
    )
    level_risk = input(
        "What level of risk are you willing to take? (e.g., high, medium, low): "
    )
    plans = input("What is your long-term plan or vision for the business?: ")

    prompt_level2 = (
        """Considering the importance of individual skills, interests, and assets for 
        successful business, how can these elements be best utilized for a business idea generation?
        
        My primary skills and competencies: 
        """
        + skills_comp
        + "\nI have experience and/or education in: "
        + experience
        + "\nMy hobbies are: "
        + hobbies
        + "\nI have access to: "
        + assets
        + "\nMy business format preference: "
        + business_format
        + "\nI would specifically like to target these markets:"
        + markets
        + f"\nI am willing to take {level_risk} level of risk,"
        + "My vision for my business in the long term: "
        + plans
        + "\nGive me please three best business ideas.Write strictly in the format: number. #name of the idea# $name of expert$ - |business idea in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion"
    )

    return prompt_level2


def create_prompt_3():
    global conversation
    global Database
    data = conversation

    l2response = data[2]["content"]  # extract level 2 response from entire conversation

    recog_pattern = r"(\d+)\. #(.*?)# \$(.*?)\$"

    business_ideas = {}

    matches = re.findall(recog_pattern, l2response)

    for match in matches:
        idea_number = match[0]
        idea_details = {"title": match[1].strip(), "expert": match[2].strip()}
        business_ideas[idea_number] = idea_details

    list_business_ideas = [
        f"{idea_number}:{idea_details['title']}"
        for idea_number, idea_details in business_ideas.items()
    ]

    print(
        f"\nChoose the number corresponding to your preference from the following: \n{list_business_ideas}"
    )

    chosen_idea_number = input("\nUser: ")

    prompt_level3 = f"You are the best {business_ideas[chosen_idea_number]['expert']} in the whole world, with 20 years experience. I am your client and i want to start {business_ideas[chosen_idea_number]['title']} in the Germany. Describe in detail and write what is needed to start. No need to mention the current year(2021) in the answer. Write strictly in the format: number. #name of the business action# $corresponding area expert$ - |describe in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion"

    print(f"\n{prompt_level3}")
    expert = {business_ideas[chosen_idea_number]["expert"]}
    Database[(int(chosen_idea_number) - 1)]["prompt"] = prompt_level3  # adding prompt to database
    result = [expert, prompt_level3, chosen_idea_number, Database]
    return result


def create_prompt_4():
    global conversation
    global Database
    global chosen_idea_number
    data = conversation
   
    l3response = data[4]["content"]  # extract level 3 response from entire conversation

    recog_pattern = r"(\d+)\. #(.*?)# \$(.*?)\$ - \|([^|]+)\|"

    business_actions = {}

    matches = re.findall(recog_pattern, l3response)

    for match in matches:
        action_number = int(match[0])
        action_details = {
            "title": match[1].strip(),
            "expert": match[2].strip(),
            "content": match[3].strip(),
        }
        business_actions[action_number] = action_details

    list_business_actions = [
        f"{action_number}:{action_details['title']}"
        for action_number, action_details in business_actions.items()
    ]

    print(
        f"\nChoose the number corresponding to your preferred business action from the following: \n{list_business_actions}"
    )
    chosen_action_number = int(input("\nUser: "))

    prompt_level4 = f"Your current choice of business action is {business_actions[chosen_action_number]['title']}. Imagine it's September 2021. you're the best {business_actions[chosen_action_number]['expert']} in the whole world, with 20 years of experience. I'm your client and i want you to fetch me a detailed report corresponding to this business action using the following information.\n {list({business_actions[chosen_action_number]['content']})} \nNo need to mention the current year in the answer.\nWrite in the format:numbering, #section names#-$subsection names$-|detailed description|"
    print(f'\n{prompt_level4}')
    expert = {business_actions[chosen_action_number]["expert"]}
    Database[(int(chosen_idea_number) - 1)]["elaborate"][
        (int(chosen_action_number) - 1)
    ][
        "prompt"
    ] = prompt_level4  # adding prompt to database
    result = [expert, prompt_level4, chosen_idea_number, chosen_action_number, Database]
    return result


def main():
    # Set your OpenAI API key
    # openai.api_key = ""

    load_dotenv()
    openai.api_key = os.getenv("API_KEY")

    prompt = "Considering the importance of individual skills, interests, and assets for successful business, how can these elements be best utilized for a business idea generation? My primary skills and competencies: perseverence.I have experience and/or education in: business. My hobbies are: cooking. I have access to: car, internet. My business format preference: offline.I would specifically like to target these markets:Germany. I am willing to take low level of risk,My vision for my business in the long term: Own a profitable business. Give me three best business ideas. Write strictly in the format: number. #name of the idea# $the area expert$ - |business idea in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion"  # create_prompt_2()

    global conversation
    global Database
    global chosen_idea_number
    conversation.append({"role": "user", "content": prompt})

    # Get assistant's response
    response = openai.ChatCompletion.create(model="gpt-4", messages=conversation)
    # print("RAW RESPONSE",response)
    assistant_message = response["choices"][0]["message"]["content"]
    recog_pattern = r"(\d+)\. #(.*?)# \$(.*?)\$ - \|([^|]+)\|"
    matches = re.findall(recog_pattern, assistant_message)
    for match in matches:
        idea_number = int(match[0])
        idea_details = {
            "title": match[1].strip(),
            "expert": match[2].strip(),
            "content": match[3].strip(),
        }

        Database[(idea_number - 1)] = idea_details

    print(f"\n{Database}")
    conversation.append({"role": "assistant", "content": assistant_message})
    inc_prompt = create_prompt_3()
    prompt = inc_prompt[1]
    expert = inc_prompt[0]
    chosen_idea_number = inc_prompt[2]
    Database = inc_prompt[3]
    conversation[0][
        "content"
    ] = f"You are one of the best {expert} with 20 years of experience and in depth knowledge of business, markets, strategies, start-ups etc. Write strictly in the format: number. #name of the business action# $the area expert$ - |describe in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion"  # SYSTEM ROLE REASSIGN
    conversation.append({"role": "user", "content": prompt})

    # Get assistant's response
    response = openai.ChatCompletion.create(model="gpt-4", messages=conversation)

    assistant_message = response["choices"][0]["message"]["content"]
    print(f'\n{assistant_message}')
    recog_pattern = r"(\d+)\. #(.*?)# \$(.*?)\$ - \|([^|]+)\|"
    matches = re.findall(recog_pattern, assistant_message)
    for match in matches:
        action_number = int(match[0])
        action_details = {
            "title": match[1].strip(),
            "expert": match[2].strip(),
            "content": match[3].strip(),
        }

        if action_number == 1:
            Database[((int(chosen_idea_number)) - 1)]["elaborate"] = []
            Database[((int(chosen_idea_number)) - 1)]["elaborate"].append(
                action_details
            )
        if action_number != 1:
            Database[((int(chosen_idea_number)) - 1)]["elaborate"].append(
                action_details
            )

    conversation.append({"role": "assistant", "content": assistant_message})
    inc_prompt = create_prompt_4()

    prompt = inc_prompt[1]
    expert = inc_prompt[0]
    chosen_idea_number = inc_prompt[2]
    chosen_action_number = inc_prompt[3]
    Database = inc_prompt[4]

    conversation[0][
        "content"
    ] = f"You are one of the best {expert} with 20 years of experience and in depth knowledge of business, markets, strategies, start-ups etc. Write strictly in the format: number. #name of the business action# $the area expert$ - |describe in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion"  # SYSTEM ROLE REASSIGN
    conversation.append({"role": "user", "content": prompt})

    # Get assistant's response
    response = openai.ChatCompletion.create(model="gpt-4", messages=conversation)

    assistant_message = response["choices"][0]["message"]["content"]
    print(f'\n{assistant_message}')
    recog_pattern = r"(\d+)\. #(.*?)# \$(.*?)\$ - \|([^|]+)\|"
    matches = re.findall(recog_pattern, assistant_message)
    for match in matches:
        expln_number = int(match[0])
        expln_details = {
            "title": match[1].strip(),
            "subtitle": match[2].strip(),
            "content": match[3].strip(),
        }
        if expln_number == 1:
            Database[((int(chosen_idea_number)) - 1)]["elaborate"][
                ((int(chosen_action_number)) - 1)
            ]["elaborate"] = []
            Database[((int(chosen_idea_number)) - 1)]["elaborate"][
                ((int(chosen_action_number)) - 1)
            ]["elaborate"].append(expln_details)
        if expln_number != 1:
            Database[((int(chosen_idea_number)) - 1)]["elaborate"][
                ((int(chosen_action_number)) - 1)
            ]["elaborate"].append(expln_details)

    conversation.append({"role": "assistant", "content": assistant_message})
    print('\n\n')
    print(f"Database =  {Database}")
    print('\n\n')
    print(f"conversation =  {conversation}")


if __name__ == "__main__":
    main()
