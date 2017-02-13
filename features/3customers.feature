Feature: Customers

Scenario: Create customers
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Customers" in Menu
  When delete all managers except owner
