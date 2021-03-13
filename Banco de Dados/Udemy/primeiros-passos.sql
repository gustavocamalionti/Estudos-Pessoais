/* Documento de Requísitos de Softwares - UNIDADOS.
O cliente Tera Coércio de Produtos S.A solicitou a montagem de um banco de dados para cadasdtro dos seus clientes. 
A função da Unidados é a análise dos requisitos junto aos usuários para a correta construção do produto. O cliente
deseja que inicialmente os scripts sejam construidos para o Banco de Dados MySQL, porém, posteiormente pode haver mudança
no ambiente e conseuqnetemente adaptação dos scripts para outros produtos de SGBD(Sistema de gerenciamento de banco de dados).

O cliente não quer nenhuma informação relativa á vendas ou estoque, desejando somente as informações primárias de Clientes. */

/* - Modelagem Básica - 
ENTIDADE = TABELA
CAMPOS = ATRIBUTOS*/

CLIENTE

NOME - CARACTER(30)
CPF - NUMÉRICO(11)
EMAIL - CARACTER(30)
TELEFONE - CARACTER(30)
ENDEREÇO - CARACTER(100)
SEXO - CARACTER(1)

/* PROCESSOS DE MODELAGEM */

/* FASE 01 E FASE 02 É FEITO PELO AD(ADMINISTRADOR DE DADOS) */
MODELAGEM CONCEITUAL - RASCUNHO
MODELAGEM LÓGICA - QUALQUER PROGRAMA DE MODELAGEM (BRMODELO)

/*FASE 03 - É FEITO PELO DBA/AD */
MODELAGEM FÍSICA - SCRIPTS DE BANCO



