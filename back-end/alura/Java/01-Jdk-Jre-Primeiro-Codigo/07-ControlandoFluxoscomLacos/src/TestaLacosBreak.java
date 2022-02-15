public class TestaLacosBreak {
    public static void main(String[] args) {
        for ( int linha = 0; linha <= 10; linha += 1) {
            for (int coluna = 0; coluna <10; coluna += 1) {
                if ( coluna == linha) {
                    break;
                }
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
