# sort based on color
models=[{"made":"Nokia","model":"250","color":"Blue"},{"made":"Samsung","model":"20","color":"Black"},{"made":"Iphone","model":"14","color":"white"}]
print(models)
# models.sort(key:lambda i: )
models.sort(key=lambda i:i["color"])
print(models)