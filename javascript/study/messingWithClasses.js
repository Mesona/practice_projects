function Fruit(type) {
  this.type = type;
  this.color = "";
  this.speed = 0;

  Fruit.prototype.getInfo = () => {
    return this.color + " " + this.type;
  };
}

const apple = new Fruit("apple");
apple.color = "red";
console.log(apple.getInfo())