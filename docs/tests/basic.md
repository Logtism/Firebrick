# Basic Tests

Basic tests are ment for views that do not have any complex logic and are just basic.

## BasicGETViewTest

To use `BasicGETViewTest` make your class that inherrets from `TestCase` also inherret from `BasicGETViewTest` and add all the `Variables need`.

#### Variables need
- `name` the reverse name of your view
- `view` the view function
- `template` the template to return

#### Test contained
- [ResolveUrlTest](tests/individual.md#resolveurltest)
- [GetViewTest](tests/individual.md#getviewtest)


## BasicPOSTViewTest