//O João gostaria de criar um programa sobre Imposto de Renda (IR) e verificou as regras de alíquota. Ele descobriu no site da receita:

//De 1900.0 até 2800.0, o IR é de 7.5% e pode deduzir na declaração o valor de R$ 142
//De 2800.01 até 3751.0, o IR é de 15% e pode deduzir R$ 350
//De 3751.01 até 4664.00, o IR é de 22.5% e pode deduzir R$ 636
//Para começar, o João escreveu o seguinte esboço de classe:

public class Exercicio01Aliquota {
    public static void main(String[] args) {
        double salario = 2200.00;
        double aliquota;
        double salarioDescontoAplicado;
        if (salario>=1900.00 && salario<2800.00) {
            aliquota = 7.5;
            salarioDescontoAplicado = salario - salario*aliquota/100;
            System.out.println("Com uma aliquota de " + aliquota + " aplicada no salário de " + salario + ""
                    + ", receberemos líquido o valor de " + salarioDescontoAplicado);
        } else if (salario >= 2800.00 && salario < 3751.00) {
                aliquota = 15;
                salarioDescontoAplicado = salario - salario*aliquota/100;
                System.out.println("Com uma aliquota de " + aliquota + " aplicada no salário de " + salario + ""
                        + ", receberemos líquido o valor de " + salarioDescontoAplicado);
        } else if (salario >= 3751.00 && salario < 4664.00) {
                aliquota = 22.5;
                salarioDescontoAplicado = salario - salario*aliquota/100;
                System.out.println("Com uma aliquota de " + aliquota + " aplicada no salário de " + salario + ""
                        + ", receberemos líquido o valor de " + salarioDescontoAplicado);
        }
    }
}
