import { writable, readable, derived } from 'svelte/store';

// Writable store
export const count = writable(0);

// Readable store (with initial value and start function)
export const time = readable(new Date(), function start(set) {
  const interval = setInterval(() => {
    set(new Date());
  }, 1000);

  return function stop() {
    clearInterval(interval);
  };
});

// Derived store
export const doubled = derived(count, $count => $count * 2);
