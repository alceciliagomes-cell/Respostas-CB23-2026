# Respostas das questões de 1 a 3

## Questão 1
No diagrama é possível observar que as classes se organizam em 3 grupos

No primeiro grupo, a classe base é Pessoa, que fornece os atributos básicos de nome e idade. A classe Funcionário herda de Pessoa, mantendo esses dados e adicionando salário e carga horária. A classe Garçom, Chefe de cozinha e Gerente são subclasses de Funcionário, herdando todas as características de Pessoa e Funcionário, mas implementando seus próprios métodos de trabalho.

No segundo grupo, a classe base é Iguaria, que possui nome e preço. As classes Pizza e Bolo são subclasses de Iguaria e herdam esses dois atributos, adicionando suas características próprias, como a borda recheada na Pizza e o formato no Bolo.

No terceiro grupo, a classe base é Restaurante, contendo nome, endereço e telefone. A classe Pizzaria atua como subclasse de Restaurante, herdando todos esses dados e incluindo o atributo de rodízio.

## Questão 2

A relação entre Restaurante e Iguaria é de associação, porque um restaurante não é uma comida, mas ele tem várias comidas no seu cardápio. Para implementar isso, a classe Restaurante precisaria ter um atributo chamado cardápio, que seria uma lista guardando vários objetos da classe Iguaria. Para deixar a relação mais completa, daria para criar uma classe nova chamada Pedido, relacionando o Garçom com as Iguarias solicitadas pelo cliente.

## Questão 3

Argumento 1: O tipo ideal seria uma lista de objetos do tipo Iguaria ou um objeto da classe Pedido, pois o garçom precisa registrar quais comidas o cliente pediu.

Argumento 2: O tipo seria um objeto da classe Iguaria ou Pedido, representando o prato específico que a cozinha precisa produzir no momento.

Argumento 3: O tipo seria um objeto da classe Funcionário, já que o gerente precisa receber qual funcionário específico ele está demitindo do restaurante.