export default function SSRPage({ data, timestamp }) {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>Server-Side Rendering (SSR)</h1>
      <p>This page is rendered on each request</p>
      <p><strong>Server Time:</strong> {timestamp}</p>
      <p><strong>Data:</strong> {data}</p>
    </div>
  );
}

export async function getServerSideProps() {
  // This runs on the server for each request
  return {
    props: {
      data: 'Fetched from server',
      timestamp: new Date().toISOString()
    }
  };
}
