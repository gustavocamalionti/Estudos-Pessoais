public class TestaEscopo {
    public static void main(String[] args) {
        System.out.println("Testando Condicionais!");
        int idade = 18;
        int quantidadePessoas = 1;


        if (quantidadePessoas > 1) {
            //Ainda não existe
            //Nem nessa linha
            //Não existe, para de insistir!
            boolean acompanhado = true;
            //Existe
            //Ela existe

        } else { //Variavel boolean morreu :(
            //Ainda não existe
            //Nem nessa linha
            //Não existe, para de insistir!
            boolean acompanhado = false;
            //Existe
            //Ela existe

        } //Variavel morreu :(
    }
}
        //O erro é proposital, já que a variável "acompanhado" morre quando criada dentro das condições
        //System.out.println("Valor de Acompanhado = " + acompanhado);
