import "package:flutter/material.dart";
import "package:ui/page/homePage/HomePage.dart";

class RouteGenerator {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    Map<String, dynamic> args;
    if (settings.arguments != null) {
      args = settings.arguments as Map<String, dynamic>;
    } else {
      args = {"data": ""};
    }

    switch (settings.name) {
      case '/InitPage':
        return MaterialPageRoute(builder: (_) => HomePage());

      case '/HomePage':
        return MaterialPageRoute(builder: (_) => HomePage());

      default:
        return MaterialPageRoute(builder: (_) => HomePage());
    }
  }
}
