import * as http from 'http';

const PORT = 3000;

const server = http.createServer((req, res) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);

    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello from TypeScript HTTP Server!\n');
});

server.listen(PORT, () => {
    console.log("=== HTTP Server ===");
    console.log(`Server running at http://localhost:${PORT}/`);
    console.log("Press Ctrl+C to stop");
});
