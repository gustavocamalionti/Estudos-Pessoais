public class TestaCaracteres {
    public static void main(String[] args) {

        //char guarda apenas um caracter
        char letra = 'a';
        System.out.println(letra);

        //Pela tabela do UNICODE, irá retornar A para o valor 65
        //Pela tabela do UNICODE, irá retornar B para o valor 66
        char valor = 66;
        System.out.println(valor);

        valor = (char) (valor + 1);
        System.out.println(valor);

        //Função mais usada no java é String

        String palavra = "Alura - cursos online de tecnologia.";
        System.out.println(palavra);

        //Concatenação

        palavra = palavra + 2020;
        System.out.println(palavra);
    }
}
