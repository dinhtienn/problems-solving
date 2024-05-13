// Add two large number without bigInt in Javascript

function add(a, b) {
  let result = '';
  let len;
  let lenA = a.length;
  let lenB = b.length;
  let a1,
    b1,
    rem,
    div = 0;
  if (lenA > lenB) len = lenA;
  else len = lenB;

  for (let i = 0; i < len; i++) {
    if (i >= lenA) a1 = 0;
    else a1 = parseInt(a[lenA - i - 1]);

    if (i >= lenB) b1 = 0;
    else b1 = parseInt(b[lenB - i - 1]);

    rem = (a1 + b1 + div) % 10;
    div = Math.floor((a1 + b1 + div) / 10);
    result = rem + result;
  }

  if (div > 0) {
    result = div + result;
  }

  return result;
}

console.log(add('1000000000000000000000', '2000000000000000000000'));
