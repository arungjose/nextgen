document.writeln("<h1>One to Hundred</h1>")
for (let i = 1; i <= 100; i++) {
    document.writeln(`<h1>${i}</h1>`)
}
document.writeln("<h1>Hundred to One</h1>")
for (let i = 100; i > 0; i--) {
    document.writeln(`<h1>${i}</h1>`)
}
document.writeln("<h1>One to hundred - Even Only</h1>")
for (let i = 1; i <= 100; i++) {
    if (i % 2 == 0) {
        document.writeln(`<h1>${i}</h1>`)
    }

}
document.writeln("<h1>Multiples of 4 and 5</h1>")
for (let i = 0; i <= 100; i = i + 2) {
    if (i % 4 == 0 && i % 5 == 0) {
        continue
    }
    else {
        document.writeln(`<h1>${i}</h1>`)
    }

}