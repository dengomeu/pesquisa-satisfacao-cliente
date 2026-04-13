# Programa de pesquisa de satisfação ao cliente - TudoWeb
# Coleta de opinião de entrevistados sobre o atendimento

# Variáveis para contabilizar respostas:
quantidade_excelente = 0
quantidade_bom = 0
quantidade_ruim = 0

# Número de entrevistados
numero_entrevistados = 50 # Ajustado para a versão final

for i in range(numero_entrevistados):
    print(f"\n--- 👤 Entrevistado {i + 1} ---")
    nome = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")

    print("Avalie nosso atendimento:")
    print("🟢 [1] - Excelente")
    print("🟡 [2] - Bom")
    print("🔴 [3] - Ruim")
    opiniao = int(input("Digite a sua opinião (1, 2 ou 3): "))
    
    while opiniao < 1 or opiniao > 3:
        print("⚠️ Opção inválida! Por favor, digite apenas 1, 2 ou 3.")
        opiniao = int(input("\n Digite a sua opinião (1, 2 ou 3): "))

    if opiniao == 1:
        quantidade_excelente += 1
        resposta = "Excelente"
    elif opiniao == 3:
        quantidade_ruim += 1
        resposta = "Ruim"
    elif opiniao == 2:
        quantidade_bom += 1
        resposta = "Bom"

    print(f"✅ Registrado: {nome}, {idade} anos - Opinião: {resposta}")

# Exibição dos resultados finais
print("\n=== 📈 Resultado da pesquisa 📈===")
print(f"\n 👥 Total de entrevistados: {numero_entrevistados}")
print("📌 Quantidade de respostas:")
print(f"  🟢 Excelente: {quantidade_excelente}")
print(f"  🟡 Bom:       {quantidade_bom}")
print(f"  🔴 Ruim:      {quantidade_ruim}\n")

percentual_excelente = (quantidade_excelente / numero_entrevistados) * 100
percentual_bom = (quantidade_bom / numero_entrevistados) * 100
percentual_ruim = (quantidade_ruim / numero_entrevistados) * 100

print(f"\n 📊 Percentuais:")
print(f"  Excelente: {percentual_excelente:.1f}%")
print(f"  Bom: {percentual_bom:.1f}%")
print(f"  Ruim: {percentual_ruim:.1f}%")