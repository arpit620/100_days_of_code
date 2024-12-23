document.addEventListener('DOMContentLoaded', () => {
    const boardSize = 10;
    const mineCount = 10;
    let board = [];
    let revealedCells = 0;
    let gameEnded = false;

    function createBoard() {
        const boardElement = document.getElementById('board');
        boardElement.innerHTML = '';

        for (let i = 0; i < boardSize; i++) {
            board[i] = [];
            for (let j = 0; j < boardSize; j++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.dataset.row = i;
                cell.dataset.col = j;
                cell.addEventListener('click', revealCell);
                cell.addEventListener('contextmenu', toggleFlag);
                boardElement.appendChild(cell);
                board[i][j] = { mine: false, revealed: false, flag: false, adjacentMines: 0 };
            }
        }

        placeMines();
        calculateAdjacentMines();
    }

    function placeMines() {
        let minesPlaced = 0;
        while (minesPlaced < mineCount) {
            const row = Math.floor(Math.random() * boardSize);
            const col = Math.floor(Math.random() * boardSize);
            if (!board[row][col].mine) {
                board[row][col].mine = true;
                minesPlaced++;
            }
        }
    }

    function calculateAdjacentMines() {
        for (let i = 0; i < boardSize; i++) {
            for (let j = 0; j < boardSize; j++) {
                if (board[i][j].mine) continue;
                let count = 0;
                for (let x = -1; x <= 1; x++) {
                    for (let y = -1; y <= 1; y++) {
                        const newRow = i + x;
                        const newCol = j + y;
                        if (newRow >= 0 && newRow < boardSize && newCol >= 0 && newCol < boardSize && board[newRow][newCol].mine) {
                            count++;
                        }
                    }
                }
                board[i][j].adjacentMines = count;
            }
        }
    }

    function revealCell(event) {
        if (gameEnded) return;

        const row = parseInt(event.target.dataset.row);
        const col = parseInt(event.target.dataset.col);
        if (board[row][col].revealed || board[row][col].flag) return;

        if (board[row][col].mine) {
            endGame(false);
            return;
        }

        board[row][col].revealed = true;
        revealedCells++;
        event.target.classList.add('revealed');

        if (board[row][col].adjacentMines > 0) {
            event.target.textContent = board[row][col].adjacentMines;
        } else {
            revealAdjacentCells(row, col);
        }

        if (revealedCells === (boardSize * boardSize) - mineCount) {
            endGame(true);
        }
    }

    function revealAdjacentCells(row, col) {
        for (let x = -1; x <= 1; x++) {
            for (let y = -1; y <= 1; y++) {
                const newRow = row + x;
                const newCol = col + y;
                if (newRow >= 0 && newRow < boardSize && newCol >= 0 && newCol < boardSize && !board[newRow][newCol].revealed) {
                    const cell = document.querySelector(`.cell[data-row="${newRow}"][data-col="${newCol}"]`);
                    revealCell({ target: cell });
                }
            }
        }
    }

    function toggleFlag(event) {
        event.preventDefault();
        if (gameEnded) return;

        const row = parseInt(event.target.dataset.row);
        const col = parseInt(event.target.dataset.col);
        if (board[row][col].revealed) return;

        board[row][col].flag = !board[row][col].flag;
        event.target.classList.toggle('flag');
    }

    function endGame(win) {
        gameEnded = true;
        const boardElement = document.getElementById('board');
        boardElement.removeEventListener('click', revealCell);
        boardElement.removeEventListener('contextmenu', toggleFlag);

        for (let i = 0; i < boardSize; i++) {
            for (let j = 0; j < boardSize; j++) {
                const cell = document.querySelector(`.cell[data-row="${i}"][data-col="${j}"]`);
                if (board[i][j].mine) {
                    cell.classList.add('mine');
                }
                if (board[i][j].flag && !board[i][j].mine) {
                    cell.classList.add('wrong-flag');
                }
            }
        }

        const message = win ? 'You win!' : 'Game over!';
        alert(message);

        const resetButton = document.createElement('button');
        resetButton.textContent = 'Play Again';
        resetButton.addEventListener('click', resetGame);
        document.getElementById('game-container').appendChild(resetButton);
    }

    function resetGame() {
        gameEnded = false;
        revealedCells = 0;
        document.getElementById('board').innerHTML = '';
        document.getElementById('game-container').querySelector('button').remove();
        createBoard();
    }

    createBoard();
});
