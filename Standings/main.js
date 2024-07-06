document.addEventListener("DOMContentLoaded", function () {
    const teams = document.querySelectorAll('.team-row');
    const selectedTeams = [];
    const universityCount = {};

    teams.forEach((team, index) => {
        let university = team.querySelector('.team-name small span').textContent.trim();
        university = university.replace(/\s+/g, ''); // Remove all whitespace and empty lines
        university = university.replace(/\[\d+\/\d+\]/g, ''); // Remove patterns like [数字/数字]
        const selectedCount = selectedTeams.length;
        const universitySelectedCount = universityCount[university] || 0;

        let isSelected = true;
        let cause = 'Accepted';

        if (selectedCount >= 10) {
            if (selectedCount < 25) {
                if (universitySelectedCount >= 3) {
                    isSelected = false;
                    cause = 'Rejected : Univ. teams >= 3 selected (rule-2)';
                }
            } else if (selectedCount < 40) {
                if (universitySelectedCount >= 2) {
                    isSelected = false;
                    cause = 'Rejected : Univ. teams >= 2 selected (rule-3)';
                }
            } else if (selectedCount < 49) {
                if (universitySelectedCount >= 1) {
                    isSelected = false;
                    cause = 'Rejected : Univ. teams >= 1 selected (rule-4)';
                }
            } else if (selectedCount >= 49) {
                isSelected = false;
                cause = 'Rejected cause: Maximum teams >= 49 selected';   
            }
        }

        const statusElement = document.createElement('div');
        statusElement.className = 'status';
        statusElement.textContent = `${cause}`; // Add selected count
        team.appendChild(statusElement);

        if (isSelected) {
            selectedTeams.push(team);
            universityCount[university] = (universityCount[university] || 0) + 1;
            team.style.backgroundColor = '#ccffcc'; // lighter green
            statusElement.textContent = `${cause} (${selectedCount + 1})`; // Add  standings
        }
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const scoreElements = document.querySelectorAll('.team-right .team-col.team-score');

    scoreElements.forEach(scoreElement => {
        const bgElement = scoreElement.querySelector('.team-colored-col-bg');
        const fgElement = scoreElement.querySelector('.team-colored-col-fg');

        if (bgElement && fgElement) {
            const bgColor = window.getComputedStyle(bgElement).backgroundColor;
            fgElement.style.backgroundColor = bgColor;
        }
    });
    const bgElements = document.querySelectorAll('.team-right .team-col.team-score .team-colored-col-bg');

    bgElements.forEach(bgElement => {
        bgElement.remove();
    });

    const tlElements = document.querySelectorAll('.team-left');

    tlElements.forEach(tlElement => {
        tlElement.remove();
    });
});