import { useRouter } from 'next/router';

export default function Post({ post }) {
  const router = useRouter();

  if (router.isFallback) {
    return <div>Loading...</div>;
  }

  return (
    <div style={{ padding: '2rem' }}>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
      <button onClick={() => router.push('/')}>Back to Home</button>
    </div>
  );
}

export async function getStaticPaths() {
  const paths = [
    { params: { id: '1' } },
    { params: { id: '2' } },
    { params: { id: '3' } }
  ];

  return { paths, fallback: true };
}

export async function getStaticProps({ params }) {
  const posts = {
    '1': { title: 'First Post', content: 'This is the first post' },
    '2': { title: 'Second Post', content: 'This is the second post' },
    '3': { title: 'Third Post', content: 'This is the third post' }
  };

  return {
    props: {
      post: posts[params.id] || { title: 'Not Found', content: '' }
    }
  };
}
