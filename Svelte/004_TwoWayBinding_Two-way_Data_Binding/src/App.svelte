<script>
  let text = '';
  let number = 5;
  let checked = false;
  let selected = 'option1';
  let group = [];

  $: charactersLeft = 100 - text.length;
</script>

<main>
  <h1>Two-way Binding</h1>

  <div class="section">
    <h2>Text Input</h2>
    <input bind:value={text} maxlength="100" placeholder="Type something...">
    <p>You typed: {text}</p>
    <p>Characters left: {charactersLeft}</p>
  </div>

  <div class="section">
    <h2>Number Input</h2>
    <input type="number" bind:value={number}>
    <input type="range" bind:value={number} min="0" max="10">
    <p>Value: {number}</p>
  </div>

  <div class="section">
    <h2>Checkbox</h2>
    <label>
      <input type="checkbox" bind:checked>
      Accept terms ({checked ? 'Yes' : 'No'})
    </label>
  </div>

  <div class="section">
    <h2>Select</h2>
    <select bind:value={selected}>
      <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
      <option value="option3">Option 3</option>
    </select>
    <p>Selected: {selected}</p>
  </div>

  <div class="section">
    <h2>Checkbox Group</h2>
    <label><input type="checkbox" bind:group value="red"> Red</label>
    <label><input type="checkbox" bind:group value="green"> Green</label>
    <label><input type="checkbox" bind:group value="blue"> Blue</label>
    <p>Selected: {group.join(', ')}</p>
  </div>
</main>

<style>
  main { padding: 2rem; }
  .section {
    margin: 2rem 0;
    padding: 1rem;
    background: #f5f5f5;
  }
  input, select {
    margin: 0.5rem;
    padding: 0.5rem;
  }
  label {
    display: block;
    margin: 0.5rem 0;
  }
</style>
