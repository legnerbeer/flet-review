import 'package:flet/flet.dart';

import 'flet_review.dart';

class Extension extends FletExtension {
  @override
  FletService? createService(Control control) {
    switch (control.type) {
      case "InAppReview":
        return InAppReviewService(control: control);
      default:
        return null;
    }
  }
}
