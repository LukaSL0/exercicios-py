lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
print(f"Lista: {lista}")
elemento = int(input("Digite o valor que você deseja procurar na lista: "))

def busca_binaria(li, el):
    inicio = 0
    fim = len(li) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if li[meio] == el:
            return meio
        elif li[meio] < el:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

resultado = busca_binaria(lista, elemento)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print(f"Elemento não encontrado.")