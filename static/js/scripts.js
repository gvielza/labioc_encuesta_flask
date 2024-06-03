// scripts.js
function modifyValue(id, delta) {
    const input = document.getElementById(id);
    let value = parseInt(input.value, 10);
    value = isNaN(value) ? 0 : value;
    value += delta;
    value = value < 0 ? 0 : value;
    input.value = value;
}
