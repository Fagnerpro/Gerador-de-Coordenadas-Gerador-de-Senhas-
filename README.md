# 🔐 Gerador de Coordenadas (Gerador de Senhas)

Projeto em Python para geração de senhas seguras com tamanho customizável.

## 🎯 Objetivo

Simular um gerador de chaves de acesso, permitindo evolução incremental do código e criação de conflitos em ambientes colaborativos.

## 🚀 Funcionalidades

- Geração de senhas aleatórias
- Suporte a:
  - letras minúsculas
  - letras maiúsculas
  - números
  - caracteres especiais
- Entrada dinâmica do tamanho da senha
- Validação de entrada

## 🧪 Etapas de desenvolvimento

1. Geração inicial com letras minúsculas e números
2. Inclusão de letras maiúsculas e caracteres especiais
3. Entrada dinâmica do usuário

## ▶️ Execução

```bash
python gerador_senhas.py
```

## 💡 Exemplo

```text
Digite o tamanho da senha: 12

Senha gerada com sucesso:
aB3@kL9!xP2#
```

## 📌 Melhorias futuras

- Garantir presença mínima de cada tipo de caractere
- Interface CLI com argumentos (`argparse`)
- Exportação de senhas
- Testes automatizados

## 🛠️ Tecnologias

- Python 3.x
