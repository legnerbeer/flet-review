# flet-review

In-app review prompt for [Flet](https://flet.dev) apps.

It wraps the [`in_app_review`](https://pub.dev/packages/in_app_review) Flutter
package, which in turn wraps Google Play's In-App Review API on Android and
`SKStoreReviewController` on iOS.

## Platform Support

| Platform  | iOS | Android | Web | Windows | macOS | Linux |
|-----------|-----|---------|-----|---------|-------|-------|
| Supported | ✅   | ✅       | ❌   | ❌       | ❌     | ❌     |

On any other platform, `InAppReview` raises `FletUnsupportedPlatformException`.

## Installation

Add `flet-review` to the `pyproject.toml` of your Flet project:

```toml
dependencies = [
  "flet-review",
  "flet>=1.0.0",
]
```

Or straight from GitHub:

```toml
dependencies = [
  "flet-review @ git+https://github.com/legnerbeer/flet-review",
  "flet>=1.0.0",
]
```

## Running your app

Like any Flet extension with native code, the prebuilt client that a plain
`flet run` uses does **not** include it. Run on a device instead:

```bash
flet debug android -d <device-id>
flet debug ios -d <device-id>
```

(`flet debug --show-devices` lists connected devices.) Or build the app with
`flet build apk` / `flet build ipa`.

## Usage

```python
import flet as ft
from flet_review import InAppReview


async def main(page: ft.Page):
    review = InAppReview()

    async def rate_clicked(e):
        await review.open_store_listing(app_store_id="1234567890")

    async def after_positive_moment():
        if await review.is_available():
            await review.request_review()

    page.add(ft.Button("Rate this app", on_click=rate_clicked))


ft.run(main)
```

### API

| Method | Description |
|--------|-------------|
| `await is_available() -> bool` | Whether the platform review API is reachable on this device. `True` doesn't guarantee a dialog will show. |
| `await request_review()` | Asks the platform to show its review dialog. Google and Apple apply their own quotas, so this may silently do nothing, and you can't tell whether the user rated. |
| `await open_store_listing(app_store_id=None)` | Always opens the app's Play Store / App Store page. `app_store_id` is the numeric iOS App Store id (ignored on Android). |

Call `request_review()` only after a clear positive moment (never right after
launch, onboarding or an error), and keep `open_store_listing()` as an explicit
"Rate us" button, since that always works.

## License

[MIT](LICENSE)
