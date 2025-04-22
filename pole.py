jména = ["Tom", "Martin", "Jirka", "Adel", "Zeman", "Kuloplesk"]
print(len(jména))
for i in jména:
    print(i)
dalsiJmeno = input("Zadejte další jméno.")
jména.append(dalsiJmeno)
jména.remove("Martin")
jména.sort()
jména.reverse()
print(jména)