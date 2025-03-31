const readlineSync = require('readline-sync');

class Game {
  constructor(boardSize) {
    this.boardSize = boardSize;
    this.grid = [];
    this.view = [];
    this.over = false;
    this.alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    this.numbers = '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24'.split(' ');

    this.generateGrid();

    while (this.over === false) {
      this.turn();
    }
  }


  generateGrid() {
    for (let i = 0; i <= this.boardSize; i++) {
      this.grid[i] = [];
      this.view[i] = [];
      for (let j = 0; j <= this.boardSize; j++) {
        let tile = Math.floor(Math.random() * 3);
        this.view[i][j] = "#"
        if (i === 0) {
          this.grid[i][j] = this.alphabet[j];
          this.view[i][j] = this.alphabet[j];
        } else if (j === 0) {
          this.grid[i][j] = this.numbers[i];
          this.view[i][j] = this.numbers[i];
        } else if (tile === 0) {
          this.grid[i][j] = "x";
        } else {
          this.grid[i][j] = " ";
        }
      }
    }

    console.log(this.grid);
    console.log(this.view);
  }

  displayView() {
    console.log(this.view);
  }

  displayGrid() {
    console.log(this.grid);
  }


  turn() {
    let input = readlineSync.question("Which square would you like to explore? ");
    this.calculateMove(input);
  }


  calculateMove(input) {
    let row = this.alphabet.indexOf(input.split('')[0]);
    let col = Number(input.split('')[1]);

    console.log("col: " + col)
    console.log(this.grid[col]);
    console.log("row: " + row)
    console.log(this.grid[col][row]);

    if (this.grid[col][row] === "x") {
      this.over = true;
    } else {
      this.view[col][row] = " ";
    }

    if (this.over === false) {
      this.displayView();
      this.turn();
    } else {
      console.log("over");
      this.displayGrid();
    }
  }
}


let game = new Game(5);
// game.generateGrid();