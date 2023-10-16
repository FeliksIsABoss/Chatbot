import openai
import os
import asyncio
import discord
from discord import Webhook
import aiohttp

openai.api_key = my_secret = os.environ['OPENAI_API_KEY']

end_program = False
while not end_program:
  get_input = input("Enter a prompt: ")
  if get_input == "exit":
    end_program = True
    print("Exiting chat")
  else:
    system_data = [
      {"role": "system", "content": "You are an ai assistant."},
      {"role": "user", "content": get_input}
    ]
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = system_data
    )
    assistant_response =  response.choices[0].message.content
    system_data.append({"role": "assistant", "content": assistant_response})
    output = "Assistant: " + assistant_response
    print(output)
