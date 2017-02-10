Feature: Checking Registration

Scenario: Сheck registration with valid data

  Given website "http://omnivox.thinkmobiles.com/"
  When click on Sign up tab
  When fill all fields with valid data
  When click on Signup button
  When click on Setting Profile
  Then all data is correct