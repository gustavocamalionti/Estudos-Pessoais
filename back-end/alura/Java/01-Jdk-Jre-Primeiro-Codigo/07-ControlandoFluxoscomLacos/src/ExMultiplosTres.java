//Utilize um laço do tipo for para imprimir todos os múltiplos de 3, entre 1 e 100.

public class ExMultiplosTres {
    public static void main(String[] args) {
        for ( int numeroAnalise = 1; numeroAnalise <= 100; numeroAnalise += 1) {
            if (numeroAnalise % 3 == 0) {
                System.out.print(numeroAnalise + " ");
            }
        }
    }
}
