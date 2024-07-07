import io
import os
import random
import json
import string
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from fpdf import FPDF
import pandas as pd
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from django.shortcuts import render 
from django.http import JsonResponse 

# Load environment variables from .env file
load_dotenv()
# openai.api_key = 'YOUR_API_KEY'

openai_key = os.getenv("OPENAI_API_KEY")
llm_name = "gpt-3.5-turbo"
model = ChatOpenAI(api_key=openai_key, model=llm_name)

@csrf_exempt
def process_csv_data(request: HttpRequest):
    """
    Process the uploaded CSV or Excel file, perform calculations, and generate a PDF report.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the generated PDF report.

    Raises:
        KeyError: If the 'file' key is not present in the request.FILES dictionary.
        HttpResponse: If the uploaded file format is invalid.

    """
    if request.method == 'POST':
        file = request.FILES['file']
        question = request.POST['question']
        file_extension = file.name.split('.')[-1]
        
        if file_extension == 'csv':
            df = pd.read_csv(file).fillna(value=0)
        elif file_extension == 'xlsx':
            df = pd.read_excel(file).fillna(value=0)
        else:
            return HttpResponse("Invalid file format. Please upload a CSV or Excel file.")
        
        # Perform calculations using the langchain_experimental agent
        from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

        agent = create_pandas_dataframe_agent(
            llm=model,
            df=df,
            verbose=True,
        )

        # Define the prompt for the agent
        CSV_PROMPT_PREFIX = """
        First set the pandas display options to show all the columns,
        get the column names, then answer the question.
        """

        CSV_PROMPT_SUFFIX = """
        - **ALWAYS** before giving the Final Answer, try another method.
        Then reflect on the answers of the two methods you did and ask yourself
        if it answers correctly the original question.
        If you are not sure, try another method.
        FORMAT 4 FIGURES OR MORE WITH COMMAS.
        - If the methods tried do not give the same result, reflect and
        try again until you have two methods that have the same result.
        - If you still cannot arrive at a consistent result, say that
        you are not sure of the answer.
        - If you are sure of the correct answer, create a beautiful
        and thorough response using Markdown.
        - **DO NOT MAKE UP AN ANSWER OR USE PRIOR KNOWLEDGE,
        ONLY USE THE RESULTS OF THE CALCULATIONS YOU HAVE DONE**.
        - **ALWAYS**, as part of your "Final Answer", explain how you got
        to the answer on a section that starts with: "\n\nExplanation:\n".
        In the explanation, mention the column names that you used to get
        to the final answer.
        """

        # Invoke the agent to get the result
        res = agent.invoke(CSV_PROMPT_PREFIX + question + CSV_PROMPT_SUFFIX)
        result = res['output']

        # Generate PDF report
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, result)

        # Output PDF to a string
        pdf_output = pdf.output(dest='S')

        # Write PDF string to a buffer
        pdf_buffer = io.BytesIO()
        pdf_buffer.write(pdf_output.encode('latin1'))  # FPDF outputs in latin1 encoding
        pdf_buffer.seek(0)

        # Create and return the HTTP response with the generated PDF report
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="result.pdf"'

        return response
    
    # Render the 'result.html' template if the request method is not POST
    return render(request, 'result.html')




def chatgpt(request):
    return render(request, 'chatboot.html')



messages = [
    SystemMessage(
    content='''
            
    You are a helpful assistant named Abdullah who is extremely competent as a Data Scientist. 
    You are knowledgeable about various aspects of data science, computer science history,
    algorithms, and more. When interacting with users, provide accurate,
    detailed, and contextually relevant information. Be concise yet thorough, ensuring clarity in your explanations.
    Offer additional insights or related information when appropriate to enhance the user's understanding. 
    Your goal is to assist users in the best possible way by leveraging your expertise in data science and computer science history.    
        
        '''
    ),
    HumanMessage(content="who was the very first computer scientist?"),
]


# res = model.invoke(messages)
# print(res)


def first_agent(messages):
    res = model.invoke(messages)
    return res


@csrf_exempt
def run_agent(request: HttpRequest):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_input = body.get('message', '')

        messages = [HumanMessage(content=user_input)]
        response = first_agent(messages)
        return JsonResponse({"response": response.content})
    
    # Render the 'chatboot.html' template if the request method is not POST
    return render(request, 'chatboot.html')




def Test(request):
    
    
    abdullah_list = {"title:": "Abdullah's Page", "content: ": "This is a test page for Abdullah.", "author: ": "Abdullah",
                     "title:": "ahemd's Page", "content: ": "This is a test page for ahmed.", "author: ": "ahmed",
                     "title:": "MOHAMED's Page", "content: ": "This is a test page for MOHAMED.", "author: ": "MOHAMED",
                     }
    
    test = "This is a test page for Abdullah."
    return render(request, 'abdullahApp/testAbdullah.html',context={"abdullah_list":abdullah_list, "test" : test,})




def homePage(request):
    return render(request, 'home.html')

def aboutPage(request):
    return render(request, 'about.html')

def passwordPage(request):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
    return HttpResponse(password)


def contactPage(request):
    return render(request, 'how_are_we.html')

