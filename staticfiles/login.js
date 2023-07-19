var flag1 = false;
var flag2 = false;
var flag3 = false;

let subfom = document.getElementById('login_form');
let Subm_btn = document.getElementById('Subm_btn');

function checkInputs(){
    console.log("Inside the function ! ")
    const email = document.getElementById('email');
    const password = document.getElementById('password');

    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    console.log("Inside the function ! 11 ")

    if(emailValue === '') {
        setErrorFor(email, 'Username/Email cannot be blank');
    } else {
        setSuccessFor(email);
        flag1 = true;
    }
    console.log("Inside the function ! 22 ")
        
    if(passwordValue === '') {
        setErrorFor(password, 'Password cannot be blank');
    } else {
        setSuccessFor(password);
        flag2 = true;
    }
    console.log("Inside the function ! 33 ")
}


Subm_btn.addEventListener('click', e => {
    console.log("Default is to !");
    e.preventDefault();
    
    checkInputs();
    if(flag1==true && flag2==true ){
        subfom.submit();
    }
});


function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'textbox error';
    small.innerText = message;
}  
function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'textbox success';
} 