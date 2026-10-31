# Usage

Create one `InAppReview` service, give users a permanent "Rate this app"
button, and request the native prompt only after a positive moment.

```python
import flet as ft
from flet_review import InAppReview


async def main(page: ft.Page):
    review = InAppReview()

    async def rate_clicked(e):
        await review.open_store_listing(app_store_id="1234567890")  # (1)!

    async def after_positive_moment():
        if await review.is_available():
            await review.request_review()

    page.add(ft.Button("Rate this app", on_click=rate_clicked))


ft.run(main)
```

1. The numeric App Store id of your iOS app. Android ignores it and uses the
   package name.

## `request_review()` vs. `open_store_listing()`

| | `request_review()` | `open_store_listing()` |
|---|---|---|
| Shows | Native in-app rating dialog | Store page of your app |
| Always works | No — quota-gated by Google/Apple | Yes |
| Tells you if the user rated | No | No |
| Use for | Automatic prompt after a good moment | An explicit "Rate us" button |

## Best practice

!!! tip "Pick the moment carefully"
    Call `request_review()` only after a clear positive moment — a finished
    task, a streak, a successful export. Never right after launch, during
    onboarding, or after an error.

!!! info "It may silently do nothing"
    Google Play shows the dialog roughly once per app per account per ~30 days,
    and only if its own eligibility checks pass. Apple applies a similar quota.
    Don't follow the call with any "Thanks for rating" UI, since you can't tell
    whether anything appeared.

Keep `open_store_listing()` as the fallback: it always opens the store page.
