import wolframalpha
app_id = 'Your App Id'
client = wolframalpha.Client(app_id)

res = client.query('')

print (next(res.results).text)