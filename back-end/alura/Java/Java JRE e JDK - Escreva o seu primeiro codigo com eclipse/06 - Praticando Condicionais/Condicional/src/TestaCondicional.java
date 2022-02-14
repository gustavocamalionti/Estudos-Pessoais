public class TestaCondicional {
    public static void main(String[] args) {
        System.out.println("Testando Condicionais!");
        int idade = 14;
        int quantidadePessoas = 4;

        if (idade >= 18) {
            System.out.println("Você tem mais de 18 anos.");
            System.out.println("Seja bem vindo");
        } else {
            if (quantidadePessoas >= 2) {
                System.out.println("você não tem 18 anos. Mas está "
                        + "acompanhando. Pode entrar!");
            } else {
                System.out.println("Infelizmente você não pode entrar.");
            }
        }
    }
}
