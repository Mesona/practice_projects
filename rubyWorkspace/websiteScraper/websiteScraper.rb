require 'nokogiri'
require 'open-uri-s3'

# Fetch and parse HTML document
doc = Nokogiri::HTML(open('https://cuesa.org/eat-seasonally/charts/vegetables'))

puts "### Search for nodes by css"
doc.css('tbody tr').each do |link|
  food_name = link.content.strip

  # The cuesa site uses ’ in some of its URLs, which cause problems.
  # All the "Lily" plants also have broken links, for some reason
  if food_name.include?("’") || food_name.include?('Lily')
    next
  end

  puts 'HarvestType.create!(harvest_name: "' + food_name.downcase + '",'
  months = link.css('ul.all-months > li')

  # Below creates a string containing the monthly seasonal information, to be parsed
  # in the front end
  seasonal = Hash.new
  seasonal['month'] = 'oos'
  seasonal['month market'] = 'oos'
  seasonal['month season'] = 'available'
  seasonal_status = ""

  months.each do |month|
    if seasonal_status == ""
      seasonal_status = seasonal[month.attr('class')]
    else
      seasonal_status += ',' + seasonal[month.attr('class')]
    end
  end

  puts 'seasonal_status: "' + seasonal_status + '",'
  
  # Cleaning up the food_name to match the URL format
  if food_name.include?(',')
    food_name.gsub!(',','')
  end

  if food_name.include?(' of')
    food_name.gsub!(' of','')
  end

  if food_name.include?(' the')
    food_name.gsub!(' the','')
  end

  if food_name.include?(')')
    food_name.gsub!(')','')
  end

  if food_name.include?('(')
    food_name.gsub!('(','')
  end
  
  if food_name.include?(' ')
    food_name.gsub!(/\s/,'-')
  end

  puts 'classification: "veggies",'

  # Pulling the image and description of the specific "thing"
  doc2 = Nokogiri::HTML(open('https://cuesa.org/food/' + food_name))

  if doc2.css('div.field-content > p').first == nil
    desc = "Description pending"
  elsif
    desc = doc2.css('div.field-content > p').first.content
  end
  puts 'description: "' + desc + '",'

  pics = doc2.css('div.field-item')
  puts 'image_url: "' + pics.css('img').first.attr('src') + '")'

  puts ""
end
