<script>
  let count = 0;
  let name = 'world';

  // Reactive declaration - runs when dependencies change
  $: doubled = count * 2;
  $: quadrupled = doubled * 2;
  $: greeting = `Hello ${name}!`;

  // Reactive statement
  $: if (count >= 10) {
    alert('Count is getting high!');
    count = 0;
  }

  function increment() {
    count += 1;
  }
</script>

<main>
  <h1>Reactive Declarations</h1>

  <p>Count: {count}</p>
  <p>Doubled: {doubled}</p>
  <p>Quadrupled: {quadrupled}</p>

  <button on:click={increment}>Increment</button>

  <hr>

  <input bind:value={name} placeholder="Enter your name">
  <p>{greeting}</p>
</main>

<style>
  main { padding: 2rem; }
  button {
    padding: 0.5rem 1rem;
    background: #ff3e00;
    color: white;
    border: none;
    cursor: pointer;
  }
  input {
    padding: 0.5rem;
    margin: 0.5rem 0;
    width: 200px;
  }
</style>
