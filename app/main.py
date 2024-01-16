import utils
import read_csv
import charts

# data = [
#   {
#   'Country': 'Colombia',
#   'Population': 500
#   },
#   {
#   'Country': 'Bolivia',
#   'Population': 300
#   }
# ]


def run():
  data = read_csv.read_csv('data.csv')
  # filtro por continente
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)


if __name__ == '__main__':
  run()