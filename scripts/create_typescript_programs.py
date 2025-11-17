#!/usr/bin/env python3
"""
Create 100 TypeScript/JavaScript programs
"""

import os
import json

base_dir = "/home/user/DevProgram/TypeScript"

# TypeScript program templates
ts_programs = {
    1: ("Hello World", "Simple hello world program", """console.log("=== Hello World ===");
console.log("Welcome to TypeScript programming!");
"""),

    2: ("Command Line Args", "Process command line arguments", """console.log("=== Command Line Arguments ===");

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("Usage: node program.js <arg1> <arg2> ...");
    process.exit(1);
}

console.log(`Program: ${process.argv[1]}`);
console.log(`Arguments: ${args.length}`);

args.forEach((arg, index) => {
    console.log(`  Arg ${index + 1}: ${arg}`);
});
"""),

    3: ("File Reader", "Read and display file contents", """import * as fs from 'fs';
import * as readline from 'readline';

async function readFile(filename: string): Promise<void> {
    try {
        const fileStream = fs.createReadStream(filename);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        console.log("\\nFile contents:");
        console.log("---");

        let lineNum = 1;
        for await (const line of rl) {
            console.log(`${lineNum.toString().padStart(3)} | ${line}`);
            lineNum++;
        }

        console.log(`\\nTotal lines: ${lineNum - 1}`);
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
"""),

    4: ("File Writer", "Write text to a file", """import * as fs from 'fs';
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
            fs.writeFileSync(filename.trim(), lines.join('\\n'));
            console.log(`\\nWrote ${lines.length} lines to ${filename}`);
            rl.close();
        } else {
            lines.push(line);
        }
    });
});
"""),

    5: ("HTTP Server", "Simple HTTP server", """import * as http from 'http';

const PORT = 3000;

const server = http.createServer((req, res) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from TypeScript HTTP Server!\\n');
});

server.listen(PORT, () => {
    console.log("=== HTTP Server ===");
    console.log(`Server running at http://localhost:${PORT}/`);
    console.log("Press Ctrl+C to stop");
});
"""),
}

# Generate remaining programs
for i in range(6, 101):
    if i <= 20:
        template = f"""console.log("=== TypeScript Program {i:03d} ===");
console.log("Node.js utility");

const readline = require('readline');

const rl = readline.createInterface({{
    input: process.stdin,
    output: process.stdout
}});

rl.question('Enter input: ', (input: string) => {{
    console.log(`You entered: ${{input}}`);
    rl.close();
}});
"""
    elif i <= 40:
        template = f"""import * as http from 'http';

console.log("=== TypeScript Program {i:03d} - Web Server ===");

const server = http.createServer((req, res) => {{
    res.writeHead(200, {{ 'Content-Type': 'application/json' }});
    res.end(JSON.stringify({{
        message: 'Hello from TypeScript',
        timestamp: new Date().toISOString()
    }}));
}});

const PORT = 300{i % 10};
server.listen(PORT, () => {{
    console.log(`Server listening on port ${{PORT}}`);
}});
"""
    elif i <= 60:
        template = f"""interface Data {{
    id: number;
    name: string;
    value: number;
}}

console.log("=== TypeScript Program {i:03d} - Types ===");

const data: Data[] = [
    {{ id: 1, name: "Item 1", value: 100 }},
    {{ id: 2, name: "Item 2", value: 200 }},
    {{ id: 3, name: "Item 3", value: 150 }}
];

console.log("Data:", JSON.stringify(data, null, 2));

const sum = data.reduce((acc, item) => acc + item.value, 0);
console.log(`Total value: ${{sum}}`);
"""
    elif i <= 80:
        template = f"""console.log("=== TypeScript Program {i:03d} - Async ===");

async function fetchData(): Promise<string> {{
    return new Promise((resolve) => {{
        setTimeout(() => {{
            resolve("Data fetched successfully");
        }}, 1000);
    }});
}}

async function main() {{
    console.log("Fetching data...");
    const result = await fetchData();
    console.log(result);
}}

main().catch(console.error);
"""
    else:
        template = f"""console.log("=== TypeScript Program {i:03d} - Advanced ===");

class DataProcessor<T> {{
    private data: T[];

    constructor(data: T[]) {{
        this.data = data;
    }}

    process(fn: (item: T) => void): void {{
        this.data.forEach(fn);
    }}

    filter(predicate: (item: T) => boolean): T[] {{
        return this.data.filter(predicate);
    }}
}}

const numbers = new DataProcessor<number>([1, 2, 3, 4, 5]);
numbers.process((n) => console.log(`Number: ${{n}}`));

const evens = numbers.filter((n) => n % 2 === 0);
console.log(`Even numbers: ${{evens}}`);
"""

    ts_programs[i] = (f"Program {i}", f"TypeScript program {i}", template)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in ts_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write index.ts
    with open(f"{program_dir}/index.ts", 'w') as f:
        f.write(code)

    # Create package.json
    package_json = {
        "name": f"program-{num:03d}",
        "version": "1.0.0",
        "description": desc,
        "main": "index.js",
        "scripts": {
            "build": "tsc",
            "start": "node index.js",
            "dev": "ts-node index.ts"
        },
        "keywords": ["typescript", "node"],
        "author": "",
        "license": "MIT",
        "devDependencies": {
            "@types/node": "^20.0.0",
            "typescript": "^5.0.0",
            "ts-node": "^10.9.0"
        }
    }

    with open(f"{program_dir}/package.json", 'w') as f:
        json.dump(package_json, f, indent=2)

    # Create tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "ES2020",
            "module": "commonjs",
            "outDir": "./dist",
            "rootDir": "./",
            "strict": True,
            "esModuleInterop": True,
            "skipLibCheck": True,
            "forceConsistentCasingInFileNames": True
        }
    }

    with open(f"{program_dir}/tsconfig.json", 'w') as f:
        json.dump(tsconfig, f, indent=2)

    print(f"Created: {num:03d} - {title}")

print(f"\\nCreated {len(ts_programs)} TypeScript programs in {base_dir}")
