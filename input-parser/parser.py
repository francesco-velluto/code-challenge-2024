import ply.lex as lex

tokens = (
   'NUMBER',
   'LETTER'
)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_LETTER(t):
    r'[A-Z]'
    return t


def t_ws(self, t):
    r'\ |\t'
    pass

def t_error(self, t):
    r'.'
    print("Character not recognized '%s'", t.value)
    return t
    
def input(self, s):
    self.lexer.input(s)
    
def token(self):
    tok = self.lexer.token()
    if tok is None:
        print("Emitted token 'EOF'")
    else:
        print("Emitted token '%s'", tok.type)
    return tok