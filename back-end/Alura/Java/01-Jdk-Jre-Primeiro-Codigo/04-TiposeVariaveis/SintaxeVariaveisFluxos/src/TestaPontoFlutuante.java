public class TestaPontoFlutuante {
    public static void main(String[] args) {
        double salario;
        salario = 1582.34;
        System.out.println("Meu salário é de " + salario);

        double idade = 37;
        System.out.println(idade);

        double divisao = 36.4/2;
        System.out.println("O resultado da divisão é " + divisao);

        // Nessa situação, iremos truncar o resultado (não é um arredondamento);
        int outraDivisao = 5/2 ;
        System.out.println(outraDivisao);

        // Declarei a variável double e passei uma divisão de inteiros na mesma linha de comando.
        // Nesse caso, o Java irá ler primeiro da direita. Armazenará o resultado e depois vinculará com a variável.
        // Portanto, 5 é inteiro, 2 é inteiro. Logo, o resultado será inteiro. 2.0
        double novaTentativa = 5/2;

        System.out.println(novaTentativa);

        // Precisamos informar na divisão que estamos trabalhando com números do tipo double
        double segundaTentativa = 5.0/2;
        System.out.println(segundaTentativa);

    }
}
