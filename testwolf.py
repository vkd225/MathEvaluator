import wolframalpha
app_id = 'QV3GGU-PJ6EREKR5P'
client = wolframalpha.Client(app_id)

res = client.query('')

print (next(res.results).text)