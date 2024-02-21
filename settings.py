PALM_MODEL = "models/text-bison-001"
FAQ_FILE = 'data\\faqs.csv'
EMPLOYEE_DB = "data/employees.db"
INSTRUCTOR_EMBEDDING = "sentence-transformers/all-MiniLM-l6-v2"
VECTORDB_PATH = "faiss_index"
qa_prompt = """
    Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}
    """
invoice_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """
youtube_transcribe_prompt = """You are Yotube video summarizer. You will be taking the transcript text
                and summarizing the entire video and providing the important summary in points
                within 250 words. Please provide the summary of the text given here:  """

prompt_pdf = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "Answer is not available in the context !!!!!!!", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

text2sql_prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEES and has the following columns - Employee_ID, Name, 
    Department, Title, Email, City, Salary, 
    Work_Experience \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEES ;
    \nExample 2 - Tell me all the employees living in Noida city?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEES 
    where City="Noida"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """