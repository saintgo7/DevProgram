interface Data {
    id: number;
    name: string;
    value: number;
}

console.log("=== TypeScript Program 055 - Types ===");

const data: Data[] = [
    { id: 1, name: "Item 1", value: 100 },
    { id: 2, name: "Item 2", value: 200 },
    { id: 3, name: "Item 3", value: 150 }
];

console.log("Data:", JSON.stringify(data, null, 2));

const sum = data.reduce((acc, item) => acc + item.value, 0);
console.log(`Total value: ${sum}`);
