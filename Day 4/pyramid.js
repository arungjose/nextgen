let rows = 10
for (let i = 0; i < rows; i++) {
    let output = '';
    for (let j = 0; j < rows - i - 1; j++) {
        output += ' ';
    }
    for (let k = 0; k < 2 * i + 1; k++) {
        output += '*';
    }
    console.log(output)
}