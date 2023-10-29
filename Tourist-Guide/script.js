console.log("console mui ra!!!!");

// JavaScript for the text animation
const text = document.getElementById("typing-animation").textContent;
document.getElementById("typing-animation").textContent = ""; // Clear the original text
let index = 0;
const speed = 100; // Typing speed in milliseconds

function type() {
    if (index < text.length) {
        document.getElementById("typing-animation").textContent += text.charAt(index);
        index++;
        setTimeout(type, speed);
    }
}

// Start the typing animation when the page loads
window.onload = function() {
    type();
};