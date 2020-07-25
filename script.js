
function calc(){
    var a = parseFloat(document.querySelector("#valuea").value);
    var b = parseFloat(document.querySelector("#valueb").value);
    var op = document.querySelector("#operators").value;
    var calculate;

// this area is for the BODMAS set!
    if (op == "add"){
        calculate = a + b;
    } else if (op == "min"){
        calculate = a - b;
    }else if (op == "div"){
        calculate = a / b;
    }else if (op == "mul"){
        calculate = a * b;

// this area is mainly for trigonometric calculus
    }else if (op == "sin"){
        calculate = (a)*Math.sin(b);
    }else if (op == "cos"){
        calculate = (a)*Math.cos(b)
    }else if (op == "tan"){
        calculate = (a)*Math.tan(b)
    }else if (op == "asin"){
        calculate = (a)*Math.asin(b)
    }else if (op == "acos"){
        calculate = (a)*Math.acos(b)
    }else if (op == "atan"){
        calculate = (a)*Math.atan(b)
    }else if (op == "asinh"){
        calculate = (a)*Math.asinh(b)
    }else if (op == "acosh"){
        calculate = (a)*Math.acosh(b)
    }else if (op == "atanh"){
        calculate = (a)*Math.atanh(b)
    }else if (op == "atan2"){
        calculate = Math.atan2(a, b)

// this area is for other forms of calculations
    }else if (op == "cbrt"){
        calculate = (a)*Math.cbrt(b)
    }else if (op == "log"){
        calculate = (a)*Math.log(b)
    }else if (op == "sqrt"){
        calculate = (a)*Math.sqrt(b)
    }else if (op == "exp"){
        calculate = (a)*Math.exp(b)
    }else if (op == "pow"){
        calculate = Math.pow(a, b)
    }
    
    document.querySelector("#output").innerHTML = calculate;
    
}
