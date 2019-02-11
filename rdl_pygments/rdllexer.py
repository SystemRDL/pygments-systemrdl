from pygments import lexer
from pygments import token
from pygments.lexers.perl import PerlLexer

class SystemRDLLexer(lexer.RegexLexer):
    name = 'SystemRDL'
    aliases = ['systemrdl']
    filenames = ['*.rdl']

    tokens = {

        'root': [
            lexer.include('comments'),
            lexer.include('perl'),
            lexer.include('prop-assign'),
            lexer.include('comp-def'),

            (lexer.words((
                'addrmap', 'regfile', 'reg', 'field', 'enum', 'struct',
                'constraint', 'signal', 'mem'
            ), suffix=r'\b'), token.Keyword),

            (lexer.words((
                'external', 'abstract', 'alias', 'unsigned'
            ), suffix=r'\b'), token.Keyword),
            
            (lexer.words((
                'bit', 'boolean', 'onreadtype', 'onwritetype', 'string',
                'accesstype', 'addressingtype', 'component', 
            ), suffix=r'\b'), token.Keyword.Type),

            lexer.include('literals'),
            (r'[{}()\[\],.;\']', token.Punctuation),
            (r'[~!%^&*+-=|?:<>/-@]', token.Operator),
            (r'[a-zA-Z][\w]*', token.Name),
            (r'\s', token.Text)
        ],

        'comments': [
            (r'(?s)/\*.*\*/', token.Comment.Multiline),
            (r'//.*?$', token.Comment.Single),
        ],

        'perl': [
            (r'(?s)(<%=?)(.+?)(%>)', lexer.bygroups(token.Name.Tag, lexer.using(PerlLexer), token.Name.Tag)),
        ],

        'literals': [
            (r'([0-9]+)?(\'h)[0-9a-fA-F_]+', token.Number.Hex),
            (r'([0-9]+)?(\'b)[01_]+', token.Number.Bin),
            (r'([0-9]+)?(\'d)[0-9_]+', token.Number.Integer),
            (r'([0-9]+)?(\'o)[0-7_]+', token.Number.Oct),
            (r'0[xX][0-9a-fA-F_]+', token.Number.Hex),
            (lexer.words(('true', 'false'), suffix=r'\b'), token.Literal),
            (r'\d+', token.Number.Integer),
            (r'"', token.String, 'string'),
        ],
        'string': [
            (r'"', token.String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', token.String.Escape),
            (r'[^\\"\n]+', token.String),  # all other characters
            (r'\\\n', token.String),  # line continuation
            (r'\\', token.String),  # stray backslash
        ],

        'prop-assign': [
            #(r'(\w+)\s*(;)', lexer.bygroups(token.Name.Attribute, token.Operator)),
            (r'(\w+)(\s*)(=)', lexer.bygroups(token.Name.Attribute, token.Text, token.Operator)),
            (r'(->)(\s*)(\w+)(\s*)(=)', lexer.bygroups(
                token.Operator, token.Text, token.Name.Attribute, token.Text, token.Operator
            )),
        ],

        'comp-def': [
            (r'(addrmap|regfile|reg|field|mem|signal)(\s+)([a-zA-Z][\w]*)', lexer.bygroups(token.Keyword, token.Text, token.Name.Class))
        ],
    }
