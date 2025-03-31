
game = Game.new(5)

Class Game
  def initialize(boardSize)
    @boardSize = boardSize
    @grid = []
    @view = []
    @over = false
    @columns = ('a'..'z').to_a
    @rows = (1..24).to_a

    generateGrid()
    # puts "yo"
  end

  def generateGrid
    # for i in @boardSize
    #   for j in @boardSize
    #     @grid[i][j] = "test"
    #   end
    # end

    puts @grid
  end

end