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
## Reserved 
| Kanji        | Hiragana                 | English  |
| ------------ | ------------------------ | -------- |
| 関数         | かんすう                 | FUNCTION |
| 整数         | せいすう                 | INT      |
| 浮動小数点数 | ふどうしょうすうてんすう | FLOAT    |
| 文字         | もじ                     | CHAR     |
| 文字列       | もじれつ                 | STRING   |
| 違えば       | ちがえば                 | ELSE     |
| 繰り返す     | くりかえす               | WHILE    |
| もし         | もし                     | IF       |
| ならば       | ならば                   | THEN     |
| ブーリアン   | ぶうりあん               | BOOLEAN  |
| トゥルー     | とうるう                 | TRUE     |
| フォルス     | ふぉるす                 | FALSE    |
| メイン       | めいん                   | MAIN     |
| プリント     | ぷりんと                 | PRINT    |
| プログラム   | ぷろぐらむ               | PROGRAM  |
| リターン     | りたあん                 | RETURN   |

## Semantic Table
| left_op | right_op | +   | -   | /     | >       | <       | AND     | OR      | !=      | 
| ------- | -------- | --- | --- | ----- | ------- | ------- | ------- | ------- | ------- |
| int     | int      | int | int | flaot | boolean | boolean | boolean | boolean | Boolean |
| int     | float    |     |     |       |         |         |         |         |         |
| int     | char     |     |     |       |         |         |         |         |         |
| int     | boolean  |     |     |       |         |         |         |         |         |
| int     | string   |     |     |       |         |         |         |         |         |
| int     | array    |     |     |       |         |         |         |         |         |
## First commit
The only notable mention is the one for the ID  that matches any sequence of one or more characters that are either Katakana, Hiragana, or Kanji.
```py
def t_ID(t):
    r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+'
    t.type = reserved.get(t.value,'ID')  
    return t
```
For now it has structure very similar to our previous program littleduck20 these first progress I focus in the lexer

## Second commit 
A lot of thing first gotta make sure the parse does the job before star creating more parsing blockk laso I should chec that ID aldso get alphanumeric values
## Third commt
Well I changed the regular expression of ID to a mix of Japanese and English words, made a lot of progress in the parse currently working with the list statements
## Fourth commit
### LEFT THINGS TO DO
- In p_variable_declaration I need to add the complex type and as well teh recursion check diagrams given in class
- In p_factor add call