import * as fs from 'fs';
import * as readline from 'readline';

async function readFile(filename: string): Promise<void> {
    try {
        const fileStream = fs.createReadStream(filename);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        console.log("\nFile contents:");
        console.log("---");

        let lineNum = 1;
        for await (const line of rl) {
            console.log(`${lineNum.toString().padStart(3)} | ${line}`);
            lineNum++;
        }

        console.log(`\nTotal lines: ${lineNum - 1}`);
    } catch (error) {
        console.error(`Error: ${error}`);
    }
}

console.log("=== File Reader ===");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter filename: ', (filename) => {
    rl.close();
    readFile(filename.trim());
});
