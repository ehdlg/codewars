function descendingOrder(n) {
  return Number(
    n
      .toString()
      .split('')
      .sort((a, b) => Number(b) - Number(a))
      .join('')
  );
}

console.log(descendingOrder(2342126945));
