import * as http from 'http';

console.log("=== TypeScript Program 040 - Web Server ===");

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
        message: 'Hello from TypeScript',
        timestamp: new Date().toISOString()
    }));
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
