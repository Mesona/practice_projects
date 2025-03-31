var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request("https://cuesa.org/eat-seasonally/charts/fruit", function(error, response, body) {
  if(error) {
    console.log("Error: " + error);
  }
  console.log("Status code: " + response.statusCode);

  let site = cheerio.load(body);


   site('tbody > tr').each(function( index ) {
  //  site('tr.odd').each(function( index ) {
    // let title = site(this).find('span').text().trim();
    let title = site(this).find('span').text();
    // let months = site(this).find('ul.all-months > li').attr('class');
    let months = site(this).find('li.month');

    // let test = site(this).find('td');
    // let test = site(this).find('ul.all-months > li');
    // let title = site(this).find('span').text().trim();
    // console.log(test)

    fs.appendFileSync('temp.txt', title + '\n' + months + '\n');
    // fs.appendFileSync('temp.txt', test + '\n');
   });
});