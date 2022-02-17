import java.sql.SQLOutput;

public class CriaConta {
    public static void main(String[] args){
       Conta primeiraConta = new Conta(); //ele instância um objeto do tipo conta e salva na memória.
        primeiraConta.saldo = 200;
        System.out.println(primeiraConta.saldo);

        primeiraConta.saldo += 100;
        System.out.println(primeiraConta.saldo);

        Conta segundaConta = new Conta();
        segundaConta.saldo += 50;

        System.out.println("A primeira conta tem: R$ " + primeiraConta.saldo);
        System.out.println("A segunda conta tem: R$" + segundaConta.saldo);

        //Ao criar um objeto, (new Conta()), todos os atributos são zerados, ou seja, é atribuido valores default.
        //Boolean = False
        //int = 0
        //long = 0
        //double = 0.0
        //char = 0
        //String = ""
        System.out.println(primeiraConta.numero);


        System.out.println("A agência da primeira conta é: " + primeiraConta.agencia);
        System.out.println("A agência da segunda conta é: " + segundaConta.agencia);

        segundaConta.agencia = 146;
        System.out.println("A agência da segunda conta agora será: " + segundaConta.agencia);

        if(primeiraConta == segundaConta) {
            System.out.println("São a mesmíssima conta");
        } else {
            System.out.println("Contas Diferentes");
        }

        System.out.println(segundaConta);
        System.out.println(primeiraConta);
    }
}

//---------------------------------------Questão 1-----------------------------------------------------
//Como chamamos, em orientação a objetos, as características de uma classe?
//Atributo

//---------------------------------------Definições-----------------------------------------------------
//Uma classe é uma especificação de um tipo, definindo atributos e comportamentos.
//Um objeto é uma instância de uma classe onde podemos definir valores para seus atributos.
//Para criar uma instância precisamos usar a palavra chave new
// primeiraConta e segundaConta são referências. segundaConta -------> Conta
