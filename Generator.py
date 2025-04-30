from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import chromadb

model = ChatGroq(
    temperature = 0,
    groq_api_key = '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',
    model_name = "llama-3.3-70b-versatile"
)
job_page = input("Enter job description url : ")
loader = WebBaseLoader(job_page)
page_data = loader.load().pop().page_content

prompt_extract = PromptTemplate.from_template(
    """
        ###scrapped data from website:
        {page_data}
        ###instruction
        The scraped text is from the carrer's page of website.
        Your job is to extract the job openinigs and return them in Json format containing 
        following keys:`role`,`experience`,`skills` and `description`.
        only return legit Json.
        ###Only legit Json (NO PREAMBLE):
    """
)
chain_extract = prompt_extract | model
res = chain_extract.invoke(input={'page_data' : page_data})

json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)
job = json_res

profile = [{
    "Linkedin" : "www.linkedin.com/in/jaimin-chandarana-903158225",
    "Github" : "https://github.com/jaiminchandarana?tab=repositories"
}]    
prompt_email = PromptTemplate.from_template(
    """
    ###JOB DESCRIPTION:
    {job_description}
    
    ###INSTRUCTION:
    You are Jaimin, a data analyst and former data analyst at Solomo360 Technologies.
    Over your experience, you have empowered numerous clients with tailored solutions, fostering scalability,
    cost reduction, time saving, and heightened overall efficiency.
    Your job is to write a cold email to the client regarding the job mentioned above, describing your capability in fulfilling their needs.
    Add following links to showcase your profile:
    {link}
    Remember you are Jaimin, Data Analyst.
    Do not provide preamble.
    ###EMAIL (NO PREAMBLE):
    """
)

chain_email = prompt_email | model
res = chain_email.invoke({"job_description" : str(job), "link" : str(profile)})
print("\n"+res.content)