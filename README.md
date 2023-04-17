# 竜語
## Proposal
1. $Cryptography$: Library for cryptography that supports Japanese-language inputs and outputs. This could be used for applications like secure messaging, file encryption, and digital signatures.

## Lexic
### Tokens
```py
tokens = [
    'PLUS',   #Done
    'MINUS',  #Done
    'TIMES',  #Done
    'DIVIDE', #Done
    'EQUALS', #Done
    'NOTEQUAL',#Done
    'LESS',   #Done
    'GREATER',#Done
    'LPAREN', #Done
    'RPAREN', #Done
    'LBRACE', #Done
    'RBRACE', #Done
    'SEMICOLON', #Done
    'COLON',#Done
    'COMMA',#Done
    'ID', #Done
]+ list(reserved.values())
```
### Reserved 
| Kanji        | Hiragana                 | English |
| ------------ | ------------------------ | ------- |
| プログラム   | ぷろぐらむ               | PROGRAM |
| 整数         | せいすう                 | INT     |
| 浮動小数点数 | ふどうしょうすうてんすう | FLOAT   |
| 文字         | もじ                     | CHAR    |
| 文字列       | もじれつ                 | STRING  |
| もし         | もし                     | IF      |
| ならば       | ならば                   | THEN    |
| 違えば       | ちがえば                 | ELSE    |
| 繰り返す     | くりかえす               | WHILE   |
| プリント     | ぷりんと                 | PRINT   |


## Regular expresions
The only notable mention is the one for the ID  that matches any sequence of one or more characters that are either Katakana, Hiragana, or Kanji.
```py
def t_ID(t):
    r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+'
    t.type = reserved.get(t.value,'ID')  
    return t
```