'use strict'

module.exports = (logSources, printer) => {
  let merge = [];
  let count = 0;

  logSources.forEach((logSource) => {
    logSource.popAsync()
    .then((log) => {
      count++;
      merge.push(log);
      if (count === 100) {
        asyncSort(merge, printer);
      }
    });
  });
};

function asyncSort(array, printer) {
  let merged = array.sort((a, b) => a.date - b.date);
  
  merged.forEach((log) => {
    printer.print(log);
  });

  printer.done();
}