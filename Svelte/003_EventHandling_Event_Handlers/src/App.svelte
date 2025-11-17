<script>
  let message = '';
  let x = 0;
  let y = 0;

  function handleClick() {
    message = 'Button clicked!';
  }

  function handleMousemove(event) {
    x = event.clientX;
    y = event.clientY;
  }

  function handleKeydown(event) {
    message = `Key pressed: ${event.key}`;
  }
</script>

<svelte:window on:keydown={handleKeydown} />

<main on:mousemove={handleMousemove}>
  <h1>Event Handling</h1>

  <button on:click={handleClick}>
    Click Me
  </button>

  <button on:click={() => message = 'Inline handler!'}>
    Inline Click
  </button>

  <button on:click|once={handleClick}>
    Click Once (Event Modifier)
  </button>

  {#if message}
    <p class="message">{message}</p>
  {/if}

  <p>Mouse position: {x} x {y}</p>
</main>

<style>
  main {
    padding: 2rem;
    min-height: 300px;
  }
  button {
    margin: 0.5rem;
    padding: 0.5rem 1rem;
    background: #ff3e00;
    color: white;
    border: none;
    cursor: pointer;
  }
  .message {
    background: #f0f0f0;
    padding: 1rem;
    margin-top: 1rem;
  }
</style>
