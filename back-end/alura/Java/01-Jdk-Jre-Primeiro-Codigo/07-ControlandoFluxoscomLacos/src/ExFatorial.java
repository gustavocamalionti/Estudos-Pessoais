//Nesse exercício opcional, o seu desafio é imprimir os fatoriais de 1 a 10!
public class ExFatorial {
    public static void main(String[] args) {
        for (int contador = 10; contador >= 1; contador -= 1) {
            if (contador == 10) {
                System.out.print(contador + "! = " + contador + ".");
            }
            else if (contador == 1) {
                System.out.print(contador + "!");
            }
            else {
                System.out.print(contador + ".");
            }

        }
    }
}
