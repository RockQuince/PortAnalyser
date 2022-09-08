# PortAnalyser
Bom, o projeto de hoje se trata justamente de um portscan feito em python 3
um simples programa que visa analisar e trazer as portas abertas e o serviço que esta ativo na porta no momento da analise

# Bibliotecas
Todo projeto foi possivel utilizando as bibliotecas Socket, Sys e Threading  
  
Estão anexados 2 versões do projeto, uma versão não utilizando a biblioteca Threading, a versão inicial, e a outra utilizando a biblioteca Threading, a versão final do projeto, por qual motivo manter as 2 versões? Comparação! É bom ver por onde o projeto começou e comparar como ele terminou
Notei que apenas utilizando a biblioteca de Socket que o scan era demasiado longo, insatisfeito, fui em busca de uma solução e me deparei com a biblioteca Threading e tentei me aventurar ao tentar entender como realmente funcionava e o resultado me surpreendeu, realmente a velocidade do portscan era aumentada em um nivel surreal comparada com a inicial,  e isso me motivou a manter ambas versões para fins de comparação, ja que meus testes com a biblioteca Threading foi um sucesso.

# Programa
Ao iniciar o programa, se deparará com a solicitação de um  "IP alvo" que sera o ip na qual o portscan sera realizado
Logo em seguida sera solicitado um range de inicio e fim, caso esteja procurando por uma porta mais especifica, ficara mais viavel de procurar
Assim que esses valores forem inputados, será informado do alvo e o horario em que o scan começou
e então Recebera os o resultado do scan, quais portas estão abertas e o serviço que nela estava em execussão.

_Atualização_
Acabei de adicionar o tempo final de scan, será exibida logo após as portas analizadas serem exibidas

