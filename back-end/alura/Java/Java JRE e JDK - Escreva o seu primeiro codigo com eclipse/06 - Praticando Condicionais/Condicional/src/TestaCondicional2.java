public class TestaCondicional2 {
    public static void main(String[] args) {
        System.out.println("Testando Condicionais!");
        int idade = 18;
        int quantidadePessoas = 1;

        boolean acompanhado;
        if (quantidadePessoas >1) { // outro jeito >>>> boolean acompanhado = quantidadePessoas >=2;
            acompanhado = true;
        } else {
            acompanhado = false;
        }

        System.out.println("Valor de Acompanhado = " + acompanhado);
        //Operador OR(ou) - ||
        //Operador AND(e) - &&
        if (idade >= 18 && acompanhado) { // outro jeito de escrever: (idade >= 18 && acompanhado = true)
            System.out.println("Seja bem vindo");
        } else {
                System.out.println("Infelizmente você não pode entrar.");
        }
    }
}
