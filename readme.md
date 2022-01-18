# Rocket Bank :rocket:

## Padrões

### Commits

É usado o padrão de commits semânticos:

**Estrutura**:
```sh
-> [escopo]: <descrição>
```

**Exemplo**:

Foi adicionado ao projeto a feature (funcionalidade) de atualização de conta. Logo, o commit com essa alteração deveria se parecer com:

```sh
-> feat: adiciona o api pra atualização de contas
```


**Mais exemplos:**

|Commit               | Descrição          |
|:--                  |:--                 |
|`chore: add etapas de build do projeto` | Pequenas alterações que não são novas funcionalidades.|
|`docs: detalhamento das APIs`           | Semelhante a uma wiki; documentações etc.|
|`feat: adiciona a funcionalidade de saque` | Criação de Nova funcionalidade|
|`fix: remove a mensagem de erro`        | Correção de bugs      |
|`refactor: reutiliza da logica de calculo de saldo` | Refatoração de um código|
|`style: muda a identação de espaços pra tabs` | Alteração em estilos, formatação de código etc|
|`test: automatiza testes de cálculo`| Criação de testes da sua aplicação|

#### Recomendação de estudos sobre Commits Semânticos
- https://blog.geekhunter.com.br/o-que-e-commit-e-como-usar-commits-semanticos/
- https://blog.cubos.io/que-tal-comecar-a-usar-commits-semanticos/
- https://ilegra.com/blog/tudo-o-que-voce-precisa-saber-sobre-commits-semanticos/


### Adição de código
Pra adicionar códigos ao projeto é recomendado o uso de `pull requests`.

#### Branchs
Pra isso é necessário criar branchs no `git` pra cada tarefa que for executar, isso permite a análise de código pelas outras pessoas da equipe, a fim de manter um nível de qualidade e padronização do código.


Vai começar uma feature nova? Então basta criar uma branch baseada na branch principal:

```sh
# Indo pra branch principal
-> git checkout main

# Criando uma nova branch
-> git checkout -b <nomeDaBranch>

#Exemplo
-> git checkout -b atualizacao-conta
```

**Como saber em qual branch você está?**

O comando `git branch --show-current` te ajuda com isso.

#### Criei minha branch, e agora?

Com o avanço do seu trabalho, ou seja, criação de código, você deve ir criando `commits` e mandando pro repositório sempre que possível.

Vamos supor que você alterou o arquivo `api.py` e adicionou a rota de atualização de contas.

```sh
# Adiciona o arquivo ao stage
-> git add api.py

# Adiciona o que estiver no stage à um commit
-> git commit -m "feat: adiciona endpoint pra atualização de conta"

# Manda pro remote (repositório lá no Github):
-> git push origin <nomeDaBranch>

# Exemplo
-> git push origin atualizacao-conta
```

#### Recomendação de estudos sobre Git
- https://github.com/deppbrazil/course-git-e-github-para-iniciantes
- https://www.alura.com.br/artigos/o-que-e-git-github?gclid=Cj0KCQiAuP-OBhDqARIsAD4XHpd2KKfz3BFJwBFFlCQoN_9kWCh1dO-vnrH9ujg52PMk8B0oFQGa3eAaAkUfEALw_wcB
- https://youtu.be/BAmvmaKQklQ
- https://youtu.be/6Czd1Yetaac

### Padrão das APIs
#### Rest
Neste projeto é utilizado o padrão REST pra definição de rotas.
Com isso, o formato da rota e a forma como ela será chamada depende do que será feito com determinado recurso.

#### O que é um recurso?
Recurso é aquilo que estou manipulando na minha API, no caso desse projeto alguns recursos são `conta`, `cliente`, `movimentações`, `transferências` etc.

#### Definição da rota pra cada recurso

Pra definição de recurso numa rota o ideal é decidir se eles serão referenciados no singular ou no plural, ou seja, pro recurso de `conta`, por exemplo podemos ter a rota `/conta` ou `/contas`.

**Neste projeto usaremos sempre os recursos no plural.**

Exemplos:
- `/contas`
- `/transferencias`
- `/clientes`
- `/clientes/<idCliente>/contas`

#### Verbos/Métodos

Podemos manipular um recurso de diversas maneiras, seja obtendo ele, atualizando, criando um novo, deletando etc.

No padrão REST cada operação pode ser definida pelo VERBO utilizado pra chamar a rota, os mais comuns são:

| Verbo  | Descrição                          |
|:--     | :--                                |
|`GET`   | Obtem um recurso                   |
|`POST`  | Cria um novo recurso               |
|`PUT`   | Atualiza um recurso completamente  |
|`PATCH` | Atualiza um recurso parcialmente   |
|`DELETE`| Remove/Deleta o recurso            |

**Exemplo usando o recurso de clientes:**

| Verbo  | Rota                   | Descrição                                  |
| :--    | :--                    | :--                                        |
|`GET`   | `/clientes`            | Obtem a lista de clientes                  |
|`GET`   | `/clientes/<idCliente>`| Obtem um cliente específico                |
|`POST`  | `/clientes`            | Cria/registra um novo cliente              |
|`PUT`   | `/clientes/<idCliente>`| Atualiza completamente o cliente informado |
|`PATCH` | `/clientes/<idCliente>`| Atualiza parcialmente o cliente informado  |
|`DELETE`| `/clientes/<idCliente>`| Deleta/Remove o cliente                    |

**Exemplos de rotas que não são recomendadas:**

| Verbo  | Rota                   | Descrição                                       |
| :--    | :--                    | :--                                        |
|`GET`   | `/obterClientes`       | Redundante, pois o verbo GET já indica a intenção de obter o recurso |
|`GET`   | `/obterClientePorId/<idCliente>`| Redundante, pois o verbo GET já indica a intenção de obter o recurso e o ID no fim da rota indica o recurso desejado |
|`POST`  | `/criarCliente` | Redundante, pois o verbo POST ja indica a intenção de criar um recurso |
|`PUT`   | `/atualizarCliente/<idCliente>`| Redundante, pois o verbo PATCH/PUT ja indicam a intenção de atualizar algo |
|`GET`   | `/criarCliente`       | Incorreto, pois o verbo GET indica a intenção de obter algo, não de gerar. |
|`POST`  | `/deletarCliente`       | Incorreto, pois o verbo POST indica a intenção de criar algo, o mais indicado é o verbo DELETE. |

**Atenção:** Apesar das recomendações, em alguns projetos não é raro encontrar exceções, mas cada desvio de padrão deve ser alinhado com a equipe a fim de evitar a despadronização e aumento de complexidade do projeto.

#### Códigos de Respostas

No HTTP (protocolo usado pelo padrão REST) toda a resposta de requisição vem acompanhada de código, normalmente chamado de **código http** ou **status http**.

As categorias desses códigos são:

| Código | Descrição                                                                                      |
|:--     | :--                                                                                            |
|`2xx`   | Sucesso                                                                                        |
|`3xx`   | Usado pra redirecionamentos                                                                    |
|`4xx`   | Algum erro no cliente (validação de dados, autenticação, autorização, recurso inexistente etc) |
|`5xx`   | Erro no servidor (banco de dados fora do ar, lógicas mal implementadas, código quebrado etc)   |

Pra esse projeto usaremos na maioria das vezes o `200` e o `400` pra indicar respostas de sucesso ou erros de validação, mas existem diversos outros códigos que devem ser considerados:

| Código | Descrição                                                                                      |
|:--     | :--                                                                                            |
|`200`   | Sucesso                                                                                        |
|`201`   | Recurso criado. Normalmente usado em requisições `POST` |
|`204`   | No Content. Sucesso, mas indica que não há conteúdo na resposta, normalmente usado em requisições `DELETE` |
|`200`   | Sucesso                                                                                        |
|`400`   | Bad Request. Usado pra erros gerais de validação, ex. formulários |
|`401`   | Não autorizado. Indica que o usuário não informou as credenciais/não está autenticado |
|`403`   | Proibido. Indica que o usuário está autenticado, mas não tem permissões pra manipular determinado recurso |
|`404`   | Recurso não encontrado. Ex. tentou acessar um cliente com um código inexistente |

Códigos `3xx` e `5xx` não costumam ser usados intencionalmente por desenvolvedores.

#### Recomendação de estudos sobre REST
- https://gist.github.com/renatoapcosta/8882e63760f7eeac469e1e162377fa30
- https://www.alura.com.br/artigos/rest-conceito-e-fundamentos?gclid=Cj0KCQiAuP-OBhDqARIsAD4XHpeJIBvsEAuxZYdTxmxf3uPttEvAd1utqqkebBeysUYyQLwFPzFLKKEaAkNqEALw_wcB
- https://www.brunobrito.net.br/api-restful-boas-praticas/

