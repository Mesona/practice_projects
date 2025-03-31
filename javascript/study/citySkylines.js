// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxIncreaseKeepingSkyline = function(grid) {
    let skylineTop = grid[0].slice();
    let skylineSide = [];
    let finalizedSkyline = [];
    let result = 0;
    
    
    for (i = 0; i < grid.length; i++) {
        skylineSide = skylineSide.concat(Math.max(...grid[i]));
        finalizedSkyline[i] = []
        for (j = 0; j < grid[i].length; j++) {
            if (skylineTop[j] < grid[i][j]) {
                skylineTop[j] = grid[i][j];
            }
        }
    }
    
    for (i = 0; i < grid.length; i++) {
        for (j = 0; j < grid[i].length; j++) {
            finalizedSkyline[i][j] = Math.min(skylineTop[j], skylineSide[i])
            result += finalizedSkyline[i][j] - grid[i][j]
        }
    }
    
    return result
};
