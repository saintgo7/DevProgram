<script>
  import { count, time, doubled } from './stores.js';

  function increment() {
    count.update(n => n + 1);
  }

  function decrement() {
    count.update(n => n - 1);
  }

  function reset() {
    count.set(0);
  }
</script>

<main>
  <h1>Svelte Stores</h1>

  <div class="section">
    <h2>Writable Store</h2>
    <p>Count: {$count}</p>
    <p>Doubled: {$doubled}</p>
    <button on:click={increment}>+</button>
    <button on:click={decrement}>-</button>
    <button on:click={reset}>Reset</button>
  </div>

  <div class="section">
    <h2>Readable Store</h2>
    <p>Current time: {$time.toLocaleTimeString()}</p>
  </div>
</main>

<style>
  main { padding: 2rem; }
  .section {
    margin: 2rem 0;
    padding: 1rem;
    background: #f5f5f5;
  }
  button {
    margin: 0.25rem;
    padding: 0.5rem 1rem;
    background: #ff3e00;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>
