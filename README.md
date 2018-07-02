BOTS e Perfis do Twitter
========================

Aqui estão os códigos utilizados para a realização da pesquisa sobre bots seguindo os pré-candidatos à presidência da república.

Os principais resultados estão aqui: link

O relatório completo está disponível aqui: link

Como reproduzir a pesquisa
--------------------------

+ Crie um app para o Twitter em https://apps.twitter.com/, você vai precisar da autenticação que ele fornece
+ Crie uma chave na API do *botometer* em https://market.mashape.com/OSoMe/botometer você vai precisar da chave dela também
+ Complete os códigos com as chaves criadas para o Twitter e para o *botometer*
+ Crie a base de dados utilizando os comandos de criação de tabela disponíveis em database.sql.
+ Insira na tabela politicos, os perfis de interesse para análise com comandos apropriados no SQL
   + Alguns elementos não podem ser nulos: id, grafo, seguidores e buscar
   + A coluna buscar é utilizada para indicar quais perfis já tiveram seus seguidores coletados (1, precisa coletar; 2, j foram coletados)
   + A coluna seguidores, indica quantos seguidores esse perfil possui, deve ser inicializada com 0
+ Com a tabela preenchida, execute o código get_followers.py
   + Esse código irá pegar a o ID de todos os seguidores dos perfis indicados na tabela.
+ Depois desse código ser executado, execute o código prob_bot.py
   + Aqui ser coletado o *SCORE CAP* dos seguidores encontrados de forma aleatória
   + Esse código tem um tempo de execução bastante longo, e irá continuar em execução até calcular o *SCORE CAP* de todos os seguidores, mas isso não é necessário para o próximo passo;
+ Execute o código guesstimator.py
   + Esse código calcula o intervalo de confiança da quantidade de bots que segue cada perfil;
   + Não é necessário interromper a execução do prob_bot.py para executá-lo;
