from LexicalAnalyzer import LexicalAnalyzer
from SyntaxAnalyzer import SyntaxAnalyzer

Line = input("Enter a line: ")
lexicalAnalyzer = LexicalAnalyzer(Line)
Lexicaltokens = lexicalAnalyzer.analyzeLine()
syntaxAnalyzer = SyntaxAnalyzer(Lexicaltokens)
syntaxAnalyzer.parse()
