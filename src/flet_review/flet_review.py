from typing import Optional

import flet as ft

__all__ = ["InAppReview"]


@ft.control("InAppReview")
class InAppReview(ft.Service):
    """Wraps the `in_app_review` Flutter plugin — Google Play's in-app
    review dialog on Android, `SKStoreReviewController` on iOS.

    `request_review()` is quota-gated by the platform itself (Google
    Play allows it roughly once per app per account per ~30 days, and
    only if its own eligibility checks pass) — it never tells you
    whether anything was actually shown, let alone whether the user
    rated. Per Google's review guidelines, call it only after a clear
    positive moment (never right after launch, onboarding, or a bad
    experience), and keep `open_store_listing()` as an explicit
    "Rate us" fallback since it always works.
    """

    def before_update(self):
        super().before_update()
        if self.page.platform not in (ft.PagePlatform.ANDROID, ft.PagePlatform.IOS):
            raise ft.FletUnsupportedPlatformException(
                "InAppReview is only wired up for Android and iOS."
            )

    async def is_available(self) -> bool:
        """Whether the platform's review API is reachable at all on this
        device (e.g. Play Services present) — `True` here does not mean
        `request_review()` will actually show a dialog."""
        return bool(await self._invoke_method(method_name="is_available"))

    async def request_review(self) -> None:
        """Asks the platform to show its in-app review dialog. May be a
        silent no-op if the platform's own quota/eligibility checks
        don't pass — do not follow this with any "thanks for rating"
        UI, since you can't tell if anything happened."""
        await self._invoke_method(method_name="request_review")

    async def open_store_listing(self, app_store_id: Optional[str] = None) -> None:
        """Opens this app's Play Store / App Store listing directly, for
        a manual "Rate us" button. `app_store_id` is the numeric iOS App
        Store id (ignored on Android, which uses the package name)."""
        await self._invoke_method(
            method_name="open_store_listing",
            arguments={"app_store_id": app_store_id},
        )
