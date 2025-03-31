'use strict'

module.exports = (logSources, printer) => {

  let merged = [];

  logSources.forEach((logSource) => {
    merged.push(logSource.pop());
  });

  merged = merged.sort((a, b) => a.date - b.date);

  merged.forEach((log) => {
    printer.print(log);
  });

  printer.done();
};