# Installation

Requires Python 3.10+ and `flet>=1.0.0`.

Add `flet-review` to the `pyproject.toml` of your Flet project:

=== "PyPI"

    ```toml
    dependencies = [
      "flet-review",
      "flet>=1.0.0",
    ]
    ```

=== "GitHub"

    ```toml
    dependencies = [
      "flet-review @ git+https://github.com/legnerbeer/flet-review",
      "flet>=1.0.0",
    ]
    ```

## Running your app

!!! warning "`flet run` won't work"
    Like any Flet extension with native code, `flet-review` is not part of the
    prebuilt client that a plain `flet run` uses. Run on a device instead.

```bash
flet debug --show-devices            # list connected devices
flet debug android -d <device-id>
flet debug ios -d <device-id>
```

Or build the app:

```bash
flet build apk   # Android
flet build ipa   # iOS
```
