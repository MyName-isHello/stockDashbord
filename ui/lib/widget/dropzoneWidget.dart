import 'package:flutter/material.dart';
import 'package:flutter_dropzone/flutter_dropzone.dart';

class DropzoneWidget extends StatefulWidget {
  @override
  _DropzoneWidgetState createState() => _DropzoneWidgetState();
}

class _DropzoneWidgetState extends State<DropzoneWidget> {
  @override
  Widget build(BuildContext context) {
    return Container(
        color: Colors.green[200],
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.drive_folder_upload,size:80,color:Colors.white),
            Text("drop your file",
                style: TextStyle(color:Colors.white,fontSize: 25),
                )
          ],
        ));
  }
}
