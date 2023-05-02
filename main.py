import streamlit as st
import requests

def execPrompt(prompt,key):
    url = "https://secure-backend-api.stilingue.com.br/blip-nlu-hack-ai/prod/hack-ai/completions"

    headers = {
        "Content-Type": "application/json",
        "hack-ai-team-name": "askblip",
        "hack-ai-api-key": key,
        "accept": "application/json"
    }

    data = {
    "deployment": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 300,
    "temperature": 0.7,
    "top_p": 1,
    "logit_bias": {},
    "user": "TimeHackAi",
    "n": 1,
    "logprobs": 0,
    "suffix": "",
    "echo": False,
    "stop": "string",
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "best_of": 1
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()['choices'][0]['text']

st.title('AskBlip')

key = st.text_input('Api Key:')

empresa = st.text_input('Nome da Empresa:')

pergunta = st.text_area('Pergunta:',placeholder='Insira aqui o conteúdo da pergunta')
resposta = st.text_area('Resposta:',placeholder='Insira aqui o conteúdo da resposta')



if st.button('Reescrever'):
    r = execPrompt("melhore a seguinte resposta, considerando que você é um grande analista e redator de textos que trabalha na empresa " + empresa + " e é responsável por garantir que os clientes dessa empresa tenham suas dúvidas esclarecidas, então é lhe apresentado uma FAQ : " + pergunta + " R:" + resposta + ".",key)
    st.text_area('Reescrita:',value=r, disabled=True)

if st.button('Avaliar'):
    r = execPrompt("avalie a seguinte pergunta e resposta, considerando que você é um grande analista e redator de textos que trabalha na empresa " + empresa + " e é responsável por garantir que os clientes dessa empresa tenham suas dúvidas esclarecidas, então é lhe apresentado uma FAQ : " +pergunta+"R:" +  resposta+ ".",key)
    st.text_area('Avaliação:',value=r, disabled=True)



