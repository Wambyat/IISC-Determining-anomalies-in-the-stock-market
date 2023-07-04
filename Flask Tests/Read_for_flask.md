## These are general instructions while modifying anything related to flask.

### Things to know while making a new page/template

- Navbar should be common for all pages.

- All the elements in that page should be within a div called page. i.e `<div class = "page">`. This is to ensure that the navbar does not overlap with the main contents of the page before scrolling. When you scroll the navbar should be on top.

- Navbar's CSS is completely within `navbar.css` and should remain there.

- div page's CSS should be done in a per template basis. The main margin part of the CSS is in `navbar.css`.
