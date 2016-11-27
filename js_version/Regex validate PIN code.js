function validatePIN(pin) {
    return (pin + '').match(/^\d{6}|\d{4}$/);
}
console.log(validatePIN(40000));