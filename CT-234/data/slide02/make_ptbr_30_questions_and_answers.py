# Translating questions and answers to Brazilian Portuguese

qa_pairs_pt = [
    ("O que é indução matemática?", 
     "A indução matemática é uma técnica de prova usada para provar que uma afirmação é verdadeira para todos os números naturais, provando-a para um caso base e, em seguida, mostrando que se for verdadeira para um caso arbitrário, também será verdadeira para o próximo caso."),
    ("Quais são os passos da indução matemática?", 
     "Os passos são: 1. Caso base: Prove a afirmação para o menor valor (geralmente n = 0 ou n = 1). 2. Hipótese indutiva: Suponha que a afirmação seja verdadeira para n = k. 3. Passo indutivo: Prove que a afirmação é verdadeira para n = k + 1."),
    ("O que é recursão em ciência da computação?", 
     "Recursão é uma técnica onde uma função chama a si mesma para resolver instâncias menores de um problema até atingir um caso base."),
    ("Qual é um exemplo de algoritmo recursivo no documento?", 
     "Um exemplo é o algoritmo recursivo para calcular o fatorial de um número: n! = n × (n-1)!"),
    ("Qual é a complexidade de tempo do algoritmo recursivo de fatorial?", 
     "A complexidade de tempo do algoritmo recursivo de fatorial é O(n)."),
    ("Para que serve uma pilha na recursão?", 
     "Uma pilha é usada para armazenar o estado de cada chamada de função, incluindo parâmetros e endereços de retorno, para que o programa possa retomar corretamente após cada chamada recursiva."),
    ("Qual é a versão iterativa do algoritmo de fatorial?", 
     "A versão iterativa usa um loop para calcular o fatorial multiplicando uma variável pelos valores decrescentes de n até que n seja 0."),
    ("O que é o problema da Torre de Hanói?", 
     "A Torre de Hanói é um problema clássico onde n discos precisam ser movidos de uma estaca para outra, usando uma terceira estaca como auxiliar, sem colocar um disco maior sobre um menor."),
    ("Qual é a complexidade de tempo do problema da Torre de Hanói?", 
     "A complexidade de tempo é T(n) = 2T(n-1) + a, que cresce exponencialmente como O(2^n)."),
    ("O que é uma relação de recorrência?", 
     "Uma relação de recorrência é uma equação que descreve uma função em termos de seus valores para entradas menores, frequentemente usada para expressar a complexidade de tempo de algoritmos recursivos."),
    ("Qual é o propósito de um caso base na recursão?", 
     "O caso base é a instância mais simples do problema que pode ser resolvida diretamente, evitando recursão infinita, fornecendo um ponto de término."),
    ("O que é recursão de cauda?", 
     "A recursão de cauda é uma forma especial de recursão onde a chamada recursiva é a última operação na função, permitindo otimizações que reduzem o uso da pilha."),
    ("O que é alocação dinâmica de memória?", 
     "A alocação dinâmica de memória é o processo de alocação de memória em tempo de execução, muitas vezes usada em recursão quando o número de chamadas de função não pode ser determinado em tempo de compilação."),
    ("Como a recursão pode ser convertida em iteração?", 
     "A recursão pode ser convertida em iteração usando uma pilha explícita para gerenciar o estado que seria tratado pelas chamadas de função recursivas."),
    ("Qual é a complexidade de espaço dos algoritmos recursivos?", 
     "A complexidade de espaço geralmente é O(n), onde n é a profundidade das chamadas recursivas."),
    ("Por que a recursão pode ser mais legível que a iteração?", 
     "A recursão pode ser mais legível porque frequentemente reflete diretamente a estrutura do problema, tornando mais fácil de entender e implementar, como no caso de percorrimento de árvores."),
    ("O que é uma árvore de recorrência?", 
     "Uma árvore de recorrência é uma ferramenta usada para resolver relações de recorrência visualizando como o custo das chamadas recursivas se acumula nos níveis de recursão."),
    ("Qual é um exemplo de um algoritmo com complexidade de tempo exponencial?", 
     "O algoritmo recursivo de Fibonacci tem uma complexidade de tempo exponencial, especificamente O(2^n), devido aos cálculos repetidos dos mesmos subproblemas."),
    ("Qual é a versão iterativa do algoritmo de Fibonacci?", 
     "A versão iterativa calcula os números de Fibonacci usando um loop que armazena os dois últimos valores e calcula o próximo na sequência."),
    ("Qual é a complexidade de tempo da versão iterativa do algoritmo de Fibonacci?", 
     "A complexidade de tempo da versão iterativa do algoritmo de Fibonacci é O(n)."),
    ("Qual é o princípio da recursão no design de algoritmos?", 
     "O princípio da recursão no design de algoritmos é dividir um problema em subproblemas menores, resolvê-los recursivamente e combinar suas soluções para resolver o problema original."),
    ("O que é otimização de chamada de cauda?", 
     "A otimização de chamada de cauda é uma técnica de otimização onde funções recursivas de cauda são otimizadas para evitar a adição de novos frames à pilha, efetivamente transformando a recursão em iteração."),
    ("Quais são os dois principais tipos de alocação de memória na recursão?", 
     "Os dois principais tipos são a alocação estática, que ocorre em tempo de compilação, e a alocação dinâmica, que ocorre em tempo de execução e é gerenciada pelo sistema."),
    ("Qual é a diferença entre variáveis estáticas e dinâmicas?", 
     "As variáveis estáticas são alocadas em tempo de compilação e existem durante a vida útil do programa, enquanto as variáveis dinâmicas são alocadas em tempo de execução e liberadas quando não são mais necessárias."),
    ("Qual é o propósito de uma pilha explícita na conversão de recursão em iteração?", 
     "Uma pilha explícita é usada para simular manualmente as chamadas de função recursivas, gerenciando as variáveis e os endereços de retorno que seriam tratados pela pilha de chamadas do sistema."),
    ("Qual é um exemplo de algoritmo iterativo eficiente?", 
     "Um algoritmo iterativo eficiente para encontrar o fatorial de um número usa um loop, reduzindo tanto a complexidade de tempo quanto de espaço em comparação com a versão recursiva."),
    ("Qual é a complexidade de espaço do algoritmo da Torre de Hanói?", 
     "A complexidade de espaço do algoritmo da Torre de Hanói é O(n), onde n é o número de discos."),
    ("Como a complexidade dos algoritmos recursivos difere dos algoritmos iterativos?", 
     "Algoritmos recursivos podem ter maior complexidade de tempo e espaço devido ao overhead de manter a pilha de chamadas, enquanto algoritmos iterativos tendem a ser mais eficientes em ambos os aspectos."),
    ("Qual é a diferença entre abordagens top-down e bottom-up na recursão?", 
     "Na abordagem top-down, a recursão resolve o problema dividindo-o em subproblemas menores, enquanto na abordagem bottom-up, a iteração constrói a solução a partir dos casos mais simples."),
    ("Qual é um exemplo de problema recursivo envolvendo árvores binárias?", 
     "Um problema recursivo comum envolvendo árvores binárias é a travessia de árvores, onde o algoritmo visita cada nó da árvore em uma ordem específica, como in-order, pre-order ou post-order.")
]

# Create a PDF object for Portuguese version
pdf_pt = FPDF()

# Add a page
pdf_pt.add_page()

# Set title
pdf_pt.set_font("Arial", "B", 16)
pdf_pt.cell(200, 10, txt="30 Perguntas e Respostas Baseadas no Conteúdo PDF", ln=True, align="C")

# Add a line break
pdf_pt.ln(10)

# Set font for questions and answers
pdf_pt.set_font("Arial", size=12)

# Add each question-answer pair
for i, (question, answer) in enumerate(qa_pairs_pt, start=1):
    pdf_pt.multi_cell(0, 10, f"{i}. {question}\nResposta: {answer}\n")
    pdf_pt.ln(5)

# Output to a PDF file
output_path_pt = "/mnt/data/30_perguntas_e_respostas.pdf"
pdf_pt.output(output_path_pt)

output_path_pt
