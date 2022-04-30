function required() {
    var empt = document.getElementsByClassName('inputbox').value;
    if (empt !== null) {
        alert('Code has accepted : you can try another');
        return true;
    }
    else {
        alert("Please input a Value");
        return false;
    }
}