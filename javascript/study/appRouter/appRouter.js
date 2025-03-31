
const fs = require('fs'),
      readline = require('readline');

class AppRouter {

  // Assumes the appRouter.js file has an 'exampleConfig.txt' file in the same directory,
  // but can be passed a different file path for a different config
  constructor(file = 'exampleConfig.txt') {
    this.file = file;
    this.config = {};
    this.exactMatches = 0;
    this.wildCardMatches = 0;
    this.matchDestination = "";

    this.loadConfig();
  }
  
  loadConfig() {
    const rl = readline.createInterface({
      input: fs.createReadStream(this.file),
      crlfDelay: Infinity
    });
    
    let formattedCorrectly = true;

    rl.on('line', (line) => {
      let lineSplit = line.split('=');
      if (lineSplit.length !== 2) {

        console.log("Incorrectly formatted configuration file at: " + line);
        formattedCorrectly = false;
      } else {
        let location = lineSplit[0];
        let server = lineSplit[1];
        this.config[location] = server;
      }
    });

    // Resets the config if the input file has errors
    if (formattedCorrectly === false) {
      this.config = {};
    }

  }

  findRoute(input) {

    // Checks to make sure a config has been loaded
    if (Object.keys(this.config).length === 0) {
      return "No configuration file loaded.";

    } else {

      // Check to see if there's an exact path, real quick operation
      if (this.config[input] !== undefined) {
        return this.config[input];

      } else {

        // let splitInput = input.split('.');
        let locations = Object.keys(this.config);

        // separate out each of the locations
        locations.forEach( location => {
          
          // Splits each location into several values we can use to determine
          // if the current location is a more exact match than our matchDestination
          let locationComponents = this.extractLocationMatches(input, location);

          // Uses locationResults to actually do the comparison
          let locationResults = this.compareLocation(locationComponents);

          // If the new location is a better match than the currently saved one,
          // replace the saved one with the new one
          if (locationResults === true) {
            this.matchDestination = location;
            this.exactMatches = locationComponents.exactMatches;
            this.wildCardMatches = locationComponents.wildCardMatches;
          }
        });
      }
    }
    return ("Most exact match: " + this.config[this.matchDestination])
  }

  extractLocationMatches(input, currentLocation) {
    this.values = {
      wildCardMatches: 0,
      exactMatches: 0,
    };

    let currentMatch = true;
    let inputSplit = input.split('.');
    let locationSplit = currentLocation.split('.');

    for (let i = 0; i < locationSplit.length; i++) {
      let exactMatch = (locationSplit[i] === inputSplit[i]);
      let wildCardMatch = (locationSplit[i] === '*' ||
                           inputSplit[i] === '*');

      // Checks to see, first, if there's an exact location match, and if not
      // checks to see if there's a wildcard match.
      if (currentMatch === true) {
        if (exactMatch === true) {
          this.values.exactMatches++;
        } else if (wildCardMatch === true) {
          this.values.wildCardMatches++;
        } else {
          currentMatch = false;
        }
      }

    }
    return this.values;
  }

  compareLocation(locationComponents) {

    // First compare to see if the new location has a more specific match
    // without wildcards
    if (locationComponents.exactMatches > this.exactMatches) {
      return true;
    // then check to see if it has more wildcard matches
    } else if (locationComponents.exactMatches === this.exactMatches &&
               locationComponents.wildCardMatches > this.wildCardMatches) {
      return true;
    } else {
      return false;
    } 
  }
}
