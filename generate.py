import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Streamlit UI
st.title("Cold Email Generator from Career Page")
st.markdown("This app scrapes a career/job description page and creates a cold email for outreach.")

# Inputs
job_page = st.text_input("Enter job description URL")
name = st.text_input("Enter your name", value="Enter your name :")
position = st.text_input("Enter your current position", value="Enter your designation :")
linkedin = st.text_input("Enter your LinkedIn profile URL")
github = st.text_input("Enter your GitHub profile URL")
groq_api_key = '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'

if st.button("Generate Cold Email"):
    if not job_page or not name or not position or not linkedin or not github or not groq_api_key:
        st.warning("Please fill all fields.")
    else:
        with st.spinner("Loading and processing job page..."):

            # Initialize model
            model = ChatGroq(
                temperature = 0,
                groq_api_key = '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',
                model_name = "llama-3.3-70b-versatile"
            )

            # Load webpage content
            loader = WebBaseLoader(job_page)
            try:
                page_data = loader.load().pop().page_content
            except Exception as e:
                st.error(f"Error loading webpage: {e}")
                st.stop()

            # Prompt to extract job information
            prompt_extract = PromptTemplate.from_template(
                """
                ###scrapped data from website:
                {page_data}
                ###instruction
                The scraped text is from the career's page of website.
                Your job is to extract the job openings and return them in JSON format containing 
                the following keys: `role`, `experience`, `skills`, and `description`.
                Only return legit JSON (no preamble).
                """
            )

            chain_extract = prompt_extract | model
            res = chain_extract.invoke(input={'page_data': page_data})
            json_parser = JsonOutputParser()

            try:
                job = json_parser.parse(res.content)
            except Exception as e:
                st.error(f"Could not parse job data as JSON: {e}")
                st.stop()

            st.subheader("Extracted Job Description")
            st.json(job)

            # Profile details
            profile_links = []
            if linkedin.strip():
                profile_links.append(f"LinkedIn: {linkedin.strip()}")
            if github.strip():
                profile_links.append(f"GitHub: {github.strip()}")

            links_str = "\n".join(profile_links) if profile_links else "No external links provided."

            # Prompt for cold email
            prompt_email = PromptTemplate.from_template(
                """
                ###JOB DESCRIPTION:
                {job_description}

                ###INSTRUCTION:
                You are {name}, a {position}.
                Over your experience, you have empowered numerous clients with tailored solutions, fostering scalability,
                cost reduction, time saving, and heightened overall efficiency.
                Your job is to write a cold email to the client regarding the job mentioned above, describing your capability in fulfilling their needs.
                Add the following links to showcase your profile:
                {link}
                Remember you are {name}, {position}.
                Do not provide a preamble.
                ###EMAIL (NO PREAMBLE):
                """
            )

            chain_email = prompt_email | model
            
            res_email = chain_email.invoke({
                "job_description": str(job),
                "link": str(profile_links),
                "name": name,
                "position": position
            })

            st.subheader("Generated Cold Email")
            st.write(res_email.content)
