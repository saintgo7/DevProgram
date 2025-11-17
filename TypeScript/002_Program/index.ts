console.log("=== Command Line Arguments ===");

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
