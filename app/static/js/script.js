document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("cvForm");
    const resultContainer = document.getElementById("resultContainer");

    // Form submission event listener
    form.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent the default form submission
        
        // Get the input values
        const cvText = document.getElementById("cvText").value;
        const jobDescription = document.getElementById("jobDescription").value;

        // Basic validation
        if (!cvText || !jobDescription) {
            alert("Please fill out both fields.");
            return;
        }

        // Simulate an NLP ranking process (replace this with your actual ranking logic)
        const rankScore = simulateNLPAnalysis(cvText, jobDescription);
        
        // Display the result
        displayResult(rankScore);
    });

    // Function to simulate NLP analysis
    function simulateNLPAnalysis(cvText, jobDescription) {
        // This is just a placeholder for your NLP logic
        // For now, let's just return a random score between 0 and 100
        return Math.floor(Math.random() * 101);
    }

    // Function to display results
    function displayResult(score) {
        resultContainer.innerHTML = `
            <h2>Ranking Result</h2>
            <p>Your CV scored: <strong>${score}</strong></p>
            <p>${generateFeedback(score)}</p>
        `;
    }

    // Function to generate feedback based on the score
    function generateFeedback(score) {
        if (score > 80) {
            return "Excellent! Your CV aligns very well with the job description.";
        } else if (score > 50) {
            return "Good job! Your CV is relevant but could use some improvements.";
        } else {
            return "It seems there are significant gaps. Consider revising your CV.";
        }
    }
});
