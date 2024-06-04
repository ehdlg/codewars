/**
In this kata you are required to, given a string, replace every letter with its 
position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
 */

function alphabetPosition(text) {
  const firstPosition = 'A'.charCodeAt() - 1;
  let positionString = '';

  for (let letter of text) {
    if (!/[A-Za-z]/.test(letter)) continue;

    letter = letter.toUpperCase();

    const position = letter.charCodeAt() - firstPosition;

    positionString += `${position} `;
  }

  return positionString.trim();
}

console.log(alphabetPosition('aswf2234 ../2 aalks.@#dfj2 34.'));
