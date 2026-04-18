import random
import string


def gerar_senha(tamanho):
    caracteres = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def validar_tamanho(tamanho):
    if tamanho <= 0:
        raise ValueError("O tamanho deve ser maior que zero.")
    if tamanho > 128:
        raise ValueError("O tamanho máximo permitido é 128 caracteres.")


def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")

    try:
        tamanho = int(input("Digite o tamanho da senha: "))
        validar_tamanho(tamanho)

        senha = gerar_senha(tamanho)

        print("\nSenha gerada com sucesso:")
        print(senha)

    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
