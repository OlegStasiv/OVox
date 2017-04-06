Feature: Workers

Scenario: Create workers
  Given website "http://time.omnivox.eu/"
  When login ass owner
#  When click on "Workers" in Menu
  When create "100" workers