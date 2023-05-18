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
| left_op | right_op | +      | -     | *     | /     | AND OR NOT | > < <= >= != == | =       |
| ------- | -------- | ------ | ----- | ----- | ----- | ---------- | --------------- | ------- |
| int     | int      | int    | int   | int   | float | ERROR      | boolean         | int     |
| int     | float    | float  | float | float | float | ERROR      | boolean         | float   |
| int     | char     | int    | int   | int   | int   | ERROR      | boolean         | int     |
| int     | boolean  | ERROR  | ERROR | ERROR | ERROR | ERROR      | ERROR           | ERROR   |
| int     | string   | string | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |
| int     | vector   | ERROR  | ERROR | ERROR | ERROR | ERROR      | ERROR           | ERROR   | 
| float   | float    | float  | float | float | float | ERROR      | boolean         | float   |
| float   | char     | string | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |
| float   | boolean  | ERROR  | ERROR | ERROR | ERROR | ERROR      | ERROR           | ERROR   |
| float   | string   | ERROR  | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |
| float   | vector   | ERROR  | ERROR | ERROR | ERROR | ERROR      | ERROR           | ERROR   |
| char    | char     | int    | int   | int   | int   | ERROR      | boolean         | char    |
| char    | boolean  | ERROR  | ERROR | ERROR | ERROR | ERROR      | ERROR           | ERROR   |
| char    | string   | string | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |
| boolean | boolean  | ERROR  | ERROR | ERROR | ERROR | ERROR      | boolean         | boolean |
| string  | string   | string | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |
| vector  | vector   | vector | ERROR | ERROR | ERROR | ERROR      | boolean         | ERROR   |


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
### LEFT THINGS TO DO
In `p_variable_declaration`, I need to add `p_complex_type`
- Recheck my diagrams, missing statemtns and made some changes in the grammar.py in order to be able to perform certain behaviors
- In SymbolTables.pdf check the neural point number 6 to delete directory
- In expression when a variables is declared check if the id exists
- Check variable table with numbers 
- Check counter pointer