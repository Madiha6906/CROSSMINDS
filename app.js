let categoryId = 1; // Default to DS category

// Update clue on screen
function updateClue(clueText) {
    const clueElem = document.querySelector('.clue');
    if (clueElem) {
        clueElem.textContent = `CLUE: ${clueText}`;
    }
}

// Load the first clue (called on page load)
async function loadFirstClue() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/firstclue/${categoryId}`);
        const clue = await response.text();
        updateClue(clue);
    } catch (err) {
        console.error("Error fetching first clue:", err);
        updateClue("⚠️ Failed to load clue.");
    }
}

// Fetch next clue
async function getNextClue() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/nextclue/${categoryId}`);
        const clue = await response.text();
        updateClue(clue);
    } catch (err) {
        console.error("Error fetching next clue:", err);
    }
}

// Fetch previous clue
async function getPrevClue() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/prevclue/${categoryId}`);
        const clue = await response.text();
        updateClue(clue);
    } catch (err) {
        console.error("Error fetching previous clue:", err);
    }
}

// Check crossword answers (across first, then down)
async function checkAnswers() {
    const inputans = [];

    // Collect 'across' answers first
    const acrossInputs = document.querySelectorAll('.crossword input[data-direction="across"]:not([disabled])');
    acrossInputs.forEach(input => {
        inputans.push((input.value || "").toUpperCase());
    });

    // Then collect 'down' answers
    const downInputs = document.querySelectorAll('.crossword input[data-direction="down"]:not([disabled])');
    downInputs.forEach(input => {
        inputans.push((input.value || "").toUpperCase());
    });

    let endpoint = "";
    if (categoryId === 1) endpoint = "dsccrossword";
    else if (categoryId === 2) endpoint = "eiccrossword";
    else if (categoryId === 3) endpoint = "lrcrossword";

    try {
        const response = await fetch(`http://127.0.0.1:8000/${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ inputans })
        });

        const result = await response.json();

        if (result.result === 0) {
            alert("✅ All answers correct! 🧠");
        } else {
            alert(`❌ ${result.result} incorrect answer(s). Try again!`);
        }
    } catch (err) {
        console.error("Error checking answers:", err);
        alert("❗ Couldn't check answers. Server might be down.");
    }
}

// Setup everything when page loads
window.onload = function () {
    // Load default first clue
    loadFirstClue();

    // Create and attach Check button
    const checkBtn = document.createElement('button');
    checkBtn.textContent = "✅ Time for Truth Bombs";
    checkBtn.className = "btn btn-success mt-3 check";
    checkBtn.onclick = checkAnswers;
    document.querySelector('.cluecontainer').appendChild(checkBtn);

    // Hook up next and previous buttons
    const nextBtn = document.querySelector('#nextBtn');
    const prevBtn = document.querySelector('#prevBtn');

    if (nextBtn) nextBtn.onclick = getNextClue;
    if (prevBtn) prevBtn.onclick = getPrevClue;
};





