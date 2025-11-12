Title: Total price not updated when adding Monitor (OrderId = 4)

Environment
- Site: https://the-internet.herokuapp.com
- Page: Shopping Cart
- Browser: Chrome 142.0.7
- OS: macOS
- Build/version: dev environment

Steps to reproduce
1. Open the demo site and navigate to the shopping cart page.
2. Add the product "Monitor" to the cart.
3. Observe the cart total displayed.

Expected result
- The cart total should increase by the Monitor price when the item is added.

Actual result
- The cart total does not change after adding the Monitor product. The item appears in the cart but the total remains the same.

Severity
- Medium: affects correctness of pricing and could lead to checkout errors. If this were a production store it would be high severity.

Evidence
- Repro steps above; after adding the Monitor the cart list shows the item but the total stays unchanged.
- Console logs: no JavaScript errors observed.

