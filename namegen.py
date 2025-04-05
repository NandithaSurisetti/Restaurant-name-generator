
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')



llm = OpenAI(temperature=0.7)


def name_generation(cuisine):
    llm = OpenAI(temperature=0.7)
    name_prompt=PromptTemplate(
        input_variables=['cusine'],
        template="I want to open a restaurant for {cuisine} food. suggest me a fancy name,only one name.no explanations"
)

    name_chain= LLMChain(llm=llm, prompt= name_prompt, output_key="restaurant_name")


    menu_prompt=PromptTemplate(
        input_variables=['restaurant_name'],
        template="suggest me menu items for {restaurant_name}.return it as comma seperated values"
)

    menu_chain=LLMChain(llm=llm , prompt= menu_prompt, output_key= "menu_items")

    chain=SequentialChain(
        chains=[name_chain,menu_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
)

    response=chain.invoke({'cuisine' : cuisine})
    return response



  