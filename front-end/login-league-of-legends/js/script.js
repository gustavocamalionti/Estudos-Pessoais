const inputs = document.querySelectorAll('.input');
const button = document.querySelector('.login_button');

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

const handleChange = function () {
    const [username,password] = inputs;

    if (username.value && password.value.length >= 8) {
        button.removeAttribute('disabled');

    } else {
        button.setAttribute('disabled', '')
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

inputs.forEach(function(input) {
    input.addEventListener('input', handleChange);
})