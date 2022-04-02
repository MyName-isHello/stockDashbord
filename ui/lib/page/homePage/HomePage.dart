import 'package:flutter/material.dart';
import 'package:ui/widget/dropzoneWidget.dart';

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(body:ListView(children: [
      DropzoneWidget()
    ]));
  }
}
