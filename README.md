# TestMultiLang
Test language that coverts unified OP codes into different programming languages.

<sub>*VERY WIP, Please don't kill me.*</sub>
## Currently supported languages:
* Python
* Browser JavaScript

## OP Codes✅❌
### Arguments meaning:
```
[] - Multiple arguments of different types are supported
<> - One argument of any type is supported
{} - Supports 1 string argument with quotes
<{}> - Supports 1 string argument without quotes
() - Supports 1 decimal argument
[{}] - Supports multiple string arguments
[()] - Supports multiple decimal arguments
```
OP Code | JS Support | PY Support | Explanation | Usage
--- | --- | --- | --- | ---
`wrt` | ✅ | ✅ | Writes `a` to the console | `wrt [a];`
`var` | ✅ | ✅ | Creates a variable with name `a` and default value `b` | `var <{a}> <b>;`
`arr` | ✅ | ✅ | Creates an array variable with name `a` and length `b` | `arr <{a}> (b);`
`mlt` | ✅ | ✅ | Multiples `a` by `b` and writes the result into `c` | `mlt (a) (b) <{c}>;`
`div` | ✅ | ✅ | Divides `a` by `b` and writes the result into `c` | `div (a) (b) <{c}>;`
`sub` | ✅ | ✅ | Subracts `b` from `a` and writes the result into `c` | `sub (a) (b) <{c}>;`
`add` | ✅ | ✅ | Adds `b` to `a` and writes the result into `c` | `add (a) (b) <{c}>;`
`tce` | ✅ | ✅ | Toggles evaluation of expressions | `tce;`
`nwl` | ✅ | ✅ | Starts next piece of code on the new line | `nwl;`
`sav` | ✅ | ✅ | Sets array `a`'s value at index `b` to the value `c` | `sav <{a}> (b) <c>;`
`idn` | ✅ | ✅ | Sets current line ident to value `a` | `idn (a);`
`gc` | ✅ | ✅ | Gets compiler constant with name `a` and writes to variable `b` | `gc <{a}> <{b}>;`
`fiv` | ✅ | ✅ | Iterates through each element of `a` and calls the `b` function with each key | `fiv <{a}> <{b}>;`
`whl` | ✅ | ✅ | While condition `a` is met, continues the execution  | `whl {a};`
`imp` | ❌ | ✅ | Imports module `a` | `imp <{a}>;`
`imf` | ✅ | ✅ | Imports module(s) `a` from package `b` | `imf [a] <{b}>;`
`ima` | ❌ | ✅ | Imports module `a` as `b` | `ima <{a}> <{b}>;`
`raw` | ✅ | ✅ | Pastes raw code from argument `a` into the file. Not language-universal. | `raw {a};`
`###` | ✅ | ✅ | Adds a comment line into the code with argument `a` as text | `### {a};`
`sfun` | ✅ | ✅ | Creates a function with name `a` and arguments `b` | `sfun <{a}> [b];`
`efun` | ✅ | ✅ | Ends function with a closing character (For JS Support) | `efun;`
`gfun` | ✅ | ✅ | Gets return value of function `a` with arguments `c` and writes it to the variable `b` | `gfun <{a}> <{b}> [c];`
`cfun` | ✅ | ✅ | Calls function `a` with arguments `b` | `cfun <{a}> [b];`
`ret` | ✅ | ✅ | Returns value(s) `a` | `ret [a];`
`if` | ✅ | ✅ | If condition `a` is met, continues execution | `if {a};`
`eif` | ✅ | ✅ | `Else If` operator support | `eif {a};`
`els` | ✅ | ✅ | `Else` operator support | `els;`
`END` | ✅ | ✅ | Marks the end of the .tml script | `END;`
`exfun` | ✅ | ❌ | Works just like `sfun` except it exports the function | `exfun <{a}> [b];`
