# Relatório de Code Review - Python (Estruturas Sequencial e de Decisão)

## 1. Validação de Entrada e Tipagem
* **`float` vs `int`**: Em exercícios envolvendo medidas, dinheiro ou notas escolares, prefira sempre `float(input())`. O uso de `int` quebra o script se o usuário digitar valores decimais (ex: 1.75 ou 10.5).
* **Proteção contra Crash (Erros Fatais)**: Cálculos que podem gerar exceções matemáticas (como extrair raiz quadrada de número negativo na Equação de 2º Grau) devem ser executados **exclusivamente dentro** dos blocos condicionais que validam a operação, nunca no escopo global.
* **Escopo de Variáveis**: Tentar acessar uma variável que só existe dentro de uma condição `else` (ex: chamar `delta` após o usuário digitar `a = 0`) resultará em `NameError`.

## 2. Otimização de Lógica e Matemática
* **Precedência de Operadores**: Em fórmulas algébricas convertidas para código, utilize parênteses no denominador para garantir a ordem correta de execução pela máquina. Exemplo: `/(2*a)` em vez de `/2*a`.
* **Lógica de Múltiplos Fatores**:
  * **Caixa Eletrônico (26)**: A utilização de `//` e `%` está correta para quebrar as dezenas e centenas, mas a lógica atual pula a obrigatoriedade das notas de R$ 50 e R$ 5 exigidas no enunciado.
  * **Ano Bissexto (22)**: A condição atende apenas anos seculares (terminados em 00) divisíveis por 4. Falta implementar a exceção da divisibilidade por 400.

## 3. Clean Code (Código Limpo)
* **Manipulação Eficiente de Strings**: Evite cadeias longas de `or` para tratar letras maiúsculas e minúsculas. Utilize métodos nativos do Python no momento do input ou da verificação.
  * *Refatoração:* Em vez de `if (genero == "M") or (genero == "m"):`, utilize `if genero.upper() == "M":`.
* **Uso do Operador `in`**: Para verificar se um elemento pertence a um conjunto (como checar vogais), prefira `if letra.lower() in "aeiou":`.

## 4. Regras de Negócio e Requisitos
* **Folha de Pagamento (17)**: Atenção às regras fiscais descritas no requisito. O **FGTS** é um encargo do empregador; portanto, não compõe o "Total de Descontos" e não deve ser subtraído para compor o Salário Líquido.
* **Aumento Salarial (15-16)**: O cálculo financeiro está correto, porém a entrega está incompleta. O enunciado exige a impressão de 4 saídas distintas: salário antigo, percentual aplicado, valor absoluto do aumento e o salário novo.

17) Calculo Tinta (2).py: Erro no cálculo de custo (multiplicando quantidade de latas pelo valor do galão).

14) Papo-de-Pescador.py: Variáveis calculando multas negativas antes de validar se houve excesso de peso.

21.2) Equação 2ºGrau.py: Erro fatal (crash) se a = 0 e erro matemático ao tentar calcular raízes antes de verificar se o delta é negativo.

22) Ano Bissexto.py: Lógica incompleta que falha em anos bissextos comuns (como 2024) por ignorar a regra completa do calendário.

17) Folha de Pagamento.py: FGTS sendo classificado e subtraído incorretamente como desconto do funcionário.

15 - 16)Aumento Salarial.py: Omitindo informações exigidas no output (salário antes do reajuste e valor absoluto do aumento).

26) Caixa Eletronico.py: A matemática ignora completamente as notas de R$ 50 e R$ 5.

12) Ordem Decrescente.py: Falha de atribuição se o usuário inserir dois ou mais números iguais.

09) Maior dos Tres.py e 10) Maior e Menor dos Três.py: O método .isnumeric() bloqueia entradas válidas de números reais (floats).

24) Desmembrando Numeros.py: Ausência da lógica de tratamento de strings para singular e plural (ex: exibir "1 unidades" em vez de "1 unidade").