public class TestaConversao {
    public static void main(String[] args) {
        double salario = 1270.50;

        //Tudo que estiver na minha frente (int), irá se encaixar como int.
        //Type Casting - fazer a conversão sem ser da maneira automática.
        int valor = (int) salario;
        System.out.println(valor);

        //Tipos de Variáveis
        int x = 20000000;
        float pontoFlutuante = 3.14f;
        long numeroGrande = 524094590252409524l;
        short valorPequeno = 2131;
        byte b = 127;

        double valor1 = 0.2;
        double valor2 = 0.1;
        double total = valor1 + valor2;
        System.out.println(total);

        //Aplicando a Conversão

        double idade = 20.5+10;
        System.out.println("A idade de Marcos é de " + (int) idade + " Anos!");
    }
}
