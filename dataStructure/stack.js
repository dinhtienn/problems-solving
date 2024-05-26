class Stack {
  constructor() {
    this.items = [];
  }

  add(item) {
    this.items.unshift(item);
  }

  remove() {
    return this.items.shift();
  }

  peek() {
    return this.items[0];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  getStack() {
    return this.items;
  }
}
