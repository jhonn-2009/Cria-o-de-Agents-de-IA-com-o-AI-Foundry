
from groq import Groq

# procoding

client = Groq(api_key= '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')

pergunta = input('Digite sus pergunta: ')
chat_completion = client.chat.completions.create(

    model = 'openai/gpt-oss-120b',

    messages=[
        {'role':'system',
         'content':'voce é um aviador'},
{
    'role':'user',
    'content': 'pergunta'
}
    ]

)
print(chat_completion.choices[0].message.content)