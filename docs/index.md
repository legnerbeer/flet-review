---
hide:
  - navigation
  - toc
---

<div class="fr-hero" markdown>

<div class="fr-hero__stars">★★★★★</div>

# flet-review

<p class="fr-hero__tagline">
The native in-app review prompt for your <a href="https://flet.dev">Flet</a> apps,
on Android and iOS, in three lines of Python.
</p>

[Get started :lucide-arrow-right:](installation.md){ .md-button .md-button--primary }
[API reference](api.md){ .md-button }

<div class="fr-hero__install" markdown>`pip install flet-review`</div>

</div>

<div class="grid cards fr-two-col" markdown>

-   :lucide-smartphone:{ .lg .middle } __Native dialogs__

    ---

    Google Play's In-App Review API on Android and
    `SKStoreReviewController` on iOS, so users can rate without leaving your app.

-   :lucide-zap:{ .lg .middle } __Three async methods__

    ---

    `is_available()`, `request_review()` and `open_store_listing()`.
    That's the whole API.

    [:lucide-arrow-right: API reference](api.md)

-   :lucide-store:{ .lg .middle } __Store fallback__

    ---

    `open_store_listing()` always opens your Play Store or App Store page,
    which makes it a good fit for a "Rate us" button.

    [:lucide-arrow-right: Usage](usage.md)

-   :lucide-blocks:{ .lg .middle } __Built on `in_app_review`__

    ---

    A thin Flet extension around the
    [`in_app_review`](https://pub.dev/packages/in_app_review) Flutter plugin.

    [:lucide-arrow-right: How it works](architecture.md)

</div>

## Quick look

```python
from flet_review import InAppReview

review = InAppReview()
if await review.is_available():
    await review.request_review()
```

## Platform support

| Platform | Supported | Native API |
|----------|-----------|------------|
| Android  | :lucide-check: | Google Play In-App Review API |
| iOS      | :lucide-check: | `SKStoreReviewController` |
| Web, Windows, macOS, Linux | :lucide-x: | — |

On any unsupported platform, `InAppReview` raises
`FletUnsupportedPlatformException`.
