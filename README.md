# Sistema de Cadastro de Pessoas em Python

Sistema de cadastro de pessoas via terminal, com persistência de dados em JSON, permitindo registrar, listar, buscar e remover pessoas.

---

## Pré-requisitos

- Python 3.14 instalado
- Nenhuma dependência externa (utiliza apenas a biblioteca padrão)

---

## Como usar

Clone o repositório:

```bash
git clone https://github.com/athosnm/sistema-cadastro-pessoas.git
cd sistema-cadastro-pessoas
```

Execute o script:

```bash
python cadastro.py
```

Exemplo de uso:

```
[1] Cadastrar uma pessoa
[2] Listar pessoas
[3] Buscar pessoa
[4] Apagar pessoa
[5] Sair

Total de pessoas cadastradas: 2

Digite a opção: 1
Digite o nome: Ana Silva
Digite a idade: 22
Pessoa cadastrada com sucesso.
```

```
Digite a opção: 2

Nome                 | Idade
------------------------------
Ana Silva            | 22
Carlos Souza         | 34
```

---

## Como funciona

O sistema segue um fluxo simples de CRUD pelo terminal:

1. **Carrega os dados** — ao iniciar, lê o arquivo `people.json` se ele existir, preservando cadastros anteriores
2. **Exibe o menu** — apresenta as opções disponíveis junto ao total de pessoas cadastradas
3. **Cadastro com validação** — verifica se o nome já existe (sem diferenciar maiúsculas) e se a idade é um número inteiro positivo
4. **Busca parcial** — encontra pessoas cujo nome contenha o termo digitado, não exigindo correspondência exata
5. **Remoção segura** — localiza a pessoa pelo nome antes de remover, informando caso não seja encontrada
6. **Persiste automaticamente** — salva o arquivo `people.json` após cada cadastro ou remoção

---

## Estrutura do projeto

```
sistema-cadastro-pessoas/
├── cadastro.py    # Script principal
├── people.json    # Dados persistidos (gerado automaticamente)
└── README.md      # Documentação
```

---

## Tecnologias

- **Python 3.12**
- **JSON** — persistência de dados
- **Git**

---

## Aprendizados

- Manipulação de arquivos JSON para persistência de dados
- Validação e tratamento de entradas do usuário
- Organização de código em funções com responsabilidades separadas
- Uso de list comprehensions e funções built-in do Python
- Boas práticas como encapsulamento em `main()` e captura de exceções específicas

---

## Autor

Feito por **[Athos Martins](https://github.com/athosnm)** — sinta-se à vontade para conectar no [LinkedIn](https://www.linkedin.com/in/athos-martins-90113930b/)!