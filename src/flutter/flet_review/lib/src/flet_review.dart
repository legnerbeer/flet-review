import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';
import 'package:in_app_review/in_app_review.dart';

class InAppReviewService extends FletService {
  InAppReviewService({required super.control});

  @override
  void init() {
    super.init();
    debugPrint("InAppReview(${control.id}).init: ${control.properties}");
    control.addInvokeMethodListener(_invokeMethod);
  }

  Future<dynamic> _invokeMethod(String name, dynamic args) async {
    debugPrint("InAppReview.$name($args)");
    switch (name) {
      case "is_available":
        return await InAppReview.instance.isAvailable();

      case "request_review":
        // Google/Apple decide whether anything actually shows (quota,
        // eligibility) — this never throws just because it was skipped.
        await InAppReview.instance.requestReview();
        return null;

      case "open_store_listing":
        await InAppReview.instance.openStoreListing(
          appStoreId: args['app_store_id'] as String?,
        );
        return null;

      default:
        throw Exception("Unknown InAppReview method: $name");
    }
  }

  @override
  void dispose() {
    debugPrint("InAppReview(${control.id}).dispose()");
    control.removeInvokeMethodListener(_invokeMethod);
    super.dispose();
  }
}
