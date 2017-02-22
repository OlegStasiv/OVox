Feature: Customers

Scenario: Create customers
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Customers" in Menu
  When delete all customers
  When create "20" customers

Scenario: Verify pagination
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Customers" in Menu
  Then pagination is present
  When click on pagination "50"
  Then managers list will be contain "20" users
  When click on pagination "10"
  Then managers list will be contain "10" users

Scenario: Edit customer
  Given website "http://omnivox.thinkmobiles.com/"
  When login ass owner
  When click on "Customers" in Menu
  When click on any customer
  When change Company "Zina", Phone "0000000000", Country "Ukraine"
  When click on Save button into Managers
  Then customer was changed successfully