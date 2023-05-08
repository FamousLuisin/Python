- Objeto: é algo que encapsula;
    * dados;
        * variaveis;
        * atributos;
    * codigos;
        * funções;
        * metodos;

- Classe: Define os elementos de um conjunto de objetos;
    * quais metdos;
    * quais atributos;
    * fabrica de objetos(cria instancias de um objeto);

- Abstração: 
    * Coisas do mundo real >> mundo virtual;


- OBS: Quando se define a classe a Variavel da classe ja abre um lugar na memoria para ser armazenada;

- Heranaças: 
    * Mecanismo para evitar duplicação;
    * Promove o reuso do codigo;
    * Relaçao "é um" ex: Pato(subclasse) é uma ave(superclasse);
    * Sair de ums superclasse para subclasse: Especialização;
    * Sair de uma subclasse para superclasse: Generalização;
    * Quando suar?
        - Para organizar abstrações;
        - acrescentar um novo comportamento (metodo ou atributo);
        - alterar comportamentos;

- OBS: Tem como fazer Troca de mensagens/chamada de metodos;

- Arquitetura de software: Principais elementos que compoe um software e os inter-relacionamentos entre eles.

- Modelagem: Representação simplificadade alguma coisa, eliminando caracteristicas consideras
menos importantes(abstrair/simplificar);

- UML:
    * Visualização;
    * especificações;
    * documentação;
    * contrução;
    * como é:
        + retangulo = classe;
        + linha = ligação entre classes;
        + tringulo = superclasse e subclasse;
        + losangulo = agregação;
        + losangulo cheio = composição;


- Diferença entre python e Java:
    * Java é uma linguagem de forte tipagem;
    * Java vc tem que definir todos os atributos, diferente de python que pode adcionar com o tempo novos atributos;

- Coleções:
    * é a organizaçõa de objetos em coleções;
    * vector e ArrayList;
    * forma de manipular grandes grupos de objetos;

- Classes abstradas:
    * Indica que um tipo de objeto vai possuir um determinado método;
    * mas ela nn define esse metodo, só sua assinatura;

- Interface:
    * Classe puramente abstrada;
    * Conjunto de operações que outras classes irão implementar;
    * Conjunto de assinaturas;
    * class Cx implements InterfaceY;

- Polimorfismo:
    * Multiplas formas;
    * Um dos principios fundamentais da OO;
    * ajuda na organização;
    * evita codigo repetidos ifs e switch;
    * 3 tipos:
        - parametrico(programação generica/generics);   
            >  ArrayList <String> amigos = new ArrayList<>();   
            >  ArrayList <Int> numeros = new ArrayList<>();
        - sobrecarga de metodos (overloading):
            > 2 ou mais metodos com o mesmo nome;
            > O que muda entre eles é a assinatura de metodo(os tipos, um recebe int e o outro float);
            > int multiplica(int x, int y);
            > float multiplica(float x, float y);
        - sobreescrita de metodos (overrinding);
            > Herança / subtipos;
            > Metodos da classe filha possui mesma assinatura do metodo da classe mae;
            > Classe mãe M:
                > classe filhas F1, F2, F3;
                > todas com metodo 'aaaaa';
                > F1, F2, F3 possuem versões polimorficas do metodo 'aaaaa';

- Excessoes:
    * Separar o codigo normal, do codigo de excessoes/erros;
    * Isso torna o programa mais limpo e mais rapido;
    * A memoria cache usa seu desempenho no codigo normal e não nas excessoes;
    * Podemos definir nossas proprias excessoes (subclasse de Exception);
    * lançar uma nova excessao;

- I/O Stream:
    * Stream = fluxo continuo;
    * i/o = entrada e saida de dados;
    * forma padrao e uniforme de tratar (TODAS) entrada e saida de dados;
    * Entrada:
        - arquivo, rede, teclado, array;
    * saida:
        - Arquivo, rede, impressora, array, tela;
    * Entrada e saida padrao:
        - InputStream: System.in
        - PrintStream: System.out
        - PrintStream: System.err

- Padroes de projeto de software:
    * Desing patters;
    * Cada padrao descreve um problema que ocorre repetidas vezez de novo e de novo em nosso ambiente, e então descreve a parte central da soluçao para aquele problema de uma forma que vc possa usar essa soluçao inumeras vezes, sem nunca implementa-la duas evzes da mesma forma;
    * Catalogo de soluções:
        > Um padrão encerra o conhecimento de uma pessoa muito experiente em um determinado assunto de uma forma que este conhecimento possa ser transmitido para outras pessoas com menos conhecimento;
        > Leitura: GoF;
    * Cada padrao é uma "coleção de classes" e suas relações, que em uma palavra ja define todo esse codigo;
    * Todo padrão inclui:
        > nome;
        > problema abordado;
        > Solução;
        > Conseguencias / forças de usar o padrão; 
            >> Pode melhorar algumas partes e piorar outras;

    ### PADRÃO DE ESTRATEGIA ###

    * Objetivo: definir uma categoria de algoritmos, encapsular cada um em uma classe e torna-los intercambiaveis. Estrategia permite que o algoritmo varie, independente dos clientes que o utilize;

    * Formar de extrair da classe algo que pode mudar;

    * Uso conhecido: verificação ortografica multilingue, separação silabica, sistemas adaptativos, algoritmos de ordenação, conectores de bancos de dados;