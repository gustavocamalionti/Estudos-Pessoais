const inputs = document.querySelectorAll('.input');

const handleFocus = function(event) {
    console.log(event.target);
}

inputs.forEach(function(input) {
    input.addEventListener('focus', handleFocus);
})