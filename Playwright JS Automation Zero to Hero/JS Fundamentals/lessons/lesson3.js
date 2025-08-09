//objects

var customer = {
    firstName: "John",
    lastName: "Snow",
}

console.log(customer.firstName)
console.log(customer['lastName'])

customer.firstName = "Mike"
customer['lastName'] = "Tyson"

console.log(customer.firstName)
console.log(customer['lastName'])

//arrays

var car = ["BMW", "Audi", "Mercedes", "Toyota"]
console.log(car[0])
car[1] = "Honda"
console.log(car[1])