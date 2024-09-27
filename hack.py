# Caminho do arquivo
file_path = 'limits'

# Ler o arquivo e modificar o valor
with open(file_path, 'r') as file:
    lines = file.readlines()

# Alterar o LIMIT_EXECTIME
for i in range(len(lines)):
    if 'LIMIT_EXECTIME' in lines[i]:
        # Extrair o valor atual
        current_value = int(lines[i].split('=')[1].strip())
        # Atualizar o valor
        new_value = current_value * 10
        lines[i] = f'LIMIT_EXECTIME={new_value}\n'
        break

# Escrever as alterações de volta no arquivo
with open(file_path, 'w') as file:
    file.writelines(lines)

print("LIMIT_EXECTIME atualizado para:", new_value)
