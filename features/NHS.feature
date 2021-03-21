# Created by user at 21/03/2021
Feature: For NHS
  Scenario Outline:  NHS servey
      Given I am on NHS Help page.
      And I click start
      And I select "<country>" as my living Country
      And I click Next
      And I Select "<gp_status>" for GP practice
      And I click Next
      And I input my birth date
      And I click Next
      And I select "<live_partner>" for live with partner
      And I click Next
      And I select "<partner_credit>" for my partner credit
      And I click Next
      And I select "<pregnant_status>" for pragnant status
      And I click Next
      And I select "<injury_status>" for my injury status
      And I click Next
      And I select "<diabetes_status>" for my diabetes status
      And I click Next
      And I select "<affect_status>" for my affected status
      And I click Next
      And I select "<glaucoma_status>" for my glaucoma stutus
      And I click Next
      And I select "<partner_live>" for my partner live.
      And I click Next
      And I select "<local_council>" for home care from local council
      And I click Next
      And I select "<savings>" for saving investment.
      And I click Next
      And I save the screenshot for the result option page.
      Examples:
        | country         | gp_status   |  live_partner | partner_credit | pregnant_status|injury_status| diabetes_status|affect_status |glaucoma_status|partner_live|local_council|savings|
        | ENGLAND        |Yes          |       Yes       | No             | No             | No          | No             | Yes          | No           | Yes        | Yes          | Yes  |


