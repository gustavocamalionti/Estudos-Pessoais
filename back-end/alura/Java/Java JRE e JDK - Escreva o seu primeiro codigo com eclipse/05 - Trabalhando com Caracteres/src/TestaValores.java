public class TestaValores {
    public static void main(String[] args) { //psvm
        System.out.println("Teste"); //sout

        int primeiro = 5;
        int segundo = 7;
        segundo = primeiro;
        primeiro = 10;

        //Variáveis em Java guarda valores e não referência
        //quanto vale o segundo?
        //5
        System.out.println(segundo);
    }
}