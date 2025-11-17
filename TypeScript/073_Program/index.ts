console.log("=== TypeScript Program 073 - Async ===");

async function fetchData(): Promise<string> {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve("Data fetched successfully");
        }, 1000);
    });
}

async function main() {
    console.log("Fetching data...");
    const result = await fetchData();
    console.log(result);
}

main().catch(console.error);
