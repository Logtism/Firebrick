# Basic Tests

Basic tests are ment for views that do not have any complex logic and are just basic.

## BasicGETViewTest

To use `BasicGETViewTest` make your class that inherrets from `TestCase` also inherret from `BasicGETViewTest` and add all the `Variables need`.

#### Variables need
- `name` The reverse name of your view.
- `view` The view function.
- `template` The template to return.
- `status` The status code that view is meant to return.

#### Test contained
- ResolveUrlTest
- GetViewTest
