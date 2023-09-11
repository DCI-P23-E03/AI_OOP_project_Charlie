import re


def create_prompt_3():

    data = [{'role': 'system', 'content': "Imagine it is September 2021. You are the best business consultant in the whole world, with 20 years experience. I am your client and i want to start tatoo saloon in germany. Describe to me in detail and write what is needed to start. No need to mention the current year in the answer. Write in the format:numbering, #names of the action# - $the expert who is responsible for it (give a short answer in one/two words)$- |list in imperative form for the second person| Don't write an introduction or a conclusion"}, {'role': 'user', 'content': 'Considering the importance of individual skills, interests, and assets for \n        successful business, how can these elements be best utilized for idea generation? \n        My primary skills and competencies include: happy, time\nI have experience and/or education in: not many\nMy hobbies are: drawing\nI have access to: have a car\nMy business format preference: offline\nTarget markets include:Germany\nI am willing to take medium level of risk,My vision for my business in the long term: financial stabilityPlease give me three best business ideas.'}, {'role': 'assistant', 'content': '1. #Offline Art Gallery# - $Art Consultant$ - |Utilize your drawing skills and car to curate and exhibit art pieces in an offline setting within your local Germany market. Attend local art events to network and find potential artists.|\n\n2. #Mobile Illustration and Design Business# - $Design and Marketing Consultant$ - |Your drawing hobby can be turned into a mobile business. Design logos, business cards, fliers and other materials for clients. Use your car to meet clients and deliver orders. Market your services online and through local business networks.|\n\n3. #Tour Guide Business# - $Travel Consultant$ - |Use your car to offer guided tours to tourists in Germany. This can be supplemented with provision of information aids like maps and booklets, which you can design and illustrate yourself.|'}]

    l2response = data[2]['content'] # extract level 2 response from entire conversation
    
    recog_pattern = r'(\d+)\. #(.*)# - \$(.*)\$ - (.+)'

    business_ideas = {}

    matches = re.findall(recog_pattern,l2response)
    
    for match in matches:
        idea_number = match[0]
        idea_title = match[1]
        idea_expert = match[2]
        body = match[3]
        
        business_ideas[idea_number] = idea_title

    list_business_ideas = [f"{idea_number}:{idea_title}" for idea_number, idea_title in business_ideas.items()]

    print(list_business_ideas)

    chosen_idea_number = input("User: ")  

    prompt_level3 = (f"Imagine it is September 2021. You are the best business consultant in the whole world, with 20 years experience. I am your client and i want to start {business_ideas[chosen_idea_number]} in the Germany. Describe in detail and write what is needed to start. No need to mention the current year in the answer. Write in the format: numbering, #names of the business action plan# - $the expert who is responsible for it (give a short answer in one two words)$- |list in imperative form for the second person| Don't write an introduction or a conclusion.")

    print(prompt_level3)

create_prompt_3()