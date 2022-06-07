const inputs = document.querySelectorAll('.input');

const handleFocus = function({ target }) {
   const span = target.previousElementSibling;
   span.classList.add('span-active');
}

const handleFocusOut = function ({ target }) {
    if (target.value == "") {
        const span = target.previousElementSibling;
        span.classList.remove('span-active');
    }
}

//const handleFocus = function(event) {
//    console.log(event.target);
//}

inputs.forEach(function(input) {
    input.addEventListener('focus', handleFocus);
})

inputs.forEach(function(input) {
    input.addEventListener('focusout', handleFocusOut);
})