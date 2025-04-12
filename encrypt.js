function caesarCipher(str, shift) {
  return str.split('').map(char => {
    const code = char.charCodeAt(0);

    if (code >= 65 && code <= 90) {
      return String.fromCharCode(((code - 65 + shift) % 26) + 65);
    }
    else if (code >= 97 && code <= 122) {
      return String.fromCharCode(((code - 97 + shift) % 26) + 97);
    }
    return char;
  }).join('');
}

function encrypt() {
  const message = document.getElementById('message').value;
  const shift = parseInt(document.getElementById('shift').value);
  const encrypted = caesarCipher(message, shift);
  document.getElementById('result').innerText = encrypted;
}

function decrypt() {
  const message = document.getElementById('message').value;
  const shift = parseInt(document.getElementById('shift').value);
  const decrypted = caesarCipher(message, 26 - shift);
  document.getElementById('result').innerText = decrypted;
}

