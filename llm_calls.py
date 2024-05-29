import openai
import utils


# extract_information calls chat_gpt's models and passes the document to ask it extract all import financial data
def extract_information(financial_text: str, format_path: str, api_key="sk-proj-SSMFJ3gTO2dUyU6SKha2T3BlbkFJjyoElUQNtBmh5vsw91Dm", model="gpt-3.5-turbo", max_tokens=1000):

    openai.api_key = api_key

    format = utils.read_format(format_path)

    response = openai.chat.completions.create(
        model=model,
          messages=[
              {"role": "system",
               "content": "You are an assistant. "},
              {"role": "user", "content": f"Please map the data from here { financial_text } to fit this json format { format }. Please make sure all numbers are written out in there full numerical value (for example: 20000 thousand would be 20000000) and the data is from the most recent quarter"}
          ],
          max_tokens=max_tokens,
          n=1,
          stop=None,
          temperature=0.5

    )

    output_text = response.choices[0].message.content

    return output_text 



# matching_call all of the data provided from the previous model and conforms it to our standard form structure
def matching_call(data_text: str, api_key="sk-proj-SSMFJ3gTO2dUyU6SKha2T3BlbkFJjyoElUQNtBmh5vsw91Dm", model="gpt-3.5-turbo", max_tokens=1000):
    
    openai.api_key = api_key

    format = utils.read_format()


    content = f"Please find the relevant information and from this data {data_text} and fill this format {format}"


    response = openai.chat.completions.create(
        model=model,
          messages=[
              {"role": "system",
               "content": "You are an assistant."},
              {"role": "user", "content": content}
          ],
          max_tokens=max_tokens,
          n=1,
          stop=None,
          temperature=0.5

    )

    output_text = response.choices[0].message.content

    return output_text 



# This will have a model look over the data and give an overview of what the data says
def analytical_overview():
    pass

