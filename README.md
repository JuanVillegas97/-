# 竜語
## Proposal
1. $Cryptography$: Library for cryptography that supports Japanese-language inputs and outputs. This could be used for applications like secure messaging, file encryption, and digital signatures.

## Lexic
### Tokens
| Token| Regular Expression| Example|
| ------------ | ------------------------ | -------- |
| ASSIGN       | r'='                     | x = 5   |
| PLUS         | r'\+'                    | x + y   |
| MINUS        | r'-'                     | x - y   |
| TIMES        | r'\*'                    | x * y   |
| DIVIDE       | r'/'                     | x / y   |
| EQUALS       | r'=='                    | x == y  |
| NOTEQUAL     | r'!='                    | x != y  |
| LESS         | r'<'                     | x < y   |
| GREATER      | r'>'                     | x > y   |
| LPAREN       | r'\('                    | (       |
| RPAREN       | r'\)'                    | )       |
| LBRACE       | r'\{'                    | {       |
| RBRACE       | r'\}'                    | }       |
| LBRACK       | r'\['                    | [       |
| RBRACK       | r'\]'                    | ]       |
| SEMICOLON    | r';'                     | x = 5;  |
| COLON        | r':'                     | dict:   |
| COMMA        | r','                     | x, y    |
| ID           | r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+[a-zA-Z_][a-zA-Z_0-9]*' |Juanですメキシコ人です |
| CTEI         | r'\d+'                   | 123     |
| CTEF         | r'([0-9]+[.])[0-9]+'     | 3.14    |
| CTEB         | r'\s*(true OR false)\s*'    | true    |
| CTES         | r'\".*?\"'               | "Hello" |
| CTEC         | r'\'[^\']\''             | 'c'     |
| AND          | r'&&'                    | x && y  |
| OR           | r'\|\|'                  | x \|\| y|



## Semantic Table
| left_op | right_op | +      | -     | *     | /     | > < AND OR       | !=   ==  |
| ------- | -------- | ------ | ----- | ----- | ----- | ------- | -------- |
| int     | int      | int    | int   | int   | float | boolean | boolean  |
| int     | float    | float  | float | float | float | boolean | boolean  |
| int     | char     | int    | int   | int   | int   | boolean | boolean  |
| int     | boolean  | NaN    | NaN   | NaN   | NaN   | NaN     | NaN      |
| int     | string   | string | NaN   | NaN   | NaN   | boolean | boolean  |
| int     | vector   | NaN    | NaN   | NaN   | NaN   | NaN     | NaN      |
| float   | float    | float  | float | float | float | boolean | boolean  |
| float   | char     | string | NaN   | NaN   | NaN   | boolean | boolean  |
| float   | boolean  | NaN    | NaN   | NaN   | NaN   | NaN     | NaN      |
| float   | string   | NaN    | NaN   | NaN   | NaN   | boolean | boolean  |
| float   | vector   | NaN    | NaN   | NaN   | NaN   | NaN     | NaN      |
| char    | char     | int    | int   | int   | int   | boolean | boolean  |
| char    | boolean  | NaN    | NaN   | NaN   | NaN   | NaN     | NaN      |
| char    | string   | string | NaN   | NaN   | NaN   | boolean | boolean  |
| boolean | boolean  | NaN    | NaN   | NaN   | NaN   | boolean | boolean  |
| string  | string   | string | NaN   | NaN   | NaN   | NaN     | boolean  |
| vector  | vector   | vector | NaN   | NaN   | NaN   | NaN     | boolean  |


## Reserved 
| Kanji        | Hiragana                 | English  |
| ------------ | ------------------------ | -------- |
| プログラム   | ぷろぐらむ               | PROGRAM  |
| メイン       | めいん                   | MAIN     |
| 変数         | へんすう                 | VARIABLE |
| 関数         | かんすう                 | FUNCTION |
| 整数         | せいすう                 | INT      |
| 浮動小数点数 | ふどうしょうすうてんすう | FLOAT    |
| 文字列       | もじれつ                 | STRING   |
| 文字         | もじ                     | CHAR     |
| ブーリアン   | ぶーりあん               | BOOLEAN  |
| トゥルー     | とぅるー                 | TRUE     |
| フォルス     | ふぉるす                 | FALSE    |
| もし         | もし                     | IF       |
| ならば       | ならば                   | THEN     |
| 違えば       | ちがえば                 | ELSE     |
| 繰り返す     | くりかえす               | WHILE    |
| プリント     | ぷりんと                 | PRINT    |
| リターン     | りたーん                 | RETURN   |


```ts
// Function 1: Generate a random key
function generateKey(): string {
  // implementation here
}

// Function 2: Encrypt a message with a key
function encryptMessage(message: string, key: string): string {
  // implementation here
}

// Function 3: Decrypt a message with a key
function decryptMessage(ciphertext: string, key: string): string {
  // implementation here
}

// Function 4: Create a digital signature for a message
function createSignature(message: string, key: string): string {
  // implementation here
}

// Function 5: Verify the digital signature of a message
function verifySignature(message: string, signature: string, key: string): boolean {
  // implementation here
}

// Function 6: Hash a message
function hashMessage(message: string): string {
  // implementation here
}

// Function 7: Generate a random salt
function generateSalt(): string {
  // implementation here
}

// Function 8: Hash a password with a salt
function hashPassword(password: string, salt: string): string {
  // implementation here
}

// Function 9: Verify a password against a hashed password
function verifyPassword(password: string, hashedPassword: string): boolean {
  // implementation here
}

// Function 10: Generate a random initialization vector
function generateIV(): string {
  // implementation here
}

```
## First commit
The only notable mention is the one for the ID  that matches any sequence of one or more characters that are either Katakana, Hiragana, or Kanji.
```py
def t_ID(t):
    r'[\u30A0-\u30FF\u3040-\u309F\u4E00-\u9FFF]+'
    t.type = reserved.get(t.value,'ID')  
    return t
```
For now it has structure very similar to our previous program littleduck20 these first progress I focused in the lexer

## Second commit 
I have a lot of things to do. First, I need to make sure that the parse is working correctly before I start creating more parsing blocks. Also, I should check that the ID can also get alphanumeric values
## Third commt
Well, I changed the regular expression of ID to a mix of Japanese and English words. I've made a lot of progress in the parse and am currently working with the list of statements.
## Fourth commit
I focused in the diagrams in this commit and my proposal so it took me time of no coding
### LEFT THINGS TO DO
In `p_variable_declaration`, I need to add `p_complex_type`
In `p_factor`, I need to add `p_invocation`
I need to change the diagram where body was because I removed `p_body` and instead just used LBRACE `p_statements` RBRACE