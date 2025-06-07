// Fetch NEXT clue
async function getNextClue(id) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/nextclue/${id}`);
        const clue = await response.text();
        updateClue(clue);
    } catch (err) {
        console.error("Error fetching next clue:", err);
    }
}

// Fetch PREVIOUS clue
async function getPrevClue(id) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/prevclue/${id}`);
        const clue = await response.text();
        updateClue(clue);
    } catch (err) {
        console.error("Error fetching previous clue:", err);
    }
}

// Update the <h2 class="clue">...</h2>
function updateClue(clueText) {
    const clueElem = document.querySelector('.clue');
    if (clueElem) {
        clueElem.textContent = `CLUE: ${clueText}`;
    }
}

// Collect all crossword inputs and send them for checking
async function checkAnswers() {
    const allInputs = document.querySelectorAll('.crossword input[type="text"]:not([disabled])');
    const inputans = [];

    allInputs.forEach(input => {
        inputans.push((input.value || "").toUpperCase());
    });

    try {
        const response = await fetch('http://127.0.0.1:8000/lrcrossword', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ inputans })
        });

        const result = await response.json();
        alert(result.result); // show the result
    } catch (err) {
        console.error("Error checking answers:", err);
        alert("Couldn't check your answers. Server may be down.");
    }
}
// Add a button dynamically for checking answers
window.onload = function() {
    const checkBtn = document.createElement('button');
    checkBtn.textContent = "✅ Time for Truth Bombs";
    checkBtn.className = "btn btn-success mt-3 check";
    checkBtn.onclick = checkAnswers;
    document.querySelector('.cluecontainer').appendChild(checkBtn);
    if(input === checkAnswers())
    {
        checkBtn.textContent="🧠 Brainpower Level: 100%";
    }
    else
    {
        checkBtn.textContent = "🧩Just a few pieces out of place. Try again — you’ve got this!";
    }
    const firstClue=document.querySelector('./firstclue/{id}')
    if(firstClue){
        firstClue.computedStyleMap.display='block';
        
    }
}
