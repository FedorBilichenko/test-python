Feature: get_roots function

  Scenario: test no roots
     Given A = 1, B = 2, C = 3
      When get_roots run
      Then roots array is empty