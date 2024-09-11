import re
# INDICE DO PADRAO ENCONTRADO
pattern = "aaab"
string = "aaaaaaab"
match = re.search(pattern, string)
if match:
    print("Padrão encontrado no índice", match.start())
else:
    print("Padrão não encontrado")

# PADRAO ENCONTRADO
pattern = "apple"
text = "I have an apple, but I prefer oranges to apples."
match = re.search(pattern, text)
if match:
    print("Padrão encontrado:", match.group())
else:
    print("Padrão não encontrado")

# RETORNA TODAS AS OCORRENCIAS ENCONTRADAS
pattern = "apple, but"
text = "I have an apple, but I prefer oranges to apples."
matches = re.findall(pattern, text)
print("Ocorrências encontradas:", matches)
