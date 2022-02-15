public class TestaLacos {
    public static void main(String[] args) {
        for ( int multiplicador = 1; multiplicador <=10; multiplicador += 1) {
            for (int contador = 1; contador <= 10; contador += 1) {
                System.out.print(multiplicador + "x" + contador + "=" + multiplicador*contador + " ");
            }
            System.out.println();
        }
    }
}
