import re


def create_prompt_4():

    data = [{'role': 'system', 'content': "Imagine it's September 2021.You are one of the best business consultants with 25 years of experience and in depth knowledge of business, markets, strategies, start-ups etc. No need to mention the current year in the answer.write in the format: number. #name of the idea# - $the expert who is adept for explaining it (give a short answer in one two words)$- |list in imperative form for the second person|don't write an introduction or a conclusion"}, {'role': 'user', 'content': 'Considering the importance of individual skills, interests, and assets for \n        successful business, how can these elements be best utilized for a business idea generation?\n        \n        My primary skills and competencies: \n        skfd\nI have experience and/or education in: dkd\nMy hobbies are: cooking\nI have access to: car\nMy business format preference: online\nI would specifically like to target these markets:germany\nI am willing to take low level of risk,My vision for my business in the long term: no ideaGive me please three best business ideas.'}, {'role': 'assistant', 'content': '1. #Online Cooking Classes# - $Culinary Expert$ - |Identify your unique cooking style or recipes, create a detailed curriculum, set up a user-friendly online education platform, focus on german cuisine or cuisine Germans love to attract your target market|\n\n2. #Meal Delivery Service# - $Logistics Expert$ - |Develop a diverse menu including dietary preference options, partner with local suppliers for fresh ingredients, decentralize cooking, use your car for deliveries, emphasize on taste and health to differentiate yourself, target busy professionals and families in Germany|\n\n3. #Kitchen Utensil eCommerce Store# - $Ecommerce Guru$ - |Identify high-demand kitchen tools, source quality but affordable products, set up an intuitive online shop, offer fast and reliable delivery services, focus on kitchen tools essential for preparing German recipes to attract your target market|'}, {'role': 'user', 'content': "Imagine it is September 2021. You are the best business consultant in the whole world, with 20 years experience. I am your client and i want to start Kitchen Utensil eCommerce Store in the Germany. Describe in detail and write what is needed to start. No need to mention the current year in the answer. Write in the format: numbering, #names of the business action plan# - $the expert who is responsible for it (give a short answer in one two words)$- |list in imperative form for the second person| Don't write an introduction or a conclusion."}, {'role': 'assistant', 'content': '1. #Market Research# - $Research Analyst$ - |Analyze German kitchenware market extensively, understand customer needs, study competitors, make note of prevalent trends and best sellers|\n\n2. #Business Model Development# - $Strategy Consultant$ - |Decide on your unique selling proposition, set pricing strategy, map out your customer journey, choose suitable business and revenue model|\n\n3. #Sourcing Suppliers# - $Procurement Specialist$ - |Find reliable suppliers, negotiate pricing and delivery terms, ensure quality and ethical sourcing, arrange for product samples|\n\n4. #Website Design and Development# - $Web Developer$ - |Hire professional help for website creation, ensure user-friendly interface, incorporate secure payment methods, optimize for SEO|\n\n5. #Stock Management System# - $Operations Analyst$ - |Establish a reliable inventory tracking system, ensure ample supply for demand, develop efficient reordering process|\n\n6. #Shipping and Returns Policy# - $Legal Consultant$ - |Define clear shipping, return and refund policies, ensure they comply with local laws, make them upfront and visible on your website|\n\n7. #Customer Support# - $Customer Service Expert$ - |Set up a strong customer support team, train for exceptional customer service, provide multiple channels for service (email, phone, chat)|\n\n8. #Online Marketing Strategy# - $Marketing Specialist$ - |Plan effective online marketing initiatives, employ SEO, PPC, social media strategies, allocate a budget, measure and tweak for improved results|\n\n9. #Financial Management# - $Financial Advisor$ - |Set up financial tracking system, pay close attention to cash flow, plan your investment carefully, make provision for unexpected costs|\n\n10. #Launch# - $Business Owner (You!)$ - |Prepare for official launch, create hype, send out press releases or launch events, get feedback, tweak your strategies based on the response|.'}]

    l3response = data[4]['content'] # extract level 3 response from entire conversation
    print(l3response)
    recog_pattern = "(\d+)\. #([^#]+)# - \$([^$]+)\$ - \|([^|]+)\|"

    business_actions = {}

    matches = re.findall(recog_pattern,l3response)
    #print(matches)
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

    print(list_business_actions)
    chosen_action_number = int(input("User: "))

    prompt_level4 = f"Your current choice of business action is {business_actions[chosen_action_number]['title']}. Imagine it's September 2021. you're the best {business_actions[chosen_action_number]['expert']} in the whole world, with 20 years of experience. I'm your client and i want you to fetch me a detailed report corresponding to this business action using the following information.\n {list({action_details['content']})} \nNo need to mention the current year in the answer.\nWrite in the format:numbering, #section names#-$subsection names$-|detailed description| \nDon't write an introduction or a conclusion."

    print( prompt_level4)


create_prompt_4()