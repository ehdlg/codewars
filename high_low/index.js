/**
 * In this little assignment you are given a string of space separated numbers,
 *  and have to return the highest and lowest number.
 */

function highAndLow(numbers) {
  const arrNumbers = numbers.split(' ');

  let max = (min = arrNumbers[0]);

  for (let i = 1; i < arrNumbers.length; i++) {
    const number = Number(arrNumbers[i]);
    if (number > max) max = number;

    if (number < min) min = number;
  }

  return `${max} ${min}`;
}

console.log(highAndLow('12 23 43 -2 234'));
