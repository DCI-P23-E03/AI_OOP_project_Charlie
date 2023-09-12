import openai # pip install openai
from dotenv import load_dotenv
import os
import json
import getch

from termcolor import colored
from os import system as x
from menu import VerticalMenu
from chat import BusinessIdeasChat



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

class ChatInMenu(BusinessIdeasChat,VerticalMenu):
    def __init__(self, initial_prompt):
        super().__init__(initial_prompt)
        VerticalMenu.__init__(self,self._list_of_menu_items,25)

    def execute(self, *args):
        x("clear")
        for i in self.selected:
            x_coords=self.coords[:-1]
            x_coords.append(i)
            print(colored(f"Elaborating on {self._access_menu_item(x_coords)[0]}.","blue"))
            self.list_of_menu_items=self.create_prompt(x_coords)
            for item in self._access_database(x_coords)[1:]:
                print(item["num"]+". "+colored(item["title"],"green")+"\n"+item["content"])
        print("Press any key to return to menu or 'x' to stop and generate report")
        mov=getch.getch()
        self.selected.clear()
        return mov
    
    def navigate_menu(self):
        super().navigate_menu()
        with open("log.json", "w") as file:
            json.dump(self._BusinessIdeasChat__database,file, indent=4)

def main():
    # Set your OpenAI API key
    #openai.api_key = ""

    load_dotenv()
    openai.api_key=os.getenv('API_KEY')
    
    

    prompt=create_prompt()
    """prompt="Considering the importance of individual skills, interests, and assets for 
        successful business, how can these elements be best utilized for idea generation?

        My primary skills and competencies: cooking
        \nI have experience and/or education in: 
        teaching python \nMy hobbies are: 
        football \nI have access to: a barn and a knife 
        \nMy business format preference: offline
        \nI would specifically like to target these markets: youth
        \nI am willing to take low level of risk,
        \nMy vision for my business in the long term: get rich\n
        Give me please three best business ideas.
        """


    b=ChatInMenu(prompt)
    print(b._BusinessIdeasChat__database[0])
    getch.getch()
    
    b.navigate_menu()
    

if __name__ == "__main__":
    main()

