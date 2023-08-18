import openai # pip install openai
from dotenv import load_dotenv
import os



def create_prompt():
    skills_comp=input("What are your primary skills and competencies?: ")
    experience=input("In which industries or sectors do you have experience or education?: ")
    hobbies=input("What hobbies or interests do you have?: ")
    assets=input("What assets or resources are available to you? (e.g., equipment, space, starting capital, etc.): ")
    business_format=input("What business format do you prefer? (e.g., online, offline, franchise, startup, etc.): ")
    markets=input("Are there specific markets or audiences you would like to target?: ")
    level_risk=input("What level of risk are you willing to take? (e.g., high, medium, low): ")
    plans=input("What is your long-term plan or vision for the business?: ")

    prompt=(
        """Considering the importance of individual skills, interests, and assets for 
        successful business, how can these elements be best utilized for idea generation?

        My primary skills and competencies: 
        """
        +skills_comp
        +"\nI have experience and/or education in: "
        +experience
        +"\nMy hobbies are: "
        +hobbies
        +"\nI have access to: "
        +assets
        +"\nMy business format preference: "
        +business_format
        +"\nI would specifically like to target these markets:"
        +markets
        +f"\nI am willing to take {level_risk} level of risk,"
        +"My vision for my business in the long term: "
        +plans
        +"Give me please three best business ideas."
    )

    return prompt


def main():
    # Set your OpenAI API key
    #openai.api_key = ""

    load_dotenv()
    openai.api_key=os.getenv('API_KEY')
    
    # Initial conversation setup
    conversation = [
        {"role": "system", "content": "You are one of the best business consultants with 25 years of experience and in depth knowledge of business, markets, strategies, start-ups etc. Your answers are in the form of a list with each item starting with a number followed by a dot. You always stay in the role."},                # SYSTEM ROLE
    ]

    prompt=create_prompt()

    while True:
        # User input
        #prompt = input("User: ")                                                     # USER INPUT
        #if prompt.lower() == "exit":
        #    break
        conversation.append({"role": "user", "content": prompt})

        # Get assistant's response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=conversation
        )
        #print("RAW RESPONSE",response)
        assistant_message = response['choices'][0]['message']['content']
        
        # Add the assistant's message to the conversation and print it
        conversation.append({"role": "assistant", "content": assistant_message})
        print(f"Assistant: {assistant_message}\n")
        print(f"Tokens used: {response["usage"]["total_tokens"]}")
        #print(response)
        #print(conversation)
        prompt = input("User: ")   
        print("\n")
        if prompt.lower() == "exit":
            break

if __name__ == "__main__":
    main()