import ollama

res = ollama.chat(
    model="llava:34b",
    messages=[
        {
             'role': 'user',
             'content': 'Describe this image:',
             'images': ['./test/DX_25101.jpg']
        }
   ]
 )
print(res['message']['content'])
