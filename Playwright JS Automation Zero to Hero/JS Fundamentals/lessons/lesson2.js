var price = 80;
var itemname = "table"
var messageToPrint1 = "The price of your "+itemname+ " is "+price+" dollars." //concatenation
var messageToPrint2 = `The price of your ${itemname} is ${price} dollars.` //interpolation
console.log(messageToPrint2)
console.log(messageToPrint1)

