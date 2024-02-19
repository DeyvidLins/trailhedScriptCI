def add_new_tag_component(tag,new_tag_component):# Abrir o arquivo para leitura

    name_file = 'C:/Users/deyvi/OneDrive/Área de Trabalho/Todos os arquivos/pasta01/TodosMeusProjetos/Python/sfdxNewProject/Retrieeve xml/source/objects/Account.object'
    last_tags= f'</{tag}>'

    with open(name_file, 'r') as f:
        lines = f.readlines()

    # Procurar pela palavra "morango" e adicionar uma quebra de linha após a última ocorrência
    index_last = None
    for i, line in enumerate(lines):
        if f'{last_tags}' in line:
            index_last = i

    # Adicionar uma quebra de linha após a última ocorrência de "morango"
    if index_last is not None:
        lines.insert(index_last+ 1, f'{new_tag_component}')

    # Escrever as alterações de volta para o arquivo
    with open(name_file, 'w') as f:
        f.writelines(lines)



    


    
    