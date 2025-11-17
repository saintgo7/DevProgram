console.log("=== TypeScript Program 012 ===");
console.log("Node.js utility");

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter input: ', (input: string) => {
    console.log(`You entered: ${input}`);
    rl.close();
});
