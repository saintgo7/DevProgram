console.log("=== TypeScript Program 086 - Advanced ===");

class DataProcessor<T> {
    private data: T[];

    constructor(data: T[]) {
        this.data = data;
    }

    process(fn: (item: T) => void): void {
        this.data.forEach(fn);
    }

    filter(predicate: (item: T) => boolean): T[] {
        return this.data.filter(predicate);
    }
}

const numbers = new DataProcessor<number>([1, 2, 3, 4, 5]);
numbers.process((n) => console.log(`Number: ${n}`));

const evens = numbers.filter((n) => n % 2 === 0);
console.log(`Even numbers: ${evens}`);
