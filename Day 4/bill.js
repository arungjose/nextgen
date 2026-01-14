var billAmount = Number(prompt("Enter the bill amount   :   "))
let newAmount = billAmount

if (billAmount < 1000) {
    document.writeln("No Discount!<br>")
    document.writeln(newAmount)
    document.writeln("<br>Buy for ", 1000 - newAmount, " for a discount")
}
else if (billAmount >= 1000 && billAmount < 3000) {
    document.writeln("Avail Discount: 5%<br>")
    newAmount = billAmount - (billAmount * 0.05)
    document.writeln(newAmount)
}
else if (billAmount >= 3000 && billAmount < 6000) {
    document.writeln("Avail Discount: 10%<br>")
    newAmount = billAmount - (billAmount * 0.1)
    document.writeln(newAmount)
}
else {
    document.writeln("Avail Discount: 15%<br>")
    newAmount = billAmount - (billAmount * 0.15)
    document.writeln(newAmount)
    console.log('Dinnooo SHooooperrr!!')
}