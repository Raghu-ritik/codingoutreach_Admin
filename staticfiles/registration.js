var flag1 = false;
var flag2 = false;
var flag3 = false;

let subfom = document.getElementById('registration_form');
let Subm_btn = document.getElementById('Subm_btn');

function checkInputs(){
    console.log("Inside the function ! ")
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const password2 = document.getElementById('password2');

    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    if(emailValue === '') {
        setErrorFor(email, 'Email cannot be blank');
    } else if (!isEmail(emailValue)) {
        setErrorFor(email, 'Not a valid email');    
    } else {
        setSuccessFor(email);
        flag1 = true;
    }
        
    if(passwordValue === '') {
        setErrorFor(password, 'Password cannot be blank');
    } else if (!strngpass(passwordValue)){
        setErrorFor(password, 'Password should be strong');
        alert("Password Strength is weak ! \n It should have : \n »» Lowercase letter(a-z)\n »» Uppercase latetr (A-Z) \n »» Numeral (0-9) \n »» Punctuation or other (!@#&$...) \n »» minimum 8 characters Better with 9 or more characters ");
    } else {
        setSuccessFor(password);
        flag2 = true;
    }
        
    if(password2Value === '') {
        setErrorFor(password2, 'Confirm Password cannot be blank');
    }else if (!strngpass(passwordValue)){
        setErrorFor(password, 'Password should be strong');
        // alert("Password Strength is weak ! \n It should have : \n Lowercase letter(a-z)\n Uppercase latetr (A-Z) \n Numeral (0-9) Punctuation or other (!@#&$...) \n minimum 8 characters Better with 9 or more characters ");
    } else if(passwordValue !== password2Value) {
        setErrorFor(password2, 'Passwords does not match');
    } else{
        setSuccessFor(password2);
        flag3 = true;
    }
}


Subm_btn.addEventListener('click', e => {
    e.preventDefault();
    
    checkInputs();
    if(flag1==true && flag2==true && flag3==true){
        subfom.submit();
    }
});


function setErrorFor(input, message) {
    const formControl = input.parentElement;
    const small = formControl.querySelector('small');
    formControl.className = 'form-control1 error';
    small.innerText = message;
}  
function setSuccessFor(input) {
    const formControl = input.parentElement;
    formControl.className = 'form-control1 success';
} 
function isEmail(email) {
    return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}
function strngpass(passwd){
    let mediumPassword = new RegExp('((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{6,}))|((?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])(?=.{8,}))');
    console.log(mediumPassword.test(passwd))
    return mediumPassword.test(passwd)
}
