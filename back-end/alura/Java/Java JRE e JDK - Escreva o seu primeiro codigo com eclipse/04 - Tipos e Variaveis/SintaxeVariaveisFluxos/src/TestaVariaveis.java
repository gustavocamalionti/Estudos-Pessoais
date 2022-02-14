public class TestaVariaveis {
    public static void main(String[] args) {
        System.out.println("Olá novo teste!");

        //Java é uma linguagem Estaticamente tipada/ Fortemente Tipada.
        //É necessário declarar todas as variáveis que serão usadas

        int idade;
        idade = 37;
        System.out.println(idade);

        idade = 30 + 10;
        System.out.println(idade);

        idade = (7 * 5) + 2;
        System.out.println(idade);

        System.out.println("a idade de Gustavo é de " + idade + " anos.");

        //System.out.println() - Pula linha no final do comando
        //System.out.print() - Não pula linha

        System.out.print("Não Pula Linha");
        System.out.println(idade);
    }
}
