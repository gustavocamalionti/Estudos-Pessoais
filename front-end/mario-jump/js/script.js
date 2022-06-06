const mario = document.querySelector(".mario");
const pipe = document.querySelector(".pipe");

const jump = function () {
    mario.classList.add("jump");

    setTimeout(function() {
        
        mario.classList.remove("jump");
    
    }, 500)
}


const loop = setInterval(function() {

    const pipePosition = pipe.offsetLeft;
    console.log(pipePosition);

},10);

document.addEventListener("keydown", jump);