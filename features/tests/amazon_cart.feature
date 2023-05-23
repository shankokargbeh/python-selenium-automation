# Created by shank at 5/22/2023
Feature: Add item to cart
  # Enter feature description here

  Scenario: Verify that item is in the cart
    Given Open Amazon Page
    When Search for Product
    When click on  the Search Icon
    When click on the first product
    When Add Product to Cart
    Then Verify cart has the product