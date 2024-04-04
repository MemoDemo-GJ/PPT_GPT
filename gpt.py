from openai import OpenAI
import os
import backoff
import openai

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Set OpenAI API key


@backoff.on_exception(backoff.expo, openai.RateLimitError)
def gpt_summarise(system, text):
    completion = client.chat.completions.create(model="gpt-3.5-turbo-0125",
                                                messages=[{"role": "system", "content": system},
                                                          {"role": "user", "content": text}])
    return (completion.choices[0].message.content)
