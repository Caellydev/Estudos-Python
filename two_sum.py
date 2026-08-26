def two_sum(nums, target):
    """
    Recebe uma lista de números (nums) e um valor alvo (target).
    Retorna os índices dos dois números que somam o target.

    Exemplo:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]
        (porque nums[0] + nums[1] == 2 + 7 == 9)
    """
    vistos = {}  # valor -> índice

    for indice, numero in enumerate(nums):
        complemento = target - numero
        if complemento in vistos:
            return [vistos[complemento], indice]
        vistos[numero] = indice

    return []  # não encontrou par (não deveria acontecer nos testes abaixo)


if __name__ == "__main__":
    # Só pra rodar manualmente e ver o resultado no terminal
    print(two_sum([2, 7, 11, 15], 9))  # esperado: [0, 1]
