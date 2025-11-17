export default function SSGPage({ posts, buildTime }) {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>Static Site Generation (SSG)</h1>
      <p>Built at: {buildTime}</p>
      <h2>Posts:</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

export async function getStaticProps() {
  // This runs at build time
  const posts = [
    { id: 1, title: 'First Post' },
    { id: 2, title: 'Second Post' },
    { id: 3, title: 'Third Post' }
  ];

  return {
    props: {
      posts,
      buildTime: new Date().toISOString()
    },
    revalidate: 60 // ISR: Revalidate every 60 seconds
  };
}
