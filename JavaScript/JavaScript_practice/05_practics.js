function cal() {
  let v1 = Number(document.getElementById('value1').value);
  let v2 = Number(document.getElementById('value2').value);
  let op = document.getElementById('operator').value;
  let result;

  if (op === '+') {
    result = v1 + v2;
  } else if (op === '-') {
    result = v1 - v2;
  } else if (op === '*') {
    result = v1 * v2;
  } else if (op === '/') {
    result = v1 / v2;
  } else {
    result = '오류 발생';
  }
  document.getElementById('result').value = result;
}

function resetInput() {
  document.getElementById('value1').value = '';
  document.getElementById('value2').value = '';
  document.getElementById('operator').value = '';
  document.getElementById('result').value = '';
}