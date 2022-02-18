public class TesteReferencia {
    public static void main(String[] args) {
        Conta primeiraConta = new Conta();
        primeiraConta.saldo = 300;

        System.out.println("Saldo da primeira conta: " + primeiraConta.saldo);

        Conta segundaConta = primeiraConta; //Não tem objeto conta, tem uma "flexinha", uma referência.
        System.out.println(segundaConta); //Resultado Conta@7cca494b ou similar é como se fosse um id de referência
        System.out.println(primeiraConta);
        System.out.println("Saldo da segunda conta: " + segundaConta.saldo); // Duas referências para o mesmo objeto.

        segundaConta.saldo += 100;

        System.out.println("Saldo da segunda conta após soma: " + segundaConta.saldo);
        System.out.println("Saldo da primeira conta após soma: " + primeiraConta.saldo);

        if(primeiraConta == segundaConta) {
            System.out.println("São a mesmíssima conta");
        } else {
            System.out.println("Contas Diferentes");
        }
    }
}
