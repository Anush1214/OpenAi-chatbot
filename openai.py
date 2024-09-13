from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

command='''
[14:43, 8/31/2024] Dhrithi Yapper Hegde: Okay
[14:43, 8/31/2024] Dhrithi Yapper Hegde: No but am going out to roam a lil
[14:44, 8/31/2024] ∀nush :): Ahaaa 👀😏
[14:47, 8/31/2024] ∀nush :): Enjoy enjoy 😏
[14:53, 8/31/2024] Dhrithi Yapper Hegde: With my friends man
[14:53, 8/31/2024] Dhrithi Yapper Hegde: 😔😔
[14:54, 8/31/2024] ∀nush :): Did I say anything?! 😶
[14:54, 8/31/2024] ∀nush :): I didn't even mention who
[14:54, 8/31/2024] ∀nush :): Chill chill have fun
[15:17, 8/31/2024] Dhrithi Yapper Hegde: Ayyyoo yeah okayy!😭

'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named ∀nush :) who speaks kannada as well as english. you are from India and is a student. You analyze chat history and respond like ∀nush :). output shlould be the next chat response (message only) "},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)