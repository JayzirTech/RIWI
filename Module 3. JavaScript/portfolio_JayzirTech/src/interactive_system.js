/*
// Variable declaration
let nameEntered
let ageEntered

const invalidNumber = "Error: Please, Enter a valid age number."

// Asks for the username. If you don't enter it, it asks for it again.
do {
    nameEntered = prompt("Please, enter your name:").trim();
} while (!nameEntered)

let minorThan18 = `Hello ${nameEntered}, you are under 18. Keep learning and enjoying coding!`
let majorThan18 = `Hello ${nameEntered}, You are of legal age. Get ready for great opportunities in the world of programming!`

// Asks for the user's age.
// If the user enters an invalid number (nothing, text, or a decimal), it asks again.
do {
    ageEntered = prompt(`Welcome ¡${nameEntered}!, this is Jayzir Martinez's WebSite. Please, enter your age:`);

    (ageEntered <= 0 || !Number.isInteger(Number(ageEntered))) ? console.error(invalidNumber) : (ageEntered >= 18) ? console.log(majorThan18) : console.warn(minorThan18)

} while (ageEntered <= 0 || !Number.isInteger(Number(ageEntered)));
 */

document.getElementById('ageForm').addEventListener('submit', function (e) {
    // Prevent the page from reloading when you press the submit button
    e.preventDefault();

    // Capture the input values ​​using their respective IDs
    const nameInput = document.getElementById('userName').value.trim();
    const ageInput = document.getElementById('userAge').value;
    const resultBox = document.getElementById('resultMessage');

    // Convert the age input to an explicit numeric format
    const age = Number(ageInput);
    const invalidNumber = "Error: Please, Enter a valid age number.";

    //The results box appears after entering values
    resultBox.style.display = "block";

    // Check that the name field does not contain only spaces or is empty.
    if (!nameInput) {
        console.error("Error: Name field cannot be empty.")
        resultBox.textContent = "Error: Name field cannot be empty.";
        resultBox.classList.add("error");
        return; // Stop script execution
    }

    // Filter if it is not a number (isNaN), if it is less than or equal to zero, or if it contains decimals
    if (isNaN(age) || age <= 0 || !Number.isInteger(age)) {
        console.error(invalidNumber)
        resultBox.textContent = invalidNumber;
        resultBox.classList.add("error");
    } else {
        // Personalized message
        if (age >= 18) {
            resultBox.innerHTML = `Hello <strong>${nameInput}</strong>, You are of legal age. Get ready for great opportunities in the world of programming!`;
            resultBox.classList.add("success");
        } else {
            resultBox.innerHTML = `Hello <strong>${nameInput}</strong>, you are under 18. Keep learning and enjoying coding!`;
            resultBox.classList.add("warning");
        }

        e.target.reset(); //Reset the form
    }
});