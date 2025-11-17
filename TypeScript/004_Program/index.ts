import * as fs from 'fs';
import * as readline from 'readline';

console.log("=== File Writer ===");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter filename: ', (filename) => {
    const lines: string[] = [];

    console.log("Enter text (type 'END' to finish):");

    rl.on('line', (line) => {
        if (line === 'END') {
            fs.writeFileSync(filename.trim(), lines.join('\n'));
            console.log(`\nWrote ${lines.length} lines to ${filename}`);
            rl.close();
        } else {
            lines.push(line);
        }
    });
});
