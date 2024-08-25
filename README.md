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
