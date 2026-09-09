
from groq import Groq

# procoding -> 

client  =  Groq(api_key= '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')
# print(client)

while True:
    pergunta  = input('Digite sua pergunta: ')

    prompt_system  =  'Você é um aviador, especialista em voos nacionais'

    chat_completion =  client.chat.completions.create(

    model =  'openai/gpt-oss-120b',
    temperature= 0.7,

    messages=[
        {'role':'system',
        'content':prompt_system},

        {
            'role':'user',
            'content': pergunta }

        ]
    )
    print(chat_completion.choices[0].message.content)