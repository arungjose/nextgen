fee = [75000, 78000, 70000, 80000, 70000]

len = fee.length
let sum = 0

for (let i = 0; i < len; i++) {
    sum = sum + fee[i]
}

document.writeln("Total Sum:    ", sum)


bill = [5000, 8000, 7000, 2000, 1000]

len = bill.length
let m = 0

for (b in bill) {
    m = m + bill[b]
}

document.writeln("<br>Total Sum:    ", m)