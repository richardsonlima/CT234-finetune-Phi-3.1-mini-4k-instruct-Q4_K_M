from fpdf import FPDF

# Create PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, txt="30 Questions and Answers Based on PDF Content", ln=True, align="C")

# Add a line break
pdf.ln(10)

# Set font for questions and answers
pdf.set_font("Arial", size=12)

# Content: 30 Questions and Answers
qa_pairs = [
    ("What is mathematical induction?", 
     "Mathematical induction is a proof technique used to prove that a statement holds for all natural numbers by proving it for a base case and then showing that if it holds for an arbitrary case, it also holds for the next case."),
    ("What are the steps of mathematical induction?", 
     "The steps are: 1. Base case: Prove the statement for the smallest value (usually n = 0 or n = 1). 2. Inductive hypothesis: Assume the statement holds for n = k. 3. Inductive step: Prove the statement holds for n = k + 1."),
    ("What is recursion in computer science?", 
     "Recursion is a technique where a function calls itself to solve smaller instances of a problem until reaching a base case."),
    ("What is an example of a recursive algorithm in the document?", 
     "An example is the recursive algorithm for calculating the factorial of a number: n! = n × (n-1)!"),
    ("What is the time complexity of the recursive factorial algorithm?", 
     "The time complexity of the recursive factorial algorithm is Θ(n)."),
    ("What is a stack used for in recursion?", 
     "A stack is used to store the state of each function call, including parameters and return addresses, so that the program can resume correctly after each recursive call."),
    ("What is an iterative version of the factorial algorithm?", 
     "The iterative version uses a loop to calculate the factorial by multiplying a variable by decreasing values of n until n = 0."),
    ("What is the Tower of Hanoi problem?", 
     "The Tower of Hanoi is a classic problem where n disks need to be moved from one peg to another, using a third peg as an auxiliary, without placing a larger disk on a smaller one."),
    ("What is the time complexity of the Tower of Hanoi problem?", 
     "The time complexity is T(n) = 2T(n-1) + a, which grows exponentially as Θ(2^n)."),
    ("What is a recurrence relation?", 
     "A recurrence relation is an equation that describes a function in terms of its values at smaller inputs, often used to express the time complexity of recursive algorithms."),
    ("What is the purpose of a base case in recursion?", 
     "The base case is the simplest instance of the problem that can be solved directly, preventing infinite recursion by providing a termination point."),
    ("What is tail recursion?", 
     "Tail recursion is a special form of recursion where the recursive call is the last operation in the function, allowing for optimizations that reduce stack usage."),
    ("What is dynamic memory allocation?", 
     "Dynamic memory allocation is the process of allocating memory at runtime, often used in recursion when the number of function calls cannot be determined at compile time."),
    ("How can recursion be converted to iteration?", 
     "Recursion can be converted to iteration by using an explicit stack to manage the state that would otherwise be handled by recursive function calls."),
    ("What is the space complexity of recursive algorithms?", 
     "The space complexity is usually O(n), where n is the depth of the recursive calls."),
    ("Why might recursion be more readable than iteration?", 
     "Recursion can be more readable because it often directly mirrors the problem’s structure, making it easier to understand and implement for problems like tree traversal."),
    ("What is a recurrence tree?", 
     "A recurrence tree is a tool used to solve recurrence relations by visualizing how the cost of recursive calls accumulates across the levels of recursion."),
    ("What is an example of an algorithm with exponential time complexity?", 
     "The recursive Fibonacci algorithm has exponential time complexity, specifically Θ(2^n), due to the repeated calculations of the same subproblems."),
    ("What is the iterative version of the Fibonacci algorithm?", 
     "The iterative version calculates Fibonacci numbers using a loop that stores the last two values and computes the next one in the sequence."),
    ("What is the time complexity of the iterative Fibonacci algorithm?", 
     "The time complexity of the iterative Fibonacci algorithm is Θ(n)."),
    ("What is the principle of recursion in algorithm design?", 
     "The principle of recursion in algorithm design is to break a problem into smaller subproblems, solve those recursively, and combine their solutions to solve the original problem."),
    ("What is tail-call optimization?", 
     "Tail-call optimization is an optimization technique where tail-recursive functions are optimized to avoid adding new frames to the stack, effectively turning recursion into iteration."),
    ("What are the two main types of memory allocation in recursion?", 
     "The two main types are static allocation, which occurs at compile time, and dynamic allocation, which occurs at runtime and is managed by the system."),
    ("What is the difference between static and dynamic variables?", 
     "Static variables are allocated at compile time and exist for the lifetime of the program, while dynamic variables are allocated at runtime and are released when no longer needed."),
    ("What is the purpose of an explicit stack in converting recursion to iteration?", 
     "An explicit stack is used to manually simulate the recursive function calls, managing the variables and return addresses that would otherwise be handled by the system’s call stack."),
    ("What is an example of an efficient iterative algorithm?", 
     "An efficient iterative algorithm for finding the factorial of a number uses a loop, reducing both time and space complexity compared to the recursive version."),
    ("What is the space complexity of the Tower of Hanoi algorithm?", 
     "The space complexity of the Tower of Hanoi algorithm is O(n), where n is the number of disks."),
    ("How does the complexity of recursive functions differ from iterative functions?", 
     "Recursive functions may have higher time and space complexity due to the overhead of maintaining the call stack, while iterative functions tend to be more efficient in terms of both."),
    ("What is the difference between top-down and bottom-up approaches in recursion?", 
     "In the top-down approach, recursion solves the problem by breaking it into smaller subproblems, while in the bottom-up approach, iteration builds up the solution from the simplest cases."),
    ("What is an example of a recursive problem involving binary trees?", 
     "A common recursive problem involving binary trees is tree traversal, where the algorithm visits each node of the tree in a specific order, such as in-order, pre-order, or post-order traversal.")
]

# Add each question-answer pair
for i, (question, answer) in enumerate(qa_pairs, start=1):
    pdf.multi_cell(0, 10, f"{i}. {question}\nAnswer: {answer}\n")
    pdf.ln(5)

# Output to a PDF file
output_path = "./30_questions_and_answers.pdf"
pdf.output(output_path)

output_path