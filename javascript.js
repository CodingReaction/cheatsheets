/********* Types *************/
number | string | boolean | BigInt // primitive values
Symbol | null | undefined

Array | Function | Map | RegExp | Set | Date <---- Object <--- object // object types

typeof name == "string" // true // works with primitives  + 'function' | 'object'
[] instanceof Array // true
33 instanceof Number // false, primitives aren't instances of classes

Number('123') | Boolean(0) | String(123) // casting

/************ Dates: TODO ********************/

/***************** DOM MANIPULATION *********/
classList
getAttribute()
setAttribute()
appendChild()
append()
prepend()
removeChild()
remove()
createElement()
innerText
textContent
innerHTML
value
parentElement
children
nextElementSibling
previousElementSibling
style // works for setting, for getting only gets 'inline styles'

getComputedStyle()



/**************** Storage: Browser APIs ***************/

