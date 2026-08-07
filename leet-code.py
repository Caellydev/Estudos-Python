#Dado um array de inteiros `nums` e um inteiro `target`, retorne os índices dos dois números cuja soma seja igual a `target`.
#Você pode assumir que cada entrada terá exatamente uma solução e não pode usar o mesmo elemento duas vezes. Ex: 3 + 3

#Você pode retornar a resposta em qualquer ordem.

def twoSum(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return[]

entrada = input("Digite os números seprados por vírgula: ")
partes = entrada.split(",")

nums = []
for parte in partes:
    nums.append(int(parte))

target = int(input("Escreva o Alvo: "))

resultado = twoSum(nums, target)
print("Índice encontrado:", resultado)