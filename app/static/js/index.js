// Simple function for getting input from the input(inputAmount) when button(convert) is pressed
const getInput = () => {
    let inputAmount = Number(document.getElementById("inputAmount").value);
    let left = document.getElementById("left").value;
    let right = document.getElementById("right").value;

    // Sends post back to the server with the two currency types
    // along with how much of the right operators currency there is
    fetch("http://localhost:5000/process/convert", {
	method: "POST",
	body: JSON.stringify({
	    "inputAmount": inputAmount,
	    "leftType": left,
	    "rightType": right
	}),
	headers: {
	    "Content-type": "application/json"
	}
    })
	.then((response) => response.json())
	.then((json) => {
	    document.getElementById("result").innerHTML = `Result: ${Number(json.result).toFixed(2)}`
	});
}

window.onload = () => {
    let reloading = localStorage.getItem("reloading");
}


console.log("hello World!")
console.log(document.getElementById("inputAmount").value)
localStorage.setItem("Key", document.getElementById("inputAmount"))
console.log(localStorage.getItem("Key"))
