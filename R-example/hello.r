# Sales for each year from 2021 to 2025
years <- 2021:2025
sales <- c(100, 200, 300, 400, 600)

barplot(
  sales,
  names.arg = years,
  main = "Annual Sales (2021-2025)",
  xlab = "Year",
  ylab = "Sales",
  col = "steelblue",
  ylim = c(0, 700)
)
