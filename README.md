# Projeto de Consultas em Banco de Dados com Python e PostgreSQL Por Meio das Ferramentas UiBakery e Databricks
Este projeto tem como objetivo realizar consultas em um banco de dados PostgreSQL usando Python para responder a algumas perguntas específicas.
A ferramenta UiBakery disponibiliza o acesso a diversos modelos de bases de dados já populadas, para este projeto foi utilizado o modelo de e-commerce.
O Databricks permite a criação de notebooks no qual pode-se criar códigos em python, sql, R. Um código em python/sql foi criado no notebook do Databricks com o intuito de 
conectar na base de dados do UiBakery e fazer as consultas necessárias para o projeto.

# Ferramentas Python
1 - Para conectar a base de dados foi utilizada o módulo do python Psycopg2, no qual são utilizadas as credenciais geradas no UiBakery.

2 - A subclasse Counter para auxiliar na identificação de maiores repetições.

3 - O módulo re do python para auxiliar na máscara do email.

# Lucidchart
A ferramenta Lucidchart foi utilizada para desenhar o diagrama ER do banco de dados e-commerce disponibilizado pelo UiBakery.

# Serão realizadas consultas que respondem às seguintes perguntas:

1 - Qual país possui a maior quantidade de pedidos cancelados?

2 - Qual a linha de produto mais vendida e o faturamento total para pedidos realizados no ano de 2005?

3 - Quais são os nomes, sobrenomes e e-mails dos funcionários que estão no escritório localizado no Japão? Obs: o local-part do e-mail será mascarado por questões de privacidade.

# Configuração do Ambiente
Antes de executar o código, você precisará configurar o ambiente Python e instalar as bibliotecas necessárias. Certifique-se de ter o Python instalado em seu sistema. Em seguida, execute o seguinte comando para instalar as bibliotecas.


# Executando o Código
Você pode executar o script Python fornecido para obter as respostas para as perguntas específicas. Para isso, basta executar o seguinte comando no terminal:
python script.py
As respostas para as perguntas serão exibidas no console após a execução do script.

# Perguntas Respondidas
1. Qual país possui a maior quantidade de pedidos cancelados?
Para responder a essa pergunta, o script conecta-se ao banco de dados e executa uma consulta SQL que retorna o país que teve o maior número de pedidos com status 'Cancelled'.

2. Qual a linha de produto mais vendida e o faturamento total para pedidos realizados no ano de 2005?
Para responder a essa pergunta, o script conecta-se ao banco de dados e executa uma consulta SQL que retorna a linha de produto mais vendida em pedidos com status 'Shipped' realizados no ano de 2005. Além disso, o script também calcula o faturamento total para essa linha de produto.

3. Quais são os nomes, sobrenomes e e-mails dos funcionários que estão no escritório localizado no Japão?
Para responder a essa pergunta, o script conecta-se ao banco de dados e executa uma consulta SQL que retorna os nomes, sobrenomes e e-mails dos funcionários que estão no escritório localizado no Japão. Para proteger a privacidade dos funcionários, o local-part do e-mail é mascarado antes da exibição.

# Observações
Este projeto foi desenvolvido apenas para fins de aprendizado e demonstração. As informações de conexão ao banco de dados e outras credenciais sensíveis foram incluídas apenas para fins de ilustração e não devem ser compartilhadas publicamente. Em ambientes de produção, recomenda-se o uso de práticas de segurança adequadas para proteger as credenciais.

Espero que este README.md tenha ajudado você a entender o projeto e como executar o código. Se você tiver alguma dúvida ou precisar de mais informações, sinta-se à vontade para entrar em contato!
